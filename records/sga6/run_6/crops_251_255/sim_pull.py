"""Simulate marker_split_word.py VOL FOLIO pull PIECE (read-only)."""
import sys
sys.path.insert(0, r"C:\Users\user\Documents\sga_scan_check_20261105")
from sga_config import MARK, files
sys.stdout.reconfigure(encoding="utf-8")
vol, folio, piece = sys.argv[1], int(sys.argv[2]), sys.argv[3]
for edition in ("diplomatic", "current"):
    for f in files(vol, edition):
        t = f.read_text(encoding="utf-8")
        m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
        if not m:
            continue
        ls = t.rfind("\n", 0, m.start()) + 1
        le = t.find("\n", m.end()) + 1
        prev_end = ls - 1
        if not t[:prev_end].endswith(piece):
            print(edition, "line before the marker does not end with piece"); continue
        t2 = t[:prev_end - len(piece)].rstrip(" ") + t[prev_end:le] + piece + t[le:]
        j = t2.find(m.group(0))
        print("==", edition); print(t2[j - 120:j + len(m.group(0)) + 120])
