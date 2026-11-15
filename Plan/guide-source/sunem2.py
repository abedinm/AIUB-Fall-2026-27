import sys

path = sys.argv[1]
s = open(path, encoding="utf-8").read()
b = s.index("{ d: `Sun Nov 8`")
c = s.index("[`15:00-17:00`,`EXAM`,`EM midterm")
sun = s[b:c]

NEW = {
    "11:15-11:40": "[`11:15-11:40`,`EM`,`Productivity: EM WS1 Productivity.pdf Q4 (a)-(c) alone, key covered.`,`0.67 / 0.30 and 238.10 / 141.41 / 179.01.`],",
    "11:45-12:10": "[`11:45-12:10`,`EM`,`Capacity: the EM session posts sl. 5 (efficiency, utilization) and the pies example (sl. 17) as short steps; redo pies covered.`,`All four answers match sl. 18.`],",
    "12:15-12:40": "[`12:15-12:40`,`EM`,`Forecasting & Accuracy.pdf Practice #3 (a)-(d) on sl. 46, alone.`,`Matches sl. 47-48.`],",
    "13:10-13:35": "[`13:10-13:35`,`EM`,`Practice #1 least squares alone (15 min), then MAD, MSE (n-1), MAPE worked with the EM session on the Practice #3 data.`,`Practice #1 matches sl. 35. Sl. 49's MAPE is wrong: use the EM session's.`],",
    "13:40-14:05": "[`13:40-14:05`,`EM`,`Capacity: sl. 10 machines, make vs buy (sl. 25-26), chargers (sl. 19) as the EM session's short steps, each redone covered.`,`Make/buy matches sl. 26. Chargers 10,500 and $46,000 at 22,000.`],",
}
lines = sun.split("\n")
for k, row in NEW.items():
    idx = [i for i, l in enumerate(lines) if l.startswith("[`" + k + "`,`EM`")]
    assert len(idx) == 1, k
    lines[idx[0]] = row
s = s[:b] + "\n".join(lines) + s[c:]
s = s.replace("midterm-plan-ticks-v11", "midterm-plan-ticks-v12")
open(path, "w", encoding="utf-8").write(s)
print("ok")
