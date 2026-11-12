"""Check findings_136_140.json: JSON syntax, fields, kinds, and that every fix's old occurs exactly once
in its page file (also after the earlier fixes of the same page are applied in list order)."""
import json
import pathlib
import re

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
F = RUN / "findings_136_140.json"
KINDS = {"word", "formula", "symbol", "font", "underline", "missing", "extra", "number", "punctuation", "accent",
         "misprint_in_print", "marker", "other"}
FIELDS = {"page", "where", "scan", "tex", "kind", "confidence", "fix", "note"}
CTRL = re.compile(r"[\x00-\x09\x0b-\x1f]")

data = json.loads(F.read_text(encoding="utf-8"))
print("findings:", len(data))


def page_file(p):
    if 136 <= p <= 140:
        return RUN / "b136_140" / f"page_{p:03d}.tex"
    lo = (p - 1) // 5 * 5 + 1
    return RUN / f"b{lo:03d}_{lo + 4:03d}" / f"page_{p:03d}.tex"


texts = {}
ok = True
for i, f in enumerate(data):
    missing = FIELDS - set(f)
    if missing:
        print(i, "missing fields", missing); ok = False
    if f["kind"] not in KINDS:
        print(i, "bad kind", f["kind"]); ok = False
    if f["confidence"] not in {"high", "medium", "low"}:
        print(i, "bad confidence"); ok = False
    if ("corrected" in f) != (f["kind"] == "misprint_in_print"):
        print(i, "corrected field mismatch"); ok = False
    for k in ("where", "scan", "tex", "note") + (("corrected",) if "corrected" in f else ()):
        if CTRL.search(f[k] or ""):
            print(i, "control character in", k); ok = False
    fx = f["fix"]
    if fx is None:
        continue
    p = f["page"]
    if p not in texts:
        raw = page_file(p).read_bytes()
        if b"\r" in raw:
            print(p, "file has CR")
        texts[p] = raw.decode("utf-8")
    t = texts[p]
    old, new = fx["old"], fx["new"]
    for k, s in (("old", old), ("new", new)):
        if CTRL.search(s):
            print(i, "control character in fix", k, repr(s)); ok = False
    if "%%%%%%%%%%" in old or "%%%%%%%%%%" in new:
        print(i, "old/new touches a marker line"); ok = False
    n0 = page_file(p).read_text(encoding="utf-8").count(old)
    n = t.count(old)
    status = "ok" if (n0 == 1 and n == 1) else "PROBLEM"
    if status != "ok":
        ok = False
    print(f"{i:2d} p{p} {f['kind']:<17} count(original)={n0} count(sequential)={n} {status} | {old[:60]!r}")
    if n == 1:
        texts[p] = t.replace(old, new, 1)
print("ALL OK" if ok else "PROBLEMS FOUND")
