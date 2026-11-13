import sys
from PIL import Image
# usage: crop.py strip.png out.png x0 y0 x1 y1 [zoom]  (coordinates in displayed 2000-wide units)
src, out = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = [float(v) for v in sys.argv[3:7]]
zoom = float(sys.argv[7]) if len(sys.argv) > 7 else 2.0
im = Image.open(src)
s = im.size[0] / 2000.0
box = (int(x0 * s), int(y0 * s), int(x1 * s), int(y1 * s))
c = im.crop(box)
c = c.resize((int(c.size[0] * zoom), int(c.size[1] * zoom)), Image.LANCZOS)
c.save(out)
print(out, box, c.size)
