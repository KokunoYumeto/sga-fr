"""Tile several crop images side by side with a label above each.
usage: python -I tile.py OUT IMG1 [IMG2 ...]"""
import pathlib
import sys

from PIL import Image, ImageDraw

here = pathlib.Path(__file__).resolve().parent
out = sys.argv[1]
ims = [Image.open(here / n).convert("L") for n in sys.argv[2:]]
pad = 20
h = max(i.height for i in ims) + 40
w = sum(i.width for i in ims) + pad * (len(ims) + 1)
canvas = Image.new("L", (w, h), 255)
d = ImageDraw.Draw(canvas)
x = pad
for n, i in zip(sys.argv[2:], ims):
    d.text((x, 5), n, fill=0)
    canvas.paste(i, (x, 35))
    x += i.width + pad
canvas.save(here / out)
print(here / out, canvas.size)
