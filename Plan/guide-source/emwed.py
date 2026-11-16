import sys

p, sk = sys.argv[1], sys.argv[2]

def edit(path, pairs):
    s = open(path, encoding="utf-8").read()
    for old, new in pairs:
        assert s.count(old) == 1, old
        s = s.replace(old, new)
    open(path, "w", encoding="utf-8").write(s)

edit(p, [
    ("EM: case study, Quiz 2 and presentations after midterms, dates not announced.",
     "EM (notice of Nov 16): Quiz 2 and case study submission Wed Nov 18 in the 14:40 class, then a new chapter (Transportation modelling); group presentations Mon Nov 23."),
    ("<td>EM Quiz 2 (math MCQ)</td><td>After midterms (moved; date not announced)</td>",
     "<td>EM Quiz 2 (math MCQ)</td><td>Wed Nov 18, 14:40 class, room 2102</td>"),
    ("<td>EM group presentation, Slide 4</td><td>After midterms (moved; date not announced)</td>",
     "<td>EM group presentation, Slide 4</td><td>Mon Nov 23, 14:40 class, room 2102</td>"),
    ("{ d: `Tue Nov 17`, n: `MIS class, Python and OOP2 prep`, r: [",
     "{ d: `Tue Nov 17`, n: `MIS class, EM Quiz 2 prep, Python, OOP2`, r: ["),
    ("[`08:00-09:30`,`MIS`,`Class, room 1116. MIS Quiz 2 date not announced; it could be today.`,``],\n",
     "[`08:00-09:30`,`MIS`,`Class, room 1116. MIS Quiz 2 date not announced; it could be today.`,``],\n"
     "[`10:00-10:35`,`EM`,`EM-Quiz2-Pack.pdf p1: read 10 min, cover the page and write every formula from memory; then redo pies, chargers and slide 25 with the answers covered.`,`Every formula right from memory; all three examples match.`],\n"
     "[`10:45-11:35`,`EM`,`Pack p2: Q1-10 closed book in 30 min; mark with p4 rows 1-10, redo each miss on paper.`,`8/10 or better; every miss labelled (formula, units, rounding or time basis) and redone.`],\n"
     "[`11:45-12:35`,`EM`,`Pack p3: Q11-20, same method; key on p4 rows 11-20.`,`8/10 or better; every miss redone.`],\n"
     "[`12:35-13:15`,`-`,`Lunch`,``],\n"
     "[`13:15-13:45`,`EM`,`EM WS3 CP Q&A.pdf Q2-Q4 closed book, then redo every miss from Q1-20 once more.`,`39,683 and $1.71; 46,000, $3,000 / $8,200, 126,000; 6,000, -7,000, 7,000, Tk 61. No miss repeated.`],\n"
     "[`13:45-14:00`,`EM`,`Case study: open 21-44625-1_EM_Case_Study_Short.pdf (Engineering-Management repo, assignments/case-study-midterm-solaric; on the Mac: EM/repo). Check it is the final version; print it if the submission is on paper.`,`File ready to hand in on Wednesday.`],\n"),
    ("[`16:40-17:15`,`EM`,`EM-Quiz2-Pack.pdf p1: read 10 min, cover the page and write every formula from memory; then redo pies, chargers and slide 25 with the answers covered.`,`Every formula right from memory; all three examples match.`],\n[`17:15-18:30`,`-`,`Break and dinner`,``],",
     "[`16:30-18:30`,`-`,`Break and dinner`,``],"),
    ("{ d: `Wed Nov 18`, n: `OOP2 Quiz 2, Python demo`, r: [",
     "{ d: `Wed Nov 18`, n: `OOP2 Quiz 2, Python demo, EM Quiz 2`, r: ["),
    ("[`12:20-12:50`,`-`,`Lunch`,``],\n"
     "[`12:50-13:40`,`EM`,`EM-Quiz2-Pack.pdf p2: Q1-10 closed book in 30 min; mark with p4 rows 1-10, redo each miss on paper.`,`8/10 or better; every miss labelled (formula, units, rounding or time basis) and redone.`],\n"
     "[`13:45-14:35`,`EM`,`Pack p3: Q11-20, same method; key on p4 rows 11-20.`,`8/10 or better; every miss redone.`],\n"
     "[`14:40-16:10`,`EM`,`Class, room 2102. Quiz 2 date not announced; it could be today.`,``],\n",
     "[`12:20-13:00`,`-`,`Lunch`,``],\n"
     "[`13:00-13:40`,`EM`,`EM-Quiz2-Pack.pdf p1 once, then Tuesday's misses only. Nothing new.`,`Every Tuesday miss redone correctly.`],\n"
     "[`14:40-16:10`,`EXAM`,`EM class, room 2102: Quiz 2 (capacity planning), case study submission, then a new chapter (Transportation modelling). Bring the case study.`,``],\n"),
    ("[`19:00-19:30`,`EM`,`EM WS3 CP Q&A.pdf Q2-Q4 closed book, then redo every miss from Q1-20 once more.`,`39,683 and $1.71; 46,000, $3,000 / $8,200, 126,000; 6,000, -7,000, 7,000, Tk 61. No miss repeated.`],\n", ""),
    ("const KEY = 'midterm-plan-ticks-v17';", "const KEY = 'midterm-plan-ticks-v18';"),
])

edit(sk, [
    ("Dates not announced yet: EM Quiz 2 + case study + presentations, MIS Quiz 2,",
     "EM Quiz 2 + case study submission Wed Nov 18 in the 14:40 class (room 2102); EM group presentations Mon Nov 23. Dates not announced yet: MIS Quiz 2,"),
])
print("ok")
