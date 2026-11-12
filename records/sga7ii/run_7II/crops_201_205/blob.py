import sys
from PIL import Image
# usage: blob.py src x0 y0 x1 y1 [thr] : print bounding box and dark-pixel map of the region
src = sys.argv[1]
x0, y0, x1, y1 = map(int, sys.argv[2:6])
thr = int(sys.argv[6]) if len(sys.argv) > 6 else 140
im = Image.open(src).convert('L').crop((x0, y0, x1, y1))
w, h = im.size
px = im.load()
rows = []
for y in range(h):
    rows.append(''.join('#' if px[x, y] < thr else '.' for x in range(w)))
dark = [(x, y) for y in range(h) for x in range(w) if px[x, y] < thr]
if dark:
    xs = [p[0] for p in dark]; ys = [p[1] for p in dark]
    print('bbox', min(xs)+x0, min(ys)+y0, max(xs)+x0, max(ys)+y0, 'w', max(xs)-min(xs)+1, 'h', max(ys)-min(ys)+1, 'n', len(dark))
for r in rows:
    print(r)
