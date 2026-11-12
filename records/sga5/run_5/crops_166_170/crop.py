"""Crop a region of a strip and enlarge it: python -I crop.py PAGE STRIP X0 Y0 X1 Y1 [SCALE] [NAME]"""
import sys
import pathlib
from PIL import Image

B = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\b166_170")
C = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\crops_166_170")

page, strip, x0, y0, x1, y1 = sys.argv[1:7]
scale = float(sys.argv[7]) if len(sys.argv) > 7 else 2.0
name = sys.argv[8] if len(sys.argv) > 8 else f"p{page}_s{strip}_{x0}_{y0}"
im = Image.open(B / f"page_{page}_s{strip}.png")
box = tuple(int(v) for v in (x0, y0, x1, y1))
c = im.crop(box)
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
out = C / f"{name}.png"
c.save(out)
print(out)
