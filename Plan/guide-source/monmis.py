import sys

p, bj = sys.argv[1], sys.argv[2]
s = open(p, encoding="utf-8").read()

P1 = "Pack 1 (F:\\\\outputs\\\\midterm-plan\\\\MIS-Pack-1-Ch1-3.pdf)"
P2 = "Pack 2 (MIS-Pack-2-Ch5-9-Practice.pdf, ready 17:30)"
MON = r"""{ d: `Mon Nov 9`, n: `MIS from zero`, r: [
[`12:20-13:15`,`-`,`Lunch and rest. The MIS session is building the pack.`,``],
[`13:15-13:55`,`MIS`,`P1: Ch 1 notes. If the pack isn't there yet, MIS18-Chapter 01_.pptx sl. 8-39.`,`Six business objectives and the 3 dimensions said without looking; self-check right.`],
[`14:05-14:30`,`MIS`,`P1: Case 1 (UPS) Q1-4. Read the model answers, then say each one with the page covered.`,`All 4 said covered.`],
[`14:35-15:20`,`MIS`,`P1: Ch 2 notes: TPS/MIS/DSS/ESS table, ERP/SCM/CRM/KMS, collaboration, IS roles.`,`System-types table redrawn from memory; self-check right.`],
[`15:25-15:50`,`MIS`,`P1: Case 2 Q1-4 covered, then the Ch 2 MCQs before reading the answers.`,`Every miss written down with its right answer.`],
[`16:05-16:50`,`MIS`,`P1: Ch 3 five forces (memorize the wording) and the four strategies.`,`Five forces and four strategies written from memory, one example each.`],
[`16:55-17:20`,`MIS`,`P1: Ch 3 rest (value chain vs value web, synergies, scalability, airline table), then the sl. 20-21 MCQs.`,`MCQs answered before checking; misses written down.`],
[`17:20-17:40`,`-`,`Snack, walk, no phone.`,``],
[`17:40-18:10`,`MIS`,`P2: Ch 5 IT infrastructure and cloud.`,`Self-check right.`],
[`18:15-18:45`,`MIS`,`P2: Ch 6 databases and blockchain.`,`File vs database problems listed; blockchain in 4 sentences.`],
[`18:50-19:10`,`MIS`,`P2: Ch 7 networks.`,`Self-check right.`],
[`19:10-19:50`,`-`,`Dinner`,``],
[`19:50-20:20`,`MIS`,`P2: Ch 9, only if it's in the midterm (ask a classmate). Otherwise redo today's missed MCQs.`,`Self-check right.`],
[`20:25-21:05`,`MIS`,`P2: 30 mixed MCQs closed-book, then the key.`,`Score written down; every miss has its right answer.`],
[`21:10-21:50`,`MIS`,`P2: long answer 1 closed-book: five forces of any company, with diagram. Then compare with the model.`,`One page with diagram; every force rated with a reason.`],
[`21:55-22:25`,`MIS`,`P2: 6 short answers aloud, then long answers 2-3 (system types, file vs database) aloud.`,`All said without looking.`],
[`22:30-22:45`,`MIS`,`P2: read the one-page morning sheet once. Nothing new.`,``],
[`23:00`,`-`,`Sleep. Phone alarm 06:45 (MIS exam at 9:00).`,``]]},
"""
a = s.index("{ d: `Mon Nov 9`")
b = s.index("{ d: `Tue Nov 10`")
s = s[:a] + MON.replace("P1:", "Pack 1:").replace("P2:", "Pack 2:") + s[b:]

def sub(old, new):
    global s
    assert s.count(old) == 1, old
    s = s.replace(old, new)

sub("[`07:30-08:00`,`MIS`,`Rewrite from memory: five forces + four strategies, six business objectives, TPS/MIS/DSS/ESS users. No new material.`",
    "[`06:45-07:30`,`-`,`Up, wash, breakfast. Pack your permit and pens.`,``],\n[`07:30-08:15`,`MIS`,`Pack 2 morning sheet: rewrite from memory five forces + four strategies, six business objectives, TPS/MIS/DSS/ESS users. No new material.`")
sub("midterm-plan-ticks-v14", "midterm-plan-ticks-v15")
open(p, "w", encoding="utf-8").write(s)

j = open(bj, encoding="utf-8").read()
old = "one: 'One full MIS day: chapters in the morning, practice in the afternoon.' }"
assert j.count(old) == 1
j = j.replace(old, "one: 'MIS from zero: two study packs, chapter by chapter, sleep at 23:00.' }")
open(bj, "w", encoding="utf-8").write(j)
print("ok")
