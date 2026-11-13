"""Render pages of the SGA 6 witness DjVu (300 dpi; DjVu page = folio + 11) into this folder.

usage:
  python -I wit.py render FOLIO [FOLIO ...]   -> wit_FOLIO.png
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
    size = im.size
    im.close()
    out.unlink()
    print(png, size)


if __name__ == "__main__":
    for f in sys.argv[2:]:
        render(int(f))
