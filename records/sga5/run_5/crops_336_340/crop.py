import sys
from PIL import Image
# usage: crop.py page strip x0 y0 x1 y1 scale outname
page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
scale = float(sys.argv[7])
out = sys.argv[8]
base = r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\b336_340"
im = Image.open(rf"{base}\page_{page}_s{strip}.png")
if x1 <= 0:
    print(im.size)
    sys.exit()
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(rf"C:\Users\user\Documents\sga_scan_check_20261105\run_5\crops_336_340\{out}.png")
print(c.size)
