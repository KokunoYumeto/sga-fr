# Checks findings_011_015.json: each fix's old occurs exactly once in its page file; applies all fixes to copies
# in memory per page and reports the result around each edit; flags control characters.
import json
import pathlib
import re

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
d = json.loads((RUN / "findings_011_015.json").read_text(encoding="utf-8"))
pages = {}
ok = True
for i, x in enumerate(d):
    p = x["page"]
    t = pages.setdefault(p, (RUN / "b011_015" / f"page_{p:03d}.tex").read_text(encoding="utf-8"))
    assert "\r" not in t
    for k, v in x.items():
        if isinstance(v, str) and re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", v):
            print("CONTROL CHAR", i, k)
            ok = False
    if x["fix"]:
        old = x["fix"]["old"]
        n = t.count(old)
        if n != 1:
            print("NOT UNIQUE", i, p, n, repr(old))
            ok = False
        if "%%%%%%%%%%" in old:
            print("MARKER IN OLD", i)
            ok = False
    if x["kind"] == "misprint_in_print" and "corrected" not in x:
        print("NO CORRECTED", i)
        ok = False
    if x["kind"] != "misprint_in_print" and "corrected" in x:
        print("STRAY CORRECTED", i)
        ok = False
# apply all fixes per page (in list order) to check that they do not collide
for p in sorted(pages):
    t = pages[p]
    for x in d:
        if x["page"] == p and x["fix"]:
            old, new = x["fix"]["old"], x["fix"]["new"]
            assert t.count(old) == 1, (p, old)
            t = t.replace(old, new)
    print(f"--- page {p} after all fixes: begin/end proof counts",
          t.count("\\begin{proof}"), t.count("\\end{proof}"), "emph Preuve:", t.count("\\emph{Preuve} : "))
print("OK" if ok else "PROBLEMS")
print(json.dumps(d, ensure_ascii=False, indent=1)[:200])
