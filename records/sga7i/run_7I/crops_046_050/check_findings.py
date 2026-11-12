import json
import sys

sys.stdout.reconfigure(encoding="utf-8")
base = "C:/Users/user/Documents/sga_scan_check_20261105/run_7I/"
findings = json.load(open(base + "findings_046_050.json", encoding="utf-8"))
ok = True
counts = {}
for i, f in enumerate(findings):
    page = f["page"]
    text = open(base + "b046_050/page_%03d.tex" % page, encoding="utf-8", newline="").read()
    if "\r" in text:
        print("CR in page", page)
    key = (page, f["kind"] == "misprint_in_print")
    counts[key] = counts.get(key, 0) + 1
    tex_n = text.count(f["tex"])
    if tex_n < 1:
        ok = False
        print(i, page, "TEX NOT FOUND:", f["tex"])
    if f["kind"] == "misprint_in_print":
        if "corrected" not in f:
            ok = False
            print(i, page, "missing corrected")
    elif "corrected" in f:
        ok = False
        print(i, page, "corrected on non-misprint")
    fix = f["fix"]
    if fix is not None:
        n = text.count(fix["old"])
        if n != 1:
            ok = False
            print(i, page, "OLD COUNT", n, fix["old"])
        if "%%%%%%%%%%" in fix["old"]:
            ok = False
            print(i, page, "old crosses marker")
    print(i, page, f["kind"], f["confidence"], "tex x%d" % tex_n,
          "old x%d" % (text.count(fix["old"]) if fix else 0))
for p in range(46, 51):
    print(p, "normal", counts.get((p, False), 0), "misprint", counts.get((p, True), 0))
print("ALL OK" if ok else "PROBLEMS")
