"""Simulate (in memory, nothing written) the marker moves proposed for folios 326, 328 and 331 on both layers,
with the logic of move_marker.py, and print the lines around each moved marker.
Also compare the batch page files with the live diplomatic main.tex spans."""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
MOVES = [(326, r"\textbf{3.3.}"), (328, "\\["), (331, r"\textbf{3.10")]


def move(t, folio, anchor):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start())
    if k < 0:
        return None, None
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    return t2, t2.find(line)


for edition in ("diplomatic", "current"):
    t = (W / "sga6" / edition / "main.tex").read_text(encoding="utf-8")
    for folio, anchor in MOVES:
        t2, p = move(t, folio, anchor)
        print("=" * 20, edition, folio, repr(anchor))
        if t2 is None:
            print("anchor not found")
            continue
        a = t2.rfind("\n", 0, max(0, p - 1))
        a = t2.rfind("\n", 0, max(0, a - 1))
        b = p
        for _ in range(3):
            b = t2.find("\n", b + 1)
        print(t2[a + 1:b])

# batch files against the live diplomatic spans
t = (W / "sga6" / "diplomatic" / "main.tex").read_text(encoding="utf-8")
ms = list(MARK.finditer(t))
for folio in range(326, 331):
    i = next(i for i, m in enumerate(ms) if int(m.group(2)) == folio)
    span = t[ms[i].start():ms[i + 1].start()]
    bf = (W / "run_6" / "b326_330" / f"page_{folio}.tex").read_text(encoding="utf-8")
    body = bf.split("\n", 1)[1]  # drop the '% from main.tex' line
    print(folio, "batch file == live span:", body == span, len(body), len(span))
