"""Print the folio and nearby lines of given literal strings in the diplomatic main.tex of SGA 6.
usage: python -I lookup.py STRING [STRING ...]"""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
T = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex").read_text(encoding="utf-8")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
for s in sys.argv[1:]:
    k = T.find(s)
    while k >= 0:
        folio = None
        for m in MARK.finditer(T, 0, k):
            folio = m.group(2)
        print(f"--- {s!r} at folio {folio}:")
        print(T[max(0, k - 200):k + 200])
        k = T.find(s, k + 1)
