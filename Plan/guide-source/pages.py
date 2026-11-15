import json
import os
import re
import sys

import fitz

pdf, out_json, png_dir, which = sys.argv[1:5]
doc = fitz.open(pdf)
keys = [f"DAY {i:02d} OF 14" for i in range(1, 15)] + ["CHEAT EM", "CHEAT AI", "CHEAT MIS", "CHEAT OOP2", "CHEAT PYTHON"]
found = {}
for pno in range(len(doc)):
    text = re.sub(r"\s+", "", doc[pno].get_text())
    for k in keys:
        if k not in found and k.replace(" ", "") in text:
            found[k] = pno + 1

r = doc[0].rect
print("pages", len(doc), "size", round(r.width), "x", round(r.height))
print(json.dumps(found))
with open(out_json, "w") as f:
    json.dump(found, f)

if which != "none":
    os.makedirs(png_dir, exist_ok=True)
    nums = range(1, len(doc) + 1) if which == "all" else [int(x) for x in which.split(",")]
    for n in nums:
        pix = doc[n - 1].get_pixmap(matrix=fitz.Matrix(1.25, 1.25))
        pix.save(os.path.join(png_dir, f"p{n:02d}.png"))
