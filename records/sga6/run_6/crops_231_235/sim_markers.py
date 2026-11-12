"""Simulate move_marker.py on an in-memory copy of main.tex (no writes) and print the context of the moved markers."""
import re
import sys

B = chr(92)
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")


def move(t, folio, anchor, before):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    if k < 0:
        return None
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        return t2[:ls] + line + "\n" + t2[ls:]
    return t2[:k] + "\n" + line + "\n" + t2[k:]


for path in sys.argv[1:]:
    t = open(path, encoding="utf-8").read()
    for folio, anchor, before in ((231, "C'est une", True), (232, B + "[", False), (233, B + "textbf{Corollaire 1.9.}", False)):
        t = move(t, folio, anchor, before)
        m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
        print("==", path[-40:], folio)
        print(repr(t[m.start() - 90:m.end() + 60]))
