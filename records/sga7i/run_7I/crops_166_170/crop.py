import sys
from PIL import Image

# usage: crop.py <page> <strip> <x0> <y0> <x1> <y1> <scale> <outname>
page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
scale = float(sys.argv[7])
out = sys.argv[8]
base = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I\b166_170"
im = Image.open(rf"{base}\page_{page}_s{strip}.png")
c = im.crop((x0, y0, x1, y1))
if scale != 1:
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(rf"{base}\crops_166_170\{out}")
print(c.size)
