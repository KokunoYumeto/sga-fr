"""Crop a region of a strip and enlarge it.
usage: python -I crop.py PAGE STRIP X0 Y0 X1 Y1 SCALE NAME"""
import pathlib
import sys

from PIL import Image

page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
scale = float(sys.argv[7])
name = sys.argv[8]
base = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
im = Image.open(base / "b186_190" / f"page_{page}_s{strip}.png")
print("strip size", im.size)
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
out = base / "crops_186_190" / f"{name}.png"
c.save(out)
print(out)
