"""Read-only simulation, in memory, of the marker fixes of pp. 261-265 on both layers of SGA 6 main.tex.
Order as proposed: content fix of p. 265 (comma into the display) first, then the marker moves. Writes nothing."""
import sys

sys.path.insert(0, r"C:\Users\user\Documents\sga_scan_check_20261105")
from sga_config import MARK, files  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")


def move(t, folio, anchor, before):
    """the logic of move_marker.py"""
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    assert k >= 0, (folio, anchor)
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        return t2[:ls] + line + "\n" + t2[ls:]
    return t2[:k] + "\n" + line + "\n" + t2[k:]


def split(t, folio, head, tail):
    """the logic of marker_split_word.py split"""
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
    ls = t.rfind("\n", 0, m.start()) + 1
    le = t.find("\n", m.end()) + 1
    assert t.startswith(head + tail, le), (folio, head, tail)
    return t[:ls] + head + "%\n" + t[ls:le] + t[le + len(head):]


def show(t, folio, before=170, after=170):
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
    print(f"--- folio {folio}")
    print(t[max(0, m.start() - before):m.end() + after])


OLD = "\\tag{5.3.1.1}\n\\end{equation}\n, composée de"
NEW = ",\\tag{5.3.1.1}\n\\end{equation}\ncomposée de"
for edition in ("diplomatic", "current"):
    f = files("6", edition)[0]
    t = f.read_text(encoding="utf-8")
    print("==========", edition, "count of the p. 265 comma old:", t.count(OLD))
    t = t.replace(OLD, NEW, 1)
    t = move(t, 261, "du", True)
    t = split(t, 262, "condi", "tion")
    t = move(t, 264, "\\item[c)]", True)
    t = move(t, 265, "composée de \\(H^{-p-1}(E^{\\vee})", False)
    for fo in (261, 262, 264, 265):
        show(t, fo)
