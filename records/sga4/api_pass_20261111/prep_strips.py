"""Strips of every SGA 4 page in PAGES.json, as prep_sga4.py makes them for the spot check: the scan page rendered in
grey at its native 300 dpi, cropped to the ink and cut into four overlapping horizontal strips
(strips/t<tome>/p<FFF>_s1..s4.png); for pages of Exposés XVII-XVIII also the second witness (Number4.pdf),
p<FFF>_w1..w4.png. Existing strips are kept. Runs several pdftoppm processes at once.

usage: python -I prep_strips.py [--jobs N]
"""
import json
import pathlib
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor

from PIL import Image

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "strips"


def strips(pdf, page_no, dpi, out, prefix):
    """Render PDF page page_no (1-based) in grey at dpi, crop to the ink, write four overlapping strips."""
    with tempfile.TemporaryDirectory(dir=HERE) as td:
        full = pathlib.Path(td) / "full"
        subprocess.run(["pdftoppm", "-png", "-gray", "-r", str(dpi), "-f", str(page_no), "-l", str(page_no),
                        "-singlefile", str(pdf), str(full)], check=True)
        im = Image.open(str(full) + ".png").convert("L")
        w, h = im.size
        ink = im.point(lambda x: 255 if x < 150 else 0)
        box = ink.getbbox() or (0, 0, w, h)
        left, right = max(0, box[0] - 20), min(w, box[2] + 20)
        top, bottom = max(0, box[1] - 20), min(h, box[3] + 20)
        step = (bottom - top) / 4
        for i in range(4):
            y0 = int(top + i * step) - (40 if i else 0)
            y1 = int(top + (i + 1) * step) + (40 if i < 3 else 0)
            im.crop((left, max(top, y0), right, min(bottom, y1))).save(out / f"{prefix}{i + 1}.png", optimize=True)
        im.close()


def job(p):
    d = OUT / f"t{p['tome']}"
    d.mkdir(parents=True, exist_ok=True)
    done = []
    if not (d / f"p{p['folio']:03d}_s4.png").exists():
        strips(p["scan_path"], p["pdf_page"], 300, d, f"p{p['folio']:03d}_s")
        done.append("s")
    if p.get("witness_pdf_page") and not (d / f"p{p['folio']:03d}_w4.png").exists():
        strips(p["witness_path"], p["witness_pdf_page"], 300, d, f"p{p['folio']:03d}_w")
        done.append("w")
    return p["tome"], p["folio"], done


if __name__ == "__main__":
    jobs = int(sys.argv[sys.argv.index("--jobs") + 1]) if "--jobs" in sys.argv else 8
    pages = json.loads((HERE / "PAGES.json").read_text(encoding="utf-8"))
    n = 0
    with ThreadPoolExecutor(jobs) as ex:
        for t, f, done in ex.map(job, pages):
            n += 1
            if n % 100 == 0:
                print(n, "pages", flush=True)
    print("done", n)
