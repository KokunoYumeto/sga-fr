import json
import sys

findings_path, folder = sys.argv[1], sys.argv[2]
with open(findings_path, encoding="utf-8") as fh:
    findings = json.load(fh)

ok = True
counts = {}
for i, f in enumerate(findings):
    page = f["page"]
    kind = f["kind"]
    key = "misprint" if kind == "misprint_in_print" else "normal"
    counts.setdefault(page, {"normal": 0, "misprint": 0})[key] += 1
    with open(f"{folder}/page_{page:03d}.tex", encoding="utf-8", newline="") as fh:
        text = fh.read()
    # every "tex" field should be found in the page (sanity check of quotations)
    if f.get("tex") and f["tex"] not in text:
        print(f"[{i}] p{page}: tex field not found verbatim: {f['tex']!r}")
    fix = f.get("fix")
    if fix is None:
        if kind != "misprint_in_print":
            print(f"[{i}] p{page}: null fix on non-misprint")
            ok = False
        continue
    old = fix["old"]
    n = text.count(old)
    if n != 1:
        print(f"[{i}] p{page}: old occurs {n} times: {old!r}")
        ok = False
    if "%%%%%%%%%%" in old:
        print(f"[{i}] p{page}: old crosses a marker line")
        ok = False
print("counts:", counts)
print("ALL OK" if ok else "PROBLEMS")
