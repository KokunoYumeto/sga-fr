import sys
import json
from PIL import Image

# usage: multi_crop.py jobs.json
# jobs: list of [src, x0, y0, x1, y1, out, scale]
jobs = json.load(open(sys.argv[1], encoding="utf-8"))
for src, x0, y0, x1, y1, out, scale in jobs:
    im = Image.open(src).convert("L")
    c = im.crop((int(x0), int(y0), int(x1), int(y1)))
    if scale != 1:
        c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
    c.save(out)
    print(out, c.size)
