import sys
from PIL import Image
# usage: profile.py src x0 y0 x1 y1 thresh -> prints runs of ink columns
src = sys.argv[1]
x0, y0, x1, y1 = map(int, sys.argv[2:6])
th = int(sys.argv[6]) if len(sys.argv) > 6 else 140
im = Image.open(src).convert('L')
px = im.load()
cols = []
for x in range(x0, x1):
    n = sum(1 for y in range(y0, y1) if px[x, y] < th)
    cols.append(n)
runs = []
start = None
for i, n in enumerate(cols):
    if n > 0 and start is None:
        start = i
    if n == 0 and start is not None:
        runs.append((x0 + start, x0 + i - 1))
        start = None
if start is not None:
    runs.append((x0 + start, x1 - 1))
for a, b in runs:
    print(a, b, b - a + 1)
