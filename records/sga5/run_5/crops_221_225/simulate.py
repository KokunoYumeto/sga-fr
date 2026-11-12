import json, pathlib, sys
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
L = json.loads((RUN / "findings_221_225.json").read_text(encoding="utf-8"))
p = int(sys.argv[1])
t = (RUN / "b221_225" / f"page_{p:03d}.tex").read_text(encoding="utf-8")
for x in L:
    if x["page"] == p and x["fix"]:
        o, n = x["fix"]["old"], x["fix"]["new"]
        assert t.count(o) == 1, o
        t = t.replace(o, n)
print(t)
