"""For statement labels (Proposition, Corollaire, Lemme, Théorème, Définition) in a line range of the SGA 6 diplomatic
main.tex, show whether the statement text carries \\emph or \\underline. Read only."""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
L = open(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex", encoding="utf-8").read().split("\n")
a, b = int(sys.argv[1]), int(sys.argv[2])
lab = re.compile(r"\\textbf\{(Proposition|Corollaire|Lemme|Théorème|Definition|Définition)[^}]*\}")
for i in range(a, b):
    m = lab.search(L[i - 1])
    if m:
        rest = L[i - 1][m.end():m.end() + 70]
        has = ("\\emph{" in L[i - 1][m.end():]) or ("\\underline{" in L[i - 1][m.end():])
        print(i, m.group(0), "EMPH" if has else "roman", "|", rest)
