"""Count strings per folio in a line range of main.tex (both layers); read-only.
usage: python -I count.py FIRST_LINE LAST_LINE STRING..."""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
a, b = int(sys.argv[1]), int(sys.argv[2])
for layer in ("diplomatic", "current"):
    lines = open(rf"C:\Users\user\Documents\sga_scan_check_20261105\sga6\{layer}\main.tex", encoding="utf-8").read().split("\n")
    folio = None
    per = {}
    for i, l in enumerate(lines, 1):
        m = MARK.search(l)
        if m:
            folio = int(m.group(2))
        if a <= i <= b:
            for s in sys.argv[3:]:
                c = l.count(s)
                if c:
                    per.setdefault(s, {}).setdefault(folio, 0)
                    per[s][folio] += c
    for s, d in per.items():
        print(layer, repr(s), sum(d.values()), dict(sorted(d.items())))
