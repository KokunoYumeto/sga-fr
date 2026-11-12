"""Count emphasis commands in line ranges of the SGA 6 diplomatic main.tex (read only)."""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
L = open(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex", encoding="utf-8").read().split("\n")
KEYS = [r"\emph{", r"\underline{", r"\uline{", r"\textbf{", r"\textit{"]


def cnt(a, b):
    s = "\n".join(L[a - 1:b - 1])
    return {k: s.count(k) for k in KEYS}


for a, b, name in [(3744, 5335, "Exp II"), (3743, 4143, "Exp II pp. 160-174"), (3200, 3743, "Exp I tail"),
                   (4143, 4778, "Exp II pp. 175-")]:
    print(name, a, b, cnt(a, b))
if len(sys.argv) > 2:
    a, b = int(sys.argv[1]), int(sys.argv[2])
    for i in range(a, b):
        for k in (r"\underline{", r"\emph{"):
            if k in L[i - 1]:
                print(i, L[i - 1][:160])
                break
