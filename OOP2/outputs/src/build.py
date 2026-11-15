"""Assemble the OOP2 crash-course PDF from content.html + results.json.

Run verify.py first. Two render passes resolve page numbers; the cover is
rendered separately (no footer) and prepended."""
import html, io, json, os, re, sys

from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import CSharpLexer
from playwright.sync_api import sync_playwright
from pypdf import PdfReader, PdfWriter

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = r"F:\outputs\aiub-oop2"
TARGETS = {
    "full": ("content.html", "cover.html", "OOP2-Quiz2-Crash-Course.pdf", "Quiz 2 crash course"),
    "quick": ("content_quick.html", "cover_quick.html", "OOP2-Quiz2-90-Minutes.pdf", "Quiz 2 in 90 minutes"),
    "mid": ("content_mid.html", "cover_mid.html", "OOP2-Midterm-3-Day-Workbook.pdf", "Midterm in 3 days"),
}
TARGET = sys.argv[1] if len(sys.argv) > 1 else "full"
CONTENT, COVER, OUT_NAME, LABEL = TARGETS[TARGET]
OUT_PDF = os.path.join(OUT_DIR, OUT_NAME)
WORK = os.path.join(HERE, "render")

R = json.load(open(os.path.join(HERE, "results.json"), encoding="utf-8"))
CSS = open(os.path.join(HERE, "style.css"), encoding="utf-8").read()
FMT = HtmlFormatter(nowrap=True)
LEX = CSharpLexer()
esc = html.escape


def code_html(i):
    # one block span per line: indentation becomes padding so wrapped lines hang under their own line
    lines = R[i]["display"].split("\n")
    spans = []
    for line in lines:
        body = line.lstrip(" ")
        h = highlight(body, LEX, FMT).rstrip("\n") if body else "&#160;"
        spans.append('<span class="ln" style="--i:%d">%s</span>' % (len(line) - len(body), h))
    cls = (" c2" if len(lines) > 30 else "") + (" long" if len(lines) > 110 else "")
    return '<pre class="code%s">%s</pre>' % (cls, "".join(spans))


def pre_cls(text):
    return ' class="c2"' if text and text.count("\n") > 14 else ""


def exc_text(r):
    return re.sub(r"^Unhandled Exception:\s*", "", r["exc"] or "")


def out_panel(i, label="Output"):
    r = R[i]
    parts = []
    if r["kind"] == "err":
        parts.append('<div class="olabel" style="color:#8e2c3a">Compiler error</div>')
        for e in r["errors"]:
            parts.append('<div class="errline">%s: %s</div>' % (e["code"], esc(e["msg"])))
    else:
        parts.append('<div class="olabel">%s</div>' % label)
        if r["stdout"]:
            parts.append("<pre%s>%s</pre>" % (pre_cls(r["stdout"]), esc(r["stdout"])))
        if r["kind"] == "rte":
            parts.append('<div class="errline">then crashes: %s</div>' % esc(exc_text(r)))
    return '<div class="out">%s</div>' % "".join(parts)


def ex(i):
    return '<div class="codewrap">%s%s</div>' % (code_html(i), out_panel(i))


def outonly(i):
    return '<div class="codewrap"><div class="out" style="border-top:0.7pt solid #e6e0cf;border-radius:3pt;margin-left:0">' \
           '<div class="olabel">Expected output</div><pre%s>%s</pre></div></div>' % (pre_cls(R[i]["stdout"]), esc(R[i]["stdout"]))


def question(label, hint, i):
    tag = ""
    if hint.startswith("+"):
        hint, tag = hint[1:].strip(), '<span class="t90">90 min only</span>'
    return ('<div class="q"><div class="qhead"><span class="qlabel">%s%s</span><span class="qhint">%s</span></div>'
            '<div class="qbody">%s</div></div>' % (esc(label), tag, esc(hint), code_html(i)))


def answer(label, i, why):
    r = R[i]
    parts = ['<div class="ans"><div class="ah"><span>%s</span></div>' % esc(label)]
    compile_q = label[0] in "KB"
    if r["kind"] == "err":
        parts.append('<div class="verdict bad">Does not compile</div>')
        for e in r["errors"]:
            parts.append('<div class="cmsg">%s: %s</div>' % (e["code"], esc(e["msg"])))
    elif r["kind"] == "rte":
        parts.append('<div class="verdict bad">Compiles, then crashes at run time</div>')
        if r["stdout"]:
            parts.append('<pre class="res">%s</pre>' % esc(r["stdout"]))
        parts.append('<div class="cmsg">%s</div>' % esc(exc_text(r)))
    else:
        if compile_q:
            parts.append('<div class="verdict good">Compiles and runs</div>')
        parts.append('<pre class="res">%s</pre>' % esc(r["stdout"]))
        if r["kind"] == "warn":
            for w in r["warnings"]:
                if w["code"] in ("CS0108", "CS1717"):
                    parts.append('<div class="cwarn">warning %s: %s</div>' % (w["code"], esc(w["msg"])))
    parts.append('<p class="why">%s</p></div>' % why.strip())
    return "".join(parts)


def expand(src, pages, markers=True):
    src = re.sub(r"\[\[include:([\w.-]+)\]\]",
                 lambda m: open(os.path.join(HERE, m.group(1)), encoding="utf-8").read(), src)
    src = re.sub(r"\[\[mk:([\w-]+)\]\]\s*<h3>", r"<h3>[[mk:\1]]", src)
    src = re.sub(r"\[\[mk:([\w-]+)\]\]",
                 lambda m: '<span class="mk">MK%sMK</span>' % m.group(1).replace("-", "_") if markers else "",
                 src)
    src = re.sub(r"\[\[page:([\w-]+)\]\]", lambda m: str(pages.get(m.group(1), "00")), src)
    src = re.sub(r"\[\[ex:(\w+)\]\]", lambda m: ex(m.group(1)), src)
    src = re.sub(r"\[\[outonly:(\w+)\]\]", lambda m: outonly(m.group(1)), src)
    src = re.sub(r"\[\[code:(\w+)\]\]", lambda m: '<div class="codewrap">%s</div>' % code_html(m.group(1)), src)
    src = re.sub(r"\[\[q:([^|\]]+)\|([^|\]]*)\|(\w+)\]\]",
                 lambda m: question(m.group(1), m.group(2), m.group(3)), src)
    src = re.sub(r"\[\[ans:([^|\]]+)\|(\w+)\|(.*?)\]\]",
                 lambda m: answer(m.group(1), m.group(2), m.group(3)), src, flags=re.S)
    left = re.findall(r"\[\[[^\]]*\]\]", src)
    if left:
        sys.exit("unexpanded macros: %s" % left[:5])
    return src


FOOTER = ('<div style="width:100%;font-family:\'Segoe UI\',Arial,sans-serif;font-size:7.5px;color:#8a909c;'
          'padding:0 16mm;display:flex;justify-content:space-between;letter-spacing:0.4px;">'
          '<span>CSC 3115 &#183; Object Oriented Programming 2 &#183; ' + LABEL + '</span>'
          '<span style="color:#a8863e;font-weight:600"><span class="pageNumber"></span></span></div>')


def page_doc(body):
    return ('<!doctype html><html><head><meta charset="utf-8"><title>OOP2 Quiz 2 Crash Course</title>'
            '<style>%s</style></head><body>%s</body></html>' % (CSS, body))


def render(page, html_text, pdf_path, footer=True):
    tmp = os.path.join(WORK, "_page.html")
    io.open(tmp, "w", encoding="utf-8").write(html_text)
    page.goto("file:///" + tmp.replace("\\", "/"))
    page.wait_for_timeout(300)
    kw = dict(path=pdf_path, format="A4", print_background=True, prefer_css_page_size=False)
    if footer:
        kw.update(margin={"top": "15mm", "bottom": "16mm", "left": "16mm", "right": "16mm"},
                  display_header_footer=True, header_template="<div></div>", footer_template=FOOTER)
    else:
        kw.update(margin={"top": "0", "bottom": "0", "left": "0", "right": "0"})
    page.pdf(**kw)


def marker_pages(pdf_path):
    pages = {}
    for n, p in enumerate(PdfReader(pdf_path).pages, start=1):
        text = (p.extract_text() or "").replace("\n", "").replace(" ", "")
        for m in re.findall(r"MK([A-Za-z0-9_]+?)MK", text):
            pages.setdefault(m.replace("_", "-"), n)
    return pages


def main():
    os.makedirs(WORK, exist_ok=True)
    os.makedirs(OUT_DIR, exist_ok=True)
    content = open(os.path.join(HERE, CONTENT), encoding="utf-8").read()
    cover = open(os.path.join(HERE, COVER), encoding="utf-8").read()
    body_pdf = os.path.join(WORK, "body.pdf")
    cover_pdf = os.path.join(WORK, "cover.pdf")

    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page()
        pages = {}
        for attempt in range(4):
            render(page, page_doc(expand(content, pages)), body_pdf)
            found = marker_pages(body_pdf)
            if found == pages:
                break
            pages = found
        else:
            sys.exit("page numbers did not settle: %s" % pages)
        n_marked = len(PdfReader(body_pdf).pages)
        render(page, page_doc(expand(content, pages, markers=False)), body_pdf)
        if len(PdfReader(body_pdf).pages) != n_marked:
            sys.exit("marker-free render changed the page count")
        render(page, expand(cover, pages, markers=False), cover_pdf, footer=False)
        browser.close()

    needed = set(re.findall(r"\[\[page:([\w-]+)\]\]", content))
    missing = needed - set(pages)
    if missing:
        sys.exit("markers not found: %s" % sorted(missing))

    w = PdfWriter()
    for src in (cover_pdf, body_pdf):
        for p in PdfReader(src).pages:
            w.add_page(p)
    w.add_metadata({"/Title": "OOP2 " + LABEL,
                    "/Subject": "CSC 3115 Object Oriented Programming 2, AIUB, Fall 2026-27"})
    with open(OUT_PDF, "wb") as f:
        w.write(f)
    n = len(PdfReader(OUT_PDF).pages)
    print("pages:", dict(sorted(pages.items(), key=lambda kv: kv[1])))
    print("wrote %s (%d pages, %.0f KB)" % (OUT_PDF, n, os.path.getsize(OUT_PDF) / 1024))


if __name__ == "__main__":
    main()
