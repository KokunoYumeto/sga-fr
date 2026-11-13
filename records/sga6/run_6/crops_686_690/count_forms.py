"""Count notation forms in a line range of the diplomatic SGA 6 main.tex (helper for the 686-690 check)."""
import re
import sys
import pathlib

p = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex")
lines = p.read_text(encoding="utf-8").split("\n")
start, end = int(sys.argv[1]), int(sys.argv[2])
seg = "\n".join(lines[start - 1:end])
BS = chr(92)
pats = [
    ("K'(", re.escape("K'(")),
    ("K^bullet(", re.escape("K^" + BS + "bullet(")),
    ("K^{bullet}(", re.escape("K^{" + BS + "bullet}(")),
    ("opGr'", re.escape(BS + "operatorname{Gr}'")),
    ("opGr^bullet", re.escape(BS + "operatorname{Gr}^" + BS + "bullet")),
    ("opGr^{bullet}", re.escape(BS + "operatorname{Gr}^{" + BS + "bullet}")),
    ("Gtop^bullet", re.escape(BS + "Gtop^" + BS + "bullet")),
    ("Gtop'", re.escape(BS + "Gtop'")),
    ("no. ", r"\bno\. "),
    ("n textsuperscript o", re.escape("n" + BS + "textsuperscript{o}")),
    ("n degree", "n\u00b0"),
    ("pp. ", r"\bpp\. "),
    ("emph", re.escape(BS + "emph{")),
    ("Illusie", "Illusie"),
    ("ILLUSIE", "ILLUSIE"),
]
for name, pat in pats:
    hits = [m.start() for m in re.finditer(pat, seg)]
    linenos = sorted({seg.count("\n", 0, h) + start for h in hits})
    print(f"{name:22s} {len(hits):4d}  lines {linenos[:12]}")
