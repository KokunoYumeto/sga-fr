"""Simulate (in memory only) the folio-395 marker move in both layers; writes nothing."""
import pathlib, sys
sys.stdout.reconfigure(encoding="utf-8")
BS = chr(92)
NL = chr(10)
ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
M395 = "%%%%%%%%%%  scan idx 408  |  folio 395  %%%%%%%%%%"
DISP = BS + "[" + NL + "  D_{" + BS + "pi'}(E)" + BS + "simeq D_{" + BS + "pi''}(F)." + NL + BS + "]" + NL
old = "canonique~:" + NL + DISP + M395 + NL
new = "canonique~:" + NL + M395 + NL + DISP
for layer in ("diplomatic", "current"):
    t = (ROOT / layer / "main.tex").read_text(encoding="utf-8")
    i = t.find(old)
    print(layer, "count:", t.count(old), " line", t.count(NL, 0, i) + 1)
    t2 = t.replace(old, new)
    j = t2.find(M395)
    print(repr(t2[j - 60:j + 150]))

# Replicate move_marker.py's algorithm (anchor '\[' --before) in memory and compare with the exact edit above.
import re
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
anchor = BS + "["
for layer in ("diplomatic", "current"):
    t = (ROOT / layer / "main.tex").read_text(encoding="utf-8")
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == 395)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == NL else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start())
    ls = t2.rfind(NL, 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + NL + t2[ls:]
    else:
        t2 = t2[:k] + NL + line + NL + t2[k:]
    print(layer, "move_marker result equals exact edit:", t2 == t.replace(old, new))
