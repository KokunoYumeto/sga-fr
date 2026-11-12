# Lists lines of s5.tex (diplomatic) where an unescaped % starts a FIX-type note after text on the same line,
# and whether text that looks like prose follows the note's end (i.e. may be swallowed). Read-only.
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
p = r"C:\Users\user\Documents\sga_scan_check_20261105\sga5\diplomatic\s5.tex"
L = open(p, encoding="utf-8").read().split("\n")
pat = re.compile(r"(?<!\\)%\s*(FIX|NB|NOTE|TODO)\b")
n = 0
for i, l in enumerate(L, 1):
    m = pat.search(l)
    if m and l[:m.start()].strip():
        n += 1
        print(i, "before:", repr(l[max(0, m.start() - 40):m.start()]))
        print("    note head:", repr(l[m.start():m.start() + 50]))
        print("    line tail:", repr(l[-60:]))
print("inline note comments after text:", n)
