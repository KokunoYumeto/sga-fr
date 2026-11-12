"""Witness helper for the 351-355 check (reads the witness DjVu; writes only into this folder).
usage:
  python -I wit.py render FOLIO [OFFSET]               (witness page of FOLIO -> wit_FOLIO.png; DjVu page = folio + OFFSET, default 11)
  python -I wit.py crop FOLIO x0 y0 x1 y1 SCALE OUT   (crop of the rendered witness page)
"""
import pathlib
import subprocess
import sys

from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
DJVU = pathlib.Path(r"C:\Users\user\Documents\Papors\OS\SGA 6.tif.djvu")
DDJVU = pathlib.Path(r"C:\Program Files (x86)\DjVuLibre\ddjvu.exe")

mode = sys.argv[1]
if mode == "render":
    folio = int(sys.argv[2])
    off = int(sys.argv[3]) if len(sys.argv) > 3 else 11
    tif = HERE / f"wit_{folio}.tif"
    subprocess.run([str(DDJVU), "-format=tiff", f"-page={folio + off}", str(DJVU), str(tif)], check=True)
    im = Image.open(tif)
    out = HERE / f"wit_{folio}.png"
    im.save(out)
    im.close()
    tif.unlink()
    print(out, Image.open(out).size)
elif mode == "crop":
    folio = int(sys.argv[2])
    x0, y0, x1, y1 = map(int, sys.argv[3:7])
    scale = float(sys.argv[7])
    out = HERE / sys.argv[8]
    im = Image.open(HERE / f"wit_{folio}.png")
    c = im.crop((x0, y0, x1, y1))
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
    c.save(out)
    print(out, c.size)
