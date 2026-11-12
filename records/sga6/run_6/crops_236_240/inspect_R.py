"""List the derived-functor R forms used in the TeX of Exposé III (folios 221-273)."""
import re
from collections import Counter

W = r"C:\Users\user\Documents\sga_scan_check_20261105"
t = open(W + r"\sga6\diplomatic\main.tex", encoding="utf-8").read()
ms = list(re.finditer(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%", t))
pat = re.compile(r"(\\mathbf ?\{?R\}?|\\mathrm ?\{?R\}?|\\mathbb ?\{?R\}?|\\R(?![a-zA-Z])|(?<![\\a-zA-Z])R(?=[a-z\\]|\^?\{?[a-z]|_))")
for i, m in enumerate(ms):
    f = int(m.group(2))
    if 221 <= f <= 273:
        end = ms[i + 1].start() if i + 1 < len(ms) else len(t)
        seg = t[m.start():end]
        c = Counter()
        ex = {}
        for h in pat.finditer(seg):
            k = h.group(1)
            c[k] += 1
            ex.setdefault(k, seg[max(0, h.start() - 10):h.end() + 12].replace("\n", " "))
        if c:
            print(f, dict(c), " | ".join(ex.values())[:240])
