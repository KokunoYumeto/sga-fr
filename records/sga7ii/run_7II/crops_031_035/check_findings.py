import json, sys
run = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II"
d = json.load(open(run + r"\findings_031_035.json", encoding="utf-8"))
keys = {"page", "where", "scan", "tex", "kind", "confidence", "fix", "note"}
for f in d:
    src = open(run + r"\b031_035\page_%03d.tex" % f["page"], encoding="utf-8").read()
    missing = keys - set(f)
    ok_tex = src.count(f["tex"])
    fix = f["fix"]
    n_old = src.count(fix["old"]) if fix else None
    mis = f["kind"] == "misprint_in_print"
    print(f["page"], f["kind"], f["confidence"], "tex_count=%d" % ok_tex, "old_count=%s" % n_old,
          "corrected" if "corrected" in f else "-", "missing=%s" % sorted(missing) if missing else "")
    assert ok_tex >= 1
    assert fix is None or n_old == 1
    assert (not mis) or ("corrected" in f)
print(len(d), "findings OK")
