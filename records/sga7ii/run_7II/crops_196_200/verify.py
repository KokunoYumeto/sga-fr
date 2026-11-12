import json
import sys

run = r"C:/Users/user/Documents/sga_scan_check_20261105/run_7II/"
data = json.load(open(run + "findings_196_200.json", encoding="utf-8"))
ok = True
out = []
for i, e in enumerate(data):
    page = e["page"]
    src = open(run + f"b196_200/page_{page:03d}.tex", encoding="utf-8", newline="").read()
    keys = set(e)
    req = {"page", "where", "scan", "tex", "kind", "confidence", "fix", "note"}
    if not req <= keys:
        ok = False
        out.append(f"#{i} missing keys {req - keys}")
    if e["kind"] == "misprint_in_print" and "corrected" not in e:
        ok = False
        out.append(f"#{i} misprint without corrected")
    if e["kind"] != "misprint_in_print" and "corrected" in e:
        ok = False
        out.append(f"#{i} corrected on non-misprint")
    if e["tex"] not in src:
        out.append(f"#{i} p{page} note: tex field not a literal substring")
    fix = e["fix"]
    if fix is not None:
        n = src.count(fix["old"])
        if n != 1:
            ok = False
        out.append(f"#{i} p{page} old count = {n}")
        if "%%%%%%%%%%" in fix["old"]:
            ok = False
            out.append(f"#{i} old crosses a marker")
        new_src = src.replace(fix["old"], fix["new"], 1)
        out.append(f"#{i} after fix: count(new) = {new_src.count(fix['new'])}")
print("\n".join(out).encode("ascii", "backslashreplace").decode("ascii"))
print("ALL OK" if ok else "PROBLEMS")
for e in data:
    if e["fix"]:
        print(repr(e["fix"]["old"]).encode("ascii", "backslashreplace").decode("ascii"), "->",
              repr(e["fix"]["new"]).encode("ascii", "backslashreplace").decode("ascii"))
