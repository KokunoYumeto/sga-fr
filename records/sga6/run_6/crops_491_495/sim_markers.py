"""Simulate the two marker moves (folios 492, 494) in memory on both layers of main.tex; print counts and line numbers.
Also simulate them together with the page-491 fix '1-J.\\n\\]\\nD'où' -> '1-J,\\n\\]\\nd'où' (no overlap expected)."""
import pathlib, sys
sys.stdout.reconfigure(encoding='utf-8')
ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
M492 = "%%%%%%%%%%  scan idx 505  |  folio 492  %%%%%%%%%%"
M494 = "%%%%%%%%%%  scan idx 507  |  folio 494  %%%%%%%%%%"
DISP = "\\[\n \\ch(i_*(i^*(y)))=\\ch(y)\\cdot\\ch(1-J).\n\\]\n"
EDITS = [
    (DISP + M492 + "\n", M492 + "\n" + DISP),
    ("réduites au degré \\(0\\).\n\nLe\n" + M494 + "\nmodule des différentielles",
     "réduites\n" + M494 + "\nau degré \\(0\\).\n\nLe module des différentielles"),
]
OTHER = [("i_*(1)=1-J.\n\\]\nD'où", "i_*(1)=1-J,\n\\]\nd'où")]
for layer in ("diplomatic", "current"):
    t = (ROOT / layer / "main.tex").read_text(encoding="utf-8")
    for old, new in EDITS + OTHER:
        n = t.count(old)
        pos = t.find(old)
        line = t[:pos].count("\n") + 1
        last = line + old.count("\n")
        print(layer, "count", n, "lines", line, "-", last)
    t2 = t
    for old, new in OTHER + EDITS:
        assert t2.count(old) == 1, (layer, old[:40])
        t2 = t2.replace(old, new, 1)
    for m in (M492, M494):
        p = t2.find(m)
        print("   ", layer, repr(t2[p - 160:p + len(m) + 80]))
