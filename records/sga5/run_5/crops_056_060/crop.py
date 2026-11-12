"""Crop a region of a strip and enlarge it. usage: python -I crop.py SRC x0 y0 x1 y1 SCALE OUT"""
import sys
from PIL import Image
src, x0, y0, x1, y1, sc, out = sys.argv[1], *map(int, sys.argv[2:6]), float(sys.argv[6]), sys.argv[7]
im = Image.open(src).convert("L").crop((x0, y0, x1, y1))
im = im.resize((int(im.width * sc), int(im.height * sc)), Image.LANCZOS)
im.save(out)
print(out, im.size)
