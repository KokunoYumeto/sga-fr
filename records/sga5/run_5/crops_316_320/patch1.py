import pathlib
p = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\crops_316_320\build_findings.py")
t = p.read_text(encoding="utf-8")
old = r"move_marker.py 5 321 \item --before "
new = r"move_marker.py 5 321 '\item' --before "
assert t.count(old) == 1
t = t.replace(old, new)
p.write_text(t, encoding="utf-8", newline="\n")
print("patched")
