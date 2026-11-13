"""Count forms of some symbols in the SGA 6 diplomatic main.tex (read only).

usage: python -I conv.py <main.tex> [start_line end_line]
"""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
path = sys.argv[1]
lines = open(path, encoding="utf-8").read().split("\n")
if len(sys.argv) > 3:
    a, b = int(sys.argv[2]), int(sys.argv[3])
    text = "\n".join(lines[a - 1:b])
else:
    text = "\n".join(lines)

B = "\\"
pats = [
    B + "mathcal H" + B + "!om",
    B + "mathcal{H}" + B + "!om",
    B + "mathcal{H}om",
    B + "mathcal Hom",
    B + "underline{" + B + "operatorname{Hom}}",
    B + "underline{" + B + "mathrm{Hom}}",
    B + "underline{Hom}",
    B + "underline{" + B + "Hom}",
    B + "uHom",
    B + "cHom",
    B + "HHom",
    B + "sHom",
    B + "mathbb{V}",
    B + "mathbb V",
    B + "mathcal O",
    B + "mathcal{O}",
    B + "cO",
    B + "underline O",
    B + "underline{O}",
    B + "underline{" + B + "mathrm{O}}",
]
for p in pats:
    print(repr(p), text.count(p))

defre = re.compile(r"\\(?:newcommand|renewcommand|providecommand|DeclareMathOperator)\*?\{?\\(\w+)\}?(.*)")
for i, ln in enumerate(lines, 1):
    m = defre.search(ln)
    if m and re.search(r"(?i)hom|^V|^cO$|^O$", m.group(1)):
        print(i, ln.strip()[:200])
