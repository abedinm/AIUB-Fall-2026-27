import sys

p = sys.argv[1]
s = open(p, encoding="utf-8").read()

def sub(old, new):
    global s
    assert s.count(old) == 1, old
    s = s.replace(old, new)

sub("[`23:15-00:45`,`AI`,`AI only, with the AI session: finish the Coder Bhai video. Hard stop 01:00.`",
    "[`23:15-01:15`,`AI`,`AI only, with the AI session: UCS done on paper. A*, diagrams and theory moved to Sun 07:30.`")
sub("[`00:45`,`-`,`Sleep (01:00 at the latest).", "[`01:15`,`-`,`Sleep.")
sub("[`07:30-08:00`,`AI`,`Read only: notes p10 and p4.`,`Nothing new.`],",
    "[`07:30-08:00`,`AI`,`A* from notes p8 (10 min), the 5 agent diagrams p11-12 (10 min), p10 traps and the p4 table (10 min). Waiting before the exam: p1-p3 if there's time.`,`A* gives cost 7; 5 diagrams drawn; traps said without looking.`],")
sub("[`12:40-13:10`,`-`,`Lunch`,``],",
    "[`12:40-13:05`,`-`,`Lunch`,``],\n[`13:05-13:20`,`-`,`Rest: eyes closed, phone alarm for 13:20.`,``],")
sub("[`13:10-13:35`,`EM`,`Practice #1", "[`13:20-13:45`,`EM`,`Practice #1")
sub("[`13:40-14:05`,`EM`,`Capacity: sl. 10", "[`13:50-14:10`,`EM`,`Capacity: sl. 10")
sub("midterm-plan-ticks-v12", "midterm-plan-ticks-v13")
open(p, "w", encoding="utf-8").write(s)
print("ok")
