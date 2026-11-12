import sys
from PIL import Image

# usage: python -I cols.py <strip.png> <x0> <y0> <x1> <y1> [threshold]
# prints x-ranges of ink columns (glyph runs) inside the box, with their y-extent
src = sys.argv[1]
x0, y0, x1, y1 = map(int, sys.argv[2:6])
thr = int(sys.argv[6]) if len(sys.argv) > 6 else 128
im = Image.open(src).convert('L')
px = im.load()
cols = []
for x in range(x0, x1):
    ys = [y for y in range(y0, y1) if px[x, y] < thr]
    cols.append((x, ys))
inrun = False
start = 0
for i in range(len(cols) + 1):
    ink = i < len(cols) and len(cols[i][1]) > 0
    if ink and not inrun:
        inrun = True
        start = i
    elif not ink and inrun:
        inrun = False
        ys = [y for c in cols[start:i] for y in c[1]]
        print(f"x {cols[start][0]}-{cols[i - 1][0]} (w {i - start})  y {min(ys)}-{max(ys)}")
