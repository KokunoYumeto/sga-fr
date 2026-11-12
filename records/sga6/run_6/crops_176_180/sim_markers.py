"""Simulate move_marker.py in memory (nothing written) for the markers of pp. 176-181, on both layers."""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
BASE = r"C:\Users\user\Documents\sga_scan_check_20261105\sga6"
MOVES = [(177, "D'%", True), (178, "équivalences de catégories :", False),
         (180, r"\item", True), (181, r"où $\Lib(A)$", True)]


def move(t, folio, anchor, before):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    if k < 0:
        return t, None
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    return t2, t2.find(line)


for layer in ("diplomatic", "current"):
    t = open(BASE + "\\" + layer + r"\main.tex", encoding="utf-8").read()
    for folio, anchor, before in MOVES:
        t, pos = move(t, folio, anchor, before)
        if pos is None:
            print(layer, folio, "ANCHOR NOT FOUND")
            continue
        a = t[max(0, pos - 90):pos]
        b = t[pos:pos + 140]
        print(f"--- {layer} folio {folio}:\n{a!r}\n{b!r}\n")
