"""Count notation forms per folio in the SGA 6 diplomatic TeX (read only).
usage: python -I count_forms.py LAYER MAXFOLIO"""
import re
import sys
from collections import OrderedDict

layer = sys.argv[1] if len(sys.argv) > 1 else "diplomatic"
maxfolio = int(sys.argv[2]) if len(sys.argv) > 2 else 90
p = r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\%s\main.tex" % layer
t = open(p, encoding="utf-8").read()
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
ms = list(MARK.finditer(t))
PATS = OrderedDict([
    ("cO", r"\\cO\b"),
    ("underlineO", r"\\underline\{?\s*O"),
    ("mathcalO", r"\\mathcal\{?O"),
    ("f_*", r"_\*"),
    ("_!", r"_!|_\{!\}"),
])
for i, m in enumerate(ms):
    fo = int(m.group(2))
    if fo > maxfolio:
        break
    end = ms[i + 1].start() if i + 1 < len(ms) else len(t)
    seg = t[m.start():end]
    counts = {k: len(re.findall(v, seg)) for k, v in PATS.items()}
    if any(counts.values()):
        print(fo, counts)
