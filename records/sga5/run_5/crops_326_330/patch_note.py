"""One-off patch of build_findings.py: correct the line numbers in the p. 326 marker note."""
import pathlib

p = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\crops_326_330\build_findings.py")
t = p.read_text(encoding="utf-8")
old = "s5.tex line 11009, current 11005, at the time of the check). Exact fix:"
new = "s5.tex line 11006, current 11002, at the time of the check; the marker stands at 11009 and 11005). Exact fix:"
assert t.count(old) == 1
p.write_text(t.replace(old, new), encoding="utf-8", newline="\n")
print("patched")
