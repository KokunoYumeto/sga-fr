"""Render a page of the SGA 6 witness DjVu (300 dpi) and crop regions of it or of the main-scan strips.

usage:
  python -I witness.py render FOLIO                 -> wit_FOLIO.png (whole page, ddjvu, page = folio + 11)
  python -I witness.py crop SRC.png X0 Y0 X1 Y1 OUT.png [SCALE]   (coordinates in SRC pixels)
"""
import pathlib
import shutil
import subprocess
import sys

from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
DDJVU = pathlib.Path(r"C:\Program Files (x86)\DjVuLibre\ddjvu.exe")
WIT = pathlib.Path(r"C:\Users\user\Documents\Papors\OS\SGA 6.tif.djvu")


def render(folio):
    tmp = HERE / "wit_sga6.djvu"
    if not tmp.exists():
        shutil.copyfile(WIT, tmp)
    out = HERE / f"wit_{folio}.tif"
    page = folio + 11
    subprocess.run([str(DDJVU), "-format=tiff", f"-page={page}", str(tmp), str(out)], check=True)
    im = Image.open(out)
    png = HERE / f"wit_{folio}.png"
    im.save(png)
    out.unlink()
    print(png, im.size)


def crop(src, x0, y0, x1, y1, out, scale=1.0):
    im = Image.open(src)
    c = im.crop((x0, y0, x1, y1))
    if scale != 1.0:
        c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
    c.save(HERE / out)
    print(HERE / out, c.size)


if __name__ == "__main__":
    if sys.argv[1] == "render":
        render(int(sys.argv[2]))
    else:
        a = sys.argv[2:]
        crop(a[0], *map(int, a[1:5]), a[5], float(a[6]) if len(a) > 6 else 1.0)
