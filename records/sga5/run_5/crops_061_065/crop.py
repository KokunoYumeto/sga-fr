"""Crop a region of a strip and upscale it for reading.
usage: python -I crop.py PAGE STRIP X0 Y0 X1 Y1 SCALE OUTNAME"""
import pathlib
import sys

from PIL import Image

here = pathlib.Path(__file__).resolve().parent
src = here.parent / "b061_065"
page, strip, x0, y0, x1, y1, scale, out = sys.argv[1:9]
im = Image.open(src / f"page_{int(page):03d}_s{int(strip)}.png")
c = im.crop((int(x0), int(y0), int(x1), int(y1)))
s = float(scale)
c = c.resize((int(c.width * s), int(c.height * s)), Image.LANCZOS)
c.save(here / out)
print(here / out, c.size)
