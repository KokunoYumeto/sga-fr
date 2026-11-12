"""Print each use of a control sequence (or a literal string with --lit) in the SGA 6 diplomatic main.tex, with its
folio and a short context.  usage: python -I uses.py NAME [--lit] [--from F] [--to F]"""
import re
import sys

sys.path.insert(0, r"C:\Users\user\Documents\sga_scan_check_20261105")
import sga_config as c  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
t = open(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex", encoding="utf-8").read()
marks = list(c.MARK.finditer(t))
name = sys.argv[1]
lit = "--lit" in sys.argv
lo = int(sys.argv[sys.argv.index("--from") + 1]) if "--from" in sys.argv else 0
hi = int(sys.argv[sys.argv.index("--to") + 1]) if "--to" in sys.argv else 10 ** 6


def folio(pos):
    m = [x for x in marks if x.start() < pos]
    return int(m[-1].group(2)) if m else None


pat = re.escape(name) if lit else re.escape("\\" + name) + r"(?![A-Za-z])"
n = 0
for m in re.finditer(pat, t):
    f = folio(m.start())
    if f is None or not (lo <= f <= hi):
        continue
    n += 1
    ln = t.count("\n", 0, m.start()) + 1
    print(f, ln, repr(t[max(0, m.start() - 50):m.end() + 50]))
print("total", n)
