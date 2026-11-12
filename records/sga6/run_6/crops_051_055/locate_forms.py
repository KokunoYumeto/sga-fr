"""Locate notation forms by folio in an SGA 6 layer (read only).
usage: python -I locate_forms.py LAYER"""
import re
import sys
from collections import Counter

layer = sys.argv[1] if len(sys.argv) > 1 else "diplomatic"
t = open(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\%s\main.tex" % layer, encoding="utf-8").read()
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
ms = list(MARK.finditer(t))


def folio_at(pos):
    f = None
    for m in ms:
        if m.start() < pos:
            f = int(m.group(2))
        else:
            break
    return f


for name, pat in [("cO", r"\\cO(?![A-Za-z])"), ("underlineO", r"\\underline\{?\s*O(?![A-Za-z])"),
                  ("Corollaire", r"\\textbf\{Corollaire[^}]*\}")]:
    c = Counter(folio_at(m.start()) for m in re.finditer(pat, t))
    print(name, sorted((k, v) for k, v in c.items() if k is not None and k <= 90))
