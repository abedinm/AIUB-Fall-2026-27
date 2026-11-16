import sys

p = sys.argv[1]
s = open(p, encoding="utf-8").read()
lines = s.split("\n")

def take(prefix):
    idx = [i for i, l in enumerate(lines) if l.startswith(prefix)]
    assert len(idx) == 1, prefix
    return idx[0]

b1 = take("[`19:40-20:25`,`MIS`,`MIS five forces")
b2 = take("[`20:30-21:15`,`MIS`,`4 strategies")
thu = take("{ d: `Thu Nov 19`, n: `MIS quiz prep`, r: [")
b3 = take("[`19:00-19:30`,`MIS`,`Ch 1-2 refresher")
b4 = take("[`19:35-20:15`,`MIS`,`MIS-Quiz2-Pack.pdf p4-5")
b5 = take("[`20:20-20:40`,`MIS`,`Only if Ch 9")
assert (b2, thu, b3, b4, b5) == (b1 + 1, b1 + 3, b1 + 4, b1 + 5, b1 + 6), (b1, b2, thu, b3, b4, b5)

row1 = lines[b1].replace("[`19:40-20:25`", "[`19:00-19:45`", 1)
row2 = lines[b2].replace("[`20:30-21:15`", "[`19:50-20:35`", 1)
assert row2.endswith("],")
row4 = lines[b4].replace("redo the Wednesday MIS block it points to", "redo the Thursday MIS block it points to")
assert row4 != lines[b4]

new = [
    lines[b1 + 2],  # Wed sleep row stays as Wednesday's last row
    "{ d: `Thu Nov 19`, n: `AI lab, MIS quiz prep part 1`, r: [",
    "[`15:00-17:20`,`AI`,`Lab class, room DS0208.`,``],",
    row1,
    row2[:-1] + "]},",
    "{ d: `Fri Nov 20`, n: `MIS quiz prep part 2`, r: [",
    lines[b3],
    row4,
    lines[b5],
]
lines[b1:b5 + 1] = new
s = "\n".join(lines)
assert s.count("const KEY = 'midterm-plan-ticks-v18';") == 1
s = s.replace("const KEY = 'midterm-plan-ticks-v18';", "const KEY = 'midterm-plan-ticks-v19';")
open(p, "w", encoding="utf-8").write(s)
print("ok")
