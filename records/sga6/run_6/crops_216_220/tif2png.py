import sys
from PIL import Image
for f in sys.argv[1:]:
    im = Image.open(f)
    print(f, im.size, im.mode)
    im.convert("L").save(f.replace(".tif", ".png"))
