"""Prepare a batch of the SGA scan check: for every printed page F in [FIRST, LAST] of volume VOL, write page_FFF.tex
(the diplomatic TeX of that page, from its marker to the next one) and four strips page_FFF_s1..s4.png of the scan
at its native resolution (360 ppi for the Internet Archive copies, 300 dpi for the others).

usage: python -I prep_sga.py VOL FIRST LAST OUTDIR [--tex-only]
"""
import pathlib
import subprocess
import sys

from PIL import Image

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from sga_config import VOLS, pages  # noqa: E402

args = [a for a in sys.argv[1:] if not a.startswith("--")]
tex_only = "--tex-only" in sys.argv
vol, first, last, out = args[0], int(args[1]), int(args[2]), pathlib.Path(args[3])
v = VOLS[vol]
out.mkdir(parents=True, exist_ok=True)
pg = pages(vol)
done, missing = [], []
for n in range(first, last + 1):
    if n not in pg:
        missing.append(n)
        continue
    parts = []
    for i, (f, s, e) in enumerate(pg[n]):
        t = f.read_text(encoding="utf-8")
        head = f"% from {f.name}\n" if i == 0 else f"\n% (continued in {f.name}, before its first page marker)\n"
        parts.append(head + t[s:e])
    (out / f"page_{n:03d}.tex").write_text("".join(parts), encoding="utf-8", newline="")
    done.append(n)
    if tex_only:
        continue
    filepage = v["idx_of"](n) + 1
    full = out / f"page_{n:03d}_full"
    cmd = ["pdftoppm", "-png", "-gray", "-r", str(v["dpi"]), "-f", str(filepage), "-l", str(filepage), "-singlefile"]
    if vol == "5":
        cmd.append("-cropbox")  # the CropBox hides the scanner margins and the facing page
    subprocess.run(cmd + [str(v["scan"]), str(full)], check=True)
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
        im.crop((left, max(top, y0), right, min(bottom, y1))).save(out / f"page_{n:03d}_s{i + 1}.png", optimize=True)
    pathlib.Path(str(full) + ".png").unlink()
print("prepared", len(done), "pages", (done[0], done[-1]) if done else None, "| no marker:", missing)
