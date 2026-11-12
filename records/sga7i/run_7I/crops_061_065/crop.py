import sys
from PIL import Image

# usage: crop.py <page> <strip> <x0> <y0> <x1> <y1> <outname> [scale]
page, strip, x0, y0, x1, y1, out = sys.argv[1:8]
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
src = r'C:/Users/user/Documents/sga_scan_check_20261105/run_7I/b061_065/page_%03d_s%d.png' % (int(page), int(strip))
im = Image.open(src)
c = im.crop((int(x0), int(y0), int(x1), int(y1)))
if scale != 1.0:
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(r'C:/Users/user/Documents/sga_scan_check_20261105/run_7I/crops_061_065/' + out)
print(out, c.size)
