import sys
from PIL import Image

base = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I\b131_135"
out = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I\crops_131_135"

# usage: crop.py name src x0 y0 x1 y1 scale
name, src = sys.argv[1], sys.argv[2]
x0, y0, x1, y1, sc = [int(v) for v in sys.argv[3:8]]
im = Image.open(base + "\\" + src)
c = im.crop((x0, y0, x1, y1))
c = c.resize((c.width * sc, c.height * sc), Image.LANCZOS)
c.save(out + "\\" + name + ".png")
print(name, im.size, c.size)
