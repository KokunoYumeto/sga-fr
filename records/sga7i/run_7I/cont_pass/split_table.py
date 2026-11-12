"""Compact table: for every CONT>> (incl. the \\mathrm{CONT{>}{>}} variant) the last 40 characters before it and for
every <<CONT the first 40 characters after it, in file order, with folio (read-only).

usage: python -I split_table.py FILE
"""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
TAG = re.compile(r"CONT>>|<<CONT|CONT\{>\}\{>\}")
t = open(sys.argv[1], encoding="utf-8", newline="").read()
marks = [(m.start(), int(m.group(2))) for m in MARK.finditer(t)]


def folio_at(pos):
    f = None
    for s, fo in marks:
        if s > pos:
            break
        f = fo
    return f


for n, m in enumerate(TAG.finditer(t)):
    k = m.group(0)
    p = m.start()
    if k.startswith("<<"):
        ctx = t[m.end():m.end() + 45]
        print(f"{n:3d} {folio_at(p)} {k:16s}          >>> {ctx!r}")
    else:
        ctx = t[max(0, p - 45):p]
        print(f"{n:3d} {folio_at(p)} {k:16s} {ctx!r} <<<")
