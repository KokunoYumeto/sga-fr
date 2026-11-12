import sys
from PIL import Image
# usage: crop.py page strip x0 y0 x1 y1 scale outname
p, s, x0, y0, x1, y1, sc, out = sys.argv[1:9]
im = Image.open(f'b461_465/page_{p}_s{s}.png')
c = im.crop((int(x0), int(y0), int(x1), int(y1)))
sc = float(sc)
c = c.resize((int(c.width*sc), int(c.height*sc)), Image.LANCZOS)
c.save(f'crops_461_465/{out}.png')
print(c.size)
