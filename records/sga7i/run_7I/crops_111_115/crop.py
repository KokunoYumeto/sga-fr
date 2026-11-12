import sys
from PIL import Image

base = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I\b111_115"
out = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I\crops_111_115"

# name, source strip, box in ORIGINAL pixel coordinates, scale
jobs = [
    ("p111_DXO", "page_111_s4.png", (1040, 60, 1360, 150), 3),
    ("p111_objXprime", "page_111_s4.png", (320, 350, 940, 425), 2),
    ("p112_extstar", "page_112_s3.png", (190, 100, 900, 220), 2),
    ("p113_sectionF", "page_113_s4.png", (1100, 100, 1990, 185), 2),
    ("p114_IPdef", "page_114_s3.png", (180, 260, 1650, 360), 2),
    ("p114_idealsIP", "page_114_s3.png", (280, 400, 460, 500), 3),
    ("p114_forallP", "page_114_s4.png", (440, 120, 1320, 330), 2),
    ("p115_GammaOx", "page_115_s3.png", (0, 470, 1260, 700), 2),
    ("p115_dots", "page_115_s4.png", (1280, 370, 1650, 470), 3),
]

sel = set(sys.argv[1:])
for name, src, box, sc in jobs:
    if sel and name not in sel:
        continue
    im = Image.open(base + "\\" + src)
    c = im.crop(box)
    c = c.resize((c.width * sc, c.height * sc), Image.LANCZOS)
    c.save(out + "\\" + name + ".png")
    print(name, c.size)
