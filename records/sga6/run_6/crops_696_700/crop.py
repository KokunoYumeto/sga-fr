"""Crop a region of an image and enlarge it.
usage: python -I crop.py SRC X0 Y0 X1 Y1 OUT [SCALE]   (coordinates in the source image's own pixels)"""
import sys

from PIL import Image, ImageOps

src, x0, y0, x1, y1, out = sys.argv[1], *map(int, sys.argv[2:6]), sys.argv[6]
scale = float(sys.argv[7]) if len(sys.argv) > 7 else 3.0
im = Image.open(src).convert("L").crop((x0, y0, x1, y1))
im = ImageOps.autocontrast(im, cutoff=1)
im = im.resize((int(im.width * scale), int(im.height * scale)), Image.LANCZOS)
im.save(out)
print(out, im.size)
