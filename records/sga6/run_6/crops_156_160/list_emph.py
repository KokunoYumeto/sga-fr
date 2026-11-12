"""List \\emph / \\underline uses (other than proof labels) in a line range of the SGA 6 diplomatic main.tex."""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
L = open(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex", encoding="utf-8").read().split("\n")
a, b = int(sys.argv[1]), int(sys.argv[2])
pat = re.compile(r"\\(emph|underline)\{([^{}]{0,60})")
for i in range(a, b):
    for m in pat.finditer(L[i - 1]):
        if not m.group(2).startswith("Preuve"):
            print(i, m.group(1), m.group(2))
