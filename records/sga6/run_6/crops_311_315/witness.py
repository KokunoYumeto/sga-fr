"""witness.py render FOLIO            -> wit_FOLIO.png (DjVu page = folio + 11)
   witness.py crop FOLIO x0 y0 x1 y1 SCALE OUT   -> crop of the rendered witness page"""
import pathlib
import subprocess
import sys

from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
DJVU = pathlib.Path(r"C:\Users\user\Documents\Papors\OS\SGA 6.tif.djvu")
DDJVU = pathlib.Path(r"C:\Program Files (x86)\DjVuLibre\ddjvu.exe")

mode = sys.argv[1]
folio = int(sys.argv[2])
if mode == "render":
    tif = HERE / f"wit_{folio}.tif"
    subprocess.run([str(DDJVU), "-format=tiff", f"-page={folio + 11}", str(DJVU), str(tif)], check=True)
    im = Image.open(tif)
    out = HERE / f"wit_{folio}.png"
    im.save(out)
    im.close()
    tif.unlink()
    print(out, Image.open(out).size)
else:
    x0, y0, x1, y1 = map(int, sys.argv[3:7])
    scale = float(sys.argv[7])
    out = HERE / sys.argv[8]
    im = Image.open(HERE / f"wit_{folio}.png")
    c = im.crop((x0, y0, x1, y1))
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
    c.save(out)
    print(out, c.size)
