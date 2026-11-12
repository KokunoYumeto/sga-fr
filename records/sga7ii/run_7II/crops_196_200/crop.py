import sys
from PIL import Image

# usage: crop.py page strip x0 y0 x1 y1 scale outname
base = r"C:/Users/user/Documents/sga_scan_check_20261105/run_7II/b196_200/"
out = r"C:/Users/user/Documents/sga_scan_check_20261105/run_7II/crops_196_200/"
page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
scale = float(sys.argv[7])
name = sys.argv[8]
im = Image.open(base + f"page_{page}_s{strip}.png")
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(out + name)
print(out + name, c.size)
