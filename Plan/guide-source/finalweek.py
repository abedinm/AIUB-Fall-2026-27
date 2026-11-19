import sys

p = sys.argv[1]
s = open(p, encoding="utf-8").read()

def sub(old, new):
    global s
    assert s.count(old) == 1, old
    s = s.replace(old, new)

sub("Quiz 2 then project viva on Wed Nov 18 in the 08:00 theory class (no lab class on Mon Nov 16).",
    "Quiz 2 on Wed Nov 18 (done); the project viva moved to the next class, Mon Nov 23, 08:00 lab, DS0204.")
sub("<td>Python demo (viva)</td><td>Wed Nov 18, after Quiz 2 (about 08:35), 10 min per team</td>",
    "<td>Python demo (viva)</td><td>Mon Nov 23, 08:00 lab, DS0204 (moved from Wed Nov 18), 10 min per team</td>")

sub("""[`15:00-17:20`,`AI`,`Lab class, room DS0208.`,``]]}
];""", """[`15:00-17:20`,`AI`,`Lab class, room DS0208.`,``]]},
{ d: `Sat Nov 21`, n: `Python defense prep, EM Slide 4 with the group`, r: [
[`11:00-12:00`,`Python`,`BazarDor-Defense-Sheet.pdf (hub: Python\\\\project-docs). Run the app on the laptop going to class: py main.py in Python\\\\files\\\\Projects\\\\bazaardor-smart-basket. Explain your Smart Basket screen out loud, then change one condition live.`,`App runs start to finish on that laptop; every defense-sheet question answered without reading.`],
[`16:00-17:00`,`EM`,`Slide 4 with your group: confirm the slide order and your numbers, then say it aloud with a 60-second timer (scenarios 20 s, recommendation 15 s, commitment and outcome 15 s, cost of delay 10 s). The words are yours; Claude only checks numbers.`,`Under 60 seconds; every number matches the case study.`]]},
{ d: `Sun Nov 22`, n: `MIS and AI classes, final run-throughs`, r: [
[`08:00-09:30`,`MIS`,`Class, room 1116.`,``],
[`15:00-17:00`,`AI`,`Class, room 9408.`,``],
[`20:00-20:30`,`EM`,`Slide 4 aloud 3 times with the 60-second timer, then the 5 management questions.`,`Under 60 seconds each time; an answer ready for each question.`],
[`20:30-21:00`,`Python`,`Final run on the class laptop: open the app and do your part once. Then pack the laptop and charger.`,`App runs; laptop charged and packed.`],
[`23:00`,`-`,`Sleep. Alarm 06:45: Python defense at 08:00.`,``]]},
{ d: `Mon Nov 23`, n: `Python project defense, OOP2 lab, EM presentation`, r: [
[`06:45-07:00`,`-`,`Up, wash, eat`,``],
[`07:00-07:30`,`Python`,`Open the app on the laptop; defense sheet once. Leave so you're in DS0204 by 07:55.`,`App open and working before you leave.`],
[`08:00-10:20`,`EXAM`,`Python project defense, lab DS0204: 10 min per team including Q&amp;A, one laptop per team, no slides.`,``],
[`10:20-12:40`,`OOP2`,`Lab class, room DN0212.`,``],
[`12:40-13:30`,`-`,`Lunch`,``],
[`13:30-14:20`,`EM`,`Slide 4 aloud twice with the timer. Nothing new.`,`Under 60 seconds both times.`],
[`14:40-16:10`,`EXAM`,`EM group presentation, room 2102. You present Slide 4.`,``]]}
];""")

sub("const KEY = 'midterm-plan-ticks-v25';", "const KEY = 'midterm-plan-ticks-v26';")
open(p, "w", encoding="utf-8").write(s)
print("ok")
