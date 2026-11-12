"""Crop helper for the SGA 6 pp. 31-35 check.

usage:
  python -I crop.py info FILE
  python -I crop.py crop FILE X0 Y0 X1 Y1 OUT [SCALE]
  python -I crop.py half FILE OUT [FACTOR]      (downscaled overview of a whole page)
  python -I crop.py contrast FILE X0 Y0 X1 Y1 OUT SCALE [LO HI]
Coordinates are in the pixels of FILE.
"""
import sys

import numpy as np
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
    f = float(sys.argv[4]) if len(sys.argv) > 4 else 2.0
    c = im.convert("L")
    c = c.resize((int(c.width / f), int(c.height / f)), Image.LANCZOS)
    c.save(out)
    print("saved", out, c.size)
elif cmd == "contrast":
    x0, y0, x1, y1 = map(int, sys.argv[3:7])
    out = sys.argv[7]
    scale = float(sys.argv[8])
    a = np.array(im.convert("L").crop((x0, y0, x1, y1))).astype(float)
    lo = float(sys.argv[9]) if len(sys.argv) > 9 else np.percentile(a, 1)
    hi = float(sys.argv[10]) if len(sys.argv) > 10 else np.percentile(a, 60)
    a = np.clip((a - lo) / max(1.0, hi - lo) * 255, 0, 255).astype(np.uint8)
    c = Image.fromarray(a)
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
    c.save(out)
    print("saved", out, c.size, "lo", lo, "hi", hi)
