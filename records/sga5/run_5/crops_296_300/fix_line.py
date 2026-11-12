p = r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\crops_296_300\build_findings.py"
L = open(p, encoding="utf-8").read().split("\n")
L[124] = '           r\'\'\'\\arrow[r,"\\varepsilon^*"\'] (label below)\'\'\', "other", "medium",'
open(p, "w", encoding="utf-8", newline="\n").write("\n".join(L))
print(L[124])
