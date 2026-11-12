import sys
from PIL import Image

# usage: python -I crop.py PAGE STRIP x0 y0 x1 y1 SCALE OUTNAME
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = map(int, sys.argv[3:7])
scale = float(sys.argv[7])
out = sys.argv[8]
base = r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\b121_125"
im = Image.open(rf"{base}\page_{page}_s{strip}.png")
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(rf"C:\Users\user\Documents\sga_scan_check_20261105\run_5\crops_121_125\{out}")
print(out, c.size)
