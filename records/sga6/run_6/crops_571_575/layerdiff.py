"""Word-level diff of the text of folios 571-575 between the diplomatic and current layers of main.tex,
and a check that page_NNN.tex equals the diplomatic layer's slice (read only)."""
import pathlib, sys, re, difflib
sys.stdout.reconfigure(encoding='utf-8')
ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
B = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\b571_575")
def slice_(t, a, b):
    ma = re.search(r"%%%%%%%%%%  scan idx \d+  \|  folio " + str(a) + r"  %%%%%%%%%%", t)
    mb = re.search(r"%%%%%%%%%%  scan idx \d+  \|  folio " + str(b) + r"  %%%%%%%%%%", t)
    return t[ma.start():mb.start()]
D = (ROOT / "diplomatic" / "main.tex").read_text(encoding="utf-8")
C = (ROOT / "current" / "main.tex").read_text(encoding="utf-8")
for f in range(571, 576):
    d = slice_(D, f, f + 1); c = slice_(C, f, f + 1)
    pg = (B / f"page_{f}.tex").read_text(encoding="utf-8")
    body = pg.split("\n", 1)[1]
    print("=== folio", f, "page file == diplomatic slice:", body == d, "| == current slice:", body == c)
    dw = re.findall(r"\S+|\n", d); cw = re.findall(r"\S+|\n", c)
    sm = difflib.SequenceMatcher(None, dw, cw, autojunk=False)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op != "equal":
            print(op, "DIPL:", " ".join(dw[max(0,i1-3):i2+3]).replace("\n","\n"))
            print("     CURR:", " ".join(cw[max(0,j1-3):j2+3]).replace("\n","\n"))
