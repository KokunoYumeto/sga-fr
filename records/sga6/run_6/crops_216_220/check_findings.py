"""Check findings_216_220.json: valid JSON, each fix's old occurs exactly once in its page file, no marker lines,
no overlapping fixes on a page, misprints carry 'corrected'; print counts per page."""
import json
import pathlib
import re
import sys

run = pathlib.Path(sys.argv[1])
data = json.loads((run / "findings_216_220.json").read_text(encoding="utf-8"))
MARK = re.compile(r"%%%%%%%%%%  scan idx")
counts = {}
spans = {}
ok = True
for i, x in enumerate(data):
    p = x["page"]
    n, m = counts.get(p, (0, 0))
    counts[p] = (n, m + 1) if x["kind"] == "misprint_in_print" else (n + 1, m)
    for key in ("page", "where", "scan", "tex", "kind", "confidence", "fix", "note"):
        if key not in x:
            print("missing key", key, i); ok = False
    if x["kind"] == "misprint_in_print" and not x.get("corrected"):
        print("misprint without corrected", i); ok = False
    if x["kind"] != "misprint_in_print" and "corrected" in x:
        print("corrected on non-misprint", i); ok = False
    fx = x["fix"]
    if not fx:
        continue
    t = (run / "b216_220" / f"page_{p}.tex").read_text(encoding="utf-8")
    old, new = fx["old"], fx["new"]
    c = t.count(old)
    if c != 1:
        print("COUNT", c, p, repr(old)); ok = False
    if MARK.search(old) or MARK.search(new):
        print("marker in fix", i); ok = False
    k = t.find(old)
    for (a, b, j) in spans.get(p, []):
        if k < b and a < k + len(old):
            print("overlap", i, j); ok = False
    spans.setdefault(p, []).append((k, k + len(old), i))
print("ok" if ok else "PROBLEMS", len(data), "findings")
for p in sorted(counts):
    print(p, "%d/%d" % counts[p])
