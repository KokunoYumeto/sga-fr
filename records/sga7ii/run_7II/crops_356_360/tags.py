import sys
from PIL import Image
# stack left-margin crops (x 0..170) of given strip/y ranges into one image, scale 3
items = [
 ("page_356_s3.png", 430, 500), ("page_356_s3.png", 640, 710),
 ("page_357_s1.png", 165, 220), ("page_357_s1.png", 310, 372), ("page_357_s1.png", 465, 532),
 ("page_357_s2.png", 245, 320), ("page_357_s2.png", 580, 655), ("page_357_s3.png", 250, 328),
 ("page_358_s1.png", 150, 230), ("page_358_s1.png", 405, 490), ("page_358_s2.png", 318, 395),
 ("page_359_s3.png", 530, 590),
]
base = sys.argv[1]; out = sys.argv[2]
crops = [Image.open(f"{base}/{f}").convert('L').crop((0, a, 170, b)) for f, a, b in items]
W = max(c.width for c in crops); H = sum(c.height for c in crops) + 6*len(crops)
canvas = Image.new('L', (W, H), 255)
y = 0
for c in crops:
    canvas.paste(c, (0, y)); y += c.height + 6
canvas = canvas.resize((canvas.width*3, canvas.height*3), Image.LANCZOS)
canvas.save(out); print(out, canvas.size)
