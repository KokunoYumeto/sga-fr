"""List the occurrences of a regular expression in a TeX file with the folio of the page marker before each.
usage: python -I grep_folio.py FILE REGEX [MAX]"""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
t = open(sys.argv[1], encoding="utf-8").read()
pat = re.compile(sys.argv[2])
mx = int(sys.argv[3]) if len(sys.argv) > 3 else 60
marks = [(m.start(), int(m.group(2))) for m in MARK.finditer(t)]


def folio(pos):
    f = None
    for s, fo in marks:
        if s < pos:
            f = fo
        else:
            break
    return f


n = 0
for m in pat.finditer(t):
    n += 1
    if n <= mx:
        print(folio(m.start()), repr(t[max(0, m.start() - 40):m.end() + 30]))
print("total:", n)
