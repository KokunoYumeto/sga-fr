"""Count uses of some macros in the SGA 5 diplomatic TeX (read only).
usage: python -I count_macros.py"""
import collections
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
p = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga5\diplomatic\s5.tex")
lines = p.read_text(encoding="utf-8").split("\n")
BS = chr(92)
for name in ("wt", "ol", "cO", "fm", "Div", "mathbf{n}", "mathbb{L}"):
    pat = re.compile(re.escape(BS + name) + (r"\{[^{}]*\}" if name in ("wt", "ol") else r"(?![A-Za-z])"))
    occ = [(i + 1, m.group(0)) for i, line in enumerate(lines) for m in pat.finditer(line)]
    c = collections.Counter(o[1] for o in occ)
    print(name, len(occ), c.most_common(8))
    print("   lines:", sorted(set(o[0] for o in occ))[:40])
