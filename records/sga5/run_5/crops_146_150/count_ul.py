import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
t = open("C:/Users/user/Documents/sga_scan_check_20261105/sga5/diplomatic/s5.tex", encoding="utf-8").read().split("\n")
EM = re.compile(r"\\emph\{")
UL = re.compile(r"\\underline\{")
for (a, b), name in (((1930, 4355), "III"), ((4355, 5200), "IIIB")):
    em = sum(len(EM.findall(l)) for l in t[a:b])
    ul = sum(len(UL.findall(l)) for l in t[a:b])
    print(name, "emph", em, "underline", ul)
SHOW = re.compile(r".{0,30}\\(emph|underline)\{.{0,40}")
n = 0
for i in range(4355, 5200):
    for m in SHOW.finditer(t[i]):
        if n < 30:
            print(i + 1, m.group(0))
        n += 1
print("shown", min(n, 30), "of", n)
# statement bodies in Exposé III: how were the underlines written?
n = 0
for i in range(1930, 4355):
    if "\\begin{statement}" in t[i]:
        body = " ".join(t[i:i + 4])
        if n < 6:
            print(i + 1, body[:220])
        n += 1
