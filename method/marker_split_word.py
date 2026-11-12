"""Put a page marker where the printed page begins inside or right after a word, in both editions of a volume.
  python -I marker_split_word.py VOL FOLIO split HEAD TAIL   the page begins at TAIL, the second half of HEAD+TAIL
      (a word divided at the page break): the text right after the marker begins with HEAD+TAIL; it becomes
      HEAD% / marker / TAIL...  (the % joins the halves in the output)
  python -I marker_split_word.py VOL FOLIO pull PIECE        the page begins with PIECE, which ends the line before the
      marker (as "d'" before "augmentation"): PIECE moves from that line's end to the start of the line after the marker
usage: as above, add --dry to show without writing"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from sga_config import MARK, files  # noqa: E402

vol, folio, mode = sys.argv[1], int(sys.argv[2]), sys.argv[3]
dry = "--dry" in sys.argv
args = [a for a in sys.argv[4:] if a != "--dry"]
for edition in ("diplomatic", "current"):
    for f in files(vol, edition):
        t = f.read_text(encoding="utf-8")
        m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
        if not m:
            continue
        ls = t.rfind("\n", 0, m.start()) + 1          # start of the marker line
        le = t.find("\n", m.end()) + 1                 # start of the line after it
        if mode == "split":
            head, tail = args
            if not t.startswith(head + tail, le):
                print(edition, f.name, "text after the marker does not begin with", repr(head + tail))
                continue
            t2 = t[:ls] + head + "%\n" + t[ls:le] + t[le + len(head):]
        elif mode == "pull":
            piece = args[0]
            prev_end = ls - 1                          # the newline that ends the line before the marker
            if not t[:prev_end].endswith(piece):
                print(edition, f.name, "the line before the marker does not end with", repr(piece))
                continue
            t2 = t[:prev_end - len(piece)].rstrip(" ") + t[prev_end:le] + piece + t[le:]
        else:
            sys.exit("mode is split or pull")
        print(edition, f.name, "folio", folio, mode, "done" + (" (dry)" if dry else ""))
        if not dry:
            f.write_text(t2, encoding="utf-8", newline="")
