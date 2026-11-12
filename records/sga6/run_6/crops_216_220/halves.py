import sys
from PIL import Image
for f in sys.argv[1:]:
    im = Image.open(f).convert("L")
    w, h = im.size
    top = im.crop((0, 0, w, h // 2 + 60))
    bot = im.crop((0, h // 2 - 60, w, h))
    top.save(f.replace(".png", "_top.png"))
    bot.save(f.replace(".png", "_bot.png"))
    print(f, w, h)
