"""probe.py LO HI SUBSTRING : list lines LO..HI of the diplomatic s5.tex containing SUBSTRING, with their folio."""
import bisect
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
root = Path(__file__).resolve().parents[2]
L = (root / "sga5" / "diplomatic" / "s5.tex").read_text(encoding="utf-8").split("\n")
mk = [(i, l) for i, l in enumerate(L, 1) if "scan idx" in l and "folio" in l]
starts = [i for i, _ in mk]


def folio(n):
    k = bisect.bisect_right(starts, n) - 1
    return mk[k][1].split("folio")[1].strip(" %") if k >= 0 else "?"


lo, hi, sub = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
for i, l in enumerate(L, 1):
    if lo <= i <= hi and sub in l:
        print(i, "p." + folio(i), l[:110])
