import re
import sys
import collections

# usage: grep_main.py <patterns_file> [max_examples]
# patterns_file: one regex per line (raw, no shell escaping)
path = r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex"
t = open(path, encoding="utf-8").read()
pats = [l.rstrip("\n") for l in open(sys.argv[1], encoding="utf-8") if l.strip()]
mx = int(sys.argv[2]) if len(sys.argv) > 2 else 0
marks = [(m.start(), m.group(2)) for m in re.finditer(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)", t)]


def folio_of(pos):
    f = None
    for s, fo in marks:
        if s < pos:
            f = fo
        else:
            break
    return f


for p in pats:
    pat = re.compile(p)
    print("==== pattern:", p)
    ms = list(pat.finditer(t))
    c = collections.Counter(m.group(0) for m in ms)
    for k, v in c.most_common(25):
        print(v, repr(k))
    if mx:
        step = max(1, len(ms) // mx)
        for m in ms[::step][:mx]:
            print("  folio", folio_of(m.start()), ":", repr(t[max(0, m.start() - 50):m.end() + 50]))
