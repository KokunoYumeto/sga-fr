import sys, pathlib
from PIL import Image
d = pathlib.Path(sys.argv[1])
for p in sorted(d.glob("w_*.pgm")):
    im = Image.open(p)
    print(p.name, im.size, im.mode)
    im.save(p.with_suffix(".png"))
    # small overview
    w, h = im.size
    im.resize((w // 3, h // 3)).save(d / (p.stem + "_small.png"))
