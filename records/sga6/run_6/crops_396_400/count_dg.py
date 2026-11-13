"""Count plain D( / D_ and G_S / G^ in Exposé VI of the diplomatic main.tex, per folio (read only)."""
import collections
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
t = (ROOT / "diplomatic" / "main.tex").read_text(encoding="utf-8").split("\n")
start = next(i for i, l in enumerate(t) if "Exposé VI}" in l and "section" in l)
end = next((i for i in range(start + 1, len(t)) if "Exposé VII" in t[i] and "section" in t[i]), len(t))
print("Exposé VI lines", start + 1, "-", end)
pat_D = re.compile(r"(?<![A-Za-z\\])D(?=[(_])")
pat_bD = re.compile(r"\\mathbf\s*\{?D")
pat_G = re.compile(r"(?<![A-Za-z\\])G(?=_S|\^\{?n)")
pat_P = re.compile(r"\\mathbb\s*\{?P")
cD, cG, cP, cbD = (collections.Counter() for _ in range(4))
folio = None
for i in range(start, end):
    m = re.match(r"%%%%%%%%%%  scan idx \d+  \|  folio (\d+)", t[i])
    if m:
        folio = int(m.group(1))
        continue
    cD[folio] += len(pat_D.findall(t[i]))
    cG[folio] += len(pat_G.findall(t[i]))
    cP[folio] += len(pat_P.findall(t[i]))
    cbD[folio] += len(pat_bD.findall(t[i]))
for name, c in (("plain D", cD), ("mathbf D", cbD), ("plain G", cG), ("mathbb P", cP)):
    print(name, {k: v for k, v in sorted(c.items(), key=lambda kv: (kv[0] or 0)) if v})
