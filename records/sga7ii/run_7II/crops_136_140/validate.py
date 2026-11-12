import json
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")
RUN = r"C:/Users/user/Documents/sga_scan_check_20261105/run_7II"
FOLDER = RUN + "/b136_140"
OUT = RUN + "/findings_136_140.json"

data = json.load(open(OUT, encoding="utf-8"))
print("findings:", len(data))
ok = True
counts = Counter()
for i, f in enumerate(data):
    page = f["page"]
    tex = open(f"{FOLDER}/page_{page:03d}.tex", encoding="utf-8", newline="").read()
    kind = f["kind"]
    counts[(page, "misprint" if kind == "misprint_in_print" else "normal")] += 1
    # the quoted TeX must occur in the page file
    if f.get("tex") and f["tex"] not in tex:
        print(f"[{i}] p{page}: 'tex' not found in page file: {f['tex']!r}")
        ok = False
    if kind == "misprint_in_print" and "corrected" not in f:
        print(f"[{i}] p{page}: misprint without 'corrected'")
        ok = False
    if kind != "misprint_in_print" and "corrected" in f:
        print(f"[{i}] p{page}: 'corrected' on a non-misprint")
        ok = False
    fx = f.get("fix")
    if fx is not None:
        n = tex.count(fx["old"])
        if n != 1:
            print(f"[{i}] p{page}: fix old occurs {n} times: {fx['old']!r}")
            ok = False
        if "%%%%%%%%%%" in fx["old"] or "%%%%%%%%%%" in fx["new"]:
            print(f"[{i}] p{page}: fix touches a marker line")
            ok = False
for p in range(136, 141):
    print(p, "normal", counts[(p, "normal")], "misprint", counts[(p, "misprint")])
print("OK" if ok else "PROBLEMS")
