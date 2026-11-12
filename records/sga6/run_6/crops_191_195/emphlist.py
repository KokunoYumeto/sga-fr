r"""usage: python -I emphlist.py LO HI  -- list emph/underline groups in lines LO..HI of sga6 diplomatic main.tex"""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
lo, hi = int(sys.argv[1]), int(sys.argv[2])
t = open(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex", encoding="utf-8").read().split("\n")
pat = re.compile(r"\\(emph|underline|textit|uline)\{([^{}]*)\}")
for i in range(lo, hi + 1):
    for m in pat.finditer(t[i - 1]):
        print(i, m.group(0)[:90])
