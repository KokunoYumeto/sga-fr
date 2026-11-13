import sys, pathlib, re
sys.stdout.reconfigure(encoding="utf-8")
BS = chr(92)
t = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex").read_text(encoding="utf-8")
a = t.find("|  folio 498  ")
b = t.find("X. Formalisme des intersections")
ix = t[a:b]
for key in [BS + "mathbb S", BS + "mathbb D", BS + "mathrm{Gl}", BS + "mathbf{Gl}", BS + "mathrm{GL}", "K^" + BS + "circ", "K^{" + BS + "bullet}", "_{0,", BS + "coprod"]:
    print(key, ix.count(key))
for m in re.finditer(re.escape(BS + "mathrm{G"), ix):
    print("  GL ctx:", repr(ix[m.start() - 60:m.end() + 20]))
i = t.find("|  folio 507  ")
print(t[i:i + 500])
