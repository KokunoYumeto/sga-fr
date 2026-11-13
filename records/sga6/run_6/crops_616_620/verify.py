import json, pathlib, sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
B = RUN / "b616_620"
data = json.loads((RUN / "findings_616_620.json").read_text(encoding="utf-8"))
ok = True
keys = {"page", "where", "scan", "tex", "kind", "confidence", "fix", "note"}
kinds = {"word", "formula", "symbol", "font", "underline", "missing", "extra", "number",
         "punctuation", "accent", "misprint_in_print", "marker", "other"}
for i, f in enumerate(data):
    missing = keys - set(f)
    if missing:
        print(i, "missing keys", missing); ok = False
    if f["kind"] not in kinds:
        print(i, "bad kind", f["kind"]); ok = False
    if f["confidence"] not in {"high", "medium", "low"}:
        print(i, "bad confidence"); ok = False
    if (f["kind"] == "misprint_in_print") != ("corrected" in f):
        print(i, "corrected field mismatch"); ok = False
    text = (B / f"page_{f['page']}.tex").read_text(encoding="utf-8")
    if f["fix"] is not None:
        old, new = f["fix"]["old"], f["fix"]["new"]
        n = text.count(old)
        marker_hit = "%%%%%%%%%%" in old
        print(f"{i:2d} p{f['page']} count={n} marker={marker_hit} | OLD: {old}")
        print(f"            NEW: {new}")
        if n != 1 or marker_hit:
            ok = False
    else:
        # sanity: the quoted TeX of a null-fix entry should be on the page (first clause only)
        t = f["tex"].split(" (")[0].split(": ")[0]
        print(f"{i:2d} p{f['page']} null fix; tex on page: {t in text} | {t}")
print("ALL OK" if ok else "PROBLEMS")
