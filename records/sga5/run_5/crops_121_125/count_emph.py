import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
t = open(r"C:/Users/user/Documents/sga_scan_check_20261105/sga5/diplomatic/s5.tex", encoding="utf-8").read().split("\n")
seg = "\n".join(t[1930:4368])
print("emph", len(re.findall(r"\\emph\{", seg)))
print("underline (text)", len(re.findall(r"\\underline\{[^\\$]", seg)))
print("textit", len(re.findall(r"\\textit\{", seg)))
for m in re.finditer(r"\\underline\{[^}]*\}", seg):
    print("  ", m.group(0)[:60])
