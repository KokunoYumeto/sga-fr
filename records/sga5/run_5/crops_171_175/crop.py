"""Crop a region of a strip image and enlarge it.

Usage: python -I crop.py PAGE STRIP X0 Y0 X1 Y1 SCALE OUTNAME
"""
import sys
from PIL import Image

BASE = r"C:/Users/user/Documents/sga_scan_check_20261105/run_5/b171_175"
OUT = r"C:/Users/user/Documents/sga_scan_check_20261105/run_5/crops_171_175"

page, strip, x0, y0, x1, y1, scale, name = sys.argv[1:9]
im = Image.open(f"{BASE}/page_{int(page):03d}_s{strip}.png")
box = (int(x0), int(y0), int(x1), int(y1))
c = im.crop(box)
s = float(scale)
c = c.resize((int(c.width * s), int(c.height * s)), Image.LANCZOS)
c.save(f"{OUT}/{name}.png")
print(f"{OUT}/{name}.png", c.size)
