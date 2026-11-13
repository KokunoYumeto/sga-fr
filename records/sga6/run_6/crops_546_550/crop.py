"""crop.py PAGE STRIP X0 Y0 X1 Y1 SCALE OUTNAME  (coordinates in the strip's original pixels)"""
import sys
from PIL import Image
base = r"C:\Users\user\Documents\sga_scan_check_20261105\run_6"
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = map(int, sys.argv[3:7])
scale = float(sys.argv[7])
out = sys.argv[8]
im = Image.open(rf"{base}\b546_550\page_{page:03d}_s{strip}.png")
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(rf"{base}\crops_546_550\{out}")
print(im.size, c.size)
