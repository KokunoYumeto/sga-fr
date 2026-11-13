"""count_forms.py START END [pattern ...]: count literal strings in diplomatic main.tex lines START..END (1-based, inclusive)."""
import sys, pathlib
MAIN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex")
L = MAIN.read_text(encoding="utf-8").split("\n")
s, e = int(sys.argv[1]), int(sys.argv[2])
seg = "\n".join(L[s - 1:e])
pats = sys.argv[3:] or [r"\underline", r"\emph", r"\mathbb P", r"\mathbb{P}", r"\mathbf P", r"\mathbf{P}", r"\bfP",
                        r"\textbf{", r"\cO", r"\mathcal O", r"\Proj", r"\mathcal C", r"\cC", r"\ch", r"\Todd", r"\check T",
                        r"\mathbb Q", r"\mathbf Q", r"_{\mathbb Q}", r"\gr", r"\mathrm{gr}", r"\Fil", r"\Gr", r"\mathrm{sp}"]
for p in pats:
    print(repr(p), seg.count(p))
