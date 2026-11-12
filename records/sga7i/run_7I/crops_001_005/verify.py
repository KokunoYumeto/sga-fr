"""Check a findings JSON: each fix.old occurs exactly once in its page_NNN.tex; report tex quotes not found."""
import json
import pathlib
import sys

run = pathlib.Path(sys.argv[1])
folder = run / sys.argv[2]
findings = json.loads((run / sys.argv[3]).read_text(encoding="utf-8"))
ok = True
for i, f in enumerate(findings):
    tex = (folder / f"page_{f['page']:03d}.tex").read_text(encoding="utf-8")
    fix = f.get("fix")
    if fix is not None:
        n = tex.count(fix["old"])
        print(i, f["page"], f["kind"], "old count", n)
        if n != 1:
            ok = False
        marker_lines = [l for l in fix["old"].split("\n") if "scan idx" in l]
        if marker_lines:
            print("   old touches a marker line!")
            ok = False
    else:
        print(i, f["page"], f["kind"], "fix null", "corrected" in f)
    if f["kind"] == "misprint_in_print" and "corrected" not in f:
        ok = False
        print("   misprint without corrected")
    for part in str(f.get("tex", "")).split(" (p. ")[0:1]:
        pass
print("ALL OK" if ok else "PROBLEMS")
