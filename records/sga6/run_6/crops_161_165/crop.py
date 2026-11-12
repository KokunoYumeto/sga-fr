import sys
from PIL import Image
src, x0, y0, x1, y1, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
scale = float(sys.argv[7]) if len(sys.argv) > 7 else 2.0
im = Image.open(src)
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width*scale), int(c.height*scale)), Image.LANCZOS)
c.save(out)
print(im.size, c.size)
