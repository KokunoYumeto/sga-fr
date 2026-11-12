import sys
from PIL import Image

# usage: lines.py SRC  -> prints y-bands of ink (text lines)
im = Image.open(sys.argv[1]).convert('L')
w, h = im.size
px = im.load()
rows = []
for y in range(h):
    n = 0
    for x in range(0, w, 2):
        if px[x, y] < 128:
            n += 1
    rows.append(n)
bands = []
inb = False
for y, n in enumerate(rows):
    if n > 0 and not inb:
        start = y
        inb = True
    elif n == 0 and inb:
        bands.append((start, y))
        inb = False
if inb:
    bands.append((start, h))
for b in bands:
    if b[1] - b[0] >= 3:
        print(b)
