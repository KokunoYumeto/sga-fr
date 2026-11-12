"""Simulate the marker fixes of pp. 402, 403, 405, 406 in memory on both layers of s5.tex (no writes)."""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
BASE = "C:/Users/user/Documents/sga_scan_check_20261105/sga5"
BS = "\\"


def move(t, folio, anchor, before):
    """The algorithm of move_marker.py."""
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    if k < 0:
        return None, line
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    return t2, line


def show(t2, line, label):
    if t2 is None:
        print(label, "ANCHOR NOT FOUND")
        return
    lines = t2.split("\n")
    i = next(j for j, s in enumerate(lines) if s == line)
    print(label, "marker now at line", i + 1)
    for s in lines[i - 3:i + 3]:
        print("    |", s[:110])


A402 = BS + "["
A405 = "donc $("
A406 = BS + "section*{Références}"

for ed in ("diplomatic", "current"):
    t = open(f"{BASE}/{ed}/s5.tex", encoding="utf-8", newline="").read()
    print("=====", ed)
    for folio in (401, 402, 403, 404, 405, 406):
        m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
        print("   folio", folio, "marker at line", t.count("\n", 0, m.start()) + 1)
    t2, line = move(t, 402, A402, True)
    show(t2, line, "402")
    t3, line = move(t, 405, A405, True)
    show(t3, line, "405")
    t4, line = move(t, 406, A406, True)
    show(t4, line, "406")
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == 403)
    old = "\n(``\n" + m.group(0) + "\nisomorphisme"
    new = "\n" + m.group(0) + "\n(``isomorphisme"
    print("403 replacement: old occurs", t.count(old), "time(s)")
    show(t.replace(old, new), m.group(0), "403")
    # all together, in either order
    tt = t
    for folio, anc in ((402, A402), (405, A405), (406, A406)):
        tt, _ = move(tt, folio, anc, True)
    tt = tt.replace(old, new)
    fol = [int(x.group(2)) for x in MARK.finditer(tt)]
    print("all four applied: markers increasing:", fol == sorted(fol), "count", len(fol), "of", len(list(MARK.finditer(t))))
