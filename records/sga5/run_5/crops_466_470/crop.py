"""Crop a region of a page strip and enlarge it.
usage: python -I crop.py PAGE STRIP X0 Y0 X1 Y1 SCALE OUTNAME"""
import sys
from pathlib import Path
from PIL import Image

base = Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\b466_470")
out = Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\crops_466_470")
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = map(int, sys.argv[3:7])
scale = float(sys.argv[7])
name = sys.argv[8]
im = Image.open(base / f"page_{page:03d}_s{strip}.png").convert("L")
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(out / name)
print(out / name, c.size)
