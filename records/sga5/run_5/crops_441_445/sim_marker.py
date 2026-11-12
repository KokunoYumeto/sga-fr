"""Simulate move_marker.py in memory (no writes): python -I sim_marker.py FOLIO ANCHOR [--before]"""
import re, sys, pathlib
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga5")
folio, anchor = int(sys.argv[1]), sys.argv[2]
before = "--before" in sys.argv
for ed in ("diplomatic", "current"):
    t = (W / ed / "s5.tex").read_text(encoding="utf-8")
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    if not m:
        print(ed, "no marker"); continue
    end = m.end() + (1 if t[m.end():m.end()+1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    if k < 0:
        print(ed, "anchor not found"); continue
    ln_marker = t[:m.start()].count("\n") + 1
    ln_anchor = t2[:k].count("\n") + 1
    print(ed, "marker line", ln_marker, "-> before anchor at line", ln_anchor, "| context:", repr(t2[max(0,k-80):k+60]))
