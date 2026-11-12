# Extract the live page texts (marker to next marker) of s5.tex and compare with the batch's page files.
import re, sys, difflib
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
root = r"C:/Users/user/Documents/sga_scan_check_20261105"
t = open(root + "/sga5/diplomatic/s5.tex", encoding="utf-8").read()
ms = list(MARK.finditer(t))
out = []
for i, m in enumerate(ms):
    f = int(m.group(2))
    if 276 <= f <= 280:
        live = t[m.start(): ms[i+1].start()]
        page = open(f"{root}/run_5/b276_280/page_{f}.tex", encoding="utf-8").read()
        page = page.split("\n", 1)[1]  # drop the '% from s5.tex' line
        d = list(difflib.unified_diff(page.splitlines(), live.splitlines(), lineterm="", n=0))
        out.append(f"== folio {f}: {'identical' if not d else 'DIFFERS'}")
        out.extend(d[:40])
open(sys.argv[1], "w", encoding="utf-8").write("\n".join(out))
