"""Simulate (in memory only, nothing is written) move_marker.py --before and marker_split_word.py split
on both layers of SGA 6 main.tex, and print the result around the moved markers."""
import pathlib, re, sys
sys.stdout.reconfigure(encoding='utf-8')
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")

def move_before(t, folio, anchor):
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start())
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        return t2[:ls] + line + "\n" + t2[ls:]
    return t2[:k] + "\n" + line + "\n" + t2[k:]

def split(t, folio, head, tail):
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
    ls = t.rfind("\n", 0, m.start()) + 1
    le = t.find("\n", m.end()) + 1
    assert t.startswith(head + tail, le), "text after marker does not start with head+tail"
    return t[:ls] + head + "%\n" + t[ls:le] + t[le + len(head):]

for ed in ("diplomatic", "current"):
    t = (W / ed / "main.tex").read_text(encoding="utf-8")
    t1 = split(move_before(t, 171, "quasi-coh"), 171, "quasi-", "coh")
    m = next(m for m in MARK.finditer(t1) if int(m.group(2)) == 171)
    print("=====", ed, "folio 171")
    print(repr(t1[m.start() - 120:m.end() + 60]))
    t2 = move_before(t, 176, "la")
    m = next(m for m in MARK.finditer(t2) if int(m.group(2)) == 176)
    print("=====", ed, "folio 176")
    print(repr(t2[m.start() - 90:m.end() + 60]))
    # only these two markers changed, all others in the same order
    print("markers:", len(list(MARK.finditer(t))), len(list(MARK.finditer(t1))), len(list(MARK.finditer(t2))))
