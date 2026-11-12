"""Compare page_NNN.tex snapshots with the live main.tex spans (both layers); read-only."""
import difflib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
base = "C:/Users/user/Documents/sga_scan_check_20261105/"
for layer in ("diplomatic", "current"):
    t = open(base + "sga6/" + layer + "/main.tex", encoding="utf-8").read()
    ms = list(MARK.finditer(t))
    spans = {int(m.group(2)): (m.start(), ms[i + 1].start() if i + 1 < len(ms) else len(t)) for i, m in enumerate(ms)}
    for folio in range(376, 381):
        snap = open(base + f"run_6/b376_380/page_{folio}.tex", encoding="utf-8").read()
        snap = snap.split("\n", 1)[1]  # drop '% from main.tex'
        a, b = spans[folio]
        live = t[a:b]
        same = snap.rstrip("\n") == live.rstrip("\n")
        print(layer, folio, "same" if same else "DIFFERENT")
        if not same:
            for l in difflib.unified_diff(snap.split("\n"), live.split("\n"), lineterm="", n=0):
                print("   ", l[:220])
