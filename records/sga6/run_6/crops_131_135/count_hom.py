import re
import sys

path = r"C:/Users/user/Documents/sga_scan_check_20261105/sga6/diplomatic/main.tex"
lines = open(path, encoding="utf-8").read().split("\n")
lo, hi = int(sys.argv[1]), int(sys.argv[2])
seg = "\n".join(lines[lo - 1:hi])
NA = r"(?![A-Za-z])"
print("Hom total", len(re.findall(r"\\Hom" + NA, seg)))
print("underline Hom", len(re.findall(r"\\underline\{\\Hom\}", seg)))
print("RHom macro", len(re.findall(r"\\RHom" + NA, seg)), "mathrm R Hom", len(re.findall(r"\\mathrm R\s*\\Hom" + NA, seg)))
print("Ho", len(re.findall(r"\\Ho" + NA, seg)))
if len(sys.argv) > 3:
    for i, l in enumerate(lines[lo - 1:hi], start=lo):
        if re.search(r"\\Hom" + NA + r"|\\RHom" + NA, l):
            print(i, l[:160])
