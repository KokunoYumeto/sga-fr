import sys
from PIL import Image

# usage: crop.py page strip x0 y0 x1 y1 scale outname
p, s, x0, y0, x1, y1, scale, out = sys.argv[1:9]
base = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I"
im = Image.open(rf"{base}\b071_075\page_{int(p):03d}_s{int(s)}.png")
c = im.crop((int(x0), int(y0), int(x1), int(y1)))
sc = float(scale)
c = c.resize((int(c.width * sc), int(c.height * sc)), Image.LANCZOS)
c.save(rf"{base}\crops_071_075\{out}.png")
print(c.size)
