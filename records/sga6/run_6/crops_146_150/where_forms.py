"""Print the folio of each line of the SGA 6 diplomatic main.tex that contains one of the given strings (read-only)."""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
path = r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex"
lines = open(path, encoding="utf-8").read().split("\n")
pats = [r"\underline{\Ext", r"\underline{\Ho}", r"\mathbb{R}\underline{\Hom}"]
folio = None
for i, l in enumerate(lines):
    m = re.match(r"%{10}\s+scan idx \d+\s+\|\s+folio (\d+)", l)
    if m:
        folio = m.group(1)
        continue
    for p in pats:
        if p in l:
            print(i + 1, folio, p, l[:90])
            break
