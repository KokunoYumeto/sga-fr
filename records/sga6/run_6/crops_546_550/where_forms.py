import re, sys
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, r"C:\Users\user\Documents\sga_scan_check_20261105")
from sga_config import MARK
t = open(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex", encoding="utf-8").read()
marks = [(m.start(), int(m.group(2))) for m in MARK.finditer(t)]
def folio(pos):
    f = None
    for s, n in marks:
        if s > pos: break
        f = n
    return f
from collections import Counter
for k in [r"K^\circ", r"\cl^\circ", r"K^\bullet", r"K^{\bullet}", r"\cl^\bullet", r"\Theta"]:
    c = Counter()
    i = t.find(k)
    while i >= 0:
        fo = folio(i)
        if fo and 515 <= fo <= 575:
            c[fo] += 1
        i = t.find(k, i + 1)
    print(k, dict(sorted(c.items())))
