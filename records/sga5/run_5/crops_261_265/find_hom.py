import sys
sys.stdout.reconfigure(encoding="utf-8")
B = chr(92)
p = r"C:\Users\user\Documents\sga_scan_check_20261105\sga5\diplomatic\s5.tex"
L = open(p, encoding="utf-8").read().split("\n")
keys = [B + "Hom(" + B + "mathbb N", B + "uHom(" + B + "mathbb N", B + "Hom(" + B + "NN", B + "uHom(" + B + "NN"]
for i in range(8458, 9357):
    s = L[i]
    for key in keys:
        j = s.find(key)
        while j >= 0:
            print(i + 1, key, "|", s[max(0, j - 30):j + 40])
            j = s.find(key, j + 1)
