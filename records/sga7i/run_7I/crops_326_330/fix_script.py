import pathlib
p = pathlib.Path(r"C:/Users/user/Documents/sga_scan_check_20261105/run_7I/crops_326_330/write_findings.py")
s = p.read_text(encoding="utf-8")
bs = chr(92)
old = '"tex": "' + bs + 'underline{est de rang unipotent nul} (cf. 1.5.5).",'
new = '"tex": chr(92) + "underline{est de rang unipotent nul} (cf. 1.5.5).",'
assert s.count(old) == 1, s.count(old)
s = s.replace(old, new)
p.write_text(s, encoding="utf-8")
print("patched")
