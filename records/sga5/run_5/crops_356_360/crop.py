"""Crop a region of a page strip and enlarge it.
usage: python -I crop.py PAGE STRIP X0 Y0 X1 Y1 SCALE NAME"""
import sys
from PIL import Image

page, strip, x0, y0, x1, y1, scale, name = sys.argv[1:9]
src = rf"C:\Users\user\Documents\sga_scan_check_20261105\run_5\b356_360\page_{page}_s{strip}.png"
im = Image.open(src).convert("L")
box = (int(x0), int(y0), int(x1), int(y1))
c = im.crop(box)
s = float(scale)
c = c.resize((int(c.width * s), int(c.height * s)), Image.LANCZOS)
out = rf"C:\Users\user\Documents\sga_scan_check_20261105\run_5\crops_356_360\{name}.png"
c.save(out)
print(out, c.size)
