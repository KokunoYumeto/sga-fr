"""Check that every fix 'old' (and every misprint 'tex') occurs exactly once in its page TeX."""
import json
import sys

findings_path, folder = sys.argv[1], sys.argv[2]
with open(findings_path, encoding="utf-8") as f:
    findings = json.load(f)

ok = True
for i, x in enumerate(findings):
    with open(f"{folder}/page_{x['page']}.tex", encoding="utf-8", newline="") as f:
        t = f.read()
    marker_lines = [ln for ln in t.split("\n") if ln.startswith("%%%%%%%%%%")]
    if x.get("fix"):
        old, new = x["fix"]["old"], x["fix"]["new"]
        n = t.count(old)
        bad_marker = any(m in old for m in marker_lines)
        print(i, x["page"], x["kind"], "old count", n, "marker in old" if bad_marker else "")
        if n != 1 or bad_marker:
            ok = False
        # simulate the edit and show the result around it
        t2 = t.replace(old, new, 1)
        j = t2.find(new)
        print("   ->", repr(t2[max(0, j - 30): j + len(new) + 30]))
    if x["kind"] == "misprint_in_print":
        n = t.count(x["tex"])
        print(i, x["page"], "misprint tex count", n, "| corrected:", x.get("corrected"))
        if n != 1 or not x.get("corrected"):
            ok = False
print("ALL OK" if ok else "PROBLEMS")
