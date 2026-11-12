"""Simulate move_marker.py (same logic, in memory only; nothing is written) for the marker fixes of pp. 61-66
on both layers of SGA 6, and print the text around each moved marker."""
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, r"C:\Users\user\Documents\sga_scan_check_20261105")
from sga_config import MARK, files  # noqa: E402


def move(t, folio, anchor, before):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    if k < 0:
        raise SystemExit(f"anchor not found: {anchor!r}")
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    return t2


MOVES = [(61, r"$\Atil$ soumis aux restrictions", False),
         (62, r"$\Atil$ (où", False),
         (63, r"$1$", True),
         (64, r"(2.8) résulte", True),
         (66, r"La", True)]
for edition in ("diplomatic", "current"):
    f = files("6", edition)[0]
    t = f.read_text(encoding="utf-8")
    n0 = len(list(MARK.finditer(t)))
    for folio, anchor, before in MOVES:
        t = move(t, folio, anchor, before)
    assert len(list(MARK.finditer(t))) == n0
    folios = [int(m.group(2)) for m in MARK.finditer(t)]
    assert folios == sorted(folios), "marker order broken"
    print("==", edition)
    for folio, _, _ in MOVES:
        m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
        print(folio, repr(t[m.start() - 80:m.start()]), "|MARKER|", repr(t[m.end():m.end() + 70]))
