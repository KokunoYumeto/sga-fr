import json, sys
run = "C:/Users/user/Documents/sga_scan_check_20261105/run_7II"
d = json.load(open(run + "/findings_166_170.json", encoding="utf-8"))
counts = {}
ok = True
for x in d:
    p = x["page"]
    tex = open(f"{run}/b166_170/page_{p}.tex", encoding="utf-8").read()
    k = "misprint" if x["kind"] == "misprint_in_print" else "normal"
    counts.setdefault(p, {"normal": 0, "misprint": 0})[k] += 1
    # the 'tex' quote should occur in the file
    if x["tex"] not in tex:
        print("TEX QUOTE NOT FOUND", p, ascii(x["tex"])); ok = False
    if x["fix"]:
        n = tex.count(x["fix"]["old"])
        if n != 1:
            print("OLD COUNT", n, p, ascii(x["fix"]["old"])); ok = False
        if "%%%%%%%%%%" in x["fix"]["old"]:
            print("MARKER IN OLD", p); ok = False
    if x["kind"] == "misprint_in_print" and "corrected" not in x:
        print("NO CORRECTED", p); ok = False
print(counts, "OK" if ok else "PROBLEMS")
