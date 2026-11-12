import sys
from PIL import Image
im = Image.open(sys.argv[1]).convert('L')
w, h = im.size
px = im.load()
th = 128
rows = []
for y in range(h):
    c = sum(1 for x in range(w) if px[x, y] < th)
    rows.append(c)
# print bands of ink
inband = False
for y, c in enumerate(rows):
    if c > 2 and not inband:
        start = y; inband = True
    elif c <= 2 and inband:
        print(f"{start}-{y-1}"); inband = False
if inband:
    print(f"{start}-{h-1}")
