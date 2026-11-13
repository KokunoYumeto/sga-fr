import sys
sys.stdout.reconfigure(encoding="utf-8")
t = open(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\crops_546_550\expX_dipl.txt", encoding="utf-8").read()
for k in [r"K^\circ", r"\cl^\circ", r"K^{\bullet}", r"K^\bullet", r"\Theta", r"\theta", r"\subsection*{"]:
    print(repr(k), t.count(k))
