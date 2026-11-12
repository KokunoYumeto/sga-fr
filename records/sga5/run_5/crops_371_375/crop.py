import sys
from PIL import Image

# usage: python -I crop.py PAGE STRIP X0 Y0 X1 Y1 SCALE OUTNAME
page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
scale = float(sys.argv[7])
out = sys.argv[8]
src = r'C:\Users\user\Documents\sga_scan_check_20261105\run_5\b371_375\page_%s_s%s.png' % (page, strip)
im = Image.open(src)
c = im.crop((x0, y0, x1, y1))
if scale != 1:
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(r'C:\Users\user\Documents\sga_scan_check_20261105\run_5\crops_371_375\%s' % out)
print(c.size)
