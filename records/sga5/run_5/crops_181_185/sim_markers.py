"""Simulate, in memory only, the marker moves proposed for pages 181, 182, 184, 185, 186 of SGA 5 (both editions),
with the same logic as move_marker.py and marker_split_word.py; print the text around each moved marker."""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
W = r"C:\Users\user\Documents\sga_scan_check_20261105\sga5"


def move(t, folio, anchor):  # move_marker.py ... --before
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start())
    assert k >= 0, (folio, anchor)
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        return t2[:ls] + line + "\n" + t2[ls:]
    return t2[:k] + "\n" + line + "\n" + t2[k:]


def pull(t, folio, piece):  # marker_split_word.py ... pull
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
    ls = t.rfind("\n", 0, m.start()) + 1
    le = t.find("\n", m.end()) + 1
    prev_end = ls - 1
    assert t[:prev_end].endswith(piece), (folio, piece)
    return t[:prev_end - len(piece)].rstrip(" ") + t[prev_end:le] + piece + t[le:]


for ed in ("diplomatic", "current"):
    t = open(rf"{W}\{ed}\s5.tex", encoding="utf-8").read()
    t = pull(t, 181, "$G$ un $A$-")
    t = move(t, 182, r"$B\otimes_KM$)")
    t = move(t, 184, r"\[")
    t = move(t, 185, "que 6.2.3 est un")
    t = move(t, 186, r"\begin{equation}")
    print("=====", ed)
    for m in MARK.finditer(t):
        if 181 <= int(m.group(2)) <= 186:
            print("--- folio", m.group(2))
            print(t[m.start() - 110:m.end() + 90])
