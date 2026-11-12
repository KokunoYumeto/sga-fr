"""pix.py STRIP x0 y0 x1 y1: darkest pixel and dark-pixel counts in a box of a strip (read-only)."""
import sys

from PIL import Image

im = Image.open(sys.argv[1]).convert("L")
box = tuple(int(v) for v in sys.argv[2:6])
c = im.crop(box)
px = list(c.getdata())
print(box, "min", min(px), "<128:", sum(p < 128 for p in px), "<200:", sum(p < 200 for p in px), "of", len(px))
# column profile: dark pixels per column
cols = [sum(1 for y in range(c.height) if c.getpixel((x, y)) < 160) for x in range(c.width)]
print("dark columns:", [box[0] + i for i, v in enumerate(cols) if v])
