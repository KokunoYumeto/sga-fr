"""usage: python -I crop.py PAGE STRIP x0 y0 x1 y1 OUTNAME [scale]
Crops a region of run_5/b211_215/page_PAGE_sSTRIP.png and writes it (optionally enlarged) to crops_211_215/OUTNAME."""
import sys, os
from PIL import Image

base = os.path.join('C:' + os.sep, 'Users', 'user', 'Documents', 'sga_scan_check_20261105', 'run_5')
page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
out = sys.argv[7]
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
im = Image.open(os.path.join(base, 'b211_215', 'page_%s_s%s.png' % (page, strip)))
print('strip size', im.size)
c = im.crop((x0, y0, x1, y1))
if scale != 1:
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(os.path.join(base, 'crops_211_215', out))
print('saved', out, c.size)
