"""Print the text around the folio markers 606-611 in both layers of main.tex, and check page_NNN.tex against the slices (read only)."""
import pathlib, sys, re
sys.stdout.reconfigure(encoding='utf-8')
ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
B = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\b606_610")
def mk(folio):
    return re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio " + str(folio) + r"  %%%%%%%%%%")
for layer in ("diplomatic", "current"):
    p = ROOT / layer / "main.tex"
    t = p.read_text(encoding="utf-8")
    print("=====", layer, p.stat().st_size, "bytes")
    for folio in range(606, 612):
        m = mk(folio).search(t)
        if not m:
            print("folio", folio, "marker not found"); continue
        q = m.start()
        line = t[:q].count("\n") + 1
        print("--- folio", folio, "line", line, "count", len(mk(folio).findall(t)))
        print(repr(t[max(0, q - 300):q + len(m.group(0)) + 150]))
    for f in range(606, 611):
        a = mk(f).search(t); b = mk(f + 1).search(t)
        sl = t[a.start():b.start()]
        pg = (B / f"page_{f}.tex").read_text(encoding="utf-8")
        body = pg.split("\n", 1)[1]
        print("folio", f, "page file == slice:", body == sl, len(body), len(sl))
