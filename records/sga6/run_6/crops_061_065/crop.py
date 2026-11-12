"""Crop a region of a strip image (or a witness TIFF) and upscale it to grey.
usage: python -I crop.py IMAGE X0 Y0 X1 Y1 SCALE OUT_NAME   (coordinates in original pixels)"""
import pathlib
import sys

from PIL import Image

src, x0, y0, x1, y1, scale, out = sys.argv[1], *map(int, sys.argv[2:6]), float(sys.argv[6]), sys.argv[7]
im = Image.open(src).convert("L").crop((x0, y0, x1, y1))
im = im.resize((int(im.width * scale), int(im.height * scale)), Image.LANCZOS)
dest = pathlib.Path(__file__).parent / out
im.save(dest)
print(dest, im.size)
