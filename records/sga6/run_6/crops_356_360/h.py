"""Helper for the SGA 6 pp. 356-360 check (writes only into this folder).
usage:
  python -I h.py strip FOLIO S x0 y0 x1 y1 SCALE OUT    crop of main-scan strip page_FOLIO_sS.png (pixels of the strip)
  python -I h.py render FOLIO [OFFSET]                  witness page (DjVu page = folio + OFFSET, default 11) -> wit_FOLIO.png
  python -I h.py wcrop FOLIO x0 y0 x1 y1 SCALE OUT      crop of the rendered witness page
  python -I h.py whalf FOLIO FACTOR OUT                 downscaled overview of the witness page
"""
import pathlib
import subprocess
import sys

from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
B = HERE.parent / "b356_360"
DJVU = pathlib.Path(r"C:\Users\user\Documents\Papors\OS\SGA 6.tif.djvu")
DDJVU = pathlib.Path(r"C:\Program Files (x86)\DjVuLibre\ddjvu.exe")

mode = sys.argv[1]
if mode == "strip":
    folio, s = int(sys.argv[2]), int(sys.argv[3])
    x0, y0, x1, y1 = map(int, sys.argv[4:8])
    scale = float(sys.argv[8])
    out = HERE / sys.argv[9]
    im = Image.open(B / f"page_{folio:03d}_s{s}.png").convert("L")
    c = im.crop((x0, y0, x1, y1))
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
    c.save(out)
    print(out, c.size, "strip size", im.size)
elif mode == "render":
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
elif mode == "whalf":
    folio = int(sys.argv[2])
    f = float(sys.argv[3])
    out = HERE / sys.argv[4]
    im = Image.open(HERE / f"wit_{folio}.png").convert("L")
    c = im.resize((int(im.width * f), int(im.height * f)), Image.LANCZOS)
    c.save(out)
    print(out, c.size, "full", im.size)
