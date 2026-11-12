"""mycrop.py strip PAGE S x0 y0 x1 y1 SCALE OUT   (coords in displayed 2000-wide units of strip S)
   mycrop.py wit PAGE x0 y0 x1 y1 SCALE OUT       (witness pixel coords, wit_PAGE.png)"""
import sys, pathlib
from PIL import Image
HERE = pathlib.Path(__file__).resolve().parent
B = HERE.parent / "b386_390"
mode = sys.argv[1]; page = int(sys.argv[2])
if mode == "strip":
    s = int(sys.argv[3]); x0, y0, x1, y1 = map(float, sys.argv[4:8]); scale = float(sys.argv[8]); out = HERE / sys.argv[9]
    im = Image.open(B / f"page_{page}_s{s}.png"); f = im.width / 2000.0
    box = tuple(int(round(v * f)) for v in (x0, y0, x1, y1))
else:
    x0, y0, x1, y1 = map(float, sys.argv[3:7]); scale = float(sys.argv[7]); out = HERE / sys.argv[8]
    im = Image.open(HERE / f"wit_{page}.png").convert("L"); box = tuple(int(v) for v in (x0, y0, x1, y1))
c = im.crop(box)
c = c.resize((max(1, int(c.width * scale)), max(1, int(c.height * scale))), Image.LANCZOS)
c.save(out); print(out, c.size)
