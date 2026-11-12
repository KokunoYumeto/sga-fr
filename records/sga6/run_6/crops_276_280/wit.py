import sys
from PIL import Image
# usage: wit.py src.tif out.png [x0 y0 x1 y1 scale]  (fractions of width/height for the box)
src, out = sys.argv[1], sys.argv[2]
im = Image.open(src).convert('L')
if len(sys.argv) > 3:
    fx0, fy0, fx1, fy1 = map(float, sys.argv[3:7])
    s = float(sys.argv[7])
    W, H = im.size
    im = im.crop((int(fx0 * W), int(fy0 * H), int(fx1 * W), int(fy1 * H)))
    if s != 1:
        im = im.resize((int(im.width * s), int(im.height * s)), Image.LANCZOS)
else:
    im.thumbnail((1400, 2000))
im.save(out)
print(im.size)
