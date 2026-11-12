"""Count the plain H of H_{n,U',X'}-type symbols in Exposé XII (diplomatic s5.tex), read-only."""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
t = open(r"C:\Users\user\Documents\sga_scan_check_20261105\sga5\diplomatic\s5.tex", encoding="utf-8").read()
a = t.find(r"\section*{Exposé XII}")
b = t.find(r"\section*{Exposé XIII", a)
if b < 0:
    b = t.find(r"\section*{Exposé", t.find(r"\section*{Exposé XII (suite et fin)}") + 10)
seg = t[a:b]
print("Exposé XII spans lines", t.count("\n", 0, a) + 1, "to", t.count("\n", 0, b) + 1, "next heading:", t[b:b + 40])
pat = re.compile(r"(?<![A-Za-z\\])H_\{[nm],U'")
print("H_{n,U' / H_{m,U' occurrences:", len(pat.findall(seg)))
pat2 = re.compile(r"(?<![A-Za-z\\])H_\{")
print("all H_{ occurrences:", len(pat2.findall(seg)))
for m in list(pat2.finditer(seg))[:3]:
    print("  e.g.", repr(seg[max(0, m.start() - 30):m.start() + 30]))
