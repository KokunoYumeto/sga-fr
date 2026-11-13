"""Word-level diff of folios 606-610 between the diplomatic and current layers of main.tex (read only)."""
import pathlib, sys, re, difflib
sys.stdout.reconfigure(encoding='utf-8')
ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
def slice_(t, a, b):
    ma = re.search(r"%%%%%%%%%%  scan idx \d+  \|  folio " + str(a) + r"  %%%%%%%%%%", t)
    mb = re.search(r"%%%%%%%%%%  scan idx \d+  \|  folio " + str(b) + r"  %%%%%%%%%%", t)
    return t[ma.start():mb.start()]
D = (ROOT / "diplomatic" / "main.tex").read_text(encoding="utf-8")
C = (ROOT / "current" / "main.tex").read_text(encoding="utf-8")
for f in range(606, 611):
    d = slice_(D, f, f + 1); c = slice_(C, f, f + 1)
    print("=== folio", f, "equal:", d == c)
    dw = re.findall(r"\S+|\n", d); cw = re.findall(r"\S+|\n", c)
    sm = difflib.SequenceMatcher(None, dw, cw, autojunk=False)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op != "equal":
            print(op, "DIPL:", " ".join(dw[max(0, i1 - 2):i2 + 2]))
            print("     CURR:", " ".join(cw[max(0, j1 - 2):j2 + 2]))
