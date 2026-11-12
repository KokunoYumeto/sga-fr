"""Read-only: count notation occurrences in the diplomatic s5.tex, with folios, near pages 80-100."""
import collections
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
t = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga5\diplomatic\s5.tex").read_text(encoding="utf-8")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
ms = list(MARK.finditer(t))


def folio(pos):
    f = None
    for m in ms:
        if m.start() <= pos:
            f = int(m.group(2))
        else:
            break
    return f


pats = sys.argv[1:]
for pat in pats:
    hits = [(folio(m.start()), t.count("\n", 0, m.start()) + 1, t[m.start():m.start() + 80].replace("\n", " "))
            for m in re.finditer(pat, t)]
    near = [h for h in hits if h[0] and 76 <= h[0] <= 100]
    print("PATTERN", pat, "total", len(hits), "near 76-100:", len(near))
    for h in hits[:3]:
        print("   first:", h)
    for h in near[:25]:
        print("   near:", h)
