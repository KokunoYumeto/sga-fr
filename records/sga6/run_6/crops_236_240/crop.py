"""Crop a region of a page strip (or witness page) and enlarge it.

usage: python -I crop.py SRC OUT x0 y0 x1 y1 [scale]
Coordinates are in the source image's own pixels.
"""
import sys
from PIL import Image

src, out = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
scale = float(sys.argv[7]) if len(sys.argv) > 7 else 2.0
im = Image.open(src)
box = im.crop((x0, y0, x1, y1))
box = box.resize((int(box.width * scale), int(box.height * scale)), Image.LANCZOS)
box.save(out)
print(out, box.size)
