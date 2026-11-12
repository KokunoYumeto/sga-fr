import sys
from PIL import Image

# usage: lines.py SRC  -> prints y-ranges (and x-extent) of ink rows
src = sys.argv[1]
thr = int(sys.argv[2]) if len(sys.argv) > 2 else 128
im = Image.open(src).convert('L')
w, h = im.size
px = im.load()
rows = []
for y in range(h):
    xs = [x for x in range(w) if px[x, y] < thr]
    rows.append((len(xs), xs[0] if xs else None, xs[-1] if xs else None))
inrun = False
start = 0
for y, (n, x0, x1) in enumerate(rows + [(0, None, None)]):
    if n > 0 and not inrun:
        inrun = True
        start = y
    elif n == 0 and inrun:
        inrun = False
        seg = rows[start:y]
        xs0 = [r[1] for r in seg if r[1] is not None]
        xs1 = [r[2] for r in seg if r[2] is not None]
        print(f"y {start}-{y-1}  x {min(xs0)}-{max(xs1)}  ink {sum(r[0] for r in seg)}")
