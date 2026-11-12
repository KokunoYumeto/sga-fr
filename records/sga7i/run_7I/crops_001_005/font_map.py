"""Count \\mathbb / \\mathbf for Z, Q, F per printed page of a diplomatic SGA 7 I file (read-only)."""
import re
import sys
from collections import defaultdict

path = sys.argv[1]
t = open(path, encoding="utf-8").read()
marks = [(m.start(), int(m.group(2))) for m in
         re.finditer(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%", t)]


def folio(pos):
    f = None
    for s, fo in marks:
        if s <= pos:
            f = fo
    return f


d = defaultdict(lambda: defaultdict(int))
for m in re.finditer(r"\\math(bb|bf)\{([ZQF])\}", t):
    d[folio(m.start())][m.group(1) + m.group(2)] += 1
for k in sorted(d, key=lambda x: (x is None, x or 0)):
    print(k, dict(d[k]))
