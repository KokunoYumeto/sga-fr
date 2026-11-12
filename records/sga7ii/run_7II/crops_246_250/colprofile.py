"""Print the ink runs (start-end columns) of one text line of a strip: colprofile.py <strip.png> x0 y0 x1 y1 [thresh]
Only the band y0..y1 is used (choose it to cover the x-height of the line, not the underline)."""
import sys
from PIL import Image

src, x0, y0, x1, y1 = sys.argv[1], *map(int, sys.argv[2:6])
th = int(sys.argv[6]) if len(sys.argv) > 6 else 140
im = Image.open(src).convert("L").crop((x0, y0, x1, y1))
w, h = im.size
px = im.load()
ink = [sum(1 for y in range(h) if px[x, y] < th) for x in range(w)]
runs, start = [], None
for x, v in enumerate(ink + [0]):
    if v and start is None:
        start = x
    elif not v and start is not None:
        runs.append((start + x0, x - 1 + x0))
        start = None
print(len(runs), "runs")
prev = None
for a, b in runs:
    gap = "" if prev is None else f" gap {a - prev - 1}"
    print(f"{a}-{b} (w {b - a + 1}){gap}")
    prev = b
