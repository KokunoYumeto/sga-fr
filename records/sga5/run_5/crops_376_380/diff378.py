import difflib
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")


def span(t, folio):
    ms = list(MARK.finditer(t))
    for i, m in enumerate(ms):
        if int(m.group(2)) == folio:
            end = ms[i + 1].start() if i + 1 < len(ms) else len(t)
            return t[m.start():end]


folio = int(sys.argv[1])
a = span((W / "sga5" / "diplomatic" / "s5.tex").read_text(encoding="utf-8"), folio)
b = span((W / "sga5" / "current" / "s5.tex").read_text(encoding="utf-8"), folio)
for op in difflib.SequenceMatcher(None, a, b).get_opcodes():
    if op[0] != "equal":
        i1, i2, j1, j2 = op[1:]
        print(op[0], repr(a[max(0, i1 - 30):i2 + 30]), "->", repr(b[max(0, j1 - 30):j2 + 30]))
