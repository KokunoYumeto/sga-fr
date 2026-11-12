"""Column profile (mean grey value) of an R stem over given row ranges.
usage: python -I stemprof.py PAGE STRIP X0 X1 Y0:Y1 [Y0:Y1 ...]"""
import pathlib, sys
from PIL import Image
here = pathlib.Path(__file__).resolve().parent
p, s, x0, x1 = (int(a) for a in sys.argv[1:5])
im = Image.open(here.parent / "b061_065" / f"page_{p:03d}_s{s}.png").convert("L")
px = im.load()
for rr in sys.argv[5:]:
    y0, y1 = (int(a) for a in rr.split(":"))
    vals = [sum(px[x, y] for y in range(y0, y1)) / (y1 - y0) for x in range(x0, x1)]
    print(f"rows {y0}-{y1-1}: " + " ".join(f"{v:3.0f}" for v in vals))
