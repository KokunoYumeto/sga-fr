import sys
from PIL import Image
src, out, x0, y0, x1, y1 = sys.argv[1], sys.argv[2], *map(int, sys.argv[3:7])
scale = float(sys.argv[7]) if len(sys.argv) > 7 else 3
im = Image.open(src).crop((x0, y0, x1, y1))
im = im.resize((int((x1 - x0) * scale), int((y1 - y0) * scale)), Image.LANCZOS)
im.save(out)
print(out, im.size)
