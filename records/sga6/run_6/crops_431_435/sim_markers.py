"""Simulate the two marker moves (folios 431, 432) in memory on both layers of main.tex; print line numbers."""
import pathlib, sys
sys.stdout.reconfigure(encoding='utf-8')
ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
M431 = "%%%%%%%%%%  scan idx 444  |  folio 431  %%%%%%%%%%"
M432 = "%%%%%%%%%%  scan idx 445  |  folio 432  %%%%%%%%%%"
EDITS = [
    (r"pour tout \(x\in P_\bullet\), on ait \(x^2=0\))," + "\n" + M431 + "\n" + r"alors il en est de même",
     r"pour tout" + "\n" + M431 + "\n" + r"\(x\in P_\bullet\), on ait \(x^2=0\)), alors il en est de même"),
    (r"il existe un voisinage ouvert \(U\) de \(x\), et une" + "\n" + M432 + "\n" + r"suite de sections",
     r"il existe un voisinage ouvert" + "\n" + M432 + "\n" + r"\(U\) de \(x\), et une suite de sections"),
]
for layer in ("diplomatic", "current"):
    t = (ROOT / layer / "main.tex").read_text(encoding="utf-8")
    for old, new in EDITS:
        n = t.count(old)
        pos = t.find(old)
        line = t[:pos].count("\n") + 1
        print(layer, "count", n, "starts at line", line)
        t2 = t.replace(old, new, 1)
        # show the result around the marker
        p2 = t2.find(new)
        print("   ->", repr(t2[p2 - 60:p2 + len(new) + 40]))
        t = t2
