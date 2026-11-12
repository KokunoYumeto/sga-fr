"""Count / show literal strings in SGA 6 diplomatic main.tex, optionally within a line range (read only).
usage: python -I grep_main.py PATTERN [FROM TO] [--show N]"""
import sys

sys.stdout.reconfigure(encoding="utf-8")
args = sys.argv[1:]
show = 0
if "--show" in args:
    i = args.index("--show")
    show = int(args[i + 1])
    del args[i:i + 2]
pat = args[0]
lo, hi = (int(args[1]), int(args[2])) if len(args) > 2 else (1, 10**9)
P = r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex"
t = open(P, encoding="utf-8").read().split("\n")
n = 0
for i, l in enumerate(t, 1):
    if lo <= i <= hi:
        k = l.find(pat)
        while k >= 0:
            n += 1
            if n <= show:
                print(i, l[max(0, k - 50):k + len(pat) + 50])
            k = l.find(pat, k + 1)
print("count", n)
