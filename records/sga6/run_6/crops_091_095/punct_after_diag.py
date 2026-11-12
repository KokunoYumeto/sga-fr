"""Count the forms of punctuation after tikzcd / tikzpicture environments in the SGA 6 diplomatic main.tex."""
import collections
import re

t = open(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex", encoding="utf-8").read()
c = collections.Counter()
ex = {}
for m in re.finditer(r"\\end\{(tikzcd|tikzpicture)\}([^\n]*)\n?([^\n]*)", t):
    key = (m.group(1), m.group(2).strip()[:12], m.group(3).strip()[:12])
    c[key] += 1
    ex.setdefault(key, t.count("\n", 0, m.start()) + 1)
for k, v in c.most_common(25):
    print(v, k, "first at line", ex[k])
