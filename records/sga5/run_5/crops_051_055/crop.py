import sys
from PIL import Image
# usage: crop.py page strip x0 y0 x1 y1 scale outname
page, strip, x0, y0, x1, y1, scale, out = sys.argv[1:9]
base = r"C:/Users/user/Documents/sga_scan_check_20261105/run_5/b051_055"
im = Image.open(f"{base}/page_{int(page):03d}_s{strip}.png")
c = im.crop((int(x0), int(y0), int(x1), int(y1)))
s = float(scale)
c = c.resize((int(c.width * s), int(c.height * s)), Image.LANCZOS)
c.save(f"C:/Users/user/Documents/sga_scan_check_20261105/run_5/crops_051_055/{out}.png")
print(c.size)
