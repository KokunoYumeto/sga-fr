"""crop.py PAGE STRIP x0 y0 x1 y1 SCALE OUTNAME  -- crop a strip of the batch and enlarge it."""
import sys
from PIL import Image
page, strip, x0, y0, x1, y1, scale, out = sys.argv[1:9]
src = r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\b291_295\page_%s_s%s.png" % (page, strip)
im = Image.open(src)
c = im.crop((int(x0), int(y0), int(x1), int(y1)))
s = float(scale)
c = c.resize((int(c.width * s), int(c.height * s)), Image.LANCZOS)
c.save(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\crops_291_295\%s.png" % out)
print(im.size, c.size)
