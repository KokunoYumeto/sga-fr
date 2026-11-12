"""Count some markup commands inside Exposé VII of the diplomatic s5.tex (lines 9359-11993)."""
import collections
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
p = r"C:\Users\user\Documents\sga_scan_check_20261105\sga5\diplomatic\s5.tex"
L = open(p, encoding="utf-8").read().split("\n")
seg = L[9358:11993]
pat = re.compile(r"\\(underline|emph|textit|textbf|mathbb\s*\{?[A-Za-z]|mathbf\s*\{?[A-Za-z]|mathcal\s*\{?[A-Za-z]"
                 r"|R(?![a-zA-Z])|P(?![a-zA-Z])|cO|V(?![a-zA-Z])|A(?![a-zA-Z])|wt|pmod|longmapsto|mapsto"
                 r"|item|subsection\*|subsubsection\*|begin\{statement\}|begin\{prooftext\}|text(?![a-z])|Gm|cupdot|muS)")
c = collections.Counter()
for l in seg:
    for m in pat.findall(l):
        c[re.sub(r"\s+", "", m)] += 1
for k, v in sorted(c.items(), key=lambda x: -x[1]):
    print(repr(k), v)
if len(sys.argv) > 1:
    rx = re.compile(sys.argv[1])
    for i, l in enumerate(seg, start=9359):
        if rx.search(l):
            print(i, l[:200])
