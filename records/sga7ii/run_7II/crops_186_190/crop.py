import sys
from PIL import Image

# usage: crop.py page strip x0 y0 x1 y1 scale outname
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = map(int, sys.argv[3:7])
scale = float(sys.argv[7])
out = sys.argv[8]
src = r'C:/Users/user/Documents/sga_scan_check_20261105/run_7II/b186_190/page_%d_s%d.png' % (page, strip)
im = Image.open(src).crop((x0, y0, x1, y1))
im = im.resize((int(im.width * scale), int(im.height * scale)), Image.LANCZOS)
im.save(r'C:/Users/user/Documents/sga_scan_check_20261105/run_7II/crops_186_190/' + out)
print(out, im.size)
