"""Simulate marker_split_word.py VOL FOLIO split HEAD TAIL in memory on both SGA 6 layers; writes nothing."""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
folio, head, tail = int(sys.argv[1]), sys.argv[2], sys.argv[3]
for edition in ("diplomatic", "current"):
    t = (W / "sga6" / edition / "main.tex").read_text(encoding="utf-8")
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    ls = t.rfind("\n", 0, m.start()) + 1
    le = t.find("\n", m.end()) + 1
    if not t.startswith(head + tail, le):
        print(edition, "text after the marker does not begin with", repr(head + tail))
        continue
    t2 = t[:ls] + head + "%\n" + t[ls:le] + t[le + len(head):]
    j = t2.find(m.group(0))
    print("==", edition)
    print(t2[max(0, j - 120):j + len(m.group(0)) + 80])
    print()
