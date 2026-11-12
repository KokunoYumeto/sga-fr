import json
import pathlib

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
L = json.loads((RUN / "findings_386_390.json").read_text(encoding="utf-8"))
keys = {"page", "where", "scan", "tex", "kind", "confidence", "fix", "note"}
kinds = {"word", "formula", "symbol", "font", "underline", "missing", "extra", "number", "punctuation", "accent",
         "misprint_in_print", "marker", "other"}
bad = 0
for i, r in enumerate(L):
    miss = keys - set(r)
    if miss:
        print(i, "missing keys", miss); bad += 1
    if r["kind"] not in kinds:
        print(i, "bad kind", r["kind"]); bad += 1
    if r["confidence"] not in ("high", "medium", "low"):
        print(i, "bad confidence"); bad += 1
    if r["kind"] == "misprint_in_print" and not r.get("corrected"):
        print(i, "misprint without corrected"); bad += 1
    if r["kind"] != "misprint_in_print" and "corrected" in r:
        print(i, "corrected on non-misprint"); bad += 1
    if r["kind"] != "misprint_in_print" and r["kind"] != "marker" and r["fix"] is None:
        print(i, "non-misprint without fix"); bad += 1
    if "<<L" in r["note"]:
        print(i, "placeholder left"); bad += 1
    if r["fix"]:
        t = (RUN / "b386_390" / f"page_{r['page']}.tex").read_text(encoding="utf-8")
        n = t.count(r["fix"]["old"])
        if n != 1:
            print(i, r["page"], "old count", n); bad += 1
        if "%%%%%%%%%%" in r["fix"]["old"] or "%%%%%%%%%%" in r["fix"]["new"]:
            print(i, "marker in fix"); bad += 1
        if r["fix"]["old"] == r["fix"]["new"]:
            print(i, "no-op fix"); bad += 1
print("records", len(L), "problems", bad)
for r in L:
    if r["kind"] == "marker":
        print(r["page"], r["note"][:230].encode("ascii", "backslashreplace").decode())
