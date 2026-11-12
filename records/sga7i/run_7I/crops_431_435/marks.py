import sys
from PIL import Image, ImageOps
# usage: marks.py out.png scale src:x0:y0:x1:y1 ...
out = sys.argv[1]; scale = int(sys.argv[2])
tiles = []
for spec in sys.argv[3:]:
    src, x0, y0, x1, y1 = spec.split(':')
    im = Image.open(src).convert('L').crop((int(x0), int(y0), int(x1), int(y1)))
    im = im.resize((im.width * scale, im.height * scale), Image.LANCZOS)
    tiles.append(ImageOps.expand(im, border=4, fill=0))
w = sum(t.width for t in tiles); h = max(t.height for t in tiles)
canvas = Image.new('L', (w, h), 255)
x = 0
for t in tiles:
    canvas.paste(t, (x, 0)); x += t.width
canvas.save(out)
