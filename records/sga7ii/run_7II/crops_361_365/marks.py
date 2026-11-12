import sys
from PIL import Image
# Build a side-by-side panel of small regions at 8x: args are src x0 y0 x1 y1 label ...
items = sys.argv[2:]
out = sys.argv[1]
tiles = []
for i in range(0, len(items), 5):
    src, x0, y0, x1, y1 = items[i:i+5]
    im = Image.open(src).convert('L')
    c = im.crop((int(x0), int(y0), int(x1), int(y1)))
    c = c.resize((c.width*8, c.height*8), Image.NEAREST)
    tiles.append(c)
W = sum(t.width for t in tiles) + 20*(len(tiles)-1)
H = max(t.height for t in tiles)
panel = Image.new('L', (W, H), 255)
x = 0
for t in tiles:
    panel.paste(t, (x, 0))
    x += t.width + 20
    # separator
    for yy in range(H):
        if x-10 < W:
            panel.putpixel((x-10, yy), 128)
panel.save(out)
print(out, panel.size)
