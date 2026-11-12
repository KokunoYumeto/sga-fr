"""usage: python -I crop.py PAGE STRIP x0 y0 x1 y1 SCALE OUTNAME
Crops page_PAGE_sSTRIP.png to the box and enlarges it by SCALE."""
import sys
from PIL import Image
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = map(int, sys.argv[3:7])
scale = float(sys.argv[7])
out = sys.argv[8]
src = r'C:/Users/user/Documents/sga_scan_check_20261105/run_5/b126_130/page_%03d_s%d.png' % (page, strip)
im = Image.open(src)
if x1 <= 0:
    x1 = im.size[0]
if y1 <= 0:
    y1 = im.size[1]
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.size[0] * scale), int(c.size[1] * scale)), Image.LANCZOS)
c.save(r'C:/Users/user/Documents/sga_scan_check_20261105/run_5/crops_126_130/' + out)
print(im.size, '->', c.size)
