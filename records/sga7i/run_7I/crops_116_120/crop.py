import sys
from PIL import Image

base = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I\b116_120"
out = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I\crops_116_120"

# usage: crop.py name strip x0 y0 x1 y1 scale
name, src, x0, y0, x1, y1, sc = sys.argv[1:8]
x0, y0, x1, y1, sc = int(x0), int(y0), int(x1), int(y1), int(sc)
im = Image.open(base + "\\" + src)
c = im.crop((x0, y0, x1, y1))
c = c.resize((c.width * sc, c.height * sc), Image.LANCZOS)
c.save(out + "\\" + name + ".png")
print(name, c.size)
