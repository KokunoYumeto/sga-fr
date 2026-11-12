"""Check findings_466_470.json: each fix's old occurs exactly once in its page_NNN.tex, does not touch the marker line,
olds of one page do not overlap, misprint entries carry 'corrected', and applying all fixes leaves each old's
replacement in place (simulation in memory only)."""
import json
import sys
from collections import Counter
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
RUN = Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
F = json.loads((RUN / "findings_466_470.json").read_text(encoding="utf-8"))
keys = {"page", "where", "scan", "tex", "kind", "confidence", "fix", "note"}
kinds = {"word", "formula", "symbol", "font", "underline", "missing", "extra", "number", "punctuation", "accent",
         "misprint_in_print", "marker", "other"}
ok = True
spans = {}
texts = {}
for i, x in enumerate(F):
    if not keys <= set(x) or x["kind"] not in kinds or x["confidence"] not in ("high", "medium", "low"):
        print(i, "BAD FIELDS", x.get("kind"), x.get("confidence")); ok = False
    if x["kind"] == "misprint_in_print" and "corrected" not in x:
        print(i, "misprint without corrected"); ok = False
    if x["kind"] != "misprint_in_print" and "corrected" in x:
        print(i, "corrected on non-misprint"); ok = False
    fx = x["fix"]
    if fx is None:
        continue
    n = x["page"]
    b = (n - 1) // 5 * 5 + 1
    p = RUN / f"b{b:03d}_{b + 4:03d}" / f"page_{n:03d}.tex"
    t = texts.setdefault(n, p.read_text(encoding="utf-8"))
    c = t.count(fx["old"])
    if c != 1:
        print(i, n, "OLD COUNT", c, repr(fx["old"][:80])); ok = False
        continue
    if "%%%%%%%%%%" in fx["old"] or "%%%%%%%%%%" in fx["new"]:
        print(i, n, "touches marker"); ok = False
    if fx["old"] == fx["new"]:
        print(i, n, "old == new"); ok = False
    k = t.index(fx["old"])
    spans.setdefault(n, []).append((k, k + len(fx["old"]), i))
for n, sp in spans.items():
    sp.sort()
    for a, b2 in zip(sp, sp[1:]):
        if b2[0] < a[1]:
            print("OVERLAP on page", n, "findings", a[2], b2[2]); ok = False
# apply all fixes per page in memory (in list order) and confirm each replacement lands
for n, t in texts.items():
    for i, x in enumerate(F):
        if x["page"] == n and x["fix"]:
            assert t.count(x["fix"]["old"]) == 1, (n, i)
            t = t.replace(x["fix"]["old"], x["fix"]["new"], 1)
    print("page", n, "all fixes apply in sequence; \\R left:", t.count("\\R^"), "| \\R\\Gamma left:", t.count("\\R\\Gamma"))
cnt = Counter((x["page"], x["kind"] == "misprint_in_print") for x in F)
for n in sorted({x["page"] for x in F}):
    print(n, "normal", cnt[(n, False)], "misprint", cnt[(n, True)])
print("kinds:", Counter(x["kind"] for x in F))
print("ALL OK" if ok else "PROBLEMS")
