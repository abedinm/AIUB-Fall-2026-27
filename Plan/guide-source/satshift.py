import sys

path = sys.argv[1]
s = open(path, encoding="utf-8").read()

old = s[s.index("[`09:00-09:30`,`-`,`Up, wash, breakfast`,``],"):s.index("[`15:30-15:55`,`EM`")]
new = r"""[`10:08-10:30`,`-`,`Up, wash, breakfast`,``],
[`10:30-10:45`,`AI`,`The Andrew video once at 1.25x (the AI session has it).`,`Watched once, no pausing to take notes.`],
[`10:45-11:10`,`AI`,`Redo the BFS and UCS traces on paper, then check against notes p5-6.`,`UCS to H gives 25.`],
[`11:15-11:40`,`AI`,`Redo the A* trace and the admissible/consistent Ex 2 (notes p8).`,`A* gives cost 7; Ex 2 comes out "not consistent".`],
[`11:45-12:10`,`AI`,`Write the complexity table from memory (p4), then draw the 5 agent diagrams (p11-12).`,`Table matches p4; all 5 diagrams drawn.`],
[`12:15-12:40`,`AI`,`The 6 environment pairs, PEAS for the taxi, the p10 traps.`,`All p10 traps answered right with the answers covered.`],
[`12:40-13:15`,`-`,`Lunch`,``],
[`13:15-13:40`,`EM`,`Productivity & Competitveness.pdf sl. 4, 12-17: productivity = output / input, single vs multifactor. Redo the smart-watch example (sl. 18-19) covered.`,`Both MFP numbers match sl. 18-19.`],
[`13:45-14:10`,`EM`,`EM WS1 Productivity.pdf Q1 and Q2, key covered.`,`Match the key on WS1's last page.`],
[`14:15-14:40`,`EM`,`Strategic Capacity Planning.pdf sl. 4-5 and 16: efficiency, utilization, P = Q(R-v) - FC. Redo the pies example (sl. 17) covered.`,`All four answers match sl. 18.`],
[`14:45-15:10`,`EM`,`Capacity sl. 10, then EM WS3 CP Q&A.pdf Q1 and Q4; then make vs buy: sl. 25, redo with sl. 26 covered.`,`WS3 matches the page-2 key; make/buy matches sl. 26.`],
[`15:10-15:30`,`-`,`Rest`,``],
"""
assert "`11:45-12:10`,`AI`,`Practice" in old
s = s.replace(old, new)
open(path, "w", encoding="utf-8").write(s)
print("ok")
