import json, pathlib, sys
sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
F = json.loads((RUN / "findings_036_040.json").read_text(encoding="utf-8"))
for p in range(36, 41):
    t = (RUN / "b036_040" / f"page_{p:03d}.tex").read_text(encoding="utf-8")
    for d in F:
        if d["page"] == p and d["fix"]:
            o, n = d["fix"]["old"], d["fix"]["new"]
            assert t.count(o) == 1, (p, o, t.count(o))
            t = t.replace(o, n)
    print(f"===== page {p} (all fixes applied)")
    print(t)
