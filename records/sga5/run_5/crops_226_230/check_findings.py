"""Check findings_226_230.json: each old occurs exactly once in its page file, olds of a page are disjoint,
the fixes apply in order; print the patched pages; report olds that do not occur once in the corrected layer."""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
run = Path(__file__).resolve().parents[1]
root = run.parent
F = json.loads((run / "findings_226_230.json").read_text(encoding="utf-8"))
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
cur = (root / "sga5" / "current" / "s5.tex").read_text(encoding="utf-8")
ms = list(MARK.finditer(cur))


def cur_page(folio):
    for i, m in enumerate(ms):
        if int(m.group(2)) == folio:
            return cur[m.start():ms[i + 1].start()]


ok = True
keys = {"page", "where", "scan", "tex", "kind", "confidence", "fix", "note"}
kinds = {"word", "formula", "symbol", "font", "underline", "missing", "extra", "number", "punctuation", "accent",
         "misprint_in_print", "marker", "other"}
for f in F:
    if not keys <= set(f) or f["kind"] not in kinds or f["confidence"] not in ("high", "medium", "low"):
        print("BAD RECORD", f)
        ok = False
    if f["kind"] == "misprint_in_print" and "corrected" not in f:
        print("MISSING corrected", f["where"])
        ok = False
pages = sorted({f["page"] for f in F})
for p in pages:
    t = (run / "b226_230" / f"page_{p}.tex").read_text(encoding="utf-8")
    assert "\r" not in t
    spans = []
    for f in F:
        if f["page"] != p or not f["fix"]:
            continue
        old = f["fix"]["old"]
        n = t.count(old)
        if n != 1:
            print(p, "COUNT", n, repr(old[:60]))
            ok = False
            continue
        if MARK.search(old) or MARK.search(f["fix"]["new"]):
            print(p, "MARKER IN FIX", repr(old[:60]))
            ok = False
        k = t.find(old)
        spans.append((k, k + len(old), old))
        c = cur_page(p)
        if c is None or c.count(old) != 1:
            print(p, "corrected layer: old occurs", None if c is None else c.count(old), "times:", repr(old[:70]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if a[1] > b[0]:
            print(p, "OVERLAP", repr(a[2][:40]), repr(b[2][:40]))
            ok = False
    # apply in list order
    u = t
    for f in F:
        if f["page"] == p and f["fix"]:
            assert u.count(f["fix"]["old"]) == 1, (p, f["fix"]["old"][:50])
            u = u.replace(f["fix"]["old"], f["fix"]["new"], 1)
    out = Path(__file__).resolve().parent / f"patched_{p}.tex"
    out.write_text(u, encoding="utf-8", newline="")
    print(p, "applied", sum(1 for f in F if f["page"] == p and f["fix"]), "fixes ->", out.name,
          "| braces", u.count("{") - u.count("}"), "| emph", u.count("\\emph{"))
print("ALL OK" if ok else "PROBLEMS")
from collections import Counter
c = Counter((f["page"], f["kind"] == "misprint_in_print") for f in F)
print({p: (c[(p, False)], c[(p, True)]) for p in pages})
