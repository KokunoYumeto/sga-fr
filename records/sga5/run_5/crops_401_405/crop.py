"""Crop a region of a strip and enlarge it.  usage: python -I -B crop.py PAGE STRIP X0 Y0 X1 Y1 SCALE NAME"""
import sys
from PIL import Image
page, strip, x0, y0, x1, y1, scale, name = sys.argv[1:9]
src = f"C:/Users/user/Documents/sga_scan_check_20261105/run_5/b401_405/page_{page}_s{strip}.png"
im = Image.open(src).crop((int(x0), int(y0), int(x1), int(y1)))
s = float(scale)
im = im.resize((int(im.width * s), int(im.height * s)), Image.LANCZOS)
out = f"C:/Users/user/Documents/sga_scan_check_20261105/run_5/crops_401_405/{name}.png"
im.save(out)
print(out, im.size)
