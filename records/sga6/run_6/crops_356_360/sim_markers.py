"""Simulate (in memory only, nothing is written) the two marker fixes of pp. 358 and 360 on both layers of SGA 6 main.tex:
(a) the exact string replacement given in findings_356_360.json, (b) the move_marker.py logic with the given anchor;
check that (a) matches once and that (a) and (b) give the same text."""
import pathlib
import re

W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
M358 = "%%%%%%%%%%  scan idx 371  |  folio 358  %%%%%%%%%%"
M360 = "%%%%%%%%%%  scan idx 373  |  folio 360  %%%%%%%%%%"
DISP = "\\[\n  \\cl_{\\Gr^i}\\bigl(\\gamma^i(\\widetilde c(x))\\bigr)=u(c^i(x)),\n\\]\n"
DIAG = ("\\[\n\\begin{tikzcd}[column sep=large,row sep=large]\n"
        "\\Lambda \\arrow[r,\"\\widetilde c\"] \\arrow[d,\"\\widetilde c_0\"'] &\n"
        "\\Ch(\\Gr\\Lambda)\\\\\n\\Ch(\\Omega) \\arrow[ur] &\n\\end{tikzcd}\n\\]\n")
FIXES = {
    358: ("donc :\n" + M358 + "\n" + DISP + "ce q", "donc :\n" + DISP + M358 + "\nce q"),
    360: ("commutatif :\n" + DIAG + M360 + "\nD'après", "commutatif :\n" + M360 + "\n" + DIAG + "D'après"),
}
ANCHORS = {358: ("ce q\\hphantom{u}i", False), 360: ("\\[", True)}


def move(t, folio, anchor, before):
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        return t2[:ls] + line + "\n" + t2[ls:]
    return t2[:k] + "\n" + line + "\n" + t2[k:]


for layer in ("diplomatic", "current"):
    t = (W / "sga6" / layer / "main.tex").read_text(encoding="utf-8")
    for folio, (old, new) in FIXES.items():
        n = t.count(old)
        a = t.replace(old, new) if n == 1 else None
        b = move(t, folio, *ANCHORS[folio])
        print(layer, folio, "old matches:", n, "| replacement == move_marker logic:", a == b)
        if a is not None:
            i = a.find(new)
            print("   ...", repr(a[i:i + len(new) + 60]))
