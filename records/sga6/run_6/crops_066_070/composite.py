"""Assemble several small crops side by side, each upscaled, for letter-shape comparison.
usage: python -I composite.py OUT SCALE IMG:X0:Y0:X1:Y1 [IMG:X0:Y0:X1:Y1 ...]"""
import pathlib
import sys

from PIL import Image

out, scale = sys.argv[1], float(sys.argv[2])
tiles = []
for spec in sys.argv[3:]:
    img, *box = spec.rsplit(":", 4)
    im = Image.open(img).convert("L").crop(tuple(map(int, box)))
    tiles.append(im.resize((int(im.width * scale), int(im.height * scale)), Image.LANCZOS))
h = max(t.height for t in tiles)
w = sum(t.width for t in tiles) + 20 * (len(tiles) - 1)
canvas = Image.new("L", (w, h), 255)
x = 0
for t in tiles:
    canvas.paste(t, (x, 0))
    x += t.width + 20
dest = pathlib.Path(__file__).parent / out
canvas.save(dest)
print(dest, canvas.size)
