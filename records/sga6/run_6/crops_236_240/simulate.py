"""Apply the findings' fixes in order to copies of the page texts (in memory) and show the changed passages."""
import json

W = r"C:\Users\user\Documents\sga_scan_check_20261105\run_6"
F = json.load(open(W + r"\findings_236_240.json", encoding="utf-8"))
for page in range(236, 241):
    t = open(W + rf"\b236_240\page_{page}.tex", encoding="utf-8").read()
    for d in F:
        if d["page"] != page or not d["fix"]:
            continue
        old, new = d["fix"]["old"], d["fix"]["new"]
        assert t.count(old) == 1, (page, old)
        t = t.replace(old, new)
    print(f"===== {page}")
    print(t)
