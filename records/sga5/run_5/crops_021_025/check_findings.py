"""Check findings_021_025.json against the page files (read only):
- every fix's "old" occurs exactly once in its page_NNN.tex, applying the page's earlier fixes first (list order,
  as process_sga.py does), and also once in the original page file when it does not depend on an earlier fix;
- no old/new touches a marker line; misprints carry "corrected"; kinds are from the allowed list;
- a dry run of process_sga.py's page lookup on the live s5.tex (both layers): each old occurs once in the page span.
usage: python -I check_findings.py"""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).parent
RUN = HERE.parent
W = RUN.parent
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
KINDS = {"word", "formula", "symbol", "font", "underline", "missing", "extra", "number", "punctuation", "accent",
         "misprint_in_print", "marker", "other"}
items = json.loads((RUN / "findings_021_025.json").read_text(encoding="utf-8"))
pages = {n: (RUN / "b021_025" / f"page_{n:03d}.tex").read_text(encoding="utf-8") for n in range(21, 26)}
cur = dict(pages)
ok = True
counts = {}
for i, x in enumerate(items):
    assert x["kind"] in KINDS, x["kind"]
    assert x["confidence"] in ("high", "medium", "low")
    p = int(x["page"])
    mis = x["kind"] == "misprint_in_print"
    counts.setdefault(p, [0, 0])[1 if mis else 0] += 1
    if mis:
        assert x.get("corrected"), f"#{i} misprint without corrected"
    elif "corrected" in x:
        print(f"#{i} WARN corrected on a non-misprint")
    fix = x.get("fix")
    if not fix:
        continue
    old, new = fix["old"], fix["new"]
    if MARK.search(old) or MARK.search(new):
        print(f"#{i} TOUCHES MARKER"); ok = False
    n_now = cur[p].count(old)
    n_orig = pages[p].count(old)
    print(f"#{i} p{p} {x['kind']}: old x{n_now} (original file x{n_orig})  {old[:60]!r}")
    if n_now != 1:
        ok = False
        print("   *** not unique in the current page text")
    cur[p] = cur[p].replace(old, new, 1)
print("counts (normal/misprint):", {k: tuple(v) for k, v in sorted(counts.items())})

# live s5.tex: the same lookup as process_sga.py (page span from marker to next marker), sequential per layer
sys.path.insert(0, str(W))
from sga_config import pages as live_pages  # noqa: E402

for edition in ("diplomatic", "current"):
    spans = live_pages("5", edition)
    texts = {}
    for x in items:
        fix = x.get("fix")
        if not fix:
            continue
        if edition == "current" and x["kind"] == "misprint_in_print":
            continue
        p = int(x["page"])
        f, s, e = spans[p][0]
        key = (f, p)
        if key not in texts:
            texts[key] = f.read_text(encoding="utf-8")[s:e]
        n = texts[key].count(fix["old"])
        if n != 1:
            ok = False
            print(f"LIVE {edition} p{p}: old occurs {n} times: {fix['old'][:60]!r}")
        texts[key] = texts[key].replace(fix["old"], fix["new"], 1)
    print(f"live {edition}: checked")
print("ALL OK" if ok else "PROBLEMS")
