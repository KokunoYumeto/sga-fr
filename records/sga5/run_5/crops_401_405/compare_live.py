"""Compare the batch's page files with the live s5.tex (both layers), read-only."""
import re, sys
sys.stdout.reconfigure(encoding="utf-8")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
base = "C:/Users/user/Documents/sga_scan_check_20261105"
for ed in ("diplomatic", "current"):
    t = open(f"{base}/sga5/{ed}/s5.tex", encoding="utf-8", newline="").read()
    ms = list(MARK.finditer(t))
    for folio in range(401, 406):
        i = next(j for j, m in enumerate(ms) if int(m.group(2)) == folio)
        seg = t[t.rfind("\n", 0, ms[i].start()) + 1: t.rfind("\n", 0, ms[i + 1].start()) + 1]
        pf = open(f"{base}/run_5/b401_405/page_{folio}.tex", encoding="utf-8", newline="").read()
        body = pf.split("\n", 1)[1]
        line = t.count("\n", 0, ms[i].start()) + 1
        print(ed, folio, "marker line", line, "identical" if body == seg else "DIFFERENT")
        if body != seg and ed == "diplomatic":
            import difflib
            for l in difflib.unified_diff(body.split("\n"), seg.split("\n"), lineterm="", n=0):
                print("   ", l[:200])
