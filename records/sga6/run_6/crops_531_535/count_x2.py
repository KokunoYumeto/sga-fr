"""count_x2.py: count K-dot forms between the Exposé X heading and the 7.7 heading, and after (read only)."""
import pathlib, sys
sys.stdout.reconfigure(encoding='utf-8')
KEYS = (r"K^\circ", r"\cl^\circ", r"K^\bullet", r"K^{\bullet}", r"\underline{", r"\emph{Démonstration :}")
for layer in ("diplomatic", "current"):
    L = pathlib.Path(rf"C:\Users\user\Documents\sga_scan_check_20261105\sga6\{layer}\main.tex").read_text(encoding="utf-8").split("\n")
    a = next(i for i, l in enumerate(L) if l.startswith(r"\section*{\underline{EXPOSÉ X}"))
    b = next(i for i, l in enumerate(L) if l.startswith(r"\subsection*{7.7."))
    c = next(i for i, l in enumerate(L) if l.startswith(r"\section*{Exposé XII."))
    for name, (lo, hi) in (("X §1-7.6", (a, b)), ("X §7.7-end", (b, c))):
        t = "\n".join(L[lo:hi])
        print(layer, name, "lines", lo + 1, hi, {k: t.count(k) for k in KEYS})
