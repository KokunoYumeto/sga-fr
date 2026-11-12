"""Simulate move_marker.py / marker_split_word.py in memory (no writes) on both layers of SGA 5."""
import re, pathlib
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga5")

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

def split(t, folio, head, tail):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    ls = t.rfind("\n", 0, m.start()) + 1
    le = t.find("\n", m.end()) + 1
    if not t.startswith(head + tail, le):
        return None
    return t[:ls] + head + "%\n" + t[ls:le] + t[le + len(head):]

def around(t, folio, n=160):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    return repr(t[max(0, m.start() - n):m.end() + n])

for ed in ("diplomatic", "current"):
    t = (W / ed / "s5.tex").read_text(encoding="utf-8")
    print("=====", ed)
    a = move(t, 362, "pour", True); print("362:", around(a, 362, 90) if a else "ANCHOR NOT FOUND")
    b = move(a, 363, "(C).", True); print("363:", around(b, 363, 90) if b else "ANCHOR NOT FOUND")
    c = split(b, 365, "pro", "positions"); print("365:", around(c, 365, 90) if c else "SPLIT FAILED")
    d = move(c, 366, "bifoncteur", True); print("366 move:", around(d, 366, 90) if d else "ANCHOR NOT FOUND")
    e = split(d, 366, "bifonc", "teur") if d else None; print("366 split:", around(e, 366, 90) if e else "SPLIT FAILED")
