"""Crop a region of a DjVu-witness page (w_<filepage>.png) and enlarge it.

Usage: python wcrop.py FILEPAGE X0 Y0 X1 Y1 SCALE OUTNAME
"""
import sys
from PIL import Image

OUT = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II\crops_151_155"

fp = sys.argv[1]
x0, y0, x1, y1 = map(int, sys.argv[2:6])
scale = float(sys.argv[6])
name = sys.argv[7]
im = Image.open(rf"{OUT}\w_{fp}.png").convert("L")
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(rf"{OUT}\{name}.png")
print(name, c.size)
