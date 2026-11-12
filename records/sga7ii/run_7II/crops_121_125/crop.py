import sys
from PIL import Image

# usage: crop.py <strip png> <x0> <y0> <x1> <y1> <scale> <out png>
# or:    crop.py <strip png> size
src = sys.argv[1]
im = Image.open(src)
if sys.argv[2] == "size":
    print(im.size)
    sys.exit(0)
x0, y0, x1, y1 = map(int, sys.argv[2:6])
scale = float(sys.argv[6])
out = sys.argv[7]
c = im.crop((x0, y0, x1, y1))
if scale != 1:
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(out)
print(out, c.size)
