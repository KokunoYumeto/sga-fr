import sys, difflib
sys.path.insert(0, r"C:\Users\user\Documents\sga_scan_check_20261105")
from sga_config import pages
sys.stdout.reconfigure(encoding="utf-8")
P = pages("6")
for folio in range(251, 256):
    f, a, b = P[folio][0]
    cur = f.read_text(encoding="utf-8")[a:b]
    old = open(rf"C:\Users\user\Documents\sga_scan_check_20261105\run_6\b251_255\page_{folio}.tex", encoding="utf-8").read()
    old = old.split("\n", 1)[1]  # drop '% from main.tex'
    if cur == old:
        print(folio, "same")
        continue
    print("==", folio)
    for l in difflib.unified_diff(old.splitlines(), cur.splitlines(), lineterm="", n=0):
        print(l[:400])
