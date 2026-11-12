"""Read-only check: count the proposed main.tex replacements for the folio-37 and folio-38 markers in both layers."""
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
M36 = "%%%%%%%%%%  scan idx 49  |  folio 36  %%%%%%%%%%"
M37 = "%%%%%%%%%%  scan idx 50  |  folio 37  %%%%%%%%%%"
M38 = "%%%%%%%%%%  scan idx 51  |  folio 38  %%%%%%%%%%"
pairs = [
    ("soit $N$ un\n" + M36 + "\nélément de $K$", "soit $N$ un élé%\n" + M36 + "\nment de $K$"),
    ("Dans le cas actuel, sa\n" + M37 + "\nrestriction à", "Dans le cas actuel,\n" + M37 + "\nsa restriction à"),
    ("est d'\n" + M38 + "\naugmentation nulle)", "est\n" + M38 + "\nd'augmentation nulle)"),
]
for layer in ("diplomatic", "current"):
    t = (W / layer / "main.tex").read_text(encoding="utf-8")
    for old, new in pairs:
        print(layer, repr(old[:30]), "old count", t.count(old), "new count", t.count(new))
