"""Counts in Exposé VI of the diplomatic layer (read only)."""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
t = open(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex", encoding="utf-8").read().split("\n")
start = [i for i, l in enumerate(t) if "folio 365 " in l][0]
ends = [i for i, l in enumerate(t) if i > start + 2 and l.startswith("\\section*{Expos")]
end = ends[0] if ends else len(t)
print("Exposé VI lines", start + 1, end, "next heading:", t[end][:80] if end < len(t) else None)
seg = t[start:end]
for pat in (r"\cdots", r"\ldots", r"\underline", r"\emph", r"\textbf{Lemme", r"\textbf{Proposition", r"\textbf{Th"):
    print(pat, sum(l.count(pat) for l in seg))
arrow = re.compile(r"(longrightarrow|\\to|rightarrow)\s*\\cdots")
print("arrow-then-cdots", sum(len(arrow.findall(l)) for l in seg))
# folios of \cdots uses
folio = None
hits = {}
for l in seg:
    m = re.search(r"folio (\d+)", l)
    if m and l.startswith("%%%%"):
        folio = int(m.group(1))
    if r"\cdots" in l:
        hits[folio] = hits.get(folio, 0) + l.count(r"\cdots")
print("cdots by folio", hits)
