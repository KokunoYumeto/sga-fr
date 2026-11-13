"""Replicate move_marker.py's logic in memory (writes nothing) for folios 646, 647, 648 in both layers of SGA 6
and print the text around each moved marker."""
import pathlib, re, sys
sys.stdout.reconfigure(encoding='utf-8')
ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")


def move(t, folio, anchor, before):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    if k < 0:
        return None
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    return t2


def show(t, folio, before=220, after=160):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    print(repr(t[max(0, m.start() - before):m.end() + after]))


MOVES = [(646, "\\[", True), (647, "en", True), (648, "est aussi repr", False)]
for layer in ("diplomatic", "current"):
    t = (ROOT / layer / "main.tex").read_text(encoding="utf-8")
    print("=====", layer)
    for folio, anchor, before in MOVES:
        print("--- before move, folio", folio)
        show(t, folio)
        t = move(t, folio, anchor, before)
        print("--- after move")
        show(t, folio)
