"""crop.py PAGE STRIP X0 Y0 X1 Y1 [SCALE] -> crops_226_230/c_PAGE_sSTRIP_X0_Y0.png (enlarged)"""
import sys
from pathlib import Path
from PIL import Image

here = Path(__file__).resolve().parent
src = here.parent / "b226_230"
page, strip, x0, y0, x1, y1 = (int(a) for a in sys.argv[1:7])
scale = float(sys.argv[7]) if len(sys.argv) > 7 else 2.0
im = Image.open(src / f"page_{page}_s{strip}.png").crop((x0, y0, x1, y1))
im = im.resize((int(im.width * scale), int(im.height * scale)), Image.LANCZOS)
out = here / f"c_{page}_s{strip}_{x0}_{y0}.png"
im.save(out)
print(out)
