"""Count notation forms in the Exposé XIV region of the diplomatic main.tex, with folios (read-only)."""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
p = r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex"
L = open(p, encoding="utf-8").read().split("\n")
start = next(i for i, l in enumerate(L) if "Exposé XIV local notation" in l)
end = next(i for i in range(start, len(L)) if "folio 692" in L[i])
seg = L[start:end]
pats = ["K'(", "K^\\bullet(", "K^{\\bullet}(", "\\operatorname{Gr}'", "\\operatorname{Gr}^\\bullet",
        "L^\\bullet", "L_\\bullet", "H^{2\\bullet}", "(\\bullet)", "g'", " no. ", " no ", "n°"]
text = "\n".join(seg)
for s in pats:
    print(repr(s), text.count(s))
mk = re.compile(r"folio (\d+)")
cur = None
for i, l in enumerate(seg, start=start + 1):
    m = mk.search(l)
    if m:
        cur = m.group(1)
    for s in ["K'(", "\\operatorname{Gr}'", "g'", "L^\\bullet", " no. ", " no "]:
        if s in l:
            print(cur, i, repr(s))
