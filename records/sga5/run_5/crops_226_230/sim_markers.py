"""Simulate move_marker.py in memory (no writes) for the given moves, on both layers of SGA 5, applied in order."""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
root = Path(__file__).resolve().parents[2]
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
MOVES = [
    (227, "\\subsubsection*{4.1.4}", True),
    (228, "\\((ii)\\Rightarrow(i)\\)", False),
    (229, "\\[", True),
    (231, "Il", True),
]


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


for layer in ("diplomatic", "current"):
    t = (root / "sga5" / layer / "s5.tex").read_text(encoding="utf-8")
    for folio, anchor, before in MOVES:
        t2 = move(t, folio, anchor, before)
        if t2 is None:
            print(layer, folio, "ANCHOR NOT FOUND")
            continue
        t = t2
        m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
        a = t.rfind("\n", 0, max(0, m.start() - 1))
        a = t.rfind("\n", 0, a)
        a = t.rfind("\n", 0, a)
        b = t.find("\n", m.end() + 1)
        b = t.find("\n", b + 1)
        print("=====", layer, folio, "before" if before else "forward", repr(anchor))
        print(t[a + 1:b])
