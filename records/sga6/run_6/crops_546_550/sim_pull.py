"""Simulate marker_split_word.py VOL FOLIO pull PIECE in memory (no writes) and show the result."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, r"C:\Users\user\Documents\sga_scan_check_20261105")
from sga_config import MARK, files
folio, piece = int(sys.argv[1]), sys.argv[2]
for edition in ("diplomatic", "current"):
    for f in files("6", edition):
        t = f.read_text(encoding="utf-8")
        m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
        if not m:
            print(edition, "no marker"); continue
        ls = t.rfind("\n", 0, m.start()) + 1
        le = t.find("\n", m.end()) + 1
        prev_end = ls - 1
        print(f"--- {edition}: before (line {t.count(chr(10), 0, m.start()) + 1})")
        print(t[max(0, ls - 140):le + 80])
        if not t[:prev_end].endswith(piece):
            print(edition, "the line before the marker does not end with", repr(piece)); continue
        t2 = t[:prev_end - len(piece)].rstrip(" ") + t[prev_end:le] + piece + t[le:]
        j = t2.find(m.group(0))
        print(f"--- {edition}: after")
        print(t2[max(0, j - 140):j + len(m.group(0)) + 120])
