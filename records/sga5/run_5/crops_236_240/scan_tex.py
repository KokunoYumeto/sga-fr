import sys, re, collections
sys.stdout.reconfigure(encoding="utf-8")
BS = chr(92)
t = open(r"C:/Users/user/Documents/sga_scan_check_20261105/sga5/diplomatic/s5.tex", encoding="utf-8").read().split(chr(10))
seg = chr(10).join(t[6855:8800])
names = ["varprojlim", "varinjlim", "lim", "Lim", "operatorname{Lim}", "mathrm{Lim}", "underleftarrow", "projlim", "injlim"]
for n in names:
    print(n, seg.count(BS + n))
for i, line in enumerate(t[6855:8800], start=6856):
    if "lim" in line.lower():
        print(i, line[:170])
