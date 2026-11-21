import sys, os, fitz
HF = os.environ.get("HANDFONT")
# usage: labels.py pack.pdf "Start marker" "End marker" "Label" [...triples]
path, args = sys.argv[1], sys.argv[2:]
d = fitz.open(path)
first = lambda m: next(i for i, p in enumerate(d) if i > 0 and p.search_for(m))
for start, end, label in zip(args[0::3], args[1::3], args[2::3]):
    for i in range(first(start), first(end)):
        p = d[i]
        rc = p.insert_textbox(fitz.Rect(0, 8, p.rect.width, 40), label, fontsize=12, fontname="hand" if HF else "hebo", fontfile=HF, color=(0.55, 0.1, 0.1), align=1)
        assert rc >= 0, (label, i + 1, rc)
    print(label, first(start) + 1, "-", first(end))
d.save(path + ".tmp"); d.close(); os.replace(path + ".tmp", path)
