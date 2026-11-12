"""crop.py main FOLIO STRIP x0 y0 x1 y1 SCALE OUT  -> crop of the main-scan strip (coordinates in strip pixels)
   crop.py wit FOLIO x0 y0 x1 y1 SCALE OUT         -> crop of the rendered witness page"""
import pathlib
import sys

from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
B = HERE.parent / "b316_320"
mode = sys.argv[1]
folio = int(sys.argv[2])
if mode == "main":
    strip = int(sys.argv[3])
    x0, y0, x1, y1 = map(int, sys.argv[4:8])
    scale = float(sys.argv[8])
    out = HERE / sys.argv[9]
    im = Image.open(B / f"page_{folio}_s{strip}.png")
else:
    x0, y0, x1, y1 = map(int, sys.argv[3:7])
    scale = float(sys.argv[7])
    out = HERE / sys.argv[8]
    im = Image.open(HERE / f"wit_{folio}.png")
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(out)
print(out, c.size)
