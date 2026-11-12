import json, sys, pathlib
sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
d = json.loads((RUN / "findings_306_310.json").read_text(encoding="utf-8"))
keys = {"page", "where", "scan", "tex", "kind", "confidence", "fix", "note"}
kinds = {"word", "formula", "symbol", "font", "underline", "missing", "extra", "number", "punctuation", "accent",
         "misprint_in_print", "marker", "other"}
problems = 0
texts = {p: (RUN / "b306_310" / f"page_{p}.tex").read_text(encoding="utf-8") for p in range(306, 311)}
seq = dict(texts)
for i, f in enumerate(d):
    miss = keys - set(f)
    if miss: print("missing keys", i, miss); problems += 1
    if f["kind"] not in kinds: print("bad kind", i); problems += 1
    if f["confidence"] not in ("high", "medium", "low"): print("bad conf", i); problems += 1
    if f["kind"] == "misprint_in_print" and "corrected" not in f: print("no corrected", i); problems += 1
    if f["kind"] != "misprint_in_print" and "corrected" in f: print("corrected on non-misprint", i); problems += 1
    s = json.dumps(f, ensure_ascii=False)
    if any(ord(c) < 32 for c in json.dumps(f, ensure_ascii=False).replace("\\n", "")):
        print("control char", i); problems += 1
    fx = f["fix"]
    if fx is not None:
        o = fx["old"]
        if texts[f["page"]].count(o) != 1 or seq[f["page"]].count(o) != 1:
            print("not unique", i, f["page"], repr(o)); problems += 1
        if "scan idx" in o: print("touches marker", i); problems += 1
        seq[f["page"]] = seq[f["page"]].replace(o, fx["new"], 1)
    print(f["page"], f["kind"], f["confidence"], "|", (repr(fx["old"]) + " -> " + repr(fx["new"])) if fx else "fix: null", "|", f.get("corrected", ""))
print("problems:", problems, "| findings:", len(d))
