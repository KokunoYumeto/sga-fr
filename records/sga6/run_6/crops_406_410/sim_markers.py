"""Simulate (in memory only) the marker moves of folios 407 and 408 in both layers; writes nothing."""
import pathlib, sys
sys.stdout.reconfigure(encoding="utf-8")
BS = chr(92); NL = chr(10)
ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
M407 = "%%%%%%%%%%  scan idx 420  |  folio 407  %%%%%%%%%%"
M408 = "%%%%%%%%%%  scan idx 421  |  folio 408  %%%%%%%%%%"
ZDISP = "  z=a_r." + BS + "left(" + BS + "sum_{i=0}^{r-1}c_{i+1}{x'}^i+{x'}^r" + BS + "right)."
a_old = "Donc :" + NL + BS + "[" + NL + ZDISP + NL + BS + "]" + NL + "Or :" + NL + BS + "[" + NL + M407 + NL
a_new = M407 + NL + "Donc :" + NL + BS + "[" + NL + ZDISP + NL + BS + "]" + NL + "Or :" + NL + BS + "[" + NL
b_old = "On note $" + BS + "varepsilon$ l'%" + NL + M408 + NL + "homomorphisme d'augmentation"
b_new = "On note" + NL + M408 + NL + "$" + BS + "varepsilon$ l'homomorphisme d'augmentation"
for layer in ("diplomatic", "current"):
    t = (ROOT / layer / "main.tex").read_text(encoding="utf-8")
    print(layer, "407 old:", t.count(a_old), " 408 old:", t.count(b_old), " M407:", t.count(M407), " M408:", t.count(M408))
    for old in (a_old, b_old):
        i = t.find(old)
        print("   starts at line", t.count(NL, 0, i) + 1)
    t2 = t.replace(a_old, a_new).replace(b_old, b_new)
    for m in (M407, M408):
        i = t2.find(m)
        print("  ", repr(t2[i - 160:i + 120]))
