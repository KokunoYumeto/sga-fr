"""Count candidate old strings in both live layers (whole file) and in the batch page files."""
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
dip = (W / "sga5" / "diplomatic" / "s5.tex").read_text(encoding="utf-8")
cur = (W / "sga5" / "current" / "s5.tex").read_text(encoding="utf-8")
B = W / "run_5" / "b381_385"
cands = {
    382: [r"\[" + "\n" + r"\R\Gamma^G(", r"\[" + "\n" + r"\R\Gamma^G(\check P"],
    381: [r"=\R\Gamma^G(\check P^\bullet\otimes_\Lambda^{\mathbf L}"],
    383: [r"multiplicité $v_x(g)$ du point $\delta(x)$"],
    385: [r"\mathbb Q_\ell[G_{y'}]$-module, ", "On a donc\n" + r"\[" + "\n" + r"a_{y'}(s)="],
}
for p, lst in cands.items():
    t = (B / f"page_{p}.tex").read_text(encoding="utf-8")
    for c in lst:
        print(p, t.count(c), dip.count(c), cur.count(c), repr(c))
