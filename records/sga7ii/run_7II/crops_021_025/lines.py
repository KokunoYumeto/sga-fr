import sys
from PIL import Image

# usage: python -I lines.py <strip.png> [threshold]
# prints y-ranges of ink rows (text lines) with x-extent
src = sys.argv[1]
thr = int(sys.argv[2]) if len(sys.argv) > 2 else 128
im = Image.open(src).convert('L')
w, h = im.size
px = im.load()
rows = []
for y in range(h):
    xs = [x for x in range(w) if px[x, y] < thr]
    rows.append((len(xs), min(xs) if xs else None, max(xs) if xs else None))
inrun = False
start = 0
for y in range(h + 1):
    ink = y < h and rows[y][0] > 0
    if ink and not inrun:
        inrun = True
        start = y
    elif not ink and inrun:
        inrun = False
        xmin = min(r[1] for r in rows[start:y] if r[1] is not None)
        xmax = max(r[2] for r in rows[start:y] if r[2] is not None)
        print(f"y {start}-{y - 1}  x {xmin}-{xmax}")
