import re, sys, pathlib
sys.stdout.reconfigure(encoding='utf-8')
ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
BS = "\\"
for layer in ("diplomatic", "current"):
    t = (ROOT / layer / "main.tex").read_text(encoding="utf-8")
    print("=====", layer)
    for key in (BS + "text{mod", BS + "mathrm{mod", BS + "operatorname{mod"):
        i = t.find(key)
        n = 0
        while i != -1 and n < 12:
            print("   ", repr(t[max(0, i - 50):i + 45]))
            i = t.find(key, i + 1)
            n += 1
    i = t.find("est la classe dans")
    while i != -1:
        print("  CLS", repr(t[i - 30:i + 80]))
        i = t.find("est la classe dans", i + 1)
