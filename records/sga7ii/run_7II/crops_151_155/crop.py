"""Crop a region of a strip and enlarge it.

Usage: python crop.py PAGE STRIP X0 Y0 X1 Y1 SCALE OUTNAME
"""
import sys
from PIL import Image

BASE = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II\b151_155"
OUT = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II\crops_151_155"

page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
scale = float(sys.argv[7])
name = sys.argv[8]
im = Image.open(rf"{BASE}\page_{page}_s{strip}.png")
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(rf"{OUT}\{name}.png")
print(name, c.size)
