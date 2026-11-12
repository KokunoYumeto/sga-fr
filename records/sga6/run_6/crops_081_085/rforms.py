import re
import sys
sys.path.insert(0, r"C:\Users\user\Documents\sga_scan_check_20261105")
import sga_config as c

t = open(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex", encoding="utf-8").read()
marks = list(c.MARK.finditer(t))


def folio(pos):
    m = [x for x in marks if x.start() < pos]
    return int(m[-1].group(2)) if m else None


pats = {
    "RHom": r"\\RHom",
    "plain Rf_": r"[^a-zA-Z\\]Rf_",
    "mathbb R": r"\\mathbb\{?R\}?",
    "mathbf R": r"\\mathbf\{?R\}?",
    "R Gamma": r"[^a-zA-Z\\]R\\Gamma",
}
for k, p in pats.items():
    fs = [folio(m.start()) for m in re.finditer(p, t)]
    fs = [f for f in fs if f and 79 <= f <= 160]
    print(k, len(fs), sorted(set(fs))[:25])
