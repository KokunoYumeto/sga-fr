"""Compare the batch page files with the same folios in both layers of s5.tex (read-only)."""
import difflib
import re
import sys
import pathlib

sys.stdout.reconfigure(encoding="utf-8")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
root = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
batch = root / "run_5" / "b216_220"


def region(t, folio):
    ms = list(MARK.finditer(t))
    for i, m in enumerate(ms):
        if int(m.group(2)) == folio:
            end = ms[i + 1].start() if i + 1 < len(ms) else len(t)
            return t[m.start():end]
    return None


for edition in ("diplomatic", "current"):
    t = (root / "sga5" / edition / "s5.tex").read_text(encoding="utf-8")
    for folio in range(216, 221):
        page = (batch / f"page_{folio}.tex").read_text(encoding="utf-8")
        page_body = page[page.find("%%%%%%%%%%"):]
        reg = region(t, folio)
        if reg == page_body:
            print(edition, folio, "identical")
        else:
            print(edition, folio, "DIFFERS")
            for line in difflib.unified_diff(page_body.splitlines(), reg.splitlines(), lineterm="", n=0):
                print("   ", line[:300])
