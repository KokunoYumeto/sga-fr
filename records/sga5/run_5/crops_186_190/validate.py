"""Validate findings_186_190.json against the live diplomatic s5.tex page spans and the batch snapshots."""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
KINDS = {"word", "formula", "symbol", "font", "underline", "missing", "extra", "number", "punctuation", "accent",
         "misprint_in_print", "marker", "other"}
d = json.loads((W / "run_5" / "findings_186_190.json").read_text(encoding="utf-8"))
t = (W / "sga5" / "diplomatic" / "s5.tex").read_text(encoding="utf-8")
ms = list(MARK.finditer(t))
span = {}
for i, m in enumerate(ms):
    end = ms[i + 1].start() if i + 1 < len(ms) else len(t)
    span[int(m.group(2))] = t[m.start():end]
errs = 0
for i, x in enumerate(d):
    keys = set(x)
    need = {"page", "where", "scan", "tex", "kind", "confidence", "fix", "note"}
    if x["kind"] == "misprint_in_print":
        need.add("corrected")
    if keys != need or x["kind"] not in KINDS or x["confidence"] not in {"high", "medium", "low"}:
        errs += 1
        print("schema", i, keys ^ need)
    fx = x["fix"]
    if fx:
        n = span[x["page"]].count(fx["old"])
        if n != 1 or MARK.search(fx["old"]) or MARK.search(fx["new"]):
            errs += 1
            print("old count", i, n)
        else:
            span[x["page"]] = span[x["page"]].replace(fx["old"], fx["new"], 1)
print(len(d), "findings,", errs, "errors")
