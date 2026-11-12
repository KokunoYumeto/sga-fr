import sys
from PIL import Image
for p in sys.argv[1:]:
    im = Image.open(f"w_{p}.pnm")
    print(p, im.size, im.mode)
    im.convert("L").save(f"w_{p}.png")
