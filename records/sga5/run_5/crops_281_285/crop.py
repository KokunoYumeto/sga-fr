"""Crop a region of a strip and enlarge it.

Usage: python -I crop.py PAGE STRIP X0 Y0 X1 Y1 SCALE OUTNAME
"""
import sys
from PIL import Image

BASE = r"C:\Users\user\Documents\sga_scan_check_20261105\run_5"
page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
scale = float(sys.argv[7])
out = sys.argv[8]
im = Image.open(rf"{BASE}\b281_285\page_{page}_s{strip}.png")
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(rf"{BASE}\crops_281_285\{out}.png")
print(c.size)
