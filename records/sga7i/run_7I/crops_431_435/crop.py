import sys
from PIL import Image
src, x0, y0, x1, y1, out = sys.argv[1], *map(int, sys.argv[2:6]), sys.argv[6]
scale = int(sys.argv[7]) if len(sys.argv) > 7 else 3
im = Image.open(src).crop((x0, y0, x1, y1))
im = im.resize((im.width * scale, im.height * scale), Image.LANCZOS)
im.save(out)
