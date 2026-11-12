"""In-memory simulation of move_marker.py (no file is written): show the text around the moved markers.
Anchors are the ASCII strings to pass on the command line: python -I move_marker.py 6 FOLIO 'ANCHOR' --before"""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
MOVES = ((325, r"de \(E\)~"), (326, r"\textbf{3.3.}"))


def move(t, folio, anchor, before=True):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    if k < 0:
        return None
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    return t2


for edition in ("diplomatic", "current"):
    t = (ROOT / edition / "main.tex").read_text(encoding="utf-8")
    for folio, anchor in MOVES:
        t2 = move(t, folio, anchor)
        if t2 is None:
            print(edition, folio, "anchor not found")
            continue
        m = next(m for m in MARK.finditer(t2) if int(m.group(2)) == folio)
        print("==", edition, folio, repr(anchor))
        print(repr(t2[m.start() - 100:m.end() + 100]))
        print()
