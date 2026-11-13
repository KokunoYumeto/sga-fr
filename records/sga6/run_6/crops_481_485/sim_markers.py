"""Simulate the two marker moves (folios 482, 485) in memory on both layers of main.tex; print counts, line numbers
and the result around each edit. Writes nothing."""
import pathlib, sys
sys.stdout.reconfigure(encoding='utf-8')
ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
M482 = "%%%%%%%%%%  scan idx 495  |  folio 482  %%%%%%%%%%"
M485 = "%%%%%%%%%%  scan idx 498  |  folio 485  %%%%%%%%%%"
PAR = (r"Par additivité, on peut donc supposer que $x$ est la classe d'un $\mathcal O_X$-Module localement libre de type "
       r"fini $E$. De plus, quitte à remplacer $X$ par le schéma des drapeaux de $E$, ce qui donne une injection sur les")
EDITS = [
    ("(1.9) est\n" + M482 + "\nconstante sur $X$.",
     "(1.9)\n" + M482 + "\nest constante sur $X$."),
    (r"$c_t(x)=\sum_{i\geq0}c^i(x)t^i$." + "\n" + M485 + "\n" + PAR + r" $\Gr K^{\bullet}$ (VI 5.5), on",
     r"$c_t(x)=\sum_{i\geq0}c^i(x)t^i$." + "\n\n" + PAR + "\n" + M485 + "\n" + r"$\Gr K^{\bullet}$ (VI 5.5), on"),
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
        print("   ->", repr(t2[p2 - 30:p2 + len(new) + 40]))
        t = t2
print("OLD1", repr(EDITS[0][0]))
print("NEW1", repr(EDITS[0][1]))
print("OLD2", repr(EDITS[1][0]))
print("NEW2", repr(EDITS[1][1]))
