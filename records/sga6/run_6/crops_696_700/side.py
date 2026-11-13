"""Paste several crops (same source scale) side by side, enlarged, for comparing glyphs.
usage: python -I side.py OUT SCALE SRC:X0:Y0:X1:Y1 [SRC:X0:Y0:X1:Y1 ...]"""
import sys

from PIL import Image, ImageOps

out, scale = sys.argv[1], float(sys.argv[2])
ims = []
for spec in sys.argv[3:]:
    src, *c = spec.rsplit(":", 4)
    x0, y0, x1, y1 = map(int, c)
    im = ImageOps.autocontrast(Image.open(src).convert("L").crop((x0, y0, x1, y1)), cutoff=1)
    ims.append(im.resize((int(im.width * scale), int(im.height * scale)), Image.LANCZOS))
w = sum(i.width for i in ims) + 20 * (len(ims) - 1)
h = max(i.height for i in ims)
canvas = Image.new("L", (w, h), 255)
x = 0
for i in ims:
    canvas.paste(i, (x, 0))
    x += i.width + 20
canvas.save(out)
print(out, canvas.size)
