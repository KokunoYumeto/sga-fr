import sys
from PIL import Image, ImageOps
# usage: zoom_contrast.py src out x0 y0 x1 y1 scale
src, out = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7]); s = int(sys.argv[7])
im = Image.open(src).crop((x0, y0, x1, y1))
im = ImageOps.autocontrast(im, cutoff=1)
im = im.resize((im.width * s, im.height * s), Image.NEAREST)
im.save(out); print(out, im.size)
# also print a coarse text map of dark pixels
px = Image.open(src).crop((x0, y0, x1, y1))
w, h = px.size
for y in range(h):
    print(''.join('#' if px.getpixel((x, y)) < 120 else ('+' if px.getpixel((x, y)) < 170 else '.') for x in range(w)))
