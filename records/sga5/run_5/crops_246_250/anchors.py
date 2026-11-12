import sys
sys.stdout.reconfigure(encoding="utf-8")
A = [r"\[" + "\n" + r"E^{(n)}_r(X)",
     r"\[" + "\n" + r"\mathcal E_r^{(n)}(X)",
     r"\[" + "\n" + r"\bigl[\mathcal B_r^{(n)}(X)"]
for ed in ("diplomatic", "current"):
    t = open(rf"C:\Users\user\Documents\sga_scan_check_20261105\sga5\{ed}\s5.tex", encoding="utf-8").read()
    for a in A:
        print(ed, repr(a), t.count(a))
