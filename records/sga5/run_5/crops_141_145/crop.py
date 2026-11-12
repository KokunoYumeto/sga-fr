"""Crop a box from a strip and enlarge it.
usage: python -I crop.py PAGE STRIP X0 Y0 X1 Y1 SCALE OUTNAME"""
import sys
from PIL import Image

page, strip, x0, y0, x1, y1, scale = (int(a) for a in sys.argv[1:8])
out = sys.argv[8]
src = rf"C:\Users\user\Documents\sga_scan_check_20261105\run_5\b141_145\page_{page}_s{strip}.png"
im = Image.open(src).crop((x0, y0, x1, y1))
im = im.resize((im.width * scale, im.height * scale), Image.LANCZOS)
im.save(rf"C:\Users\user\Documents\sga_scan_check_20261105\run_5\crops_141_145\{out}.png")
print(im.size)
