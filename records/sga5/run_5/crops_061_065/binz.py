"""Crop regions of strips, binarize, upscale with nearest neighbour, and stack them vertically.
usage: python -I binz.py OUT SCALE THRESH PAGE:STRIP:X0:Y0:X1:Y1 [...]"""
import pathlib
import sys

from PIL import Image, ImageDraw

here = pathlib.Path(__file__).resolve().parent
src = here.parent / "b061_065"
out, scale, thresh = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
parts = []
for spec in sys.argv[4:]:
    p, s, x0, y0, x1, y1 = (int(a) for a in spec.split(":"))
    im = Image.open(src / f"page_{p:03d}_s{s}.png").convert("L").crop((x0, y0, x1, y1))
    im = im.point(lambda v: 0 if v < thresh else 255)
    im = im.resize((im.width * scale, im.height * scale), Image.NEAREST)
    parts.append((spec, im))
w = max(i.width for _, i in parts) + 20
h = sum(i.height + 30 for _, i in parts) + 10
canvas = Image.new("L", (w, h), 255)
d = ImageDraw.Draw(canvas)
y = 5
for spec, i in parts:
    d.text((10, y), spec, fill=0)
    canvas.paste(i, (10, y + 20))
    y += i.height + 30
canvas.save(here / out)
print(here / out, canvas.size)
