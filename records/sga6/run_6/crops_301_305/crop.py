"""Crop helper for the 301-305 check (read only on the batch folder).
usage:
  python -I crop.py strip PAGE STRIP x0 y0 x1 y1 SCALE OUTNAME   (coordinates in the strip's original pixels)
  python -I crop.py witness FOLIO                                 (render the witness page of FOLIO to wit_FOLIO.png; DjVu page = folio + 11)
  python -I crop.py wcrop FOLIO x0 y0 x1 y1 SCALE OUTNAME         (crop the rendered witness page)
"""
import pathlib
import subprocess
import sys

from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
BATCH = HERE.parent / "b301_305"
DJVU = pathlib.Path(r"C:\Users\user\Documents\Papors\OS\SGA 6.tif.djvu")
DDJVU = pathlib.Path(r"C:\Program Files (x86)\DjVuLibre\ddjvu.exe")

mode = sys.argv[1]
if mode == "strip":
    page, strip = int(sys.argv[2]), int(sys.argv[3])
    x0, y0, x1, y1 = map(int, sys.argv[4:8])
    scale = float(sys.argv[8])
    out = HERE / sys.argv[9]
    im = Image.open(BATCH / f"page_{page:03d}_s{strip}.png")
    c = im.crop((x0, y0, x1, y1))
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
    c.save(out)
    print(out, c.size)
elif mode == "witness":
    folio = int(sys.argv[2])
    pg = folio + 11
    tif = HERE / f"wit_{folio}.tif"
    subprocess.run([str(DDJVU), "-format=tiff", f"-page={pg}", str(DJVU), str(tif)], check=True)
    im = Image.open(tif)
    out = HERE / f"wit_{folio}.png"
    im.save(out)
    im.close()
    tif.unlink()
    print(out, Image.open(out).size)
elif mode == "wcrop":
    folio = int(sys.argv[2])
    x0, y0, x1, y1 = map(int, sys.argv[3:7])
    scale = float(sys.argv[7])
    out = HERE / sys.argv[8]
    im = Image.open(HERE / f"wit_{folio}.png")
    c = im.crop((x0, y0, x1, y1))
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
    c.save(out)
    print(out, c.size)
