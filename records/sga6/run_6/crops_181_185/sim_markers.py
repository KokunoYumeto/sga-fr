"""Simulate, in memory, the marker commands proposed for pp. 181 and 185 on both layers of SGA 6 (writes nothing).
Each command is simulated on its own:
  python -I move_marker.py 6 181 'où $\\Lib(A)$' --before
  python -I marker_split_word.py 6 185 split loca liser"""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
W = r"C:\Users\user\Documents\sga_scan_check_20261105\sga6"
BS = chr(92)


def move_before(t, folio, anchor):
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


def split_word(t, folio, head, tail):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    ls = t.rfind("\n", 0, m.start()) + 1
    le = t.find("\n", m.end()) + 1
    if not t.startswith(head + tail, le):
        return None
    return t[:ls] + head + "%\n" + t[ls:le] + t[le + len(head):]


def show(t, folio):
    m2 = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
    return repr(t[m2.start() - 90:m2.end() + 60])


for ed in ("diplomatic", "current"):
    t = open(W + BS + ed + BS + "main.tex", encoding="utf-8").read()
    print(ed, "181 now:", show(t, 181))
    t1 = move_before(t, 181, "où $" + BS + "Lib(A)$")
    print(ed, "181 after move:", "anchor not found (no change)" if t1 is None else show(t1, 181))
    t2 = split_word(t, 185, "loca", "liser")
    print(ed, "185 after split:", "text after the marker does not begin with localiser" if t2 is None
          else show(t2, 185))
    print()
