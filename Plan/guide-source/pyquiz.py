import sys

p, sk = sys.argv[1], sys.argv[2]

def edit(path, pairs):
    s = open(path, encoding="utf-8").read()
    for old, new in pairs:
        assert s.count(old) == 1, old
        s = s.replace(old, new)
    open(path, "w", encoding="utf-8").write(s)

edit(p, [
    ("demo Wed Nov 18 in the 08:00 theory class (no lab class on Mon Nov 16), Quiz 2 in the first week after midterms.",
     "Quiz 2 then project viva on Wed Nov 18 in the 08:00 theory class (no lab class on Mon Nov 16)."),
    ("Python Quiz 2: first week after midterms, OOP, file and exception handling, NumPy to ndarray iteration, no make-up.",
     "Python Quiz 2 (notice of Nov 16): Wed Nov 18, first 30 minutes of the 08:00 class, be there at 8 sharp; OOP, file and exception handling, NumPy as covered in class; no make-up. Then a 5-minute break and the project viva: 10 minutes per team including Q&amp;A, one laptop per team, no slides."),
    ("<td>Python demo</td><td>Wed Nov 18, 08:00 theory class</td>",
     "<td>Python demo (viva)</td><td>Wed Nov 18, after Quiz 2 (about 08:35), 10 min per team</td>"),
    ("<td>Python Quiz 2</td><td>First week after midterms (date not announced)</td>",
     "<td>Python Quiz 2</td><td>Wed Nov 18, 08:00 sharp, room 9305</td>"),
    ("[`16:30-18:30`,`-`,`Break and dinner`,``],\n[`19:00-19:50`,`OOP2`,`OOP2-Quiz2-90-Minutes.pdf",
     "[`16:30-17:00`,`-`,`Break`,``],\n"
     "[`17:00-17:30`,`Python`,`Viva check: the app runs on the team laptop (merged main or your local copy), and you can explain your Smart Basket screen and change one condition live.`,`App runs start to finish on the laptop going to class; laptop charged.`],\n"
     "[`17:30-18:30`,`-`,`Dinner`,``],\n[`19:00-19:50`,`OOP2`,`OOP2-Quiz2-90-Minutes.pdf"),
    ("{ d: `Wed Nov 18`, n: `OOP2 Quiz 2, Python demo, EM Quiz 2`, r: [",
     "{ d: `Wed Nov 18`, n: `Python Quiz 2 + viva, OOP2 Quiz 2, EM Quiz 2`, r: ["),
    ("[`06:45-07:30`,`OOP2`,`OOP2-Quiz2-Pack.pdf p2-3 once, then redo Tuesday's misses. Nothing new.`,`Every Tuesday miss redone correctly.`],\n"
     "[`08:00-10:00`,`Python`,`Theory class, room 9305: project demo. No slides needed.`,``],\n",
     "[`06:45-07:15`,`Python`,`Python-Quiz2-Pack.pdf: the rules on p1-5 once, then Tuesday's mini-quiz misses. Nothing new.`,`Every Tuesday miss redone correctly.`],\n"
     "[`07:15-07:30`,`OOP2`,`OOP2-Quiz2-Pack.pdf p2-3 (cheat sheet) once. Then pack the laptop and charger.`,``],\n"
     "[`08:00-08:30`,`EXAM`,`Python Quiz 2, room 9305. Be in class at 8 sharp. No make-up.`,``],\n"
     "[`08:35-10:00`,`Python`,`Project viva: 10 minutes per team including Q&amp;A, one laptop per team, no slides.`,``],\n"
     "[`10:00-10:20`,`OOP2`,`Redo Tuesday's OOP2 misses from the Miss log. Nothing new.`,`Every Tuesday miss redone correctly.`],\n"),
    ("const KEY = 'midterm-plan-ticks-v20';", "const KEY = 'midterm-plan-ticks-v21';"),
])

edit(sk, [
    ("Python demo Wed Nov 18 08:00 theory class (no Mon lab class);",
     "Python Quiz 2 Wed Nov 18 08:00 sharp (first 30 min, no make-up), then project viva (10 min per team, one laptop per team, no slides);"),
    ("Dates not announced yet: MIS Quiz 2, Python Quiz 2 (first week after midterms).",
     "Dates not announced yet: MIS Quiz 2."),
])
print("ok")
