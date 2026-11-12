"""In memory only: apply the fixes of findings_031_035.json in order to each page file (each old must still occur
exactly once), check the $ and brace balance of each page afterwards, and count every non-misprint old in the
same page of both layers of main.tex (pages cut at the markers).
usage: python -I check_apply.py"""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
SGA6 = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
F = json.loads((RUN / "findings_031_035.json").read_text(encoding="utf-8"))


def layer_pages(edition):
    t = (SGA6 / edition / "main.tex").read_text(encoding="utf-8")
    ms = list(MARK.finditer(t))
    out = {}
    for i, m in enumerate(ms):
        end = ms[i + 1].start() if i + 1 < len(ms) else len(t)
        out[int(m.group(2))] = t[m.start():end]
    return out


layers = {e: layer_pages(e) for e in ("diplomatic", "current")}
pages = {p: (RUN / "b031_035" / f"page_{p:03d}.tex").read_text(encoding="utf-8") for p in range(31, 36)}
for i, f in enumerate(F):
    if not f["fix"]:
        continue
    p, old, new = f["page"], f["fix"]["old"], f["fix"]["new"]
    c = pages[p].count(old)
    assert c == 1, (i, p, c)
    pages[p] = pages[p].replace(old, new)
    counts = {e: layers[e][p].count(old) for e in layers}
    flag = "" if f["kind"] == "misprint_in_print" or counts["current"] == 1 else "  <-- corrected layer differs"
    print(f"#{i} p{p} {f['kind']:18} diplomatic={counts['diplomatic']} current={counts['current']}{flag}")
for p, t in pages.items():
    body = "\n".join(line for line in t.split("\n") if not line.startswith("%"))
    dollars = len(re.findall(r"(?<!\\)\$", body))
    print(f"p{p}: braces {body.count('{') - body.count('}')}, dollars {dollars} ({'even' if dollars % 2 == 0 else 'ODD'})")
