"""Simulate, in memory, on both layers: move_marker.py 6 157 '\\[' --before run twice, then move_marker.py 6 159
'\\section*{' --before, with and without this batch's fixes of the moved lines applied first. Writes nothing."""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
W = r"C:\Users\user\Documents\sga_scan_check_20261105\sga6"
BS = chr(92)
A_DISPLAY = BS + "["
A_SECTION = BS + "section*{"


def move(t, folio, anchor):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start())
    if k < 0:
        return None
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    return t2


def around(t, folio, before=200, after=260):
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
    return t[m.start() - before:m.end() + after]


fixes = [
    (BS + "section*{Bibliographie}", BS + "section*{BIBLIOGRAPHIE}"),
    (BS + 'arrow[d,"' + BS + "Id" + BS + "otimes" + BS + 'tau_F"]', BS + 'arrow[d,"' + BS + "Id" + BS + "otL" + BS + 'tau_F"]'),
]
for ed in ("diplomatic", "current"):
    for pre in (False, True):
        t = open(W + "\\" + ed + "\\main.tex", encoding="utf-8").read()
        if pre:
            for old, new in fixes:
                print(ed, "count of", repr(old), t.count(old))
                t = t.replace(old, new, 1)
        t = move(t, 157, A_DISPLAY)
        t = move(t, 157, A_DISPLAY)
        t = move(t, 159, A_SECTION)
        print("=" * 30, ed, "fixes first" if pre else "markers only")
        print(around(t, 157))
        print("-" * 10)
        print(around(t, 159, 120, 120))
        # the text of p. 156 must end with 'mécanique~») :' and contain no tikzcd
        m156 = next(m for m in MARK.finditer(t) if int(m.group(2)) == 156)
        m157 = next(m for m in MARK.finditer(t) if int(m.group(2)) == 157)
        seg = t[m156.end():m157.start()]
        print("p.156 segment ends:", repr(seg[-60:]), "| tikzcd in p.156:", "tikzcd" in seg)
