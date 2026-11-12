"""Validate findings: python -I validate.py <findings.json> <batch_folder>"""
import json
import os
import sys

findings = json.load(open(sys.argv[1], encoding="utf-8"))
folder = sys.argv[2]
ok = True
for i, f in enumerate(findings):
    page = f["page"]
    path = os.path.join(folder, "page_%03d.tex" % page)
    text = open(path, encoding="utf-8").read()
    for key in ("page", "where", "scan", "tex", "kind", "confidence", "fix", "note"):
        if key not in f:
            print(i, page, "missing key", key)
            ok = False
    if f["kind"] == "misprint_in_print" and "corrected" not in f:
        print(i, page, "misprint without corrected")
        ok = False
    if f["kind"] != "misprint_in_print" and "corrected" in f:
        print(i, page, "corrected on a non-misprint")
        ok = False
    fix = f.get("fix")
    if fix:
        old, new = fix["old"], fix["new"]
        n = text.count(old)
        marker = "%%%%%%%%%%" in old
        print(i, page, f["kind"], "fix old count =", n, "| changed:", old != new, "| marker in old:", marker)
        if n != 1 or old == new or marker:
            ok = False
    elif f["kind"] == "misprint_in_print":
        n = text.count(f["tex"])
        print(i, page, f["kind"], "tex count =", n)
        if n != 1:
            ok = False
    else:
        print(i, page, f["kind"], "fix null (convention); tex present:", f["tex"] in text)
print("ALL OK" if ok else "PROBLEMS")
