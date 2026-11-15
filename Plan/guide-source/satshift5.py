import sys

path = sys.argv[1]
s = open(path, encoding="utf-8").read()

def retime(line, t):
    return "[`" + t + line[line.index("`", 2):]

a = s.index("{ d: `Sat Nov 7`")
b = s.index("{ d: `Sun Nov 8`")
lines = s[a:b].split("\n")
rows = [i for i, l in enumerate(lines) if l.startswith("[`")]
assert lines[rows[7]].startswith("[`14:10-14:45`,`-`,`Lunch`")
assert lines[rows[19]].startswith("[`19:45-20:15`,`-`,`Dinner`")
assert lines[rows[20]].startswith("[`20:15-20:40`,`EM`,`WS1 Q3 and Q4")
assert lines[rows[24]].startswith("[`22:15-22:40`,`EM`,`WS2 Q3")

NEW = ["14:20-15:10",
       "15:10-15:35", "15:40-16:05", "16:10-16:35", "16:40-17:05",
       "17:05-17:15",
       "17:15-17:40", "17:45-18:10", "18:15-18:40", "18:45-19:10", "19:15-19:40", "19:45-20:10",
       "20:10-20:40"]
for i, t in zip(rows[7:20], NEW):
    lines[i] = retime(lines[i], t)
lines[rows[7]] = lines[rows[7]].replace("`Lunch`", "`Shower (10 min), lunch (20 min)`")

ws2q3 = lines[rows[24]]
lines[rows[24]] = retime(lines[rows[20]], "22:15-22:40")
del lines[rows[20]]
sat = "\n".join(lines)

c = s.index("{ d: `Mon Nov 9`") if "{ d: `Mon Nov 9`" in s else None
sun = s[b:c]
old_lunch = "[`12:30-13:30`,`-`,`Lunch, rest`,``],"
anchor = "[`13:45-14:15`,`EM`"
assert old_lunch in sun and anchor in sun
sun = sun.replace(old_lunch, "[`12:30-13:10`,`-`,`Lunch, rest`,``],")
sun = sun.replace(anchor, retime(ws2q3, "13:15-13:40") + "\n" + anchor)

s = s[:a] + sat + sun + (s[c:] if c is not None else "")
assert "midterm-plan-ticks-v8" in s
s = s.replace("midterm-plan-ticks-v8", "midterm-plan-ticks-v9")
open(path, "w", encoding="utf-8").write(s)
print("ok")
