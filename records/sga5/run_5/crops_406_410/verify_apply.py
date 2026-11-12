"""Read findings_406_410.json, apply every fix in memory to its page (in file order), and show the edited spots."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
F = json.loads((RUN / "findings_406_410.json").read_text(encoding="utf-8"))
pages = {n: (RUN / "b406_410" / f"page_{n}.tex").read_text(encoding="utf-8") for n in range(406, 411)}
for d in F:
    fx = d["fix"]
    if not fx:
        continue
    t = pages[d["page"]]
    assert t.count(fx["old"]) == 1, (d["page"], fx["old"])
    k = t.index(fx["old"])
    t = t[:k] + fx["new"] + t[k + len(fx["old"]):]
    pages[d["page"]] = t
    s = max(0, k - 40)
    print(d["page"], d["kind"], "->", repr(t[s:k + len(fx["new"]) + 40]))
print()
print(pages[406])
print(pages[408].split("\n")[8:13])
print(pages[409].split("\n")[24])
print("\n".join(pages[410].split("\n")[2:9]))
