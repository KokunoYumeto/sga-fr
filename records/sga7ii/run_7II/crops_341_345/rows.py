import sys
from PIL import Image
# print bands of rows containing ink: start-end
src = sys.argv[1]
thr = int(sys.argv[2]) if len(sys.argv) > 2 else 128
im = Image.open(src).convert('L')
w, h = im.size
px = im.load()
rows = []
for y in range(h):
    cnt = 0
    for x in range(0, w, 2):
        if px[x, y] < thr:
            cnt += 1
    rows.append(cnt)
bands = []
inb = False
for y, c in enumerate(rows):
    if c > 0 and not inb:
        inb = True; s = y
    elif c == 0 and inb:
        inb = False; bands.append((s, y - 1))
if inb:
    bands.append((s, h - 1))
for b in bands:
    print(b, max(rows[b[0]:b[1]+1]))
