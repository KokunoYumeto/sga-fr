import re
import sys

path = r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex"
lo, hi = int(sys.argv[1]), int(sys.argv[2])
needle = sys.argv[3]
lines = open(path, encoding="utf-8").read().split("\n")
cur = None
for i in range(1, len(lines) + 1):
    l = lines[i - 1]
    m = re.search(r"folio (\d+)", l)
    if m:
        cur = m.group(1)
    if lo <= i <= hi and needle in l:
        for mm in re.finditer(r".{0,40}" + re.escape(needle) + r".{0,40}", l):
            print(i, cur, mm.group(0))
