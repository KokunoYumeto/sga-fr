"""Show, for some pages of a volume, the TeX right after the page marker and the start of the scan's OCR text.
usage: python -I show_marker.py VOL PAGE [PAGE ...]"""
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from sga_config import W, pages  # noqa: E402

vol = sys.argv[1]
pg = pages(vol)
for a in sys.argv[2:]:
    n = int(a)
    if n not in pg:
        print(n, "NO MARKER")
        continue
    f, s, e = pg[n][0]
    t = f.read_text(encoding="utf-8")
    body = t[s:e].split("\n", 1)[1] if "\n" in t[s:e] else ""
    prev_tail = t[max(0, s - 120):s].replace("\n", " | ")
    ocr = (W / f"ocr_{vol}" / f"page_{n:03d}.txt")
    o = ocr.read_text(encoding="utf-8", errors="replace").strip().splitlines() if ocr.exists() else []
    print(f"=== {n}  TeX before: ...{prev_tail[-90:]}")
    print("   TeX after :", body.strip()[:160].replace("\n", " | "))
    print("   OCR start :", " | ".join(x.strip() for x in o[:3])[:160])
