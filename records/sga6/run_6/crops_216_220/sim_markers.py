"""Simulate move_marker.py (in memory, nothing written) and print the context around each moved marker."""
import pathlib
import sys
sys.path.insert(0, r"C:\Users\user\Documents\sga_scan_check_20261105")
from sga_config import MARK, files  # noqa: E402

moves = [(218, "Si $S$ est"), (219, "$\operatorname{Ell}"), (220, "\subsection*{"), (221, "\item")]
for edition in ("diplomatic", "current"):
    for f in files("6", edition):
        t = f.read_text(encoding="utf-8")
        for folio, anchor in moves:
            m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
            line = m.group(0)
            end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
            t2 = t[:m.start()] + t[end:]
            k = t2.rfind(anchor, 0, m.start())
            ls = t2.rfind("\n", 0, k) + 1
            if t2[ls:k].strip() == "":
                t2 = t2[:ls] + line + "\n" + t2[ls:]
            else:
                t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
            t = t2
        for folio, _ in moves:
            m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
            print("==", edition, folio, repr(t[m.start() - 120:m.start()]), "|| MARKER ||", repr(t[m.end():m.end() + 90]))
