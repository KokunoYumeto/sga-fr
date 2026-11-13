"""Simulate (in memory, nothing written) the folio-490 marker move and the deletion of the added heading
above the folio-486 marker, in both layers; print counts and the resulting text around the edits."""
import pathlib

ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
MARK490 = "%%%%%%%%%%  scan idx 503  |  folio 490  %%%%%%%%%%"
MARK486 = "%%%%%%%%%%  scan idx 499  |  folio 486  %%%%%%%%%%"
edits = [
    ("faisceau inversible. Soit \\(\\xi\\) la\n" + MARK490 + "\nclasse d'un tel faisceau.",
     "faisceau inversible. Soit\n" + MARK490 + "\n\\(\\xi\\) la classe d'un tel faisceau."),
    ("est commutatif.\n\n\n\n\\subsection*{Suite de la d\u00e9monstration du th\u00e9or\u00e8me 3.6}\n\n" + MARK486 + "\n",
     "est commutatif.\n\n" + MARK486 + "\n"),
]
for layer in ("diplomatic", "current"):
    t = (ROOT / layer / "main.tex").read_text(encoding="utf-8")
    for old, new in edits:
        n = t.count(old)
        line = t[:t.find(old)].count("\n") + 1 if n else None
        print(layer, "count", n, "at line", line)
        if n == 1:
            t2 = t.replace(old, new)
            k = t2.find(new)
            print("   ->", repr(t2[k - 60:k + len(new) + 40]))
