"""In-memory check of the folio-344 marker fix on both layers of SGA 6 main.tex (reads only, writes nothing)."""
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
BASE = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
MARKER = "%%%%%%%%%%  scan idx 357  |  folio 344  %%%%%%%%%%"
OLD = "et \\(X_0\\) sur \\(x\\), d'où le\n" + MARKER + "\nrésultat,"
NEW = "et \\(X_0\\)\n" + MARKER + "\nsur \\(x\\), d'où le résultat,"
for layer in ("diplomatic", "current"):
    t = (BASE / layer / "main.tex").read_text(encoding="utf-8")
    n = t.count(OLD)
    t2 = t.replace(OLD, NEW)
    k = t2.find(MARKER)
    print(layer, "occurrences:", n, "| after:", repr(t2[k - 60:k + len(MARKER) + 80]))
