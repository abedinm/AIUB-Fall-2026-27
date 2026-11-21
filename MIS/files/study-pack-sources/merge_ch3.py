import fitz
HF = "C:/Windows/Fonts/Inkfree.ttf"
D = "F:/outputs/midterm-plan/"
OUT = D + "MIS-Ch3-Quiz2-Focus.pdf"
SRC = {"Quiz2": "MIS-Quiz2-Pack.pdf", "Visual": "MIS-Visual-Sheets-Ch1-3.pdf",
       "Crash": "MIS-Crash-Notes-Ch1-3.pdf", "Pack 1": "MIS-Pack-1-Ch1-3.pdf"}
ORDER = [("Quiz2", [3]), ("Visual", [1, 2, 8]), ("Crash", range(11, 17)),
         ("Pack 1", range(18, 25)), ("Quiz2", range(4, 8))]
SKIP = "Ch 3 ONLY: skip MCQ 21-25 (Ch 1-2). Score out of 20, pass = 16."

out = fitz.open()
srcs = []
for name, pages in ORDER:
    d = fitz.open(D + SRC[name])
    srcs.append(d)
    for p in pages:
        out.insert_pdf(d, from_page=p - 1, to_page=p - 1)
        out[-1].src = f"{name} p{p}"
n = out.page_count
labels = [f"{name} p{p}" for name, pages in ORDER for p in pages]
for i, (pg, lab) in enumerate(zip(out, labels), 1):
    w = pg.rect.width
    rc = pg.insert_textbox(fitz.Rect(w - 260, 6, w - 14, 30), f"Ch 3 focus {i}/{n} | from {lab}",
                           fontsize=10, fontname="hand", fontfile=HF, color=(0.55, 0.1, 0.1), align=2)
    assert rc >= 0, (lab, rc)
    if lab in ("Quiz2 p4", "Quiz2 p5", "Quiz2 p6"):
        rc = pg.insert_textbox(fitz.Rect(14, 6, w - 270, 30), SKIP, fontsize=10, fontname="hand",
                               fontfile=HF, color=(0.8, 0, 0))
        assert rc >= 0, (lab, rc)
out.save(OUT)
assert fitz.open(OUT).page_count == n == 21
print(OUT, n, "pages")
