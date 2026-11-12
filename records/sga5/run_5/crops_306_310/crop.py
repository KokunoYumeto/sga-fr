"""usage: python -I crop.py PAGE STRIP x0 y0 x1 y1 SCALE OUTNAME"""
import sys, os
from PIL import Image
here = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(os.path.dirname(here), 'b306_310')
page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
scale = float(sys.argv[7])
out = sys.argv[8]
im = Image.open(os.path.join(src, f'page_{page}_s{strip}.png'))
if x0 == -1:
    print(im.size)
    sys.exit()
c = im.crop((x0, y0, x1, y1))
if scale != 1:
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(os.path.join(here, out))
print('saved', out, c.size, 'from', im.size)
