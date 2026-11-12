"""Check that every fix 'old' occurs exactly once in its page_NNN.tex and does not cross a marker line."""
import json
import sys
from pathlib import Path

findings = Path(sys.argv[1])
folder = Path(sys.argv[2])
data = json.loads(findings.read_text(encoding="utf-8"))
ok = True
counts = {}
for i, f in enumerate(data):
    p = f["page"]
    kind = f["kind"]
    key = "misprint" if kind == "misprint_in_print" else "normal"
    counts.setdefault(p, {"normal": 0, "misprint": 0})[key] += 1
    for field in ("page", "where", "scan", "tex", "kind", "confidence", "fix", "note"):
        if field not in f:
            print(f"#{i} p{p}: missing field {field}")
            ok = False
    if kind == "misprint_in_print" and "corrected" not in f:
        print(f"#{i} p{p}: misprint without 'corrected'")
        ok = False
    fix = f["fix"]
    if fix is None:
        continue
    tex = (folder / f"page_{p:03d}.tex").read_text(encoding="utf-8")
    old = fix["old"]
    n = tex.count(old)
    marker = "%%%%%%%%%%" in old
    status = "OK" if n == 1 and not marker else "FAIL"
    if status == "FAIL":
        ok = False
    print(f"#{i} p{p} {kind}: count={n} marker={marker} {status} | {old!r}")
print(counts)
print("ALL OK" if ok else "PROBLEMS")
