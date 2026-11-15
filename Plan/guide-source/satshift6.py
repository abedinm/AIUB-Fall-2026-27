import sys

path = sys.argv[1]
s = open(path, encoding="utf-8").read()

def retime(line, t):
    return "[`" + t + line[line.index("`", 2):]

a = s.index("{ d: `Sat Nov 7`")
b = s.index("{ d: `Sun Nov 8`")
lines = s[a:b].split("\n")
rows = [i for i, l in enumerate(lines) if l.startswith("[`")]
assert lines[rows[7]].startswith("[`14:20-15:10`,`-`,`Shower")
assert lines[rows[18]].startswith("[`19:45-20:10`,`EM`,`WS2 Q2")
assert lines[rows[19]].startswith("[`20:10-20:40`,`-`,`Dinner`")
assert lines[rows[23]].startswith("[`22:15-22:40`,`EM`,`WS1 Q3 and Q4")
assert lines[rows[26]].startswith("[`00:00`")

T = {7: "14:20-15:35",
     8: "15:35-16:00", 9: "16:05-16:30", 10: "16:35-17:00", 11: "17:05-17:30",
     12: "17:30-17:40",
     13: "17:40-18:05", 14: "18:10-18:35", 15: "18:40-19:05", 16: "19:10-19:35", 17: "19:40-20:05",
     19: "20:05-20:40",
     24: "23:15-23:40", 25: "23:45-00:10", 26: "00:25"}
for k, t in T.items():
    lines[rows[k]] = retime(lines[rows[k]], t)

ws2q2 = retime(lines[rows[18]], "22:45-23:10")
lines.insert(rows[24], ws2q2)
del lines[rows[18]]

s = s[:a] + "\n".join(lines) + s[b:]
assert "midterm-plan-ticks-v9" in s
s = s.replace("midterm-plan-ticks-v9", "midterm-plan-ticks-v10")
open(path, "w", encoding="utf-8").write(s)
print("ok")
