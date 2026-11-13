import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
t = open(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex", encoding="utf-8").read()
a = t.index("folio 667  %")
b = t.index("Bibliographie de l'Exposé XIV")
s = t[a:b]
lits = ["L^\\bullet", "L_\\bullet", "L^{\\prime\\bullet}", "L'_\\bullet", "\\cl(", "\\cl^", "K^\\circ", "K^\\bullet",
        "K_\\bullet", "\\Q", "\\mathbb Q", "no. ", "no.~", "no ", "n°", "vis-à-vis", "vis à vis", "quelques-uns",
        "quelques uns", "Module", "module", "\\pmod", "\\mapsto", "\\longmapsto"]
for p in lits:
    print(repr(p), s.count(p))
ms = list(re.finditer(r"folio (\d+)  %", s))
for i, m in enumerate(ms):
    e = ms[i + 1].start() if i + 1 < len(ms) else len(s)
    seg = s[m.start():e]
    print(m.group(1), "L^bullet", seg.count("L^\\bullet"), "L_bullet", seg.count("L_\\bullet"),
          "Lprime", seg.count("L^{\\prime"), "K^circ", seg.count("K^\\circ"), "no.", len(re.findall(r"\bno\.?[ ~]\d", seg)))
