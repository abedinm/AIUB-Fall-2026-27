import sys

p, sk = sys.argv[1], sys.argv[2]

def edit(path, pairs):
    s = open(path, encoding="utf-8").read()
    for old, new in pairs:
        assert s.count(old) == 1, old
        s = s.replace(old, new)
    open(path, "w", encoding="utf-8").write(s)

edit(p, [
    ("project due Sun Nov 15, demos Mon Nov 16 (lab) and Wed Nov 18 (theory),",
     "project due Sun Nov 15, demo Wed Nov 18 in the 08:00 theory class (no lab class on Mon Nov 16),"),
    ("<td>Python demo</td><td>Mon Nov 16, lab class</td>",
     "<td>Python demo</td><td>Wed Nov 18, 08:00 theory class</td>"),
    ("""{ d: `Mon Nov 16`, n: `Python demo, quiz prep starts`, r: [
[`08:00-10:20`,`Python`,`Project demo, lab class, room DS0204. No slides needed.`,``],
[`10:30-14:30`,`-`,`Sleep and lunch. You were up past 3 AM.`,``],""",
     """{ d: `Mon Nov 16`, n: `No class, quiz prep starts`, r: [
[`04:00-13:00`,`-`,`Sleep in. Up by 13:00 at the latest.`,``],
[`13:00-14:30`,`-`,`Up, wash, lunch`,``],"""),
    ("[`22:30`,`-`,`Sleep. Alarm 06:30.`,``]]},\n{ d: `Tue Nov 17`",
     "[`23:30`,`-`,`Sleep. Alarm 08:00, to be back on an early clock for Wednesday.`,``]]},\n{ d: `Tue Nov 17`"),
    ("[`08:00-10:00`,`Python`,`Theory class, room 9305 (second demo date).`,``],",
     "[`08:00-10:00`,`Python`,`Theory class, room 9305: project demo. No slides needed.`,``],"),
])

edit(sk, [
    ("Python demos Mon Nov 16 (lab) and Wed Nov 18 (theory);",
     "Python demo Wed Nov 18 08:00 theory class (no Mon lab class);"),
])
print("ok")
