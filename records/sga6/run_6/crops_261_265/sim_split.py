"""Read-only simulation of marker_split_word.py: sim_split.py VOL FOLIO split HEAD TAIL | pull PIECE.
Prints the context after the change for both layers; writes nothing."""
import pathlib
import sys

sys.path.insert(0, r"C:\Users\user\Documents\sga_scan_check_20261105")
from sga_config import MARK, files  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
vol, folio, mode = sys.argv[1], int(sys.argv[2]), sys.argv[3]
args = sys.argv[4:]
for edition in ("diplomatic", "current"):
    for f in files(vol, edition):
        t = f.read_text(encoding="utf-8")
        m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
        if not m:
            continue
        ls = t.rfind("\n", 0, m.start()) + 1
        le = t.find("\n", m.end()) + 1
        if mode == "split":
            head, tail = args
            if not t.startswith(head + tail, le):
                print(edition, f.name, "text after the marker does not begin with", repr(head + tail))
                continue
            t2 = t[:ls] + head + "%\n" + t[ls:le] + t[le + len(head):]
        else:
            piece = args[0]
            prev_end = ls - 1
            if not t[:prev_end].endswith(piece):
                print(edition, f.name, "the line before the marker does not end with", repr(piece))
                continue
            t2 = t[:prev_end - len(piece)].rstrip(" ") + t[prev_end:le] + piece + t[le:]
        j = t2.find(m.group(0))
        print("==", edition, f.name)
        print(t2[max(0, j - 160):j + len(m.group(0)) + 160])
