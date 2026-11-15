import sys

path = sys.argv[1]
s = open(path, encoding="utf-8").read()

TUE = r"""{ d: `Tue Nov 3`, n: `today`, r: [
[`18:00-18:10`,`Admin`,`Send the 3 messages from the 18:00 calendar event: EM group (Slide 4 data by 21:30), MIS group (Assignment 1 split), Sadman Rafi (Lab Mid Task).`,`All 3 sent.`],
[`18:10-19:05`,`OOP2`,`OOP2-Quiz2-90-Minutes.pdf (page numbers = the number at the bottom). 18:10-18:35 read Part 1, p. 1-2: C# from zero. Break. 18:40-19:05 Q1-Q2 on paper, check on p. 17.`,`You can say what class, new, a constructor and Console.WriteLine do.`],
[`19:10-20:05`,`OOP2`,`19:10-19:35 read Part 2, p. 4-5: inheritance, constructor order, base(...), protected, hiding with new. Break. 19:40-20:05 Q3-Q5 on paper, check on p. 17.`,`Your traces match the key; every miss re-traced, not just read.`],
[`20:05-20:20`,`-`,`Break: stand up, water, no phone`,``],
[`20:20-21:15`,`OOP2`,`20:20-20:45 read Part 3, p. 7-8: parent variable holding a child, virtual/override vs new. Break. 20:50-21:15 read p. 9: abstract, sealed, overloading.`,`You can say which method runs for override vs new without looking.`],
[`21:20-21:45`,`OOP2`,`Q6-Q8 on paper (p. 10-11), check on p. 17-18.`,`Every miss re-traced.`],
[`21:50-22:45`,`EM`,`Slide 4 with your own numbers and the group's data. 21:50-22:15 demand 2027-30 (conservative = 0.8 x Series 1; policy = Series 2) and capacity from slide 2's plan. Break. 22:20-22:45 volume = min(demand, capacity), profit with slide 3's numbers, unmet demand x margin; draft it in the team template; send your working to the EM session.`,`Both scenarios done for every year; slide drafted and sent to the group.`],
[`22:45-23:05`,`-`,`Break, snack`,``],
[`23:05-00:30`,`EM`,`Strategic Capacity Planning.pdf. Solve each problem slide on paper before the next slide shows the answer. 23:05-23:30 sl. 4-5 and 13-16, solve sl. 5. Break. 23:35-00:00 sl. 17-22, solve sl. 17 and 19. Break. 00:05-00:30 sl. 23-26, solve sl. 25.`,`Sl. 5 = 90% and 72%. Pies 1,200 / -$1,000 / 2,000 / $7.50. Chargers 10,500 and $46,000 at 22,000. Make/buy 7,500 units, make $870k vs buy $960k.`],
[`00:35-01:00`,`EM`,`EM WS3 CP Q&A.pdf Q1-Q2 (page 1) without notes.`,`Q1 4 machines. Q2 39,683 and $1.71.`],
[`01:00-01:15`,`-`,`Break, snack`,``],
[`01:15-01:40`,`EM`,`WS3 Q3-Q4, then mark all four with the key on page 2.`,`Q3 46,000; $3,000 / $8,200; 126,000. Q4 6,000; -7,000; 7,000; Tk 61.`],
[`01:45-02:10`,`OOP2`,`Q9-Q12 compile-or-not (p. 11), check on p. 18.`,`Every miss explained by a rule from p. 7-9.`],
[`02:15-03:05`,`OOP2`,`02:15-02:40 Part 4, p. 12-15: closed book, 20-minute timer. Break. 02:45-03:05 mark it with p. 17-18, re-read the rule behind every miss, then say the cheat sheet (p. 16) out loud.`,`Most answers right; every rule said without looking.`],
[`03:10-06:10`,`-`,`Sleep, 2 cycles. Phone alarm at 06:10.`,``]]},
"""

a = s.index("{ d: `Tue Nov 3`")
b = s.index("{ d: `Wed Nov 4`")
s = s[:a] + TUE + s[b:]

old_wed = "[`06:45-07:30`,`OOP2`"
assert s.count(old_wed) == 1
s = s.replace(old_wed, "[`06:10-06:45`,`-`,`Up, wash, eat`,``],\n" + old_wed)

assert s.count("midterm-plan-ticks-v5") == 1
s = s.replace("midterm-plan-ticks-v5", "midterm-plan-ticks-v6")

open(path, "w", encoding="utf-8").write(s)
print("ok")
