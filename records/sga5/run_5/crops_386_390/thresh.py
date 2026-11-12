"""usage: python -I thresh.py PAGE STRIP x0 y0 x1 y1 OUTNAME SCALE THRESH -- binarized enlargement (nearest neighbour)."""
import pathlib
import sys

from PIL import Image

HERE = pathlib.Path(__file__).parent
B = HERE.parent / "b386_390"
page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(float, sys.argv[3:7])
out, scale, th = sys.argv[7], int(sys.argv[8]), int(sys.argv[9])
im = Image.open(B / f"page_{page}_s{strip}.png").convert("L")
w, h = im.size
c = im.crop((int(x0 * w), int(y0 * h), int(x1 * w), int(y1 * h)))
c = c.point(lambda v: 0 if v < th else 255)
c = c.resize((c.width * scale, c.height * scale), Image.NEAREST)
c.save(HERE / f"{out}.png")
print(c.size)
