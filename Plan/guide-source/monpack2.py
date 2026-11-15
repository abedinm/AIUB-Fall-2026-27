import sys

p = sys.argv[1]
s = open(p, encoding="utf-8").read()

def sub(old, new):
    global s
    assert s.count(old) == 1, old
    s = s.replace(old, new)

sub("`Lunch and rest. Pack 1 is ready: F:\\\\outputs\\\\midterm-plan\\\\MIS-Pack-1-Ch1-3.pdf`",
    "`Lunch and rest. Both packs are in F:\\\\outputs\\\\midterm-plan: MIS-Pack-1-Ch1-3.pdf and MIS-Pack-2-Ch5-9-Practice.pdf`")
sub("`Pack 2: Ch 5 IT", "`Pack 2 p2-4: Ch 5 IT")
sub("`Pack 2: Ch 6 databases", "`Pack 2 p5-7: Ch 6 databases")
sub("`Pack 2: Ch 7 networks.`", "`Pack 2 p8-9: Ch 7 networks.`")
sub("`Pack 2: Ch 9, only if", "`Pack 2 p10-13: Ch 9, only if")
sub("`Pack 2: 30 mixed MCQs closed-book, then the key.`", "`Pack 2 p14-15: 30 mixed MCQs closed-book, then the key on p16.`")
sub("`Pack 2: long answer 1 closed-book: five forces of any company, with diagram. Then compare with the model.`",
    "`Pack 2 p17-20: case-answer template (p17), then long answer 1 closed-book: five forces of any company, with diagram. Then compare with the bKash model.`")
sub("`Pack 2: 6 short answers aloud, then long answers 2-3 (system types, file vs database) aloud.`",
    "`Pack 2 p21-22: 6 short answers aloud, then long answers 2-3 (p17-20: system types, file vs database) aloud.`")
sub("`Pack 2: read the one-page morning sheet once.", "`Pack 2 p23: read the one-page morning sheet once.")
sub("`Pack 2 morning sheet: rewrite", "`Pack 2 p23 morning sheet: rewrite")
open(p, "w", encoding="utf-8").write(s)
print("ok")
