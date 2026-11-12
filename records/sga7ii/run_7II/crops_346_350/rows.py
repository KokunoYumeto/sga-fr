import sys
from PIL import Image
im = Image.open(sys.argv[1]).convert('L')
w, h = im.size
px = im.load()
rows = []
for y in range(h):
    dark = sum(1 for x in range(0, w, 2) if px[x, y] < 128)
    rows.append(dark)
# print bands of text
inb = False
for y, d in enumerate(rows):
    if d > 0 and not inb:
        start = y; inb = True
    elif d == 0 and inb:
        print(f"band {start}-{y-1}")
        inb = False
if inb: print(f"band {start}-{h-1}")
