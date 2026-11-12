"""Check findings_121_125.json: every fix's old occurs exactly once in its page file, the edits apply in
listed order, and the edited pages keep balanced $ and braces (nothing is written)."""
import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = r"C:\Users\user\Documents\sga_scan_check_20261105\run_5"
F = json.load(open(rf"{RUN}\findings_121_125.json", encoding="utf-8"))
pages = {}
for p in range(121, 126):
    with open(rf"{RUN}\b121_125\page_{p}.tex", encoding="utf-8", newline="") as fh:
        pages[p] = fh.read()
orig = dict(pages)

ok = True
for i, f in enumerate(F):
    fx = f["fix"]
    if fx is None:
        continue
    n = orig[f["page"]].count(fx["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE in original:", i, f["page"], n, repr(fx["old"]))
    m = pages[f["page"]].count(fx["old"])
    if m != 1:
        ok = False
        print("NOT UNIQUE at application:", i, f["page"], m, repr(fx["old"]))
    else:
        pages[f["page"]] = pages[f["page"]].replace(fx["old"], fx["new"])
    if "%%%%%%%%%%" in fx["old"]:
        ok = False
        print("marker line touched:", i)


def balance(t):
    body = "\n".join(line for line in t.split("\n") if not line.lstrip().startswith("%"))
    body = body.replace("\\$", "")
    return body.count("$") % 2, body.count("{") - body.count("}")


for p in pages:
    print(p, "orig $/{}:", balance(orig[p]), "edited $/{}:", balance(pages[p]))
print("all olds unique and applicable:", ok)
kinds = {}
for f in F:
    key = (f["page"], "misprint" if f["kind"] == "misprint_in_print" else "normal")
    kinds[key] = kinds.get(key, 0) + 1
print(sorted(kinds.items()))
for p in (122, 123, 124, 125):
    print("----", p)
    print(pages[p])
