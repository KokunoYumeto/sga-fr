"""Make several crops of the strip images of b126_130 (coordinates in original pixels), upscaled.
usage: python -I batch_crop.py SPEC_FILE   (lines: out_name page strip x0 y0 x1 y1 scale)"""
import pathlib
import sys

from PIL import Image

here = pathlib.Path(__file__).parent
src = here.parent / "b126_130"
for line in pathlib.Path(sys.argv[1]).read_text().splitlines():
    if not line.strip() or line.startswith("#"):
        continue
    name, page, strip, x0, y0, x1, y1, scale = line.split()
    im = Image.open(src / f"page_{page}_s{strip}.png").convert("L")
    im = im.crop((int(x0), int(y0), int(x1), int(y1)))
    s = float(scale)
    im = im.resize((int(im.width * s), int(im.height * s)), Image.LANCZOS)
    im.save(here / name)
    print(name, im.size)
