import sys
from PIL import Image, ImageDraw
src, x0, y0, x1, y1, scale, out = sys.argv[1:8]
x0, y0, x1, y1 = map(int, (x0, y0, x1, y1)); s = float(scale)
im = Image.open(src).convert('RGB').crop((x0, y0, x1, y1))
im = im.resize((int(im.width*s), int(im.height*s)), Image.LANCZOS)
d = ImageDraw.Draw(im)
for gx in range((x0//25+1)*25, x1, 25):
    X = (gx-x0)*s
    d.line([(X,0),(X,im.height)], fill=(255,0,0) if gx%100==0 else (255,180,180), width=1)
    if gx%50==0: d.text((X+2,2), str(gx), fill=(255,0,0))
for gy in range((y0//25+1)*25, y1, 25):
    Y = (gy-y0)*s
    d.line([(0,Y),(im.width,Y)], fill=(0,0,255) if gy%100==0 else (180,180,255), width=1)
    if gy%50==0: d.text((2,Y+2), str(gy), fill=(0,0,255))
im.save(out); print(out, im.size)
