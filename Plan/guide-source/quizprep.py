import sys

p = sys.argv[1]
s = open(p, encoding="utf-8").read()

def sub(old, new):
    global s
    assert s.count(old) == 1, old
    s = s.replace(old, new)

sub("Python Quiz 2: first week after midterms, OOP, file and exception handling, NumPy to ndarray iteration, no make-up.</p>",
    "Python Quiz 2: first week after midterms, OOP, file and exception handling, NumPy to ndarray iteration, no make-up.</p>\n"
    "<p class=\"sub\">Quiz 2 packs (Nov 16), all in F:\\outputs\\midterm-plan: OOP2-Quiz2-Pack.pdf (10 p), Python-Quiz2-Pack.pdf (8 p), EM-Quiz2-Pack.pdf (4 p), MIS-Quiz2-Pack.pdf (7 p). The MIS syllabus is a guess (Ch 3 plus Ch 1-2 review); no syllabus was announced.</p>")

sub("<td>You trace a 3-class hierarchy (constructor order, override vs new) alone; 8/10 on Part B tonight.</td>",
    "<td>OOP2-Quiz2-Pack mini-quiz (p6-7) marked on Tuesday; every miss redone Wednesday morning.</td>")
sub("<td>13/15 on the EM session's MCQ test; every capacity formula written from memory.</td>",
    "<td>8/10 on each half of EM-Quiz2-Pack (Q1-10, Q11-20); every formula on p1 written from memory.</td>")
sub("<tr><td>11</td><td>Python demo</td><td>Mon Nov 16, lab class</td><td>Each member explains their own functions and changes a condition live.</td></tr>",
    "<tr><td>11</td><td>Python demo</td><td>Mon Nov 16, lab class</td><td>Each member explains their own functions and changes a condition live.</td></tr>\n"
    "<tr><td>12</td><td>Python Quiz 2</td><td>First week after midterms (date not announced)</td><td>15/20 on the Python-Quiz2-Pack mini-quiz (p6); Lab 6 and Lab 7 written by hand.</td></tr>\n"
    "<tr><td>13</td><td>MIS Quiz 2</td><td>Just after midterms (date not announced)</td><td>20/25 MCQs on the MIS-Quiz2-Pack mini-quiz (p4-5); five forces lines from memory.</td></tr>")

a = s.index("{ d: `Mon Nov 16`")
b = s.index("\n];\n\nconst KEY")
assert s.count("{ d: `Mon Nov 16`") == 1

NEW = """{ d: `Mon Nov 16`, n: `Python demo, quiz prep starts`, r: [
[`08:00-10:20`,`Python`,`Project demo, lab class, room DS0204. No slides needed.`,``],
[`10:30-14:30`,`-`,`Sleep and lunch. You were up past 3 AM.`,``],
[`15:00-15:40`,`Python`,`Python-Quiz2-Pack.pdf p1-2: OOP rules, then O1-O7 on paper; check with the key on p7.`,`At least 6/7; you can say why O1 and O6 come out as they do.`],
[`15:45-16:25`,`Python`,`Lab 6 P1-P3 by hand without looking (pack p1-2, checks on p8), then run them.`,`Bus prints 4400.0; BankAccount rejects -50 and an overdraw; Shape prints 20 and 12.5664.`],
[`16:25-16:40`,`-`,`Break: stand up, water, no phone`,``],
[`16:40-17:20`,`Python`,`Pack p2-4: exception and file rules, then E1-E5 and F1-F5; check with p7.`,`At least 8/10; file-modes table (r, w, a, x) written from memory.`],
[`17:25-17:55`,`Python`,`Pack p3: Lab 7 P1-P4 by hand (checks on p8).`,`Divide by zero, "abc", index 9, a missing file and "x" on an existing file each print a message and the program keeps running.`],
[`18:00-19:00`,`-`,`Dinner`,``],
[`19:00-19:45`,`OOP2`,`OOP2-Quiz2-Pack.pdf p2-3: read the cheat sheet, then write the child-class recipe and the two-question rule from memory.`,`Your paper matches p2-3.`],
[`19:45-20:00`,`-`,`Break`,``],
[`20:00-20:50`,`OOP2`,`Pack p4-5: re-trace T1-T3 on paper; check with the key on p8.`,`All 3 outputs match line by line; misses go in the Miss log.`],
[`22:30`,`-`,`Sleep. Alarm 06:30.`,``]]},
{ d: `Tue Nov 17`, n: `Python and OOP2 prep`, r: [
[`15:00-15:45`,`Python`,`Python-Quiz2-Pack.pdf p4-5: NumPy rules, then N1-N7; check with p7.`,`At least 6/7; you can explain copy vs view and what reshape(2, 3, 2) means.`],
[`15:50-16:30`,`Python`,`Pack p6: mini-quiz closed book, 30 min; mark it with p7-8 (10 min).`,`15/20 or more; each miss goes back to its topic's snippets.`],
[`16:40-17:15`,`EM`,`EM-Quiz2-Pack.pdf p1: read 10 min, cover the page and write every formula from memory; then redo pies, chargers and slide 25 with the answers covered.`,`Every formula right from memory; all three examples match.`],
[`17:15-18:30`,`-`,`Break and dinner`,``],
[`19:00-19:50`,`OOP2`,`OOP2-Quiz2-90-Minutes.pdf p10-11: Q6-Q12 (traces and compile-or-not); check with its key on p17-18.`,`All 7 marked; every miss re-traced.`],
[`19:50-20:05`,`-`,`Break`,``],
[`20:05-20:45`,`OOP2`,`OOP2-Quiz2-Pack.pdf p6-7: mini-quiz, closed book, 40-minute timer.`,`Every question has a written answer.`],
[`20:45-20:55`,`-`,`Break`,``],
[`20:55-21:35`,`OOP2`,`Pack p8-10: mark it, re-trace each miss, compare Part D line by line.`,`Score written on top; misses in the Miss log.`],
[`23:00`,`-`,`Sleep. Alarm 06:30.`,``]]},
{ d: `Wed Nov 18`, n: `OOP2 Quiz 2, Python demo`, r: [
[`06:30-06:45`,`-`,`Up, wash`,``],
[`06:45-07:30`,`OOP2`,`OOP2-Quiz2-Pack.pdf p2-3 once, then redo Tuesday's misses. Nothing new.`,`Every Tuesday miss redone correctly.`],
[`08:00-10:00`,`Python`,`Theory class, room 9305 (second demo date).`,``],
[`10:20-12:20`,`EXAM`,`OOP2 Quiz 2, room 9303: inheritance and polymorphism, no make-up. Time not in the notice; this is your class slot.`,``],
[`12:20-12:50`,`-`,`Lunch`,``],
[`12:50-13:40`,`EM`,`EM-Quiz2-Pack.pdf p2: Q1-10 closed book in 30 min; mark with p4 rows 1-10, redo each miss on paper.`,`8/10 or better; every miss labelled (formula, units, rounding or time basis) and redone.`],
[`13:45-14:35`,`EM`,`Pack p3: Q11-20, same method; key on p4 rows 11-20.`,`8/10 or better; every miss redone.`],
[`14:40-16:10`,`EM`,`Class, room 2102. Quiz 2 date not announced; it could be today.`,``],
[`19:00-19:30`,`EM`,`EM WS3 CP Q&A.pdf Q2-Q4 closed book, then redo every miss from Q1-20 once more.`,`39,683 and $1.71; 46,000, $3,000 / $8,200, 126,000; 6,000, -7,000, 7,000, Tk 61. No miss repeated.`],
[`19:40-20:25`,`MIS`,`MIS five forces: Visual Sheets p1, Crash Notes p11-13, Pack 1 p21. Say each force (means, strong when, example), then write the 5 exam lines.`,`Lines from memory match Crash Notes p12.`],
[`20:30-21:15`,`MIS`,`4 strategies, Internet, value chain and value web: Visual Sheets p2 and p8, Crash Notes p14-16, MIS-Quiz2-Pack p3.`,`4 strategies with examples, 5 primary + 4 support activities and the value web definition written from memory.`],
[`23:00`,`-`,`Sleep`,``]]},
{ d: `Thu Nov 19`, n: `MIS quiz prep`, r: [
[`19:00-19:30`,`MIS`,`Ch 1-2 refresher: Visual Sheets p3-7, then Pack 1 p16-17 (27 MCQs).`,`Score written; every miss re-read.`],
[`19:35-20:15`,`MIS`,`MIS-Quiz2-Pack.pdf p4-5: mini-quiz closed book, 30 min; mark with p6-7 (10 min).`,`20/25 or more on the MCQs; every miss re-read on the page the key gives. Below 20: redo the Wednesday MIS block it points to.`],
[`20:20-20:40`,`MIS`,`Only if Ch 9 is announced for the quiz: Pack 2 p10-13.`,`Ch 9 self-check right.`]]}"""

s = s[:a] + NEW + s[b:]
sub("const KEY = 'midterm-plan-ticks-v15';", "const KEY = 'midterm-plan-ticks-v16';")
open(p, "w", encoding="utf-8").write(s)
print("ok")
