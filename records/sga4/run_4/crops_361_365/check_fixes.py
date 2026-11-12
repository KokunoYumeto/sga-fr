import json
import pathlib

run = pathlib.Path(r"C:/Users/user/Documents/sga_scan_check_20261105/run_4")
data = json.loads((run / "findings_361_365.json").read_text(encoding="utf-8"))
ok = True
for i, f in enumerate(data):
    for k in ("page", "where", "scan", "tex", "kind", "confidence", "fix", "note"):
        if k not in f:
            print("missing key", k, "in finding", i)
            ok = False
    if f["kind"] == "misprint_in_print":
        if f["fix"] is not None or "corrected" not in f:
            print("misprint format problem in finding", i)
            ok = False
    elif "corrected" in f:
        print("corrected on a non-misprint, finding", i)
        ok = False
    fix = f["fix"]
    if fix:
        raw = (run / "b361_365" / ("page_%d.tex" % f["page"])).read_bytes()
        if b"\r" in raw:
            print("CR found in page", f["page"])
        txt = raw.decode("utf-8")
        first = txt.split("\n", 1)[0]
        n = txt.count(fix["old"])
        print(f["page"], repr(fix["old"]), "->", repr(fix["new"]), "count", n, "in first line:", fix["old"] in first)
        if n != 1 or fix["old"] in first:
            ok = False
    for k, v in f.items():
        vals = [v] if isinstance(v, str) else (list(v.values()) if isinstance(v, dict) else [])
        for s in vals:
            if any(ord(c) < 32 and c != "\n" for c in s):
                print("control character in finding", i, "field", k)
                ok = False
    if f.get("corrected"):
        print(f["page"], "corrected:", repr(f["corrected"]))
print("OK" if ok else "PROBLEMS", len(data), "findings")
