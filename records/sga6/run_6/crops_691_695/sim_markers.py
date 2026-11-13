"""Simulate in memory (no writing) the two marker moves for pp. 695-697 on both layers of SGA 6 main.tex,
with the logic of move_marker.py, and print the resulting region."""
import pathlib
import re

W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")


def move(t, folio, anchor, before=False):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    assert k >= 0, "anchor not found"
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    return t2


A697 = "\(\Dcat^{-}(\Qcoh(S))_{\coh}"
A696 = "\section*{Index des notations}"
for ed in ("diplomatic", "current"):
    t = (W / ed / "main.tex").read_text(encoding="utf-8")
    print(ed, "anchor counts:", t.count(A697), t.count(A696))
    t2 = move(move(t, 697, A697), 696, A696)
    i = t2.find("folio 695  %")
    j = t2.find("folio 698  %")
    seg = t2[i - 40:j if j > 0 else i + 4000]
    # print the part from the 695 marker to the 697 marker
    k = seg.find("folio 697  %")
    print(seg[:k + 60])
    print("....")
    # markers in order?
    fol = [int(m.group(2)) for m in MARK.finditer(t2)]
    print("markers increasing:", all(a < b for a, b in zip(fol, fol[1:])))
    print("=" * 60)
