import sys

import fitz

src_path, out_path = sys.argv[1], sys.argv[2]
# booklet pages (1-based) in study order: Java->C#, inheritance 2.1-2.3, 2.5-2.6, traces T2.1-2.2,
# polymorphism 3.1-3.3, abstract 3.5, quiz-level A1-A3, cheat sheet, answers (T, A)
PICK = [3, 13, 14, 15, 17, 19, 22, 23, 24, 26, 33, 34, 45, 46, 47, 49]

src = fitz.open(src_path)
out = fitz.open()
w, h = src[0].rect.width, src[0].rect.height
cover = out.new_page(width=w, height=h)

ink, red, grey = (0.08, 0.08, 0.11), (0.86, 0.15, 0.15), (0.42, 0.42, 0.46)
cover.draw_rect(fitz.Rect(0, 0, w, 150), color=None, fill=ink)
cover.insert_text((40, 70), "OOP2 QUIZ 2", fontname="hebo", fontsize=34, color=(1, 1, 1))
cover.insert_text((40, 110), "TONIGHT ONLY: 16 PAGES", fontname="hebo", fontsize=22, color=(0.98, 0.8, 0.08))
cover.insert_text((40, 185), "Skip the rest of the big booklet. Ignore the times printed on the pages.", fontname="helv", fontsize=11.5, color=ink)

rows = [
    ("17:45-18:00", "p. 2", "Java to C#: what changes"),
    ("18:00-19:00", "p. 3-6", "Inheritance: class B : A, constructor order, base(...), hiding with new"),
    ("", "p. 7", "Practice T2.1-T2.2, then check on p. 15-16"),
    ("19:00-19:15", "", "Break"),
    ("19:15-20:15", "p. 8-11", "Polymorphism: parent variable holds a child, virtual/override, override vs new, abstract"),
    ("20:15-21:00", "p. 12-13", "Quiz-level traces A1-A3, then check on p. 17"),
    ("21:00-21:15", "p. 14", "Cheat sheet: say every rule out loud once"),
    ("21:15-21:45", "", "Break, dinner. Then the EM test at 21:45"),
    ("Wed 06:45-07:30", "p. 14", "Cheat sheet again, then redo every trace you missed. No new pages."),
]
y = 225
for t, p, what in rows:
    cover.draw_line(fitz.Point(40, y - 16), fitz.Point(w - 40, y - 16), color=(0.88, 0.87, 0.84), width=0.8)
    cover.insert_text((40, y), t, fontname="hebo", fontsize=12, color=red if t.startswith("Wed") else ink)
    cover.insert_text((150, y), p, fontname="hebo", fontsize=12, color=grey)
    cover.insert_textbox(fitz.Rect(215, y - 12, w - 40, y + 30), what, fontname="helv", fontsize=11, color=ink)
    y += 46

cover.insert_text((40, y + 10), "Rule: trace on paper first, check the answer second. A miss = re-trace it, don't just read the answer.",
                  fontname="helv", fontsize=10, color=grey)

for p in PICK:
    out.insert_pdf(src, from_page=p - 1, to_page=p - 1)
out.save(out_path)
print("pages", len(out))
