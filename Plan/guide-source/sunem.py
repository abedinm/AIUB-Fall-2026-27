import sys

path = sys.argv[1]
s = open(path, encoding="utf-8").read()

a = s.index("{ d: `Sat Nov 7`")
b = s.index("{ d: `Sun Nov 8`")
lines = s[a:b].split("\n")
rows = [i for i, l in enumerate(lines) if l.startswith("[`")]
assert lines[rows[7]].startswith("[`14:20-15:35`,`-`,`Shower")
lines[rows[8]:] = [
    "[`23:10-00:25`,`AI`,`AI only, with the AI session: UCS, A*, agent diagrams, PEAS, p10 traps.`,`The AI session's checks.`],",
    "[`00:25`,`-`,`Sleep. Phone alarm 07:00 (AI exam at 9:00).`,``]]},",
    ""]
sat = "\n".join(lines)

c = s.index("[`15:00-17:00`,`EXAM`,`EM midterm")
sun = s[b:c]
i = sun.index("[`11:30-11:55`,`EM`")
assert "[`13:45-14:15`,`EM`" in sun[i:]
sun = sun[:i] + r"""[`11:00-11:15`,`-`,`Out of the hall: water, toilet. Don't discuss the AI paper.`,``],
[`11:15-11:40`,`EM`,`Productivity & Competitveness.pdf sl. 4, 12-17: productivity = output / input, single vs multifactor, growth %. Redo the smart-watch example (sl. 18-19) covered.`,`Both MFP numbers match sl. 18-19.`],
[`11:45-12:10`,`EM`,`Strategic Capacity Planning.pdf sl. 4-5 and 16: efficiency, utilization, P = Q(R-v) - FC. Redo the pies example (sl. 17) covered.`,`All four answers match sl. 18.`],
[`12:15-12:40`,`EM`,`Forecasting & Accuracy.pdf sl. 13-25: naive, moving average, weighted moving average, exponential smoothing. Then Practice #3 (a)-(d) on sl. 46.`,`Matches sl. 47-48.`],
[`12:40-13:10`,`-`,`Lunch`,``],
[`13:10-13:35`,`EM`,`Sl. 30-41: least squares (b and a), then MAD, MSE (divide by n-1), MAPE. Redo Practice #1 (sl. 34), then Practice #3 (e).`,`Practice #1 matches sl. 35. MAPE: ask the EM session (sl. 49 is wrong).`],
[`13:40-14:05`,`EM`,`Capacity sl. 10; make vs buy (sl. 25, redo with sl. 26 covered); chargers (sl. 19) covered.`,`Make/buy matches sl. 26. Chargers 10,500 and $46,000 at 22,000.`],
[`14:10-14:30`,`EM`,`One page from memory: every formula from today, plus the lists (8 determinants, 3 strategies).`,`Written without looking, then checked against the slides.`],
[`14:30-14:45`,`-`,`Walk to the exam room. Read your one-page sheet only.`,``],
"""
s = s[:a] + sat + sun + s[c:]
old = "[`07:00-07:30`,`-`,`Up, wash, breakfast`,``],"
assert s.count(old) == 1
s = s.replace(old, "[`07:00-07:30`,`-`,`Up, wash, breakfast. Pack calculator, and laptop or phone with the EM PDFs.`,``],")
assert "midterm-plan-ticks-v10" in s
s = s.replace("midterm-plan-ticks-v10", "midterm-plan-ticks-v11")
open(path, "w", encoding="utf-8").write(s)
print("ok")
