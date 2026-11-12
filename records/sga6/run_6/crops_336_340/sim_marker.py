"""In-memory check of the marker replacements for pp. 336 and 340 on both layers of SGA 6 main.tex (writes nothing)."""
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
M336 = "%%%%%%%%%%  scan idx 349  |  folio 336  %%%%%%%%%%"
M340 = "%%%%%%%%%%  scan idx 353  |  folio 340  %%%%%%%%%%"
REPL = [
    ("\(A\)~; on\n" + M336 + "\ndéfinit un", "\(A\)~;\n" + M336 + "\non définit un"),
    ("de \(A\) dans \(B\) qui\n" + M340 + "\nenvoie \(N\)", "de \(A\) dans\n" + M340 + "\n\(B\) qui envoie \(N\)"),
]
for layer in ("diplomatic", "current"):
    t = (ROOT / layer / "main.tex").read_text(encoding="utf-8")
    for old, new in REPL:
        n = t.count(old)
        print(layer, "count", n, repr(old[:30]))
        if n == 1:
            t2 = t.replace(old, new)
            k = t2.find(new)
            print("   ->", repr(t2[k - 60:k + len(new) + 40]))
