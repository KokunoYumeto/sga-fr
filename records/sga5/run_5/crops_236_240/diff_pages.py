import difflib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = r"C:/Users/user/Documents/sga_scan_check_20261105/run_5/"
SRC = r"C:/Users/user/Documents/sga_scan_check_20261105/sga5/"
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
for layer in ("diplomatic", "current"):
    t = open(SRC + layer + "/s5.tex", encoding="utf-8").read()
    ms = list(MARK.finditer(t))
    for i, m in enumerate(ms):
        p = int(m.group(2))
        if 236 <= p <= 240:
            seg = t[m.start():ms[i + 1].start()]
            pf = open(RUN + "b236_240/page_%03d.tex" % p, encoding="utf-8").read()
            pf = pf.split(chr(10), 1)[1]  # drop the '% from s5.tex' line
            if seg != pf:
                print("==", layer, p, "differs")
                for d in difflib.unified_diff(pf.split(chr(10)), seg.split(chr(10)), lineterm="", n=0):
                    print(d[:200])
            else:
                print("==", layer, p, "same")
