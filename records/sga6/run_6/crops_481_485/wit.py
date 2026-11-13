"""wit.py render FOLIO [OFFSET]   -> wit_FOLIO.png (DjVu page = folio + offset, default 11)
   wit.py crop FOLIO x0 y0 x1 y1 SCALE OUT   (witness page pixels)
   wit.py strip PAGE S x0 y0 x1 y1 SCALE OUT (main-scan strip, coords in displayed 2000-wide units)"""
import pathlib, subprocess, sys
from PIL import Image
HERE = pathlib.Path(__file__).resolve().parent
B = HERE.parent / "b481_485"
DJVU = pathlib.Path(r"C:\Users\user\Documents\Papors\OS\SGA 6.tif.djvu")
DDJVU = pathlib.Path(r"C:\Program Files (x86)\DjVuLibre\ddjvu.exe")
mode = sys.argv[1]
if mode == "render":
    folio = int(sys.argv[2])
    off = int(sys.argv[3]) if len(sys.argv) > 3 else 11
    tif = HERE / f"wit_{folio}.tif"
    subprocess.run([str(DDJVU), "-format=tiff", f"-page={folio + off}", str(DJVU), str(tif)], check=True)
    im = Image.open(tif); out = HERE / f"wit_{folio}.png"; im.save(out); im.close(); tif.unlink()
    im = Image.open(out); print(out, im.size)
    half = im.convert("L").resize((im.width // 2, im.height // 2), Image.LANCZOS)
    half.save(HERE / f"wit_{folio}_half.png")
elif mode == "crop":
    folio = int(sys.argv[2])
    x0, y0, x1, y1 = map(int, sys.argv[3:7]); scale = float(sys.argv[7]); out = HERE / sys.argv[8]
    im = Image.open(HERE / f"wit_{folio}.png").convert("L"); c = im.crop((x0, y0, x1, y1))
    c = c.resize((max(1, int(c.width * scale)), max(1, int(c.height * scale))), Image.LANCZOS); c.save(out); print(out, c.size)
else:
    page = int(sys.argv[2]); s = int(sys.argv[3])
    x0, y0, x1, y1 = map(float, sys.argv[4:8]); scale = float(sys.argv[8]); out = HERE / sys.argv[9]
    im = Image.open(B / f"page_{page}_s{s}.png"); f = im.width / 2000.0
    box = tuple(int(round(v * f)) for v in (x0, y0, x1, y1))
    c = im.crop(box)
    c = c.resize((max(1, int(c.width * scale)), max(1, int(c.height * scale))), Image.LANCZOS); c.save(out); print(out, c.size)
