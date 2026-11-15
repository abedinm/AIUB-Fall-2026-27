"""Compile and run every example in examples.txt with the VS 2022 Roslyn compiler
(C# 7.3, .NET Framework), check each against its declared expectation, and
write results.json for build.py."""
import json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
WORK = os.path.join(HERE, "work")
CSC = r"C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Current\Bin\Roslyn\csc.exe"


def parse(path):
    items, cur = [], None
    for line in open(path, encoding="utf-8").read().split("\n"):
        if line.startswith("@@ "):
            parts = line[3:].split()
            cur = {"id": parts[0], "kind": parts[1],
                   "codes": parts[2].split(",") if len(parts) > 2 else [],
                   "body": [], "expect": None}
            items.append(cur)
        elif cur is not None and line.strip() == ">>>":
            cur["expect"] = []
        elif cur is not None:
            (cur["body"] if cur["expect"] is None else cur["expect"]).append(line)
    for it in items:
        while it["body"] and not it["body"][-1].strip():
            it["body"].pop()
        if it["expect"] is not None:
            while it["expect"] and not it["expect"][-1].strip():
                it["expect"].pop()
    return items


def split_items(lines):
    """Split top-level declarations into (is_static_member, text) chunks."""
    chunks, cur, depth = [], [], 0
    for line in lines:
        code = line.split("//")[0]
        if not cur and not line.strip():
            continue
        cur.append(line)
        depth += code.count("{") - code.count("}")
        if depth == 0 and (code.strip().endswith("}") or code.strip().endswith(";") or not code.strip()):
            text = "\n".join(cur)
            chunks.append((cur[0].lstrip().startswith("static "), text))
            cur = []
    if cur:
        chunks.append((cur[0].lstrip().startswith("static "), "\n".join(cur)))
    return chunks


def program_for(it):
    body = it["body"]
    if it["kind"] == "full":
        return "\n".join(body)
    if "// Main" in [l.strip() for l in body]:
        i = [l.strip() for l in body].index("// Main")
        pre, main = body[:i], body[i + 1:]
    elif any(re.match(r"((abstract|sealed|static|public)\s+)*class |static ", l) for l in body):
        pre, main = body, []
    else:
        pre, main = [], body
    tops, members = [], []
    for is_static, text in split_items(pre):
        (members if is_static else tops).append(text)
    out = ["using System;", ""] + tops + ["", "class Program", "{"]
    for m in members:
        out += ["    " + l for l in m.split("\n")]
    out += ["    static void Main()", "    {"]
    out += ["        " + l if l.strip() else "" for l in main]
    out += ["    }", "}"]
    return "\n".join(out)


def diag(text, kind):
    res = []
    for line in text.splitlines():
        m = re.search(r"\((\d+),\d+\): %s (CS\d+): (.*)$" % kind, line)
        if m:
            res.append({"line": int(m.group(1)), "code": m.group(2), "msg": m.group(3).strip()})
    return res


def main():
    os.makedirs(WORK, exist_ok=True)
    items = parse(os.path.join(HERE, "examples.txt")) + parse(os.path.join(HERE, "examples_mid.txt"))
    results, failures = {}, []
    if len(sys.argv) > 1:  # verify only ids with this prefix, keep the other stored results
        items = [it for it in items if it["id"].startswith(tuple(sys.argv[1].split(",")))]
        if os.path.exists(os.path.join(HERE, "results.json")):
            results = json.load(open(os.path.join(HERE, "results.json"), encoding="utf-8"))
    for it in items:
        src = program_for(it)
        cs = os.path.join(WORK, it["id"] + ".cs")
        exe = os.path.join(WORK, it["id"] + ".exe")
        open(cs, "w", encoding="utf-8").write(src)
        if os.path.exists(exe):
            os.remove(exe)
        c = subprocess.run([CSC, "/nologo", "/langversion:7.3", "/out:" + exe, cs],
                           capture_output=True, text=True)
        errors, warnings = diag(c.stdout, "error"), diag(c.stdout, "warning")
        r = {"kind": it["kind"], "display": "\n".join(it["body"]), "program": src,
             "compiled": c.returncode == 0, "errors": errors, "warnings": warnings,
             "stdout": None, "exc": None, "exit": None}
        if c.returncode == 0:
            p = subprocess.run([exe], capture_output=True, text=True, timeout=30)
            out = p.stdout.replace("\r\n", "\n")
            if out.endswith("\n"):
                out = out[:-1]
            r["stdout"], r["exit"] = out, p.returncode
            if p.returncode != 0:
                first = [l for l in p.stderr.splitlines() if l.strip()]
                r["exc"] = first[0].strip() if first else "exit %d" % p.returncode
        results[it["id"]] = r

        problems = []
        kind, codes = it["kind"], it["codes"]
        if kind in ("run", "full", "warn", "rte"):
            if not r["compiled"]:
                problems.append("did not compile: %s" % errors)
            else:
                if kind == "rte":
                    if r["exit"] == 0:
                        problems.append("expected a runtime exception")
                elif r["exit"] != 0:
                    problems.append("runtime failure: %s" % r["exc"])
                if kind == "warn" and not set(codes) <= set(w["code"] for w in warnings):
                    problems.append("warnings %s lack %s" % ([w["code"] for w in warnings], codes))
                norm = lambda s: "\n".join(l.rstrip() for l in s.split("\n")).rstrip("\n")
                if it["expect"] is not None and norm(r["stdout"]) != norm("\n".join(it["expect"])):
                    problems.append("output mismatch:\n--- expected\n%s\n--- actual\n%s"
                                    % ("\n".join(it["expect"]), r["stdout"]))
        elif kind == "err":
            if r["compiled"]:
                problems.append("expected compile error, but it compiled")
            elif sorted(e["code"] for e in errors) != sorted(codes):
                problems.append("errors %s != %s" % ([e["code"] for e in errors], codes))
        if problems:
            failures.append((it["id"], problems))
        status = "FAIL" if problems else "ok"
        detail = ",".join(e["code"] for e in errors) or (r["exc"] or "")
        print("%-8s %-5s %s" % (it["id"], status, detail))

    json.dump(results, open(os.path.join(HERE, "results.json"), "w", encoding="utf-8"), indent=1)
    print("\n%d/%d examples verified" % (len(items) - len(failures), len(items)))
    for fid, probs in failures:
        print("\n##", fid)
        for p in probs:
            print(p)
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
