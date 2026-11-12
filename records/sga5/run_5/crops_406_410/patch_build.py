import pathlib

p = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\crops_406_410\build_findings.py")
s = p.read_text(encoding="utf-8")
old = '"tel que les' + chr(92) + chr(92) + 'nrelations suivantes"'
new = '"tel que les' + chr(92) + 'nrelations suivantes"'
assert s.count(old) == 1, s.count(old)
s = s.replace(old, new)
p.write_text(s, encoding="utf-8", newline="\n")
print("patched")
