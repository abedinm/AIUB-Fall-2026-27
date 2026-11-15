import sys

path = sys.argv[1]
s = open(path, encoding="utf-8").read()

a = s.index("{ d: `Sat Nov 7`")
b = s.index("{ d: `Sun Nov 8`")
block = s[a:b]
lines = block.split("\n")

i_ai = next(i for i, l in enumerate(lines) if l.startswith("[`20:45-21:10`,`AI`"))
assert lines[i_ai + 1].startswith("[`21:15-21:40`,`EM`")
assert lines[i_ai + 5].startswith("[`23:30`")

AI = ["[`20:45-21:10`,`AI`,`UCS trace, then the A* trace (the AI session coaches).`,`UCS to H gives 25; A* gives cost 7.`],",
      "[`21:15-21:40`,`AI`,`The 5 agent diagrams (p11-12), PEAS for the taxi, the 6 environment pairs, then the p10 traps.`,`All 5 diagrams drawn; every p10 trap answered with the answers covered.`],"]
NEW = ["21:45-22:10", "22:15-22:40", "22:45-23:10", "23:15-23:40"]
em = []
for l, t in zip(lines[i_ai + 1:i_ai + 5], NEW):
    end = l.index("`", 2)
    em.append("[`" + t + l[end:])
sleep = lines[i_ai + 5].replace("[`23:30`", "[`00:00`", 1)

lines[i_ai:i_ai + 6] = AI + em + [sleep]
s = s[:a] + "\n".join(lines) + s[b:]
s = s.replace("midterm-plan-ticks-v7", "midterm-plan-ticks-v8")
open(path, "w", encoding="utf-8").write(s)
print("ok")
