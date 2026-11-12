"""Glyph measure: python -I glyph.py <strip.png> <x0> <y0> <x1> <y1> <out.png>
Prints the ink bounding box (threshold 128) of each connected column-run in the box,
and saves a 6x enlargement of the box."""
import sys
from PIL import Image

src, x0, y0, x1, y1, out = sys.argv[1:7]
x0, y0, x1, y1 = int(x0), int(y0), int(x1), int(y1)
im = Image.open(src).convert("L")
c = im.crop((x0, y0, x1, y1))
w, h = c.size
px = c.load()
cols = [any(px[x, y] < 128 for y in range(h)) for x in range(w)]
runs = []
x = 0
while x < w:
    if cols[x]:
        s = x
        while x < w and cols[x]:
            x += 1
        e = x - 1
        ys = [y for y in range(h) for xx in range(s, e + 1) if px[xx, y] < 128]
        runs.append((s + x0, e + x0, e - s + 1, min(ys) + y0, max(ys) + y0, max(ys) - min(ys) + 1))
    else:
        x += 1
for r in runs:
    print("x %d-%d  w=%d   y %d-%d  h=%d" % r)
c.resize((w * 6, h * 6), Image.NEAREST).save(out)
