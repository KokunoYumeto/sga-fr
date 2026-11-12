"""Crop a region of a strip and enlarge it.
usage: python -I crop.py STRIP x0 y0 x1 y1 SCALE OUTNAME"""
import sys
from PIL import Image
src, x0, y0, x1, y1, sc, out = sys.argv[1], *map(int, sys.argv[2:7]), sys.argv[7]
im = Image.open(src).crop((x0, y0, x1, y1))
im = im.resize((im.width * sc, im.height * sc), Image.LANCZOS)
im.save(out)
print(out, im.size)
