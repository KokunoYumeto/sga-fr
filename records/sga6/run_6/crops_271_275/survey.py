"""survey.py A B -- count emphasis commands in main.tex between folio A and folio B markers; print statement heads."""
import collections
import re
import sys

t = open(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex", encoding="utf-8").read()
M = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
pos = {int(m.group(2)): m.start() for m in M.finditer(t)}
a, b = pos[int(sys.argv[1])], pos[int(sys.argv[2])]
s = t[a:b]
for cmd in ("underline", "emph", "textit", "uline", "textbf"):
    print(cmd, len(re.findall("\\\\" + cmd + r"\{", s)))
c = collections.Counter(re.findall(r"\\(?:underline|emph)\{([^}]{0,30})", s))
print(c.most_common(80))
for m in re.finditer(r"\\textbf\{(Proposition|Th[ée]or[èe]me|Lemme|Corollaire|D[ée]finition)[^}]*\}[^\n]{0,120}", s):
    print("STMT:", m.group(0)[:200])
