"""Render pages of the SGA 6 witness DjVu (300 dpi; page = folio + 11) into this folder, and crop regions.

usage:
  python -I wit.py render FOLIO [FOLIO ...]                 -> wit_FOLIO.png
  python -I wit.py crop SRC.png X0 Y0 X1 Y1 OUT.png [SCALE]  (coordinates in SRC pixels; SRC relative to this folder
                                                              or absolute)
"""
import pathlib
import subprocess
import sys

from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
DDJVU = pathlib.Path(r"C:\Program Files (x86)\DjVuLibre\ddjvu.exe")
WIT = pathlib.Path(r"C:\Users\user\Documents\Papors\OS\SGA 6.tif.djvu")


def render(folio):
    out = HERE / f"wit_{folio}.tif"
    subprocess.run([str(DDJVU), "-format=tiff", f"-page={folio + 11}", str(WIT), str(out)], check=True)
    im = Image.open(out)
    png = HERE / f"wit_{folio}.png"
    im.save(png)
    im.close()
    out.unlink()
    print(png, im.size)


def crop(src, x0, y0, x1, y1, out, scale=1.0):
    p = pathlib.Path(src)
    if not p.is_absolute():
        p = HERE / p
    im = Image.open(p)
    c = im.crop((x0, y0, x1, y1))
    if scale != 1.0:
        c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
    c.save(HERE / out)
    print(HERE / out, c.size)


if __name__ == "__main__":
    if sys.argv[1] == "render":
        for f in sys.argv[2:]:
            render(int(f))
    else:
        a = sys.argv[2:]
        crop(a[0], *map(int, a[1:5]), a[5], float(a[6]) if len(a) > 6 else 1.0)
