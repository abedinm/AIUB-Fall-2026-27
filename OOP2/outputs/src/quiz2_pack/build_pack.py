import html, json, os, re, subprocess, sys
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import CSharpLexer
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
R = json.load(open(r"F:\outputs\aiub-oop2\src\results.json", encoding="utf-8"))
OUT = r"F:\outputs\midterm-plan\OOP2-Quiz2-Pack.pdf"
FMT = HtmlFormatter(cssclass="hl", style="default")
esc = html.escape

TIMETABLE = [
    ("Mon 16 Nov", "20:10-20:55", "45", "pp 2-3", "Read the cheat sheet. Then, on blank paper, write the child-class recipe and the two-question rule from memory.", "Your paper matches pp 2-3 with nothing missing; any miss rewritten once."),
    ("", "21:55-22:35", "40", "pp 4-5, key p 8", "Re-trace T1, T2, T3 on paper with a variable table, then check.", "All three outputs match line for line; misses added to the Miss log."),
    ("Tue 17 Nov", "19:00-19:50", "50", "90-Minutes PDF pp 10-11, key pp 17-18", "Q6-Q8 traces and Q9-Q12 compile-or-not, on paper, then check.", "All 7 marked; every miss re-traced."),
    ("", "19:50-20:05", "15", "", "Break", ""),
    ("", "20:05-20:45", "40", "pp 6-7", "Mini-quiz, closed book, 40-minute timer. No cheat sheet.", "Every question has a written answer when the timer ends."),
    ("", "20:45-20:55", "10", "", "Break", ""),
    ("", "20:55-21:35", "40", "pp 8-10", "Mark the mini-quiz. Re-trace every missed trace; compare Part D line by line.", "Score written on top; every miss in the Miss log."),
    ("Wed 18 Nov", "07:15-07:30", "15", "pp 2-3", "Cheat sheet once, before Python Quiz 2 at 08:00.", "Every rule on pp 2-3 read once."),
    ("", "10:00-10:20", "20", "your Tue misses (Miss log)", "After the Python viva: redo only what you missed on Tuesday. Nothing new.", "Every Tuesday miss redone correctly, before the 10:20 quiz."),
]


def code_src(name):
    p = os.path.join(HERE, name + ".cs")
    if os.path.exists(p):
        return open(p, encoding="utf-8").read().rstrip("\n")
    return R[name]["display"].rstrip("\n")


def hl(name, cls="hl"):
    return highlight(code_src(name), CSharpLexer(), HtmlFormatter(cssclass=cls, style="default"))


CSC = r"C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Current\Bin\Roslyn\csc.exe"


def out(name):
    exe = os.path.join(HERE, name + ".exe")
    if name not in R and not os.path.exists(exe):
        subprocess.run([CSC, "/nologo", "/langversion:7.3", "/out:" + exe, os.path.join(HERE, name + ".cs")], check=True)
    if os.path.exists(exe):
        text = subprocess.run([exe], capture_output=True, text=True, check=True).stdout
    else:
        text = R[name]["stdout"]
    return "<pre class='out'>%s</pre>" % esc(text.rstrip("\n"))


def timetable():
    rows = []
    for day, t, m, pages, task, done in TIMETABLE:
        cls = " class='brk'" if task == "Break" else ""
        rows.append("<tr%s><td>%s</td><td class='t'>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>"
                    % (cls, day, t, m, esc(pages), esc(task), esc(done)))
    total = sum(int(r[2]) for r in TIMETABLE if r[4] != "Break")
    return ("<table class='tt'><tr><th>Day</th><th>Time</th><th>Min</th><th>Pages</th><th>Task</th><th>Done when</th></tr>%s</table>"
            "<p class='small'>Study time %d min (%.1f h) plus breaks.</p>") % ("".join(rows), total, total / 60)


def expand(src):
    src = src.replace("[[timetable]]", timetable())
    src = re.sub(r"\[\[codefile:(\w+)\]\]", lambda m: hl(m.group(1)), src)
    src = re.sub(r"\[\[code2:(\w+)\]\]", lambda m: hl(m.group(1), "hl two"), src)
    src = re.sub(r"\[\[out:(\w+)\]\]", lambda m: out(m.group(1)), src)
    left = re.findall(r"\[\[[^\]]*\]\]", src)
    if left:
        sys.exit("unexpanded: %s" % left)
    return src


CSS = """
@page { size: A4; margin: 11mm 12mm 13mm 12mm; }
body { font-family: 'Segoe UI', Arial, sans-serif; font-size: 9.2pt; color: #1a1a1a; line-height: 1.3; margin: 0; }
section.page { break-before: page; }
h1 { font-size: 16pt; margin: 0 0 4pt; color: #1f3557; } h2 { font-size: 11.5pt; margin: 9pt 0 4pt; color: #1f3557; border-bottom: 1.2pt solid #1f3557; }
h3 { font-size: 10pt; margin: 7pt 0 3pt; color: #1f3557; }
.kicker { font-size: 8pt; letter-spacing: .06em; text-transform: uppercase; color: #a8863e; font-weight: 700; }
.sub { margin: 0 0 6pt; } .small { font-size: 8.4pt; color: #333; margin: 3pt 0; }
table { border-collapse: collapse; width: 100%; margin: 2pt 0 4pt; } td, th { border: 0.5pt solid #c4c8d0; padding: 2pt 4pt; vertical-align: top; text-align: left; }
th { background: #eef2f7; } tr { break-inside: avoid; }
.tt td.t { white-space: nowrap; } .tt tr.brk td { color: #888; background: #fafafa; }
.box { border-left: 3pt solid #1f3557; background: #f4f7fb; padding: 4pt 7pt; margin: 5pt 0; }
.key-rule { border: 1pt solid #a8863e; background: #fffaf0; padding: 4pt 7pt; margin: 5pt 0; }
.cols { display: flex; gap: 10pt; } .cols > div { flex: 1; min-width: 0; }
code, pre { font-family: Consolas, 'Cascadia Mono', monospace; font-size: 7.9pt; } code { background: #f1f3f6; padding: 0 1.5pt; }
pre { margin: 0; white-space: pre; line-height: 1.22; }
.hl { background: #fbfbfc; border: 0.5pt solid #d9dce2; padding: 4pt 6pt; margin: 2pt 0 4pt; }
.hl.two pre { column-count: 2; column-gap: 12pt; column-rule: 0.5pt solid #e0e0e0; }
.out { background: #14181f; color: #e8e8e8; padding: 4pt 6pt; border-radius: 2pt; margin: 2pt 0 4pt; }
ol.tight, ul.tight { margin: 2pt 0; padding-left: 15pt; } ol.tight li, ul.tight li { margin: 1pt 0; }
.qgrid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 6pt; } .qgrid .hl { padding: 3pt 4pt; } .qgrid pre { font-size: 7.4pt; }
ol.mcq { padding-left: 16pt; margin: 2pt 0; } ol.mcq li { margin: 0 0 4pt; }
.errs td:first-child, .errs td:nth-child(3) { white-space: nowrap; width: 1%; font-weight: 600; }
.q { margin: 4pt 0 1pt; } .map td:first-child { white-space: nowrap; }
""" + FMT.get_style_defs(".hl")

body = expand(open(os.path.join(HERE, "pack.html"), encoding="utf-8").read())
doc = "<!doctype html><html><head><meta charset='utf-8'><title>OOP2 Quiz 2 Pack</title><style>%s</style></head><body>%s</body></html>" % (CSS, body)
tmp = os.path.join(HERE, "pack_render.html")
open(tmp, "w", encoding="utf-8").write(doc)
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page()
    pg.goto("file:///" + tmp.replace("\\", "/"))
    pg.wait_for_timeout(300)
    pg.pdf(path=OUT, format="A4", print_background=True, prefer_css_page_size=True,
           display_header_footer=True, header_template="<div></div>",
           footer_template="<div style='font-size:8pt;width:100%;text-align:center;color:#666;font-family:Segoe UI,Arial'>OOP2 Quiz 2 pack &middot; page <span class='pageNumber'></span> of <span class='totalPages'></span></div>")
    b.close()
print(OUT)
