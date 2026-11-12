"""Read-only: count the proof-label forms of s5.tex (diplomatic layer) and list where \\begin{prooftext}[Preuve] stands."""
import collections
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, r"C:\Users\user\Documents\sga_scan_check_20261105")
from sga_config import MARK  # noqa: E402

t = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga5\diplomatic\s5.tex").read_text(encoding="utf-8")
lines = t.split("\n")
pat = re.compile(r"\\begin\{prooftext\}(\[[^\]]*\])?")
c = collections.Counter(m.group(1) for m in pat.finditer(t))
print(c.most_common(12))
folio = None
where = []
for i, l in enumerate(lines, 1):
    m = MARK.search(l)
    if m:
        folio = int(m.group(2))
    if r"\begin{prooftext}[Preuve]" in l:
        where.append((i, folio))
print(len(where), where)
print("emph{Preuve} :", t.count(r"\emph{Preuve} :"), " begin{proof}:", t.count(r"\begin{proof}"))
