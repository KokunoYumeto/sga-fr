import sys
from PIL import Image

# usage: python -I crop.py <page> <strip> <x0> <y0> <x1> <y1> <scale> <outname>
base = r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\b446_450"
out = r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\crops_446_450"
page, strip, x0, y0, x1, y1, scale, name = sys.argv[1:9]
im = Image.open(rf"{base}\page_{page}_s{strip}.png")
box = (int(x0), int(y0), int(x1), int(y1))
c = im.crop(box)
s = float(scale)
c = c.resize((int(c.width * s), int(c.height * s)), Image.LANCZOS)
c.save(rf"{out}\{name}.png")
print(c.size)
