"""Simulate the marker edits of findings_586_590 on both layers of main.tex in memory (nothing is written)."""
import pathlib, sys
sys.stdout.reconfigure(encoding="utf-8")
ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
M = {588: "%%%%%%%%%%  scan idx 601  |  folio 588  %%%%%%%%%%",
     590: "%%%%%%%%%%  scan idx 603  |  folio 590  %%%%%%%%%%",
     591: "%%%%%%%%%%  scan idx 604  |  folio 591  %%%%%%%%%%"}
EDITS = [
    ("Signalons seulement qu'il\n" + M[588] + "\nrésulte de 7.16.2",
     "Signalons seulement\n" + M[588] + "\nqu'il résulte de 7.16.2"),
    ("de spécialisation au cas où la\n" + M[590] + "\nbase est un trait.",
     "de spécialisation au\n" + M[590] + "\ncas où la base est un trait."),
    ("nous cherchons des critères\n" + M[591] + "\npour que",
     "nous cherchons des cri%\n" + M[591] + "\ntères pour que"),
]
for layer in ("diplomatic", "current"):
    t = (ROOT / layer / "main.tex").read_text(encoding="utf-8")
    for old, new in EDITS:
        n = t.count(old)
        print(layer, "count", n, "|", old.split("\n")[0][-30:])
        if n == 1:
            i = t.index(old)
            t2 = t.replace(old, new)
            j = t2.index(new)
            print("   ->", repr(t2[max(0, j - 40): j + len(new) + 30]))
