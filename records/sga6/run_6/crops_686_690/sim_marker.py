"""Simulate move_marker.py in memory (no file is written): print the text around the moved marker.

usage: python -I sim_marker.py VOL FOLIO ANCHOR [--before]
"""
import pathlib
import sys

sys.path.insert(0, r"C:\Users\user\Documents\sga_scan_check_20261105")
from sga_config import MARK, files  # noqa: E402

vol, folio, anchor = sys.argv[1], int(sys.argv[2]), sys.argv[3]
before = "--before" in sys.argv
out = sys.stdout.buffer
for edition in ("diplomatic", "current"):
    for f in files(vol, edition):
        if not f.exists():
            continue
        t = f.read_text(encoding="utf-8")
        m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
        if not m:
            continue
        line = m.group(0)
        end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
        t2 = t[:m.start()] + t[end:]
        k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
        if k < 0:
            out.write(f"{edition} {f.name}: anchor not found\n".encode("utf-8"))
            continue
        ls = t2.rfind("\n", 0, k) + 1
        if t2[ls:k].strip() == "":
            t2 = t2[:ls] + line + "\n" + t2[ls:]
        else:
            t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
        j = t2.find(line)
        out.write(f"== {edition} {f.name}: before ==\n".encode("utf-8"))
        out.write(t[max(0, m.start() - 160):m.end() + 120].encode("utf-8") + b"\n")
        out.write(f"== {edition} {f.name}: after ==\n".encode("utf-8"))
        out.write(t2[max(0, j - 160):j + len(line) + 120].encode("utf-8") + b"\n")
