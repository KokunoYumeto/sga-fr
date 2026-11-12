"""Crop a region of an image (strip PNG or witness TIFF) and upscale it, in grey.
usage: python -I crop.py IMAGE X0 Y0 X1 Y1 SCALE OUT_NAME   (coordinates in original pixels; X1/Y1 = 0 means full size)"""
import pathlib
import sys

from PIL import Image

here = pathlib.Path(__file__).parent
src, x0, y0, x1, y1, scale, out = sys.argv[1], *map(int, sys.argv[2:6]), float(sys.argv[6]), sys.argv[7]
im = Image.open(src).convert("L")
if x1 == 0:
    x1 = im.width
if y1 == 0:
    y1 = im.height
im = im.crop((x0, y0, x1, y1))
im = im.resize((max(1, int(im.width * scale)), max(1, int(im.height * scale))), Image.LANCZOS)
dest = here / out
im.save(dest)
print(dest, im.size)
