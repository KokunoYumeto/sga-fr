"""Crop a region of a strip and enlarge it.
usage: python -I crop.py PAGE STRIP X0 Y0 X1 Y1 SCALE OUTNAME"""
import pathlib
import sys

from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE.parent / "b231_235"
page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
scale = float(sys.argv[7])
out = HERE / sys.argv[8]
im = Image.open(SRC / f"page_{page}_s{strip}.png").crop((x0, y0, x1, y1))
im = im.resize((int(im.width * scale), int(im.height * scale)), Image.LANCZOS)
im.save(out)
print(out)
