"""Print lines of the diplomatic s5.tex in a line range that match a regex.

usage: python -I grep_tex.py FIRST LAST REGEX [layer]
"""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
first, last, rx = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
layer = sys.argv[4] if len(sys.argv) > 4 else "diplomatic"
path = rf"C:\Users\user\Documents\sga_scan_check_20261105\sga5\{layer}\s5.tex"
lines = open(path, encoding="utf-8").read().split("\n")
pat = re.compile(rx)
n = 0
for i in range(first - 1, min(last, len(lines))):
    m = pat.search(lines[i])
    if m:
        n += 1
        s = lines[i]
        print(i + 1, s[max(0, m.start() - 60):m.end() + 80])
print("matches:", n)
