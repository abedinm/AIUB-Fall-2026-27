import sys

p = sys.argv[1]
s = open(p, encoding="utf-8").read()

def span(start, end_incl):
    assert s.count(start) == 1 and s.count(end_incl) == 1, (start, end_incl)
    a = s.index(start)
    b = s.index(end_incl) + len(end_incl)
    assert a < b
    return s[a:b]

def sub(old, new):
    global s
    assert s.count(old) == 1, old
    s = s.replace(old, new)

sub("{ d: `Wed Nov 18`, n: `Python Quiz 2 + viva, OOP2 Quiz 2, EM Quiz 2`, r: [",
    "{ d: `Wed Nov 18`, n: `Python Quiz 2 + viva, OOP2 Quiz 2, EM Quiz 2 + case study Part 5`, r: [")

morning = span("[`06:30-06:45`,`-`,`Up, wash`,``],", "Then pack the laptop and charger.`,``],")
s = s.replace(morning, """[`03:15-06:15`,`-`,`Sleep now. Alarm 06:15.`,``],
[`06:15-06:25`,`-`,`Up, wash. No phone.`,``],
[`06:25-07:25`,`EM`,`Case study Part 5: write it yourself at course level, with the EM session's numbers and checklist. Plain student wording.`,`Part 5 complete in your own words; every number traced to the case.`],
[`07:25-07:30`,`EM`,`Send Part 5 to the EM session for the arithmetic check. Pack the laptop and charger.`,`Sent; laptop packed.`],""")

midday = span("[`12:20-13:00`,`-`,`Lunch`,``],", "Every Tuesday miss redone correctly.`],\n[`14:40-16:10`")
s = s.replace(midday, """[`12:20-12:45`,`EM`,`Read the EM session's check, fix any flagged numbers, print the case study.`,`Printed copy in your bag.`],
[`12:45-13:00`,`-`,`Lunch, quick`,``],
[`13:00-13:35`,`EM`,`EM-Quiz2-Pack.pdf p1: read 10 min, cover it, write every formula from memory.`,`Every formula right from memory.`],
[`13:40-14:30`,`EM`,`Pack p2: Q1-10 closed book in 30 min; mark with p4 rows 1-10, redo each miss.`,`8/10 or better; every miss redone.`],
[`14:40-16:10`""")

sub("Quiz 2 (capacity planning), case study submission, then a new chapter (Transportation modelling). Bring the case study.",
    "Quiz 2 (capacity planning), case study submission with the redone Part 5 (bring the printed copy), then a new chapter (Transportation modelling).")
sub("const KEY = 'midterm-plan-ticks-v23';", "const KEY = 'midterm-plan-ticks-v24';")
open(p, "w", encoding="utf-8").write(s)
print("ok")
