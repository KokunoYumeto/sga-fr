import pathlib
H = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\crops_246_250")
p = H / "build_findings.py"
s = p.read_text(encoding="utf-8")
a0 = s.index("M248 = (")
a1 = s.index("items = [")
s = s[:a0] + (H / "block.txt").read_text(encoding="utf-8") + s[a1:]
assert "\x08" not in s
p.write_text(s, encoding="utf-8")
print("patched")
