"""Simulate (in memory only) the marker repairs proposed for SGA 6 pp. 53, 54, 56 on both layers and print the
neighbourhoods. Nothing is written.
usage: python -I simulate_markers.py"""
import re

MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
BASE = r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\%s\main.tex"


def move(t, folio, anchor, before):
    """Same logic as move_marker.py."""
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    assert k >= 0, ("anchor not found", folio, anchor)
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    return t2


def show(t, folio, before=300, after=200):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    print("----- folio", folio)
    print(t[max(0, m.start() - before):m.end() + after])
    print()


for layer in ("diplomatic", "current"):
    t = open(BASE % layer, encoding="utf-8").read()
    print("=========", layer)
    # p. 53: split the \emph group at the page break, then move the folio-53 marker down to the new group
    old = "transversal à $f$, la formule (2.22) est exacte"
    assert t.count(old) == 1, ("count", old, t.count(old))
    t = t.replace(old, "transversal à $f$, la formule}\n\\emph{(2.22) est exacte")
    t = move(t, 53, "\\emph{(2.22) est exacte", before=False)
    # p. 54: the word parti-culier divided by the page break
    m54 = next(m for m in MARK.finditer(t) if int(m.group(2)) == 54)
    old54 = "est un cas\n" + m54.group(0) + "\nparticulier"
    n = t.count(old54)
    print("p54 pattern count:", n)
    if n == 1:
        t = t.replace(old54, "est un cas parti%\n" + m54.group(0) + "\nculier")
    # p. 56: the display (2.30) opens p. 56
    t = move(t, 56, "\\begin{equation}\\tag{2.30}", before=True)
    show(t, 53, 420, 260)
    show(t, 54, 160, 120)
    show(t, 56, 330, 120)
