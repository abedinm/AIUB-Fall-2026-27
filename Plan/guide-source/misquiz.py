import sys

p, sk = sys.argv[1], sys.argv[2]
s = open(p, encoding="utf-8").read()

def sub(old, new):
    global s
    assert s.count(old) == 1, old
    s = s.replace(old, new)

def cut(start, end_incl):
    """Replace the span from start through end_incl (both unique) with a placeholder."""
    global s
    assert s.count(start) == 1 and s.count(end_incl) == 1, (start, end_incl)
    a = s.index(start)
    b = s.index(end_incl) + len(end_incl)
    assert a < b
    old = s[a:b]
    return old

sub("MIS Quiz 2: just after midterms, date not announced.",
    "MIS Quiz 2 (sudden notice of Nov 16): Tue Nov 17 at the start of the 08:00 class, room 1116, Chapter 3 only; late arrival may miss it.")
sub("Python-Quiz2-Pack.pdf (8 p)", "Python-Quiz2-Pack.pdf (9 p)")
sub("mini-quiz (p6)", "mini-quiz (p7)")
sub("<td>MIS Quiz 2</td><td>Just after midterms (date not announced)</td>",
    "<td>MIS Quiz 2</td><td>Tue Nov 17, 08:00 sharp (start of class), room 1116; Chapter 3</td>")

# Monday: from the first Python row through the sleep row.
mon_old = cut("[`15:00-15:40`,`Python`,`Python-Quiz2-Pack.pdf p1-2", "[`23:00`,`-`,`Sleep. Alarm 06:45: MIS class at 08:00.`,``]]},")
MON = """[`17:05-17:50`,`MIS`,`Ch 3 five forces: Visual Sheets p1, Crash Notes p11-13, Pack 1 p21. Say each force (means, strong when, example), then write the 5 exam lines.`,`Lines from memory match Crash Notes p12.`],
[`17:55-18:40`,`MIS`,`Ch 3 four strategies, Internet, value chain and value web: Visual Sheets p2 and p8, Crash Notes p14-16, MIS-Quiz2-Pack p3.`,`4 strategies with examples, 5 primary + 4 support activities and the value web definition written from memory.`],
[`18:40-19:20`,`-`,`Dinner`,``],
[`19:20-20:00`,`MIS`,`MIS-Quiz2-Pack.pdf p4-5: mini-quiz closed book, 30 min; mark with p6-7 (10 min). Ch 3 questions are the ones that count.`,`Every miss re-read on the page the key gives.`],
[`20:00-20:10`,`-`,`Break`,``],
[`20:10-20:55`,`OOP2`,`OOP2-Quiz2-Pack.pdf p2-3: read the cheat sheet, then write the child-class recipe and the two-question rule from memory.`,`Your paper matches p2-3.`],
[`21:00-21:50`,`Python`,`Python-Quiz2-Pack.pdf p1: basics primer (you're starting from zero, so this comes first).`,`Every example on p1 predicted before you check it.`],
[`21:55-22:35`,`OOP2`,`OOP2-Quiz2-Pack.pdf p4-5: re-trace T1-T3 on paper; check with the key on p8.`,`All 3 outputs match line by line; misses go in the Miss log.`],
[`22:45`,`-`,`Sleep. Alarm 06:30: MIS Quiz 2 at 08:00 sharp.`,``]]},"""
s = s.replace(mon_old, MON)

sub("{ d: `Tue Nov 17`, n: `MIS class, EM Quiz 2 prep, Python, OOP2`, r: [\n"
    "[`06:45-07:30`,`-`,`Up, wash, eat`,``],\n"
    "[`08:00-09:30`,`MIS`,`Class, room 1116. MIS Quiz 2 date not announced; it could be today.`,``],",
    "{ d: `Tue Nov 17`, n: `MIS Quiz 2, EM Quiz 2 prep, Python, OOP2`, r: [\n"
    "[`06:30-07:00`,`-`,`Up, wash, eat`,``],\n"
    "[`07:00-07:30`,`MIS`,`MIS-Quiz2-Pack p3 (Ch 3 one-liners) once, then last night's misses. Nothing new. Leave so you're in room 1116 by 07:50.`,`Every miss from last night right.`],\n"
    "[`08:00-09:30`,`EXAM`,`MIS Quiz 2 (Chapter 3) at the start of class, room 1116. It starts promptly; late arrival may miss it.`,``],")

tue_old = cut("[`15:00-15:45`,`Python`,`Python-Quiz2-Pack.pdf p4-5", "[`17:30-18:30`,`-`,`Dinner`,``],")
TUE = """[`14:05-14:50`,`Python`,`Python-Quiz2-Pack.pdf p2-3: OOP rules, then O1-O7 on paper; check with the key on p8-9.`,`At least 6/7.`],
[`15:00-15:40`,`Python`,`Pack p3-5: exception and file rules, then E1-E5 and F1-F5; key p8-9.`,`At least 8/10; file-modes table (r, w, a, x) written from memory.`],
[`15:45-16:30`,`Python`,`Pack p5-6: NumPy rules, then N1-N7; key p8-9.`,`At least 6/7; you can explain copy vs view and what reshape(2, 3, 2) means.`],
[`16:30-16:40`,`-`,`Break`,``],
[`16:40-17:20`,`Python`,`Pack p7: mini-quiz closed book, 30 min; mark it with p8-9 (10 min).`,`15/20 or more; each miss goes back to its topic's snippets.`],
[`17:20-17:45`,`Python`,`Viva check: the app runs on the team laptop (merged main or your local copy), and you can explain your Smart Basket screen and change one condition live.`,`App runs start to finish on the laptop going to class; laptop charged.`],
[`17:45-18:45`,`-`,`Dinner`,``],"""
s = s.replace(tue_old, TUE)

sub("Python-Quiz2-Pack.pdf: the rules on p1-5 once, then Tuesday's mini-quiz misses.",
    "Python-Quiz2-Pack.pdf: the rules on p1-6 once, then Tuesday's mini-quiz misses.")

thu_old = cut("{ d: `Thu Nov 19`, n: `AI lab, MIS quiz prep part 1`, r: [", "redo the Thursday MIS block it points to.`]]}")
s = s.replace(thu_old, "{ d: `Thu Nov 19`, n: `AI lab`, r: [\n[`15:00-17:20`,`AI`,`Lab class, room DS0208.`,``]]}")

sub("const KEY = 'midterm-plan-ticks-v21';", "const KEY = 'midterm-plan-ticks-v22';")
open(p, "w", encoding="utf-8").write(s)

k = open(sk, encoding="utf-8").read()
old = "Dates not announced yet: MIS Quiz 2."
assert k.count(old) == 1
open(sk, "w", encoding="utf-8").write(k.replace(old, "MIS Quiz 2 Tue Nov 17 at the start of the 08:00 class (room 1116), Chapter 3, be on time."))
print("ok")
