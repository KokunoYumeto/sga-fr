"""Search SGA 6 main.tex (diplomatic or current) for a literal string or a regex, within a line range (read only).
usage: python -I grep_main.py [--current] [--re] PATTERN [FROM TO]"""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
args = sys.argv[1:]
ed = "diplomatic"
if "--current" in args:
    ed = "current"
    args.remove("--current")
use_re = "--re" in args
if use_re:
    args.remove("--re")
pat = args[0]
lo, hi = (int(args[1]), int(args[2])) if len(args) > 2 else (1, 10**9)
P = rf"C:\Users\user\Documents\sga_scan_check_20261105\sga6\{ed}\main.tex"
t = open(P, encoding="utf-8").read().split("\n")
rx = re.compile(pat if use_re else re.escape(pat))
for i, l in enumerate(t, 1):
    if lo <= i <= hi:
        for m in rx.finditer(l):
            a, b = max(0, m.start() - 40), min(len(l), m.end() + 40)
            print(i, l[a:b])
