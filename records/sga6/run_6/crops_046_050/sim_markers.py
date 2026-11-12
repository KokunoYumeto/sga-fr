"""Simulate move_marker.py (same logic, in memory only; nothing is written) for the marker fixes of pp. 46-50,
plus the word join of p. 46, on both layers of SGA 6, and print the text around each moved marker."""
import pathlib
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


for edition in ("diplomatic", "current"):
    f = files("6", edition)[0]
    t = f.read_text(encoding="utf-8")
    n0 = len(list(MARK.finditer(t)))
    t = move(t, 46, "brique sur", False)
    old = "algé\n%%%%%%%%%%  scan idx 59"
    assert t.count(old) == 1, t.count(old)
    t = t.replace(old, "algé%\n%%%%%%%%%%  scan idx 59")
    t = move(t, 48, "non", True)
    t = move(t, 49, sys.argv[1] if len(sys.argv) > 1 else "du début", True)
    assert len(list(MARK.finditer(t))) == n0
    print("==", edition)
    for folio in (46, 48, 49):
        m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
        print(repr(t[m.start() - 90:m.end() + 60]))
