"""Crop a region of a strip and enlarge it.
usage: python -I crop.py PAGE STRIP X0 Y0 X1 Y1 SCALE OUTNAME"""
import pathlib
import sys

from PIL import Image

page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
scale = float(sys.argv[7])
out = sys.argv[8]
src = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\b321_325") / f"page_{page}_s{strip}.png"
im = Image.open(src).crop((x0, y0, x1, y1))
im = im.resize((int(im.width * scale), int(im.height * scale)), Image.LANCZOS)
dst = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\crops_321_325") / out
im.save(dst)
print(dst, im.size)
