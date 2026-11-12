"""Validate findings_386_390.json: JSON loads, required keys, each fix 'old' occurs exactly once in its page file,
misprints carry 'corrected'; also apply all fixes per page in memory to check that no edit destroys another's anchor."""
import json, pathlib, sys
sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
d = json.loads((RUN / "findings_386_390.json").read_text(encoding="utf-8"))
keys = {"page", "where", "scan", "tex", "kind", "confidence", "fix", "note"}
kinds = {"word", "formula", "symbol", "font", "underline", "missing", "extra", "number", "punctuation", "accent",
         "misprint_in_print", "marker", "other"}
pages = {}
ok = True
counts = {}
for n, x in enumerate(d):
    miss = keys - set(x)
    if miss:
        print(n, "missing keys", miss); ok = False
    if x["kind"] not in kinds:
        print(n, "bad kind", x["kind"]); ok = False
    if x["confidence"] not in ("high", "medium", "low"):
        print(n, "bad confidence"); ok = False
    if x["kind"] == "misprint_in_print" and "corrected" not in x:
        print(n, "misprint without corrected"); ok = False
    if x["kind"] != "misprint_in_print" and "corrected" in x:
        print(n, "corrected on non-misprint"); ok = False
    p = x["page"]
    c = counts.setdefault(p, [0, 0])
    c[1 if x["kind"] == "misprint_in_print" else 0] += 1
    if p not in pages:
        pages[p] = (RUN / "b386_390" / f"page_{p}.tex").read_text(encoding="utf-8")
    f = x["fix"]
    if f is not None:
        k = pages[p].count(f["old"])
        if k != 1:
            print(n, "page", p, "old occurs", k, "times:", repr(f["old"])); ok = False
        if "%%%%%%%%%%" in f["old"] or "%%%%%%%%%%" in f["new"]:
            print(n, "touches a marker line"); ok = False
# apply all fixes of each page in order and in reverse order, checking that every old is still found exactly once
for order in ("forward", "reverse"):
    texts = dict(pages)
    seq = d if order == "forward" else list(reversed(d))
    for n, x in enumerate(seq):
        f = x["fix"]
        if f is None:
            continue
        t = texts[x["page"]]
        if t.count(f["old"]) != 1:
            print(order, "page", x["page"], "anchor lost or doubled:", repr(f["old"])); ok = False
            continue
        texts[x["page"]] = t.replace(f["old"], f["new"])
print("entries", len(d), "counts (normal/misprint):", {p: tuple(v) for p, v in sorted(counts.items())})
print("ALL OK" if ok else "PROBLEMS")
