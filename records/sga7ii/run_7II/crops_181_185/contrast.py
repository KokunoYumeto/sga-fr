import sys
from PIL import Image, ImageOps
src, out = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
scale = float(sys.argv[7])
im = Image.open(src).convert('L').crop((x0, y0, x1, y1))
# print min pixel value per column band to detect faint marks
w, h = im.size
px = im.load()
cols = []
for x in range(w):
    cols.append(min(px[x, y] for y in range(h)))
print('column minima:', cols)
im = ImageOps.autocontrast(im, cutoff=1)
im = im.resize((int(w * scale), int(h * scale)), Image.LANCZOS)
im.save(out)
