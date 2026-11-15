import sys

p, bj, sk = sys.argv[1], sys.argv[2], sys.argv[3]

def edit(path, pairs):
    s = open(path, encoding="utf-8").read()
    for old, new in pairs:
        assert s.count(old) == 1, old
        s = s.replace(old, new)
    open(path, "w", encoding="utf-8").write(s)

edit(p, [
    ("<p class=\"sub\">Quizzes: OOP2 Quiz 2 Wed Nov 4 10:20 AM. EM Quiz 2 Wed Nov 4 2:40 PM (math MCQ). AI Quiz 2 held Nov 1. MIS Quiz 2 postponed from Nov 3, date not announced.</p>",
     "<p class=\"sub\">Quizzes after midterms (notices of Nov 14): OOP2 Quiz 2 Wed Nov 18, inheritance and polymorphism, no make-up (time not in the notice; your Wed OOP2 class is 10:20). EM: case study, Quiz 2 and presentations after midterms, dates not announced. AI Quiz 2: uninformed search (BFS, UCS, DFS, DLS, IDS, bidirectional, complexity), short Q&amp;A, date not announced. MIS Quiz 2: just after midterms, date not announced. Python Quiz 2: first week after midterms, OOP, file and exception handling, NumPy to ndarray iteration, no make-up.</p>"),
    ("<td>OOP2 Quiz 2</td><td>Wed Nov 4, 10:20</td>", "<td>OOP2 Quiz 2</td><td>Wed Nov 18 (moved; time not in the notice)</td>"),
    ("<td>EM Quiz 2 (math MCQ)</td><td>Wed Nov 4, 14:40</td>", "<td>EM Quiz 2 (math MCQ)</td><td>After midterms (moved; date not announced)</td>"),
    ("<td>EM group presentation, Slide 4</td><td>Wed Nov 4, 14:40</td>", "<td>EM group presentation, Slide 4</td><td>After midterms (moved; date not announced)</td>"),
])

edit(bj, [
    ("sub: 'Midterm Sun 8 Nov, 15:00-17:00 · Quiz 2 Wed 4 Nov (calculation MCQs)'",
     "sub: 'Midterm Sun 8 Nov, 15:00-17:00 · Quiz 2, case study, presentations after midterms'"),
    ("sub: 'Quiz 2 Wed 4 Nov, 10:20 · Midterm Sun 15 Nov, 12:00-14:00'",
     "sub: 'Midterm Sun 15 Nov, 12:00-14:00 · Quiz 2 Wed 18 Nov (inheritance, polymorphism)'"),
])

edit(sk, [
    ("Deadlines: OOP2 Quiz 2 Wed Nov 4 10:20 AM; EM Quiz 2 (math MCQ) Wed Nov 4 2:40 PM; ",
     "Deadlines: "),
    ("Python demos Mon Nov 16 (lab) and Wed Nov 18 (theory).",
     "Python demos Mon Nov 16 (lab) and Wed Nov 18 (theory); OOP2 Quiz 2 Wed Nov 18 (inheritance and polymorphism, no make-up; time not announced, Wed OOP2 class is 10:20). Dates not announced yet: AI Quiz 2 (uninformed search), EM Quiz 2 + case study + presentations, MIS Quiz 2, Python Quiz 2 (first week after midterms)."),
])
print("ok")
