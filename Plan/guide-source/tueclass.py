import sys

p = sys.argv[1]
s = open(p, encoding="utf-8").read()

def sub(old, new):
    global s
    assert s.count(old) == 1, old
    s = s.replace(old, new)

sub("[`23:30`,`-`,`Sleep. Alarm 08:00, to be back on an early clock for Wednesday.`,``]]},",
    "[`23:00`,`-`,`Sleep. Alarm 06:45: MIS class at 08:00.`,``]]},")
sub("{ d: `Tue Nov 17`, n: `Python and OOP2 prep`, r: [\n",
    "{ d: `Tue Nov 17`, n: `MIS class, Python and OOP2 prep`, r: [\n"
    "[`06:45-07:30`,`-`,`Up, wash, eat`,``],\n"
    "[`08:00-09:30`,`MIS`,`Class, room 1116. MIS Quiz 2 date not announced; it could be today.`,``],\n")
sub("const KEY = 'midterm-plan-ticks-v16';", "const KEY = 'midterm-plan-ticks-v17';")
open(p, "w", encoding="utf-8").write(s)
print("ok")
