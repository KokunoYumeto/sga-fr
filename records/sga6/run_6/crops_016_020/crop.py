"""Crop helper for the SGA 6 pp. 16-20 check.

usage:
  python -I crop.py info FILE
  python -I crop.py crop FILE X0 Y0 X1 Y1 OUT [SCALE]
  python -I crop.py half FILE OUT            (downscaled overview of a whole page)
  python -I crop.py band FILE Y0 Y1 OUT [SCALE]  (full-width horizontal band)
Coordinates are in the pixels of FILE.
"""
import sys

from PIL import Image

cmd = sys.argv[1]
im = Image.open(sys.argv[2])
if cmd == "info":
    print(im.size, im.mode)
elif cmd == "crop":
    x0, y0, x1, y1 = map(int, sys.argv[3:7])
    out = sys.argv[7]
    scale = float(sys.argv[8]) if len(sys.argv) > 8 else 1.0
    c = im.convert("L").crop((x0, y0, x1, y1))
    if scale != 1.0:
        c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
    c.save(out)
    print("saved", out, c.size)
elif cmd == "half":
    out = sys.argv[3]
    c = im.convert("L")
    c = c.resize((c.width // 2, c.height // 2), Image.LANCZOS)
    c.save(out)
    print("saved", out, c.size)
elif cmd == "band":
    y0, y1 = map(int, sys.argv[3:5])
    out = sys.argv[5]
    scale = float(sys.argv[6]) if len(sys.argv) > 6 else 1.0
    c = im.convert("L").crop((0, y0, im.width, y1))
    if scale != 1.0:
        c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
    c.save(out)
    print("saved", out, c.size)
