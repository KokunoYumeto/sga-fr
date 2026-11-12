"""Count \\overset{\\mathbf L}{\\otimes} and \\R per folio in Exposé III of the diplomatic s5.tex (read only)."""
import re
from collections import Counter

path = r"C:\Users\user\Documents\sga_scan_check_20261105\sga5\diplomatic\s5.tex"
lines = open(path, encoding="utf-8").read().split("\n")
mark = re.compile(r"scan idx \d+  \|  folio (\d+)")
folio = None
bold, rmac = Counter(), Counter()
for n, line in enumerate(lines, 1):
    m = mark.search(line)
    if m:
        folio = int(m.group(1))
        continue
    if 1925 <= n <= 4370:
        bold[folio] += line.count(r"\overset{\mathbf L}{\otimes}")
        rmac[folio] += len(re.findall(r"\\R(?![A-Za-z])", line))
print("bold L per folio:", sorted((k, v) for k, v in bold.items() if v), sum(bold.values()))
print("\\R per folio:", sorted((k, v) for k, v in rmac.items() if v), sum(rmac.values()))
