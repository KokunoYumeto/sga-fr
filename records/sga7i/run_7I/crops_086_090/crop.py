import sys
from PIL import Image

# usage: crop.py page strip x0 y0 x1 y1 scale outname
# coordinates in original strip pixels
BASE = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I"
page, strip, x0, y0, x1, y1, scale, out = sys.argv[1:9]
im = Image.open(rf"{BASE}\b086_090\page_{int(page):03d}_s{strip}.png")
box = (int(x0), int(y0), int(x1), int(y1))
c = im.crop(box)
s = float(scale)
c = c.resize((int(c.width * s), int(c.height * s)), Image.LANCZOS)
c.save(rf"{BASE}\crops_086_090\{out}.png")
print(out, c.size)
