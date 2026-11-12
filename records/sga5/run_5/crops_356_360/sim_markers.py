"""Simulate, in memory only, the marker commands proposed for folios 356, 357 and 359 on both layers of s5.tex
(same logic as move_marker.py and marker_split_word.py; nothing is written)."""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga5")


def move(t, folio, anchor, before):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    if k < 0:
        return None, "anchor not found"
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    return t2, "moved %d chars" % (m.start() - k)


def split(t, folio, head, tail):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    ls = t.rfind("\n", 0, m.start()) + 1
    le = t.find("\n", m.end()) + 1
    if not t.startswith(head + tail, le):
        return None, "text after the marker does not begin with " + repr(head + tail)
    return t[:ls] + head + "%\n" + t[ls:le] + t[le + len(head):], "split"


def show(t, folio, before=160, after=160):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    ln = t.count("\n", 0, m.start()) + 1
    print("   marker line", ln)
    print("   " + repr(t[max(0, m.start() - before):m.start()]))
    print("   " + repr(t[m.start():m.end() + after]))


for layer in ("diplomatic", "current"):
    t = (W / layer / "s5.tex").read_text(encoding="utf-8")
    print("=====", layer)
    t1, msg = move(t, 356, "\\[", True)
    print("356 move '\\[' --before:", msg)
    show(t1, 356)
    t2, msg = move(t, 357, "engendrée", True)
    print("357 move 'engendrée' --before:", msg)
    t3, msg = split(t2, 357, "en", "gendrée")
    print("357 split en gendrée:", msg)
    show(t3, 357)
    t4, msg = move(t, 359, "tel que $L_1", True)
    print("359 move 'tel que $L_1' --before:", msg)
    show(t4, 359)
    # all three together, in this order, then a second run of each to check idempotence
    a, _ = move(t, 356, "\\[", True)
    a, _ = move(a, 357, "engendrée", True)
    a, _ = split(a, 357, "en", "gendrée")
    a, _ = move(a, 359, "tel que $L_1", True)
    b, msg1 = move(a, 356, "\\[", True)
    print("second run 356:", msg1, "unchanged" if b == a else "CHANGED")
    b, msg2 = move(a, 359, "tel que $L_1", True)
    print("second run 359:", msg2, "unchanged" if b == a else "CHANGED")
    b, msg3 = move(a, 357, "engendrée", True)
    print("second run 357 move:", msg3, "unchanged" if b == a else "CHANGED")
    # text outside the markers must be unchanged apart from the 'en%' split
    strip = lambda s: MARK.sub("", s).replace("\n", "").replace("%", "").replace(" ", "")
    print("text identical apart from markers/space/%:", strip(a) == strip(t))
