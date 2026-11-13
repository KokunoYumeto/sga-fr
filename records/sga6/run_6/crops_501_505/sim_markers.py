"""Simulate the two marker moves (folios 502, 505) in memory on both layers of main.tex (no file is written);
print the count of each old string, its line, and the result around the marker."""
import pathlib, sys
sys.stdout.reconfigure(encoding='utf-8')
ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
M502 = "%%%%%%%%%%  scan idx 515  |  folio 502  %%%%%%%%%%"
M505 = "%%%%%%%%%%  scan idx 518  |  folio 505  %%%%%%%%%%"
EDITS = [
    ("car $i$ est\n" + M502 + "\npropre et $f$ plat. Soit $(x_i)_{i\\in I}",
     "car $i$ est\npropre et $f$ plat.\n\n" + M502 + "\nSoit $(x_i)_{i\\in I}"),
    ("si on suppose $f$ de\n" + M505 + "\nprésentation finie).",
     "si on suppose $f$\n" + M505 + "\nde présentation finie)."),
]
for layer in ("diplomatic", "current"):
    t = (ROOT / layer / "main.tex").read_text(encoding="utf-8")
    for old, new in EDITS:
        n = t.count(old)
        pos = t.find(old)
        line = t[:pos].count("\n") + 1 if pos >= 0 else None
        print(layer, "count", n, "starts at line", line)
        if n == 1:
            t2 = t.replace(old, new, 1)
            p2 = t2.find(new)
            print("   ->", repr(t2[p2 - 40:p2 + len(new) + 40]))
            t = t2
        else:
            # show context of the marker for diagnosis
            mk = M502 if M502 in old else M505
            q = t.find(mk)
            print("   context:", repr(t[q - 200:q + 200]))
