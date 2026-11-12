"""Crop a region of a strip and enlarge it.
usage: python -I crop.py PAGE STRIP X0 Y0 X1 Y1 [SCALE] [NAME]"""
import pathlib
import sys

from PIL import Image

here = pathlib.Path(__file__).parent
src = here.parent / "b131_135"
page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
scale = float(sys.argv[7]) if len(sys.argv) > 7 else 2.0
name = sys.argv[8] if len(sys.argv) > 8 else f"p{page}_s{strip}_{x0}_{y0}"
im = Image.open(src / f"page_{page}_s{strip}.png").crop((x0, y0, x1, y1))
im = im.resize((int(im.width * scale), int(im.height * scale)), Image.LANCZOS)
out = here / f"{name}.png"
im.save(out)
print(out)
