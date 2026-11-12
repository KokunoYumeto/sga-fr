import re
W = r"C:\Users\user\Documents\sga_scan_check_20261105"
BS = chr(92)
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
t = open(W + r"\sga5\diplomatic\s5.tex", encoding="utf-8").read()
lines = t.split("\n")
folio = None
for i, l in enumerate(lines, 1):
    m = MARK.search(l)
    if m:
        folio = int(m.group(2))
    if 12684 <= i <= 13754:
        for pat in ["EP", "RG", "Gamma"]:
            if BS + pat in l:
                print(folio, i, pat, l[:110])
                break
