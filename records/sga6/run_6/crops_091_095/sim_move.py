"""Simulate move_marker.py (same logic, nothing written) and print the text around the moved marker in both layers.
usage: python -I sim_move.py VOL FOLIO ANCHOR [--before]"""
import pathlib
import sys

sys.path.insert(0, r"C:\Users\user\Documents\sga_scan_check_20261105")
from sga_config import MARK, files  # noqa: E402

vol, folio, anchor = sys.argv[1], int(sys.argv[2]), sys.argv[3]
before = "--before" in sys.argv
for edition in ("diplomatic", "current"):
    for f in files(vol, edition):
        t = f.read_text(encoding="utf-8")
        m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
        if not m:
            continue
        line = m.group(0)
        end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
        t2 = t[:m.start()] + t[end:]
        k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
        if k < 0:
            print(edition, f.name, "anchor not found")
            continue
        ls = t2.rfind("\n", 0, k) + 1
        if t2[ls:k].strip() == "":
            t2 = t2[:ls] + line + "\n" + t2[ls:]
        else:
            t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
        p = t2.find(line)
        print("=====", edition, f.name)
        print("--- before (old):")
        print(t[max(0, m.start() - 300):m.end() + 120])
        print("--- after (simulated):")
        print(t2[max(0, p - 300):p + len(line) + 300])
