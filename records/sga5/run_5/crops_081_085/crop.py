"""Crop a region of a strip and enlarge it.
usage: python -I crop.py PAGE STRIP x0 y0 x1 y1 SCALE OUTNAME
PAGE like 081, STRIP 1-4; output written next to this script."""
import pathlib
import sys
from PIL import Image

here = pathlib.Path(__file__).parent
page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1, sc = map(int, sys.argv[3:8])
out = here / sys.argv[8]
src = here.parent / "b081_085" / f"page_{page}_s{strip}.png"
im = Image.open(src).crop((x0, y0, x1, y1))
im = im.resize((im.width * sc, im.height * sc), Image.LANCZOS)
im.save(out)
print(out.name, im.size)
