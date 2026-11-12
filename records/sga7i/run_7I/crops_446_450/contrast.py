import sys
from PIL import Image, ImageOps
out = sys.argv[1]; scale = float(sys.argv[2]); args = sys.argv[3:]
crops = []
for i in range(0, len(args), 5):
    src = args[i]; x0, y0, x1, y1 = map(int, args[i+1:i+5])
    c = Image.open(src).convert('L').crop((x0, y0, x1, y1))
    c = ImageOps.autocontrast(c, cutoff=1)
    crops.append(c.resize((int(c.width*scale), int(c.height*scale)), Image.NEAREST))
W = sum(c.width for c in crops) + 20*(len(crops)-1)
H = max(c.height for c in crops)
canvas = Image.new('L', (W, H), 255)
x = 0
for c in crops:
    canvas.paste(c, (x, 0)); x += c.width + 20
canvas.save(out)
