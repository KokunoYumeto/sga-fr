"""Crop a region of a strip and enlarge it.
usage: python -I crop.py PAGE STRIP X0 Y0 X1 Y1 SCALE OUTNAME"""
import sys
from PIL import Image

page, strip, x0, y0, x1, y1 = (int(a) for a in sys.argv[1:7])
scale = float(sys.argv[7])
out = sys.argv[8]
src = rf"C:\Users\user\Documents\sga_scan_check_20261105\run_5\b201_205\page_{page}_s{strip}.png"
im = Image.open(src).crop((x0, y0, x1, y1))
im = im.resize((int(im.width * scale), int(im.height * scale)), Image.LANCZOS)
im.save(rf"C:\Users\user\Documents\sga_scan_check_20261105\run_5\crops_201_205\{out}.png")
print(out, im.size)
