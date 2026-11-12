"""Simulate in memory (never writes): move_marker.py VOL FOLIO ANCHOR [--before], optionally followed by
marker_split_word.py VOL FOLIO split HEAD TAIL, on both layers of SGA 5; print the text around the marker.
usage: sim_marker.py FOLIO ANCHOR before|after [HEAD TAIL]"""
import pathlib, re, sys
sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
folio, anchor, mode = int(sys.argv[1]), sys.argv[2], sys.argv[3]
split = sys.argv[4:6] if len(sys.argv) > 5 else None
for edition in ("diplomatic", "current"):
    f = W / "sga5" / edition / "s5.tex"
    t = f.read_text(encoding="utf-8")
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if mode == "before" else t2.find(anchor, m.start())
    if k < 0:
        print(edition, "anchor not found"); continue
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    if split:
        head, tail = split
        m = next(m for m in MARK.finditer(t2) if int(m.group(2)) == folio)
        ls = t2.rfind("\n", 0, m.start()) + 1
        le = t2.find("\n", m.end()) + 1
        if not t2.startswith(head + tail, le):
            print(edition, "split: text after marker does not begin with", repr(head + tail)); continue
        t2 = t2[:ls] + head + "%\n" + t2[ls:le] + t2[le + len(head):]
    m = next(m for m in MARK.finditer(t2) if int(m.group(2)) == folio)
    print("=====", edition, "line", t2.count("\n", 0, m.start()) + 1)
    print(t2[max(0, m.start() - 260):m.end() + 200])
