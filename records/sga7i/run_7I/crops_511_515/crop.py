import sys
from PIL import Image, ImageOps

# usage: crop.py src x0 y0 x1 y1 out [scale] [contrast]
src, x0, y0, x1, y1, out = sys.argv[1:7]
scale = float(sys.argv[7]) if len(sys.argv) > 7 else 2.0
contrast = sys.argv[8] if len(sys.argv) > 8 else "no"
im = Image.open(src).convert("L")
c = im.crop((int(x0), int(y0), int(x1), int(y1)))
if contrast == "yes":
    c = ImageOps.autocontrast(c, cutoff=1)
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(out)
print(out, c.size)
