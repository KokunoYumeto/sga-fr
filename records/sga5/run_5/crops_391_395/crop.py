"""Crop a region of a strip and enlarge it.
usage: python -I crop.py PAGE STRIP X0 Y0 X1 Y1 SCALE OUTNAME"""
import sys
from PIL import Image

page, strip, x0, y0, x1, y1, scale, out = sys.argv[1:9]
src = f"C:/Users/user/Documents/sga_scan_check_20261105/run_5/b391_395/page_{page}_s{strip}.png"
im = Image.open(src)
box = (int(x0), int(y0), int(x1), int(y1))
c = im.crop(box)
s = float(scale)
c = c.resize((int(c.width * s), int(c.height * s)), Image.LANCZOS)
c.save(f"C:/Users/user/Documents/sga_scan_check_20261105/run_5/crops_391_395/{out}.png")
print(out, c.size)
