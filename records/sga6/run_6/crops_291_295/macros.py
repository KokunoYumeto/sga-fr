"""List the definitions of some macros in the SGA 6 diplomatic main.tex, and count forms in Exposé IV."""
import io
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
p = r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex"
t = open(p, encoding="utf-8").read().split("\n")
names = sys.argv[1:] or ["parf", "coh", "Kprime", "Kdot", "naif", "cl", "Parf", "Ob", "Loclib"]
pat = re.compile(r"(?:command\*?\{\\(" + "|".join(names) + r")\}|\\def\\(" + "|".join(names) + r")\b)")
for i, l in enumerate(t, 1):
    if pat.search(l):
        print(i, l[:170])
ex4 = "\n".join(t[6560:7194])
for form in [r"_{\parf}", r"\parf", r"\underline{\parf}", r"\underline{\mathrm{parf}}", r"\mathbf L", r"\varinjlim_i",
             r"\varinjlim", r"\varprojlim_i", r"\varprojlim", "K'", r"K_{\bullet}", r"K^{\bullet}", r"\emph{"]:
    print(repr(form), ex4.count(form))
