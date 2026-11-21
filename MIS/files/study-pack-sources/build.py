import os, sys, subprocess, pathlib, fitz
HF = os.environ.get("HANDFONT")

EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
src, out = pathlib.Path(sys.argv[1]).resolve(), pathlib.Path(sys.argv[2])
tmp = src.with_suffix(".raw.pdf")
tmp.unlink(missing_ok=True)
subprocess.run([EDGE, "--headless", "--disable-gpu", "--no-pdf-header-footer", f"--user-data-dir={src.parent / 'edgeprof'}",
                f"--print-to-pdf={tmp}", src.as_uri()], check=True, timeout=120)
doc = fitz.open(tmp)
n = doc.page_count
for i, p in enumerate(doc, 1):
    w, h = p.rect.width, p.rect.height
    p.insert_textbox(fitz.Rect(0, h - 34, w, h - 14), f"Page {i} of {n}", fontsize=12, align=1, fontname="hand" if HF else "helv", fontfile=HF)
out.parent.mkdir(parents=True, exist_ok=True)
doc.save(out)
assert fitz.open(out).page_count == n
print(out, n, "pages")
