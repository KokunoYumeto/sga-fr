"""Dry run in memory: apply the fixes of findings_166_170.json in list order to the page spans of both layers of
SGA 6 main.tex, as process_sga.py does (old unique on the page at the time of applying; misprints not replayed on
the corrected layer). Also checks brace balance of every new text. Writes nothing."""
import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
W = r"C:\Users\user\Documents\sga_scan_check_20261105\sga6"
F = json.load(open(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\findings_166_170.json", encoding="utf-8"))


def balanced(s):
    s = s.replace(r"\{", "").replace(r"\}", "")
    d = 0
    for ch in s:
        d += ch == "{"
        d -= ch == "}"
        if d < 0:
            return False
    return d == 0


for x in F:
    if x["fix"] and not balanced(x["fix"]["new"]):
        print("UNBALANCED new:", x["page"], x["fix"]["new"][:80])

for ed in ("diplomatic", "current"):
    t = open(W + "\\" + ed + "\\main.tex", encoding="utf-8").read()
    ok = n = 0
    for x in F:
        if not x["fix"]:
            continue
        if ed == "current" and x["kind"] == "misprint_in_print":
            continue
        n += 1
        ms = list(MARK.finditer(t))
        m = next(m for m in ms if int(m.group(2)) == x["page"])
        nxt = next(mm for mm in ms if mm.start() > m.start())
        s, e = m.end(), nxt.start()
        old, new = x["fix"]["old"], x["fix"]["new"]
        hits = [k for k in range(s, e) if t.startswith(old, k) and k + len(old) <= e]
        if len(hits) != 1:
            print(ed, "page", x["page"], "hits", len(hits), repr(old[:70]))
            continue
        k = hits[0]
        t = t[:k] + new + t[k + len(old):]
        ok += 1
    print(ed, "applied", ok, "of", n)
    for p in (166, 167, 168, 169, 170):
        ms = list(MARK.finditer(t))
        m = next(m for m in ms if int(m.group(2)) == p)
        nxt = next(mm for mm in ms if mm.start() > m.start())
        if ed == "diplomatic" and p in (168, 169):
            print("----", ed, p)
            print(t[m.end():nxt.start()][:1400])
