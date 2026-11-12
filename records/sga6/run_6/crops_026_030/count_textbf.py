"""Count the \\textbf{...} forms of a TeX file (numbers folded to N): python -I count_textbf.py FILE"""
import collections
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
t = open(sys.argv[1], encoding="utf-8").read()
pat = re.compile(r"\\textbf\{([^}]*)\}")
c = collections.Counter(re.sub(r"[0-9.]+", "N", m) for m in pat.findall(t))
for k, v in c.most_common(40):
    print(v, k)
