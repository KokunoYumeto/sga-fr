"""Witness helper for folios 616-620.
   wit.py render DJVUPAGE            -> wit_p<DJVUPAGE>.png and a half-size copy
   wit.py crop DJVUPAGE x0 y0 x1 y1 SCALE OUT   (witness page pixels)"""
import pathlib, subprocess, sys
from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
DJVU = pathlib.Path(r"C:\Users\user\Documents\Papors\OS\SGA 6.tif.djvu")
DDJVU = pathlib.Path(r"C:\Program Files (x86)\DjVuLibre\ddjvu.exe")

mode = sys.argv[1]
if mode == "render":
    pg = int(sys.argv[2])
    tif = HERE / f"wit_p{pg}.tif"
    subprocess.run([str(DDJVU), "-format=tiff", f"-page={pg}", str(DJVU), str(tif)], check=True)
    im = Image.open(tif)
    out = HERE / f"wit_p{pg}.png"
    im.save(out)
    half = im.resize((im.width // 2, im.height // 2), Image.LANCZOS)
    half.save(HERE / f"wit_p{pg}_half.png")
    print(out, im.size)
    im.close()
    tif.unlink()
elif mode == "crop":
    pg = int(sys.argv[2])
    x0, y0, x1, y1 = map(int, sys.argv[3:7])
    scale = float(sys.argv[7])
    out = HERE / sys.argv[8]
    im = Image.open(HERE / f"wit_p{pg}.png").crop((x0, y0, x1, y1))
    im = im.resize((int(im.width * scale), int(im.height * scale)), Image.LANCZOS)
    im.save(out)
    print(out, im.size)
