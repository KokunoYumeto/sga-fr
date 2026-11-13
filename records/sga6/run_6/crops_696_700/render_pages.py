"""Render printed pages of SGA 6 (main scan, 360 ppi gray) into four strips, as prep_sga.py does, into this folder.
usage: python -I render_pages.py FOLIO [FOLIO ...]"""
import pathlib
import subprocess
import sys

from PIL import Image

OUT = pathlib.Path(__file__).parent
SCAN = pathlib.Path(r"C:\Users\user\Documents\Papors\OS") / "Théorie des Intersections et Théorème de Riemann-Roch.pdf"
for a in sys.argv[1:]:
    n = int(a)
    filepage = n + 13 + 1
    full = OUT / f"page_{n:03d}_full"
    cmd = ["pdftoppm", "-png", "-gray", "-r", "360", "-f", str(filepage), "-l", str(filepage), "-singlefile"]
    subprocess.run(cmd + [str(SCAN), str(full)], check=True)
    im = Image.open(str(full) + ".png").convert("L")
    w, h = im.size
    ink = im.point(lambda x: 255 if x < 150 else 0)
    box = ink.getbbox() or (0, 0, w, h)
    left, right = max(0, box[0] - 20), min(w, box[2] + 20)
    top, bottom = max(0, box[1] - 20), min(h, box[3] + 20)
    step = (bottom - top) / 4
    for i in range(4):
        y0 = int(top + i * step) - (40 if i else 0)
        y1 = int(top + (i + 1) * step) + (40 if i < 3 else 0)
        im.crop((left, max(top, y0), right, min(bottom, y1))).save(OUT / f"page_{n:03d}_s{i + 1}.png", optimize=True)
    print(n, "size", w, h, "box", box)
