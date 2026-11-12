"""Crop a box from a strip and enlarge it.

usage: python -I crop.py PAGE STRIP X0 Y0 X1 Y1 SCALE NAME
writes crops_396_400/NAME.png
"""
import sys
import pathlib
from PIL import Image

here = pathlib.Path(__file__).resolve().parent
src = here.parent / "b396_400"
page, strip, x0, y0, x1, y1, scale, name = sys.argv[1:9]
im = Image.open(src / f"page_{page}_s{strip}.png")
box = (int(x0), int(y0), int(x1), int(y1))
c = im.crop(box)
s = float(scale)
c = c.resize((int(c.width * s), int(c.height * s)), Image.LANCZOS)
out = here / f"{name}.png"
c.save(out)
print(out, c.size)
