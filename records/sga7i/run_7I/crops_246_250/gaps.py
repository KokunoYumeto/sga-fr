import sys
from PIL import Image
# usage: gaps.py src x0 y0 x1 y1 [thresh]
# prints runs of ink columns and blank gaps (in source pixels) inside the box
src = sys.argv[1]
x0, y0, x1, y1 = map(int, sys.argv[2:6])
th = int(sys.argv[6]) if len(sys.argv) > 6 else 140
im = Image.open(src).convert("L")
px = im.load()
cols = []
for x in range(x0, x1):
    ink = sum(1 for y in range(y0, y1) if px[x, y] < th)
    cols.append(ink > 0)
runs = []
cur = cols[0]; start = 0
for i, c in enumerate(cols[1:], 1):
    if c != cur:
        runs.append((cur, start + x0, i - start))
        cur = c; start = i
runs.append((cur, start + x0, len(cols) - start))
print(" ".join(("I" if c else "_") + f"{s}:{w}" for c, s, w in runs))
