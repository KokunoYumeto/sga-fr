import json

run = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II"
d = json.load(open(run + r"\findings_036_040.json", encoding="utf-8"))
keys = {"page", "where", "scan", "tex", "kind", "confidence", "fix", "note"}
kinds = {"word", "formula", "symbol", "font", "underline", "missing", "extra", "number",
         "punctuation", "accent", "misprint_in_print", "marker", "other"}
for f in d:
    src = open(run + r"\b036_040\page_%03d.tex" % f["page"], encoding="utf-8").read()
    assert "\r" not in src
    missing = keys - set(f)
    ok_tex = src.count(f["tex"])
    fix = f["fix"]
    n_old = src.count(fix["old"]) if fix else None
    mis = f["kind"] == "misprint_in_print"
    print(f["page"], f["kind"], f["confidence"], "tex_count=%d" % ok_tex, "old_count=%s" % n_old,
          "corrected" if "corrected" in f else "-", "missing=%s" % sorted(missing) if missing else "")
    assert not missing
    assert f["kind"] in kinds
    assert ok_tex >= 1
    assert fix is None or n_old == 1
    if fix:
        assert "%%%%%%%%%%" not in fix["old"]
    assert mis == ("corrected" in f)
# simulate applying all fixes per page, in order, each old still unique at its turn
for p in sorted({f["page"] for f in d}):
    src = open(run + r"\b036_040\page_%03d.tex" % p, encoding="utf-8").read()
    for f in d:
        if f["page"] == p and f["fix"]:
            assert src.count(f["fix"]["old"]) == 1, (p, f["fix"]["old"])
            src = src.replace(f["fix"]["old"], f["fix"]["new"])
print(len(d), "findings OK")
