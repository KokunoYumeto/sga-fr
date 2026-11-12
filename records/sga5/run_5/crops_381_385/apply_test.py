"""Apply every fix of findings_381_385.json to the batch page files in memory; print the results and brace/dollar
balance (no file is written)."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
F = json.loads((RUN / "findings_381_385.json").read_text(encoding="utf-8"))
show = "--show" in sys.argv
for p in range(381, 386):
    t = (RUN / "b381_385" / f"page_{p}.tex").read_text(encoding="utf-8")
    t0 = t
    for d in F:
        if d["page"] != p or d["fix"] is None:
            continue
        o, n = d["fix"]["old"], d["fix"]["new"]
        assert t.count(o) == 1, (p, o)
        t = t.replace(o, n)
    body = t.replace("\\{", "").replace("\\}", "").replace("\\$", "")
    print(p, "braces", body.count("{") - body.count("}"), "dollars", body.count("$") % 2,
          "| before:", t0.replace("\\{", "").replace("\\}", "").count("{") - t0.replace("\\{", "").replace("\\}", "").count("}"))
    if show:
        print(t)
