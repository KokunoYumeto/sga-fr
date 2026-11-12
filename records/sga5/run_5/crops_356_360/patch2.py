import pathlib

p = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\crops_356_360\build_findings.py")
s = p.read_text(encoding="utf-8")
old = r"""r"As the file's '\emph{Démonstration}.' in Exposé II (s5.tex lines 1714, 1888).")"""
new = r"""r"As the file's own '\emph{Démonstration}.' at s5.tex lines 1714 and 1888.")"""
print(s.count(old))
s = s.replace(old, new)
p.write_text(s, encoding="utf-8")
