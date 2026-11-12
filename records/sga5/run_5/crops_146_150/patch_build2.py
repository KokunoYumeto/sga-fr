p = "C:/Users/user/Documents/sga_scan_check_20261105/run_5/crops_146_150/build_findings.py"
t = open(p, encoding="utf-8").read()
anchor = "# ---------------- checks ----------------\n"
assert t.count(anchor) == 1
block = ('exec(open("C:/Users/user/Documents/sga_scan_check_20261105/run_5/crops_146_150/extra_findings.py", '
         'encoding="utf-8").read())\n'
         'F.sort(key=lambda d: d["page"])\n\n')
if "extra_findings.py" not in t:
    t = t.replace(anchor, block + anchor)
open(p, "w", encoding="utf-8", newline="\n").write(t)
print("patched")
