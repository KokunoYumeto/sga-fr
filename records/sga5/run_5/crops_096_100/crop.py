"""Crop a region of a strip and enlarge it.
usage: python -I crop.py PAGE STRIP X0 Y0 X1 Y1 SCALE OUTNAME"""
import pathlib
import sys

from PIL import Image

here = pathlib.Path(__file__).resolve().parent
page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
scale = float(sys.argv[7])
out = sys.argv[8]
src = here.parent / "b096_100" / f"page_{page}_s{strip}.png"
im = Image.open(src).crop((x0, y0, x1, y1))
im = im.resize((int(im.width * scale), int(im.height * scale)), Image.LANCZOS)
im.save(here / out)
print(here / out, im.size)
