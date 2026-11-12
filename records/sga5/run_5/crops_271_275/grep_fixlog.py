"""grep_fixlog.py FIXLOG PAGE_MIN PAGE_MAX NEEDLE...: print fix-log rows whose old or new contains a needle."""
import json
import sys
sys.stdout.reconfigure(encoding="utf-8")
fn, lo, hi = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
needles = sys.argv[4:]
for line in open(fn, encoding="utf-8"):
    r = json.loads(line)
    try:
        p = int(r.get("page"))
    except (TypeError, ValueError):
        continue
    if not lo <= p <= hi:
        continue
    o, n = r.get("old") or "", r.get("new") or ""
    if any(x in o or x in n for x in needles):
        print(p, r.get("kind"), repr(o)[:160], "->", repr(n)[:160], r.get("source", ""))
