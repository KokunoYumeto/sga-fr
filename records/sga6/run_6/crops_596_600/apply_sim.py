import json, pathlib
RUN = pathlib.Path(r"C:/Users/user/Documents/sga_scan_check_20261105/run_6")
F = json.loads((RUN / "findings_596_600.json").read_text(encoding="utf-8"))
for p in (596, 597, 598, 599, 600):
    t = (RUN / "b596_600" / ("page_%03d.tex" % p)).read_text(encoding="utf-8")
    for d in F:
        if d["page"] == p and d["fix"]:
            assert t.count(d["fix"]["old"]) == 1, (p, d["fix"]["old"])
            t = t.replace(d["fix"]["old"], d["fix"]["new"])
    out = RUN / "crops_596_600" / ("sim_%03d.tex" % p)
    out.write_text(t, encoding="utf-8")
    print("page", p, "ok")
