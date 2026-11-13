"""Simulate (in memory only) the marker moves of folios 402, 403 and 406 in both layers; writes nothing."""
import pathlib, sys
sys.stdout.reconfigure(encoding="utf-8")
BS = chr(92)
NL = chr(10)
ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
M402 = "%%%%%%%%%%  scan idx 415  |  folio 402  %%%%%%%%%%"
M403 = "%%%%%%%%%%  scan idx 416  |  folio 403  %%%%%%%%%%"
M406 = "%%%%%%%%%%  scan idx 419  |  folio 406  %%%%%%%%%%"
SUM403 = "  " + BS + "sum_{i=0}^{r+1}(-1)^i" + BS + "lambda^i(E)f_*(" + BS + "xi^{" + BS + ",n-i})=0 ."
OPEN = BS + "["
CLOSE = BS + "]"
a_old = "$f$" + NL + M402 + NL
a_new = M402 + NL + "$f$" + NL
b_old = "On peut lui appliquer $f_*$ :" + NL + OPEN + NL + SUM403 + NL + CLOSE + NL + "Le" + NL + M403 + NL
b_new = "On peut lui appliquer $f_*$ :" + NL + M403 + NL + OPEN + NL + SUM403 + NL + CLOSE + NL + "Le" + NL
for layer in ("diplomatic", "current"):
    t = (ROOT / layer / "main.tex").read_text(encoding="utf-8")
    lines = t.split(NL)
    print(layer, "402 old:", t.count(a_old), " 403 old:", t.count(b_old), " 406 marker:", t.count(M406))
    for old in (a_old, b_old):
        i = t.find(old)
        print("   starts at line", t.count(NL, 0, i) + 1)
    # 406: move the marker line up to directly after 'De la relation $E=F+\xi$, on déduit donc :'
    anchor = "De la relation $E=F+" + BS + "xi$, on déduit donc :"
    ia = [n for n, l in enumerate(lines) if l == anchor]
    im = [n for n, l in enumerate(lines) if l == M406]
    print("   406 anchor line(s):", [n + 1 for n in ia], " marker line(s):", [n + 1 for n in im])
    t2 = t.replace(a_old, a_new).replace(b_old, b_new)
    l2 = t2.split(NL)
    j = l2.index(M406)
    del l2[j]
    k = l2.index(anchor)
    l2.insert(k + 1, M406)
    t3 = NL.join(l2)
    for f in ("folio 402", "folio 403", "folio 406"):
        i = t3.find(f)
        print("  ", f, repr(t3[i - 120:i + 160]))
