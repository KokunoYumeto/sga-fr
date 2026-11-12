import re
import difflib
import pathlib

MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
B = pathlib.Path(r"C:/Users/user/Documents/sga_scan_check_20261105/run_5/b301_305")
for edition in ("diplomatic", "current"):
    t = pathlib.Path(r"C:/Users/user/Documents/sga_scan_check_20261105/sga5/%s/s5.tex" % edition).read_text(encoding="utf-8")
    ms = list(MARK.finditer(t))
    for i, m in enumerate(ms):
        f = int(m.group(2))
        if 301 <= f <= 305:
            seg = t[m.start(): ms[i + 1].start()]
            page = (B / ("page_%d.tex" % f)).read_text(encoding="utf-8")
            page_body = page.split("\n", 1)[1]
            same = page_body == seg
            print(edition, f, "identical" if same else "DIFFERS")
            if not same:
                for line in difflib.unified_diff(page_body.splitlines(), seg.splitlines(), lineterm="", n=0):
                    print("   ", line)
