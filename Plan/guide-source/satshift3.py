import sys

path = sys.argv[1]
s = open(path, encoding="utf-8").read()

a = s.index("{ d: `Sat Nov 7`")
b = s.index("{ d: `Sun Nov 8`")
block = s[a:b]
lines = block.split("\n")

NEW = ["10:08-11:15",
       "11:15-11:40", "11:45-12:10", "12:15-12:40", "12:45-13:10", "13:15-13:40", "13:45-14:10",
       "14:10-14:45",
       "14:45-15:10", "15:15-15:40", "15:45-16:10", "16:15-16:40",
       "16:40-16:50",
       "16:50-17:15", "17:20-17:45", "17:50-18:15", "18:20-18:45", "18:50-19:15", "19:20-19:45",
       "19:45-20:15"]
OLD_FIRST, OLD_LAST = "10:08-10:45", "19:30-20:15"

rows = [i for i, l in enumerate(lines) if l.startswith("[`")]
assert lines[rows[0]].startswith("[`" + OLD_FIRST + "`")
assert lines[rows[len(NEW) - 1]].startswith("[`" + OLD_LAST + "`")
for i, t in zip(rows, NEW):
    end = lines[i].index("`", 2)
    lines[i] = "[`" + t + lines[i][end:]

block = "\n".join(lines).replace("`Video chapter 1 at normal speed,", "`Coder Bhai video, chapter 1 at normal speed,")
s = s[:a] + block + s[b:]
open(path, "w", encoding="utf-8").write(s)
print("ok")
