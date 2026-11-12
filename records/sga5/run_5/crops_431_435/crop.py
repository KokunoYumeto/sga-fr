"""Usage: python -I crop.py <page> <strip> <x0> <y0> <x1> <y1> <scale> <outname>"""
import sys
from PIL import Image
b = 'C:/Users/user/Documents/sga_scan_check_20261105/run_5/b431_435/'
page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
s = float(sys.argv[7])
out = sys.argv[8]
im = Image.open(b + 'page_%s_s%s.png' % (page, strip))
c = im.crop((x0, y0, x1, y1))
c = c.resize((int((x1 - x0) * s), int((y1 - y0) * s)), Image.LANCZOS)
c.save('C:/Users/user/Documents/sga_scan_check_20261105/run_5/crops_431_435/' + out)
