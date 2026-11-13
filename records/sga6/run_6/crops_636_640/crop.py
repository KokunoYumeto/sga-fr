import sys
from PIL import Image
# usage: crop.py SRC OUT x0 y0 x1 y1 [scale]   (fractions 0..1 allowed for x0..y1)
src, out = sys.argv[1], sys.argv[2]
im = Image.open(src).convert("L")
W, H = im.size
vals = [float(v) for v in sys.argv[3:7]]
if all(v <= 1.0 for v in vals):
    x0, y0, x1, y1 = int(vals[0] * W), int(vals[1] * H), int(vals[2] * W), int(vals[3] * H)
else:
    x0, y0, x1, y1 = map(int, vals)
scale = float(sys.argv[7]) if len(sys.argv) > 7 else 2.0
c = im.crop((x0, y0, x1, y1))
c = c.resize((max(1, int(c.width * scale)), max(1, int(c.height * scale))), Image.LANCZOS)
c.save(out)
print(out, im.size, (x0, y0, x1, y1), c.size)
