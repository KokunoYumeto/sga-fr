"""Simulate in memory (no file is written) the two marker fixes of pp. 230-231 on both layers of SGA 6:
  1. marker_split_word.py 6 230 pull '\((-1)\)-'
  2. move_marker.py 6 231 "C'est une" --before
and show the text around the moved markers."""
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, r"C:\Users\user\Documents\sga_scan_check_20261105")
from sga_config import MARK, files  # noqa: E402


def pull(t, folio, piece):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    ls = t.rfind("\n", 0, m.start()) + 1
    le = t.find("\n", m.end()) + 1
    prev_end = ls - 1
    if not t[:prev_end].endswith(piece):
        return None, "the line before the marker does not end with " + repr(piece)
    return t[:prev_end - len(piece)].rstrip(" ") + t[prev_end:le] + piece + t[le:], "ok"


def move_before(t, folio, anchor):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start())
    if k < 0:
        return None, "anchor not found"
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    return t2, "ok"


for edition in ("diplomatic", "current"):
    for f in files("6", edition):
        t = f.read_text(encoding="utf-8")
        t1, s1 = pull(t, 230, r"\((-1)\)-")
        print(edition, "pull 230:", s1)
        if t1 is None:
            continue
        t2, s2 = move_before(t1, 231, "C'est une")
        print(edition, "move 231:", s2)
        if t2 is None:
            continue
        for folio in (230, 231):
            m = next((m for m in MARK.finditer(t2) if int(m.group(2)) == folio))
            print("---", edition, folio)
            print(t2[m.start() - 90:m.end() + 90])
        print()
