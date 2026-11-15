import sys

p = sys.argv[1]
s = open(p, encoding="utf-8").read()

def sub(old, new):
    global s
    assert s.count(old) == 1, old
    s = s.replace(old, new)

sub("`Lunch and rest. The MIS session is building the pack.`",
    "`Lunch and rest. Pack 1 is ready: F:\\\\outputs\\\\midterm-plan\\\\MIS-Pack-1-Ch1-3.pdf`")
sub("`Pack 1: Ch 1 notes. If the pack isn't there yet, MIS18-Chapter 01_.pptx sl. 8-39.`", "`Pack 1 p2-5: Ch 1 notes.`")
sub("`Pack 1: Case 1 (UPS) Q1-4.", "`Pack 1 p6-7: Case 1 (UPS) Q1-4.")
sub("`Pack 1: Ch 2 notes:", "`Pack 1 p8-13: Ch 2 notes:")
sub("`Pack 1: Case 2 Q1-4 covered, then the Ch 2 MCQs before reading the answers.`",
    "`Pack 1 p14-17: Case 2 Q1-4 covered, then the 27 Ch 2 MCQs before reading the key.`")
sub("`Pack 1: Ch 3 five forces", "`Pack 1 p18-20: Ch 3 five forces")
sub("`Pack 1: Ch 3 rest", "`Pack 1 p21-24: Ch 3 rest")
open(p, "w", encoding="utf-8").write(s)
print("ok")
