"""Print the text around the folio markers 571-576 in both layers of main.tex (read only)."""
import pathlib, sys, re
sys.stdout.reconfigure(encoding='utf-8')
ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
for layer in ("diplomatic", "current"):
    p = ROOT / layer / "main.tex"
    t = p.read_text(encoding="utf-8")
    print("=====", layer, p.stat().st_size, "bytes")
    for folio in (571, 572, 573, 574, 575, 576):
        m = re.search(r"%%%%%%%%%%  scan idx (\d+)  \|  folio " + str(folio) + r"  %%%%%%%%%%", t)
        if not m:
            print("folio", folio, "marker not found"); continue
        q = m.start()
        line = t[:q].count("\n") + 1
        print("--- folio", folio, "line", line, "count", t.count(m.group(0)))
        print(repr(t[max(0, q - 260):q + len(m.group(0)) + 120]))
