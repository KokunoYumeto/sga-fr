"""Read-only: count each proposed marker replacement's old text in both layers of SGA 6 main.tex and simulate it."""
import pathlib, sys
sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
M = "%%%%%%%%%%  scan idx {}  |  folio {}  %%%%%%%%%%"
moves = [
    (r"projectif sur \(S\)), on" + "\n" + M.format(594, 581) + "\n" + "peut dans ce diagramme",
     r"projectif sur \(S\))," + "\n" + M.format(594, 581) + "\n" + "on peut dans ce diagramme"),
    ("on définit alors un\n" + M.format(595, 582) + "\nhomomorphisme de spécialisation :",
     "on définit alors\n" + M.format(595, 582) + "\nun homomorphisme de spécialisation :"),
    ("et la réduction au cas d'un\n" + M.format(596, 583) + "\ncorps résiduel",
     "et la réduction\n" + M.format(596, 583) + "\nau cas d'un corps résiduel"),
]
for ed in ("diplomatic", "current"):
    t = (W / ed / "main.tex").read_text(encoding="utf-8")
    for old, new in moves:
        n = t.count(old)
        print(ed, repr(old[:30]), "count", n)
        if n == 1:
            t2 = t.replace(old, new)
            k = t2.index(new)
            print("   after:", repr(t2[k - 20:k + len(new) + 20]))
