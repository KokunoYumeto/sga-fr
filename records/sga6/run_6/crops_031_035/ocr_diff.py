"""Word diff of the scan's OCR (ocr_6/page_NNN.txt) against page_NNN.tex: list OCR words of 4+ letters that do
not occur in the TeX page, with the closest TeX word (hints for silent corrections; OCR noise expected).
usage: python -I ocr_diff.py PAGE [PAGE ...]"""
import difflib
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
WORD = re.compile(r"[A-Za-zÀ-ÿ]{4,}")
for a in sys.argv[1:]:
    n = int(a)
    ocr = (RUN / "ocr_6" / f"page_{n:03d}.txt").read_text(encoding="utf-8", errors="replace")
    tex = (RUN / "run_6" / "b031_035" / f"page_{n:03d}.tex").read_text(encoding="utf-8")
    tex = re.sub(r"\\[A-Za-z]+", " ", tex)
    tw = set(WORD.findall(tex))
    tl = sorted(tw)
    print(f"=== p. {n}")
    for w in sorted(set(WORD.findall(ocr))):
        if w in tw:
            continue
        close = difflib.get_close_matches(w, tl, n=1, cutoff=0.75)
        if close:
            print(f"  {w!r:22} ~ {close[0]!r}")
