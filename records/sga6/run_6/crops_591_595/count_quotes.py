import re, sys
sys.stdout.reconfigure(encoding="utf-8")
t = open(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex", encoding="utf-8").read()
print("guillemets", t.count("\u00ab"), "backticks", t.count("``"))
# where are the quotes in Exposé X-XII region
start = t.find("folio 519 ")
end = t.find("folio 700 ")
seg = t[start:]
for m in re.finditer(r"\u00ab~?[^\u00bb]{0,60}\u00bb|``[^']{0,60}''", seg):
    print(repr(m.group(0)))
