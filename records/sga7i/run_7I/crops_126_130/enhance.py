import sys
from PIL import Image, ImageOps

# usage: enhance.py <src png> <x0> <y0> <x1> <y1> <scale> <out png>
# crops, converts to grey, stretches contrast strongly to reveal faint strokes
src, x0, y0, x1, y1, scale, out = sys.argv[1:8]
im = Image.open(src).convert('L')
c = im.crop((int(x0), int(y0), int(x1), int(y1)))
c = ImageOps.autocontrast(c, cutoff=1)
# gamma to emphasise light-grey marks
lut = [int(255 * ((v / 255.0) ** 2.2)) for v in range(256)]
c = c.point(lut)
s = float(scale)
c = c.resize((int(c.width * s), int(c.height * s)), Image.NEAREST)
c.save(out)
print(out, c.size)
