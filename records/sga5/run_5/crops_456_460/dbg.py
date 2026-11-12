"""Line numbers of the anchors and markers of folios 456, 457, 460, 461 in both live layers (read-only)."""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
for layer in ("diplomatic", "current"):
    p = W / "sga5" / layer / "s5.tex"
    t = p.read_text(encoding="utf-8")
    print(layer, p.stat().st_mtime)
    for folio in (456, 457, 460, 461):
        m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
        print("  marker", folio, "line", t[:m.start()].count("\n") + 1)
    for name, a in (("et varphi", "et $\\varphi_F(U)"), ("item", "\\item\nPour tout faisceau de groupes"),
                    ("[ resizebox", "\\[\n\\resizebox")):
        k = t.find(a)
        print("  anchor", name, "line", t[:k].count("\n") + 1, "count", t.count(a))
