"""Crop a region of a strip and enlarge it.
usage: python -I crop.py STRIP x0 y0 x1 y1 SCALE OUTNAME"""
import pathlib
import sys

from PIL import Image

here = pathlib.Path(__file__).parent
strip, x0, y0, x1, y1, scale, out = sys.argv[1], *map(int, sys.argv[2:7]), sys.argv[7]
im = Image.open(here.parent / "b021_025" / strip)
c = im.crop((x0, y0, x1, y1))
c = c.resize((c.width * scale, c.height * scale), Image.LANCZOS)
c.save(here / out)
print(here / out, c.size)
