"""Crop a region of a strip and enlarge it.
usage: python -I crop.py PAGE STRIP X0 Y0 X1 Y1 SCALE NAME"""
import pathlib
import sys

from PIL import Image

page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = map(int, sys.argv[3:7])
scale = float(sys.argv[7])
name = sys.argv[8]
src = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\b091_095") / f"page_{page:03d}_s{strip}.png"
out = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\crops_091_095") / f"{name}.png"
im = Image.open(src).crop((x0, y0, x1, y1))
im = im.resize((int(im.width * scale), int(im.height * scale)), Image.LANCZOS)
im.save(out)
print(out, im.size)
