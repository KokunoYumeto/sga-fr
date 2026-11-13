import sys, pathlib, re
sys.stdout.reconfigure(encoding="utf-8")
t = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex").read_text(encoding="utf-8")
a = t.find("|  folio 498  ")
b = t.find("|  folio 519  ")
for m in re.finditer(r"(?<![A-Za-z\\])D\(E\)", t[a:b]):
    s = a + m.start()
    fol = re.findall(r"folio (\d+)", t[:s])[-1]
    print(fol, repr(t[s - 50:s + 15]))
