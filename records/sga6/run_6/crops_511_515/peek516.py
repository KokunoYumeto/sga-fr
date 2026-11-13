import sys, pathlib
sys.stdout.reconfigure(encoding="utf-8")
for layer in ("diplomatic", "current"):
    p = pathlib.Path(rf"C:\Users\user\Documents\sga_scan_check_20261105\sga6\{layer}\main.tex")
    t = p.read_text(encoding="utf-8")
    import os, time
    print("=====", layer, time.ctime(os.path.getmtime(p)))
    i = t.find("|  folio 516  ")
    print(t[i - 700:i + 400])
