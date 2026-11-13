"""Compare the page files of b476_480 with the folio 476-480 region of both main.tex layers."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
SGA6 = r"C:\Users\user\Documents\sga_scan_check_20261105\sga6"
B = r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\b476_480"
allp = ""
for n in range(476, 481):
    s = open(B + rf"\page_{n}.tex", encoding="utf-8", newline="").read()
    allp += s.split("\n", 1)[1]
for L in ("diplomatic", "current"):
    t = open(SGA6 + "\\" + L + r"\main.tex", encoding="utf-8", newline="").read()
    i = t.find("scan idx 489  |  folio 476")
    j = t.find("scan idx 494  |  folio 481")
    seg = t[t.rfind("\n", 0, i) + 1:t.rfind("\n", 0, j) + 1]
    print(L, "start line", t.count("\n", 0, i) + 1, len(seg), len(allp), seg == allp)
    if seg != allp:
        import difflib
        for line in difflib.unified_diff(allp.split("\n"), seg.split("\n"), "pages", L, lineterm="", n=0):
            print(line[:300])
