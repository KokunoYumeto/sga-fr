"""usage: python -I crop.py PAGE STRIP x0 y0 x1 y1 OUTNAME [SCALE]
Coordinates are fractions (0-1) of the strip's width and height. Writes OUTNAME.png into this folder."""
import pathlib
import sys

from PIL import Image

HERE = pathlib.Path(__file__).parent
B = HERE.parent / "b386_390"
page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(float, sys.argv[3:7])
out = sys.argv[7]
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
im = Image.open(B / f"page_{page}_s{strip}.png")
w, h = im.size
box = (int(x0 * w), int(y0 * h), int(x1 * w), int(y1 * h))
c = im.crop(box)
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(HERE / f"{out}.png")
print(im.size, box, c.size)
