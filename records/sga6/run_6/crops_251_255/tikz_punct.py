import re, sys
sys.stdout.reconfigure(encoding="utf-8")
B = chr(92)
t = open(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex", encoding="utf-8").read()
key = B + "end{tikzcd}"
n = 0
i = t.find(key)
while i >= 0:
    s = t[i + len(key): i + len(key) + 30]
    if any(c in s[:14] for c in ",.;"):
        n += 1
        if n <= 15:
            print(t.count("\n", 0, i) + 1, repr(s))
    i = t.find(key, i + 1)
print("total", n)
