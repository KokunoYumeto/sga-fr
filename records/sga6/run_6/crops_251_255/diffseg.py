import sys, difflib
sys.path.insert(0, r"C:\Users\user\Documents\sga_scan_check_20261105")
from sga_config import pages
sys.stdout.reconfigure(encoding="utf-8")
for layer in ("diplomatic", "current"):
    P = pages("6", layer)
    for folio in range(251, 256):
        f, a, b = P[folio][0]
        cur = f.read_text(encoding="utf-8")[a:b]
        old = open(rf"C:\Users\user\Documents\sga_scan_check_20261105\run_6\b251_255\page_{folio}.tex", encoding="utf-8").read().split("\n", 1)[1]
        sm = difflib.SequenceMatcher(None, old, cur, autojunk=False)
        segs = [(op, old[i1:i2], cur[j1:j2]) for op, i1, i2, j1, j2 in sm.get_opcodes() if op != "equal"]
        print(layer, folio, "same" if not segs else segs)
