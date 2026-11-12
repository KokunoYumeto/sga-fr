"""Simulate (in memory only) the two marker moves of folios 389 and 390 in both layers; writes nothing."""
import pathlib, sys
sys.stdout.reconfigure(encoding="utf-8")
BS = chr(92)
NL = chr(10)
ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
M389 = "%%%%%%%%%%  scan idx 402  |  folio 389  %%%%%%%%%%"
M390 = "%%%%%%%%%%  scan idx 403  |  folio 390  %%%%%%%%%%"
H = BS + "textbf{2.8.}"
for layer in ("diplomatic", "current"):
    t = (ROOT / layer / "main.tex").read_text(encoding="utf-8")
    a_old = H + NL + M389 + NL
    a_new = M389 + NL + H + NL
    b_old = "on achève par" + NL + M390 + NL + "récurrence,"
    b_new = "on" + NL + M390 + NL + "achève par récurrence,"
    print(layer, "389:", t.count(a_old), " 390:", t.count(b_old))
    for old in (a_old, b_old):
        i = t.find(old)
        print("   line", t.count(NL, 0, i) + 1)
    t2 = t.replace(a_old, a_new).replace(b_old, b_new)
    i = t2.find("folio 389")
    print(repr(t2[i - 80:i + 120]))
    i = t2.find("folio 390")
    print(repr(t2[i - 80:i + 120]))
