import json, pathlib, sys
sys.stdout.reconfigure(encoding='utf-8')
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
F = json.loads((RUN / "findings_526_530.json").read_text(encoding="utf-8"))
KINDS = {"word", "formula", "symbol", "font", "underline", "missing", "extra", "number", "punctuation", "accent",
         "misprint_in_print", "marker", "other"}
bad = 0
for i, f in enumerate(F):
    assert f["kind"] in KINDS, f
    assert f["confidence"] in ("high", "medium", "low"), f
    assert ("corrected" in f) == (f["kind"] == "misprint_in_print"), f
    fx = f["fix"]
    if fx is None:
        continue
    t = (RUN / "b526_530" / f"page_{f['page']}.tex").read_text(encoding="utf-8")
    n = t.count(fx["old"])
    marker = "%%%%%%%%%%" in fx["old"] or "%%%%%%%%%%" in fx["new"]
    if n != 1 or marker or fx["old"] == fx["new"]:
        bad += 1
    print(i, f["page"], f["kind"], "count", n, "marker" if marker else "", repr(fx["old"][:50]))
print("entries", len(F), "bad", bad)
