import pathlib

p = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\crops_216_220\make_findings.py")
s = p.read_text(encoding="utf-8")
BS = chr(92)
old = "of Exposé V a " + BS + "tag{S});"
new = "of Exposé V a " + BS + BS + "tag{S});"
assert s.count(old) == 1, s.count(old)
s = s.replace(old, new, 1)
p.write_text(s, encoding="utf-8")
print("ok")
