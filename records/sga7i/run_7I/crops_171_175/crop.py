"""Enlarged crops of scan strips: python crop.py NAME STRIP x0 y0 x1 y1 [SCALE]."""
import sys
import pathlib
from PIL import Image

B = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I\b171_175")
OUT = pathlib.Path(__file__).resolve().parent

name, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
scale = float(sys.argv[7]) if len(sys.argv) > 7 else 3.0
im = Image.open(B / strip).crop((x0, y0, x1, y1))
im = im.resize((int(im.width * scale), int(im.height * scale)), Image.LANCZOS)
im.save(OUT / f"{name}.png")
print(OUT / f"{name}.png", im.size)
