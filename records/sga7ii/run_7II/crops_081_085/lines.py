import sys
from PIL import Image
# usage: lines.py <png> : prints row bands containing ink
im = Image.open(sys.argv[1]).convert('L')
w, h = im.size
px = im.load()
thr = 128
rows = []
for y in range(h):
    c = 0
    for x in range(0, w, 2):
        if px[x, y] < thr:
            c += 1
    rows.append(c)
bands = []
inb = False
for y, c in enumerate(rows):
    if c > 0 and not inb:
        start = y; inb = True
    elif c == 0 and inb:
        bands.append((start, y)); inb = False
if inb:
    bands.append((start, h))
print(w, h)
for b in bands:
    # x-extent
    xs = [x for x in range(w) for y in range(b[0], b[1]) if px[x, y] < thr]
    print(b, min(xs) if xs else None, max(xs) if xs else None)
