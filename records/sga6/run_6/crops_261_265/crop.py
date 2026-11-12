"""crop.py SRC OUT x0 y0 x1 y1 [scale] -- crop a region of an image (pixel coords of SRC), optionally upscale.
crop.py --conv P...  -- convert w_P.pgm to w_P.png (witness pages)."""
import sys
from PIL import Image

if sys.argv[1] == "--conv":
    for p in sys.argv[2:]:
        im = Image.open(f"w_{p}.pgm")
        print(p, im.size, im.mode)
        im.convert("L").save(f"w_{p}.png")
    sys.exit()
src, out = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
s = float(sys.argv[7]) if len(sys.argv) > 7 else 1.0
im = Image.open(src).convert("L").crop((x0, y0, x1, y1))
if s != 1.0:
    im = im.resize((int(im.width * s), int(im.height * s)), Image.LANCZOS)
im.save(out)
print(out, im.size)
