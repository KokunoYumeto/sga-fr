"""count_x.py: count notation forms in the Exposé X region of sga6/diplomatic/main.tex (read only)."""
import pathlib, re, sys
sys.stdout.reconfigure(encoding='utf-8')
P = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex")
L = P.read_text(encoding="utf-8").split("\n")
lo, hi = int(sys.argv[1]), int(sys.argv[2])
seg = L[lo - 1:hi]
txt = "\n".join(seg)
pats = {
    "K^\\circ": r"K\^\\circ",
    "K^{\\bullet}": r"K\^\{\\bullet\}",
    "K^\\bullet": r"K\^\\bullet",
    "\\cl^\\circ": r"\\cl\^\\circ",
    "\\cl^{\\bullet}": r"\\cl\^\{\\bullet\}",
    "\\underline{": r"\\underline\{",
    "\\emph{": r"\\emph\{",
    "\\mathcal O": r"\\mathcal O",
    "\\subsection*{": r"\\subsection\*\{",
}
for k, p in pats.items():
    print(k, len(re.findall(p, txt)))
if len(sys.argv) > 3:
    rx = re.compile(sys.argv[3])
    for i, l in enumerate(seg):
        if rx.search(l):
            print(lo + i, "|", l[:220])
