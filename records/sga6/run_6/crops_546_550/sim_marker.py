"""Simulate move_marker.py in memory (no writes): sim_marker.py FOLIO ANCHOR [--before]; prints the result around the marker."""
import pathlib, sys
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, r"C:\Users\user\Documents\sga_scan_check_20261105")
from sga_config import MARK, files
folio, anchor = int(sys.argv[1]), sys.argv[2]
before = "--before" in sys.argv
for edition in ("diplomatic", "current"):
    for f in files("6", edition):
        t = f.read_text(encoding="utf-8")
        m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
        if not m:
            print(edition, "no marker"); continue
        line = m.group(0)
        end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
        print(f"--- {edition}: before (line {t.count(chr(10), 0, m.start()) + 1})")
        print(t[max(0, m.start() - 160):m.end() + 120])
        t2 = t[:m.start()] + t[end:]
        k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
        if k < 0:
            print(edition, "anchor not found"); continue
        print(f"    anchor found {m.start() - k} chars before the old marker place" if before else f"    anchor {k - m.start()} after")
        ls = t2.rfind("\n", 0, k) + 1
        if t2[ls:k].strip() == "":
            t2 = t2[:ls] + line + "\n" + t2[ls:]
        else:
            t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
        j = t2.find(line)
        print(f"--- {edition}: after")
        print(t2[max(0, j - 160):j + len(line) + 160])
