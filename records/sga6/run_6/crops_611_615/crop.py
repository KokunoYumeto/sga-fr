"""Crop helper for the scan check of SGA 6 folios 611-615.

usage: python -I crop.py SRC X0 Y0 X1 Y1 OUT [SCALE]
SRC is a PNG strip or a witness PGM; coordinates are in SRC pixels; SCALE enlarges the crop (default 2).
"""
import sys
from PIL import Image

src, x0, y0, x1, y1, out = sys.argv[1], *map(int, sys.argv[2:6]), sys.argv[6]
scale = float(sys.argv[7]) if len(sys.argv) > 7 else 2.0
im = Image.open(src)
c = im.crop((x0, y0, x1, y1))
if scale != 1:
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(out)
print(out, c.size)
