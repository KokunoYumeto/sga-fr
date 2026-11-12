"""Read-only simulation of move_marker.py for folios 193, 194, 196 of SGA 5 (both editions). Writes nothing."""
import re, sys, pathlib
sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga5")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")

def move(t, folio, anchor, before):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    if k < 0:
        return None, None
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    return t2, t2.find(line)

jobs = [(193, chr(92)+"begin{equation}", True), (194, "d'%", True), (196, "(III 4.7) entraîne", False)]
for ed in ("diplomatic", "current"):
    t = (W / ed / "s5.tex").read_text(encoding="utf-8")
    for folio, anchor, before in jobs:
        t2, p = move(t, folio, anchor, before)
        print("=====", ed, folio, repr(anchor), "before" if before else "after")
        if t2 is None:
            print("anchor not found"); continue
        print(t2[max(0, p - 260):p + 160])
        # check: text unchanged apart from marker position
        strip = lambda s: MARK.sub("", s).replace("\n", "")
        print("text identical apart from marker/newlines:", strip(t) == strip(t2))
