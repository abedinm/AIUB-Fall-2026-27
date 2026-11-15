import sys

path = sys.argv[1]
s = open(path, encoding="utf-8").read()

SAT = r"""{ d: `Sat Nov 7`, n: `AI first, then EM math from zero`, r: [
[`10:08-10:45`,`-`,`Up, wash, breakfast`,``],
[`10:45-11:10`,`AI`,`Video chapter 1 at normal speed, then solve it on paper (the AI session gives each chapter).`,`Your answer matches the AI session's check.`],
[`11:15-11:40`,`AI`,`Video chapter 2, then solve it on paper.`,`Your answer matches the AI session's check.`],
[`11:45-12:10`,`AI`,`Video chapter 3, then solve it on paper.`,`Your answer matches the AI session's check.`],
[`12:15-12:40`,`AI`,`Video chapter 4, then solve it on paper.`,`Your answer matches the AI session's check.`],
[`12:45-13:10`,`AI`,`Video chapter 5, then solve it on paper.`,`Your answer matches the AI session's check.`],
[`13:15-13:40`,`AI`,`Video chapter 6, then solve it on paper.`,`Your answer matches the AI session's check.`],
[`13:40-14:15`,`-`,`Lunch`,``],
[`14:15-14:40`,`EM`,`Productivity & Competitveness.pdf sl. 4, 12-17: productivity = output / input, single vs multifactor. Redo the smart-watch example (sl. 18-19) covered.`,`Both MFP numbers match sl. 18-19.`],
[`14:45-15:10`,`EM`,`EM WS1 Productivity.pdf Q1 and Q2, key covered.`,`Match the key on WS1's last page.`],
[`15:15-15:40`,`EM`,`Strategic Capacity Planning.pdf sl. 4-5 and 16: efficiency, utilization, P = Q(R-v) - FC. Redo the pies example (sl. 17) covered.`,`All four answers match sl. 18.`],
[`15:45-16:10`,`EM`,`Capacity sl. 10, then EM WS3 CP Q&A.pdf Q1 and Q4; then make vs buy: sl. 25, redo with sl. 26 covered.`,`WS3 matches the page-2 key; make/buy matches sl. 26.`],
[`16:10-16:30`,`-`,`Rest`,``],
[`16:30-16:55`,`EM`,`Forecasting & Accuracy.pdf sl. 13-21: naive, moving average, weighted moving average. Then Practice #3 (a)-(c) on sl. 46.`,`Matches sl. 47.`],
[`17:00-17:25`,`EM`,`Sl. 22-25: exponential smoothing. Redo the sl. 24 table, then Practice #3 (d).`,`Matches sl. 24 and 48.`],
[`17:30-17:55`,`EM`,`Sl. 30-35: least squares, the b and a formulas. Redo Practice #1 (sl. 34).`,`Equation, F7 and F8 match sl. 35.`],
[`18:00-18:25`,`EM`,`Sl. 36-41: MAD, MSE (divide by n-1), MAPE. Redo Technique 1, then Practice #3 (e). Send your MAPE to the EM session: sl. 49's MAPE column is wrong.`,`Technique 1 matches sl. 39.`],
[`18:30-18:55`,`EM`,`EM WS2 Forecasting.pdf Q1, solutions covered (printed under each question).`,`Matches the printed solution.`],
[`19:00-19:25`,`EM`,`WS2 Q2, solution covered.`,`Matches the printed solution.`],
[`19:30-20:15`,`-`,`Dinner`,``],
[`20:15-20:40`,`EM`,`WS1 Q3 and Q4, key covered.`,`Q3 4 workers, 1.6%. Q4 0.67 / 0.30 and 238.10 / 141.41 / 179.01.`],
[`20:45-21:10`,`AI`,`Night before: notes p10 traps and the p4 table. Read, cover, say aloud.`,`Every trap and the whole table said without looking.`],
[`21:15-21:40`,`EM`,`Capacity sl. 19 (chargers, cost-volume) covered; then WS3 Q2 and Q3.`,`Chargers 10,500 and $46,000 at 22,000. Q2 39,683 and $1.71. Q3 46,000; $3,000 / $8,200; 126,000.`],
[`21:45-22:10`,`EM`,`WS2 Q3, solution covered.`,`782 and 790.`],
[`22:15-22:40`,`EM`,`Theory 1: Capacity sl. 2-12, Forecasting sl. 8-11, then the EM session's drill items 10-15, 17, 18.`,`Answers sent to the EM session for marking.`],
[`22:45-23:10`,`EM`,`Theory 2: Intro to EM+Ops sl. 7, 11-15, 21; Intro of Ops Mgmt sl. 3, 6-9; Productivity sl. 10. Then drill items 1-9, 16, 19, 20.`,`Answers sent to the EM session for marking.`],
[`23:30`,`-`,`Sleep. Phone alarm 07:00 (AI exam at 9:00).`,``]]},
"""

a = s.index("{ d: `Sat Nov 7`")
b = s.index("{ d: `Sun Nov 8`")
s = s[:a] + SAT + s[b:]
open(path, "w", encoding="utf-8").write(s)
print("ok")
