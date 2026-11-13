"""Count notations in Expose IX of the SGA 6 diplomatic main.tex (read only)."""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
t = open(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex", encoding="utf-8").read()
a = t.index("\\section*{Exposé IX.")
b = t.index("\\section*{Exposé X.")
s = t[a:b]
print("IX chars", len(s), "lines", t[:a].count("\n") + 1, "-", t[:b].count("\n") + 1)
pats = {
    "K^\\circ": r"K\^\\circ",
    "K^{\\circ}": r"K\^\{\\circ\}",
    "K^\\bullet": r"K\^\\bullet",
    "K^{\\bullet}": r"K\^\{\\bullet\}",
    "K_\\bullet": r"K_\\bullet",
    "K_{\\bullet}": r"K_\{\\bullet\}",
    "\\cdot": r"\\cdot(?!s)",
    "\\underline": r"\\underline",
    "\\mathcal O": r"\\mathcal O",
    "\\cO": r"\\cO",
}
for name, p in pats.items():
    print(name, len(re.findall(p, s)))
folios = re.findall(r"folio (\d+)", s)
print("folios", folios[:2], "...", folios[-2:])
# where K^\circ occurs: folio of each
pos = 0
cur = None
for m in re.finditer(r"%%%%%%%%%%  scan idx \d+  \|  folio (\d+)|K\^\\circ|K\^\{\\circ\}", s):
    if m.group(1):
        cur = m.group(1)
    else:
        print("K^circ at folio", cur)
