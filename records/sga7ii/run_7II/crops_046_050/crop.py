import sys
from PIL import Image

# usage: crop.py page strip x0 y0 x1 y1 scale outname
d = 'C:/Users/user/Documents/sga_scan_check_20261105/run_7II/b046_050'
out = 'C:/Users/user/Documents/sga_scan_check_20261105/run_7II/crops_046_050'
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = map(int, sys.argv[3:7])
scale = float(sys.argv[7])
name = sys.argv[8]
im = Image.open(f'{d}/page_{page:03d}_s{strip}.png')
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(f'{out}/{name}.png')
print(c.size)
