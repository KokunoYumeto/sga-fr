import sys, json
from PIL import Image, ImageDraw
# usage: sheet.py out scale 'json list of [label, src, x0, y0, x1, y1]'
out, scale, spec = sys.argv[1], float(sys.argv[2]), json.loads(sys.argv[3])
tiles = []
for label, src, x0, y0, x1, y1 in spec:
    im = Image.open(src).convert('RGB').crop((x0, y0, x1, y1))
    im = im.resize((int(im.width*scale), int(im.height*scale)), Image.LANCZOS)
    tiles.append((label, im))
W = max(t.width for _, t in tiles) + 10
H = sum(t.height + 22 for _, t in tiles)
sheet = Image.new('RGB', (W, H), 'white')
d = ImageDraw.Draw(sheet); y = 0
for label, t in tiles:
    d.text((4, y + 4), label, fill=(255, 0, 0)); y += 18
    sheet.paste(t, (5, y)); y += t.height + 4
    d.line([(0, y), (W, y)], fill=(0, 0, 255))
sheet.save(out); print(out, sheet.size)
