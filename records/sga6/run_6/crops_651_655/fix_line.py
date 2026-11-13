import pathlib

p = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\crops_651_655\build_findings.py")
lines = p.read_text(encoding="utf-8").split("\n")
i = 217
assert lines[i].lstrip().startswith('r"656 ""De'), lines[i]
lines[i] = "    r'656 \"De $s\\ge1$\" --before; then rejoin the split word (r\\'esulte on one line, or r\\'% at the line end), '"
p.write_text("\n".join(lines), encoding="utf-8")
print(lines[i])
