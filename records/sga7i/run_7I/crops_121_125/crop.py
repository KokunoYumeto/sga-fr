import sys
from PIL import Image

base = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I\b121_125"
out = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I\crops_121_125"

# usage: crop.py name strip x0 y0 x1 y1 scale   (coordinates in original pixels)
name, src, x0, y0, x1, y1, sc = sys.argv[1:8]
x0, y0, x1, y1, sc = int(x0), int(y0), int(x1), int(y1), float(sc)
im = Image.open(base + "\\" + src)
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * sc), int(c.height * sc)), Image.LANCZOS)
c.save(out + "\\" + name + ".png")
print(name, c.size)
