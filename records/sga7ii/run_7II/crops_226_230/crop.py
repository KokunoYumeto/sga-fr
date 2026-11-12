import sys
from PIL import Image

SRC = r"C:/Users/user/Documents/sga_scan_check_20261105/run_7II/b226_230/"
DST = r"C:/Users/user/Documents/sga_scan_check_20261105/run_7II/crops_226_230/"

# name, strip file, box (l, t, r, b), scale
JOBS = [
    ("p226_simeq", "page_226_s3.png", (950, 235, 1459, 300), 3),
    ("p226_reduit", "page_226_s3.png", (250, 235, 850, 300), 2),
    ("p227_ouverts", "page_227_s1.png", (0, 395, 760, 470), 2),
    ("p227_precisement", "page_227_s1.png", (760, 325, 1459, 392), 2),
    ("p228_naive", "page_228_s2.png", (500, 310, 1150, 380), 2),
    ("p228_sing", "page_228_s2.png", (450, 118, 950, 185), 3),
    ("p228_a_hyp", "page_228_s3.png", (250, 650, 1050, 712), 2),
    ("p229_355", "page_229_s1.png", (300, 340, 900, 428), 2),
    ("p229_et", "page_229_s3.png", (1000, 95, 1320, 160), 3),
    ("p229_ferme", "page_229_s1.png", (0, 545, 1000, 622), 2),
    ("p229_tpr", "page_229_s3.png", (250, 255, 1050, 320), 2),
    ("p230_ke", "page_230_s2.png", (0, 662, 820, 725), 2),
]

only = set(sys.argv[1:])
for name, f, box, sc in JOBS:
    if only and name not in only:
        continue
    im = Image.open(SRC + f)
    c = im.crop(box)
    c = c.resize((c.width * sc, c.height * sc), Image.LANCZOS)
    c.save(DST + name + ".png")
    print(name, c.size)
