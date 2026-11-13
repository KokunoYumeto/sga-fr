"""Simulate the two marker moves (folios 461, 462) in memory on both layers of main.tex; print counts and line numbers.
Writes nothing."""
import pathlib, sys
sys.stdout.reconfigure(encoding='utf-8')
ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
M461 = "%%%%%%%%%%  scan idx 474  |  folio 461  %%%%%%%%%%"
M462 = "%%%%%%%%%%  scan idx 475  |  folio 462  %%%%%%%%%%"
DISP = (r"donc :" "\n" r"\[" "\n"
        r"  i_{\gr}:\operatorname{Gr}^{k-d}K^\circ(Y)_{\mathbb Q}" "\n"
        r"  \to \operatorname{Gr}^{k}K^\circ(X)_{\mathbb Q};" "\n"
        r"  \qquad" "\n"
        r"  j_{\gr}:\operatorname{Gr}^{k-1}K^\circ(Y')_{\mathbb Q}" "\n"
        r"  \to \operatorname{Gr}^{k}K^\circ(X')_{\mathbb Q}." "\n"
        r"\]")
EDITS = [
    (r"et définissent" "\n" + M461 + "\n" + DISP + "\n" + r"Enfin, on remarque",
     r"et définissent" "\n" + DISP + "\n" + M461 + "\n" + r"Enfin, on remarque"),
    (r"à la relation (4.8.1), on" "\n" + M462 + "\n" + r"obtient :",
     r"à la relation" "\n" + M462 + "\n" + r"(4.8.1), on obtient :"),
]
for layer in ("diplomatic", "current"):
    t = (ROOT / layer / "main.tex").read_text(encoding="utf-8")
    for old, new in EDITS:
        n = t.count(old)
        pos = t.find(old)
        line = t[:pos].count("\n") + 1
        nl = old.count("\n")
        print(layer, "count", n, "lines", line, "-", line + nl)
        t2 = t.replace(old, new, 1)
        p2 = t2.find(new)
        print("   ->", repr(t2[p2 - 40:p2 + len(new) + 30]))
        t = t2
