"""Simulate move_marker.py for folios 18, 19 and 20 of SGA 6 on in-memory copies (writes nothing)."""
import pathlib
import re

MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
base = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")


def move(t, folio, anchor, before):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    assert k >= 0, anchor
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    return t2


for ed in ("diplomatic", "current"):
    t = (base / ed / "main.tex").read_text(encoding="utf-8")
    t = move(t, 18, "pos\\'e est", True)
    t = t.replace("cet ex\n%%%%%%%%%%  scan idx 31", "cet ex%\n%%%%%%%%%%  scan idx 31", 1)
    t = move(t, 19, "\\section*{Bibliographie}", True)
    t = move(t, 20, "\\section*{Appendice", True)
    for folio in (18, 19, 20):
        m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
        print("==", ed, folio)
        print(t[m.start() - 120:m.end() + 90])
