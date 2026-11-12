"""Compare the page files of batch 186-190 with the current text of SGA 6 diplomatic main.tex between the markers
(read only): reports whether each page's text is unchanged."""
import re
import sys
import difflib

sys.stdout.reconfigure(encoding="utf-8")
W = r"C:\Users\user\Documents\sga_scan_check_20261105"
B = W + r"\run_6\b186_190"
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
t = open(W + r"\sga6\diplomatic\main.tex", encoding="utf-8").read()
marks = [(m.start(), int(m.group(2))) for m in MARK.finditer(t)]
for folio in range(186, 191):
    i = next(k for k, (p, f) in enumerate(marks) if f == folio)
    seg = t[marks[i][0]:marks[i + 1][0]]
    page = open(B + rf"\page_{folio}.tex", encoding="utf-8").read()
    body = page.split("\n", 1)[1]  # drop '% from main.tex'
    if body == seg:
        print(folio, "unchanged")
    else:
        print(folio, "CHANGED")
        for l in difflib.unified_diff(body.split("\n"), seg.split("\n"), lineterm="", n=0):
            print("   ", l[:200])
