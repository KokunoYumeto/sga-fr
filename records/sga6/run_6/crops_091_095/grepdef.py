"""Find every line of the SGA 6 diplomatic main.tex that mentions one of the given control sequences in a definition
context (newcommand, renewcommand, providecommand, def, let, DeclareMathOperator), and count its uses by folio."""
import re
import sys

sys.path.insert(0, r"C:\Users\user\Documents\sga_scan_check_20261105")
import sga_config as c  # noqa: E402

t = open(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex", encoding="utf-8").read()
marks = list(c.MARK.finditer(t))


def folio(pos):
    m = [x for x in marks if x.start() < pos]
    return int(m[-1].group(2)) if m else None


for name in sys.argv[1:]:
    cs = "\\" + name
    for m in re.finditer(re.escape(cs) + r"(?![A-Za-z])", t):
        ls = t.rfind("\n", 0, m.start()) + 1
        le = t.find("\n", m.end())
        line = t[ls:le]
        if re.search(r"\\(newcommand|renewcommand|providecommand|def|let|DeclareMathOperator)", line):
            print("DEF", name, t.count("\n", 0, m.start()) + 1, line[:150])
    uses = [folio(m.start()) for m in re.finditer(re.escape(cs) + r"(?![A-Za-z])", t)]
    print("USES", name, len(uses), sorted(set(u for u in uses if u))[:40])
