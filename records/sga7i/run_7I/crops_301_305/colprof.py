import sys
from PIL import Image

# usage: colprof.py src x0 y0 x1 y1 [thresh]
# prints runs of ink / blank columns in the box
src = sys.argv[1]
x0, y0, x1, y1 = map(int, sys.argv[2:6])
th = int(sys.argv[6]) if len(sys.argv) > 6 else 140
im = Image.open(src).convert('L')
px = im.load()
cols = []
for x in range(x0, x1):
    ink = sum(1 for y in range(y0, y1) if px[x, y] < th)
    cols.append(ink)
runs = []
cur = None
start = x0
for i, v in enumerate(cols):
    s = v > 0
    if cur is None:
        cur = s
        start = x0 + i
    elif s != cur:
        runs.append((cur, start, x0 + i - 1))
        cur = s
        start = x0 + i
runs.append((cur, start, x1 - 1))
for s, a, b in runs:
    print(('INK ' if s else 'gap ') + f'{a}-{b} ({b - a + 1})')
