"""crop.py strip PAGE S x0 y0 x1 y1 SCALE OUT   (main-scan strip; coords in displayed 2000-wide units)
   crop.py render FOLIO [OFFSET]                (witness DjVu page = folio + offset, default 11) -> wit_FOLIO.png + wit_FOLIO_half.png
   crop.py wcrop FOLIO x0 y0 x1 y1 SCALE OUT    (witness page pixels)"""
import pathlib, subprocess, sys
from PIL import Image
HERE = pathlib.Path(__file__).resolve().parent
B = HERE.parent / "b571_575"
DJVU = pathlib.Path(r"C:\Users\user\Documents\Papors\OS\SGA 6.tif.djvu")
DDJVU = pathlib.Path(r"C:\Program Files (x86)\DjVuLibre\ddjvu.exe")
mode = sys.argv[1]
if mode == "strip":
    page = int(sys.argv[2]); s = int(sys.argv[3])
    x0, y0, x1, y1 = map(float, sys.argv[4:8]); scale = float(sys.argv[8]); out = HERE / sys.argv[9]
    im = Image.open(B / f"page_{page}_s{s}.png")
    f = im.width / 2000.0
    im = im.crop((int(x0 * f), int(y0 * f), int(x1 * f), int(y1 * f)))
    im = im.resize((int(im.width * scale), int(im.height * scale)), Image.LANCZOS)
    im.save(out); print(out, im.size)
elif mode == "render":
    folio = int(sys.argv[2]); off = int(sys.argv[3]) if len(sys.argv) > 3 else 11
    tif = HERE / f"wit_{folio}.tif"
    subprocess.run([str(DDJVU), "-format=tiff", f"-page={folio + off}", str(DJVU), str(tif)], check=True)
    im = Image.open(tif); out = HERE / f"wit_{folio}.png"; im.save(out); im.close(); tif.unlink()
    im = Image.open(out); print(out, im.size, im.mode)
    half = im.convert("L").resize((im.width // 2, im.height // 2), Image.LANCZOS)
    half.save(HERE / f"wit_{folio}_half.png")
elif mode == "wcrop":
    folio = int(sys.argv[2]); x0, y0, x1, y1 = map(int, sys.argv[3:7]); scale = float(sys.argv[7]); out = HERE / sys.argv[8]
    im = Image.open(HERE / f"wit_{folio}.png").convert("L").crop((x0, y0, x1, y1))
    im = im.resize((int(im.width * scale), int(im.height * scale)), Image.LANCZOS)
    im.save(out); print(out, im.size)
