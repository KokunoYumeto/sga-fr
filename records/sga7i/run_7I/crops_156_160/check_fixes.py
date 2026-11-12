import json
import sys
from pathlib import Path

findings = Path(sys.argv[1])
folder = Path(sys.argv[2])
data = json.loads(findings.read_text(encoding="utf-8"))
ok = True
counts = {}
for i, f in enumerate(data):
    page = f["page"]
    kind = f["kind"]
    key = "misprint" if kind == "misprint_in_print" else "normal"
    counts.setdefault(page, {"normal": 0, "misprint": 0})[key] += 1
    if kind == "misprint_in_print" and "corrected" not in f:
        print(f"#{i} p{page}: misprint without 'corrected'")
        ok = False
    if kind != "misprint_in_print" and "corrected" in f:
        print(f"#{i} p{page}: 'corrected' on a non-misprint")
        ok = False
    fix = f.get("fix")
    if fix is None:
        continue
    tex = (folder / f"page_{page:03d}.tex").read_text(encoding="utf-8")
    n = tex.count(fix["old"])
    marker_hit = any("%%%%%%%%%%" in line for line in fix["old"].split("\n"))
    print(f"#{i} p{page}: old occurs {n}x; marker in old: {marker_hit}")
    if n != 1 or marker_hit:
        ok = False
print("counts:", counts)
print("ALL OK" if ok else "PROBLEMS")
