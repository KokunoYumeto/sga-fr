"""Simulate the marker fixes of pp. 167, 168 and 170 (171 shown as it stands) in memory on both layers of SGA 6, after the page fixes
that touch the same lines (\\emph{canonique} on p. 168). Prints the text around each marker. Writes nothing."""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
W = r"C:\Users\user\Documents\sga_scan_check_20261105\sga6"


def move(t, folio, anchor, before):
    """As move_marker.py."""
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    assert k >= 0, (folio, anchor)
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    return t2


for ed in ("diplomatic", "current"):
    t = open(W + "\\" + ed + "\\main.tex", encoding="utf-8").read()
    # page fix of p. 168 that touches the line after the marker
    old = "canonique\n\\[\n\\mathrm D^{-}"
    assert t.count(old) == 1, (ed, t.count(old))
    t = t.replace(old, "\\emph{canonique}\n\\[\n\\mathrm D^{-}")
    t = move(t, 167, r"$0\to L_1\to L_0\to L\to0$", True)
    t = move(t, 168, r"\[", False)
    t = move(t, 170, r"$F\,|\,S_{f_{ij}}$ est", True)
    for folio in (167, 168, 170, 171):  # 171: already split in main.tex (20:09)
        m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
        print(ed, folio, repr(t[m.start() - 110:m.end() + 70]))
        print()
