"""Simulate (in memory only) the move of the folio-398 marker in both layers; writes nothing."""
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
BS = chr(92)
NL = chr(10)
ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
M398 = "%%%%%%%%%%  scan idx 411  |  folio 398  %%%%%%%%%%"
DISP = BS + "[" + NL + "  " + BS + "xi_1^{" + BS + "alpha_1}" + BS + "cdots" + BS + "xi_{n-1}^{" + BS + "alpha_{n-1}}," + NL + "  " + BS + "qquad" + NL
OLD = "les éléments~:" + NL + DISP + M398 + NL
NEW = "les éléments~:" + NL + M398 + NL + DISP
for layer in ("diplomatic", "current"):
    t = (ROOT / layer / "main.tex").read_text(encoding="utf-8")
    i = t.find(OLD)
    print(layer, "count(OLD) =", t.count(OLD), " starts at line", t.count(NL, 0, i) + 1,
          " marker line", t.count(NL, 0, t.find(M398)) + 1)
    # what move_marker.py 6 398 '\[' --before would pick: the last '\[' before the marker
    m = t.find(M398)
    k = t.rfind(BS + "[", 0, m)
    print("   last '\\[' before marker at line", t.count(NL, 0, k) + 1)
    t2 = t.replace(OLD, NEW)
    j = t2.find(M398)
    print(repr(t2[j - 60:j + 200]))
