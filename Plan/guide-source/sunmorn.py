import sys

p = sys.argv[1]
s = open(p, encoding="utf-8").read()

def sub(old, new):
    global s
    assert s.count(old) == 1, old
    s = s.replace(old, new)

sub("[`07:00-07:30`,`-`,`Up, wash, breakfast.", "[`06:26-06:50`,`-`,`Up (woke 06:26), shower, breakfast.")
sub("[`07:30-08:00`,`AI`,`A* from notes p8 (10 min), the 5 agent diagrams p11-12 (10 min), p10 traps and the p4 table (10 min). Waiting before the exam: p1-p3 if there's time.`",
    "[`06:50-08:15`,`AI`,`With the AI session: A* from notes p8, the 5 agent diagrams p11-12, p10 traps and the p4 table. Waiting before the exam: p1-p3 if there's time.`")
sub("midterm-plan-ticks-v13", "midterm-plan-ticks-v14")
open(p, "w", encoding="utf-8").write(s)
print("ok")
