import sys

path = sys.argv[1]
s = open(path, encoding="utf-8").read()

WEEKEND = r"""{ d: `Sat Nov 7`, n: `AI first, then EM math from zero`, r: [
[`09:00-09:30`,`-`,`Up, wash, breakfast`,``],
[`09:30-09:45`,`AI`,`The Andrew video once at 1.25x (the AI session has it).`,`Watched once, no pausing to take notes.`],
[`09:45-10:10`,`AI`,`Redo the BFS and UCS traces on paper, then check against notes p5-6.`,`UCS to H gives 25.`],
[`10:15-10:40`,`AI`,`Redo the A* trace and the admissible/consistent Ex 2 (notes p8).`,`A* gives cost 7; Ex 2 comes out "not consistent".`],
[`10:45-11:10`,`AI`,`Write the complexity table from memory (p4), then draw the 5 agent diagrams (p11-12).`,`Table matches p4; all 5 diagrams drawn.`],
[`11:15-11:40`,`AI`,`The 6 environment pairs, PEAS for the taxi, the p10 traps.`,`All p10 traps answered right with the answers covered.`],
[`11:45-12:10`,`AI`,`Practice: A* on the notes p9 Ex 3 graph, then IDS on the p7 tree (goal K).`,`A* gives S-A-D-F-G, cost 6; IDS finds K at limit 3.`],
[`12:10-13:00`,`-`,`Lunch`,``],
[`13:00-13:25`,`EM`,`Productivity & Competitveness.pdf sl. 4, 12-17: productivity = output / input, single vs multifactor. Redo the smart-watch example (sl. 18-19) covered.`,`Both MFP numbers match sl. 18-19.`],
[`13:30-13:55`,`EM`,`EM WS1 Productivity.pdf Q1 and Q2, key covered.`,`Match the key on WS1's last page.`],
[`14:00-14:25`,`EM`,`Strategic Capacity Planning.pdf sl. 4-5 and 16: efficiency, utilization, P = Q(R-v) - FC. Redo the pies example (sl. 17) covered.`,`All four answers match sl. 18.`],
[`14:30-14:55`,`EM`,`Capacity sl. 10, then EM WS3 CP Q&A.pdf Q1 and Q4; then make vs buy: sl. 25, redo with sl. 26 covered.`,`WS3 matches the page-2 key; make/buy matches sl. 26.`],
[`15:00-15:30`,`-`,`Rest`,``],
[`15:30-15:55`,`EM`,`Forecasting & Accuracy.pdf sl. 13-21: naive, moving average, weighted moving average. Then Practice #3 (a)-(c) on sl. 46.`,`Matches sl. 47.`],
[`16:00-16:25`,`EM`,`Sl. 22-25: exponential smoothing. Redo the sl. 24 table, then Practice #3 (d).`,`Matches sl. 24 and 48.`],
[`16:30-16:55`,`EM`,`Sl. 30-35: least squares, the b and a formulas. Redo Practice #1 (sl. 34).`,`Equation, F7 and F8 match sl. 35.`],
[`17:00-17:25`,`EM`,`Sl. 36-41: MAD, MSE (divide by n-1), MAPE. Redo Technique 1, then Practice #3 (e). Send your MAPE to the EM session: sl. 49's MAPE column is wrong.`,`Technique 1 matches sl. 39.`],
[`17:30-17:55`,`EM`,`EM WS2 Forecasting.pdf Q1, solutions covered (printed under each question).`,`Matches the printed solution.`],
[`18:00-18:25`,`EM`,`WS2 Q2, solution covered.`,`Matches the printed solution.`],
[`18:30-19:15`,`-`,`Dinner`,``],
[`19:15-19:40`,`EM`,`WS1 Q3 and Q4, key covered.`,`Q3 4 workers, 1.6%. Q4 0.67 / 0.30 and 238.10 / 141.41 / 179.01.`],
[`19:45-20:10`,`EM`,`Capacity sl. 19 (chargers, cost-volume) covered; then WS3 Q2 and Q3.`,`Chargers 10,500 and $46,000 at 22,000. Q2 39,683 and $1.71. Q3 46,000; $3,000 / $8,200; 126,000.`],
[`20:15-20:40`,`EM`,`WS2 Q3, solution covered.`,`782 and 790.`],
[`20:45-21:10`,`AI`,`Night before: notes p10 traps and the p4 table. Read, cover, say aloud.`,`Every trap and the whole table said without looking.`],
[`21:10-21:30`,`-`,`Break`,``],
[`21:30-21:55`,`EM`,`Theory 1: Capacity sl. 2-12, Forecasting sl. 8-11, then the EM session's drill items 10-15, 17, 18.`,`Answers sent to the EM session for marking.`],
[`22:00-22:25`,`EM`,`Theory 2: Intro to EM+Ops sl. 7, 11-15, 21; Intro of Ops Mgmt sl. 3, 6-9; Productivity sl. 10. Then drill items 1-9, 16, 19, 20.`,`Answers sent to the EM session for marking.`],
[`22:45`,`-`,`Sleep. Phone alarm 07:00 (AI exam at 9:00).`,``]]},
{ d: `Sun Nov 8`, n: `AI exam + EM exam`, r: [
[`07:00-07:30`,`-`,`Up, wash, breakfast`,``],
[`07:30-08:00`,`AI`,`Read only: notes p10 and p4.`,`Nothing new.`],
[`09:00-11:00`,`EXAM`,`AI midterm. Bring your permit.`,``],
[`11:30-11:55`,`EM`,`Write one page: every formula from Saturday, plus the lists (8 determinants, 3 strategies, MAD/MSE/MAPE).`,`Written without looking.`],
[`12:00-12:25`,`EM`,`Closed book: WS1 Q4(a), WS2 Q1(a-b), WS3 Q3.`,`Each matches its key.`],
[`12:30-13:30`,`-`,`Lunch, rest`,``],
[`13:45-14:15`,`EM`,`Read your one-page sheet and redo anything you got wrong on Saturday. No new material.`,``],
[`15:00-17:00`,`EXAM`,`EM midterm. Bring your permit and calculator.`,``],
[`19:30-20:30`,`MIS`,`Ch 1 deck (MIS18-Chapter 01_.pptx) sl. 8-39, counted in the file, not the footer; MIS18_Case_1 Q1-4 (UPS) in bullets.`,`4 answers (2-3 lines each); six business objectives and the organization/management/technology dimensions listed.`],
[`20:30-21:30`,`MIS`,`Ch 2 deck sl. 5-8, 12-23, 27-29, 32-36, 40-45, 63-64, 68-69, 77-78; MIS18_Case_2 Q1-4.`,`4 answers; who uses TPS/MIS/DSS/ESS and what ERP/SCM/CRM/KMS do, from memory.`]]},
"""

a = s.index("{ d: `Sat Nov 7`")
b = s.index("{ d: `Mon Nov 9`")
s = s[:a] + WEEKEND + s[b:]
assert s.count("midterm-plan-ticks-v6") == 1
s = s.replace("midterm-plan-ticks-v6", "midterm-plan-ticks-v7")
open(path, "w", encoding="utf-8").write(s)
print("ok")
