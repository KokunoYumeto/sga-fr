"""usage: python -I crop.py PAGE STRIP X0 Y0 X1 Y1 SCALE OUTNAME  (coordinates in original strip pixels)"""
import sys
from PIL import Image
page, strip, x0, y0, x1, y1, scale, out = sys.argv[1:9]
src = rf"C:\Users\user\Documents\sga_scan_check_20261105\run_6\b211_215\page_{int(page):03d}_s{strip}.png"
im = Image.open(src)
c = im.crop((int(x0), int(y0), int(x1), int(y1)))
s = float(scale)
c = c.resize((int(c.width * s), int(c.height * s)), Image.LANCZOS)
c.save(rf"C:\Users\user\Documents\sga_scan_check_20261105\run_6\crops_211_215\{out}")
print(c.size)
