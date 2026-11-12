import sys, difflib
sys.path.insert(0, r"C:\Users\user\Documents\sga_scan_check_20261105")
from sga_config import pages
sys.stdout.reconfigure(encoding="utf-8")
P = pages("6")
for folio in (252,):
    f, a, b = P[folio][0]
    cur = f.read_text(encoding="utf-8")[a:b].split("\n")[1]
    old = open(rf"C:\Users\user\Documents\sga_scan_check_20261105\run_6\b251_255\page_{folio}.tex", encoding="utf-8").read().split("\n")[2]
    sm = difflib.SequenceMatcher(None, old, cur)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op != "equal":
            print(op, repr(old[max(0,i1-40):i2+40]), "->", repr(cur[max(0,j1-40):j2+40]))
