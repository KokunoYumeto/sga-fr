"""Fifth one-off patch of build_findings.py: say which line numbers are those of the batch extraction."""
import pathlib

p = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\crops_381_385\build_findings.py")
s = p.read_text(encoding="utf-8")
R = [(r'''(diplomatic s5.tex line 12937, current 12933)''',
      r'''(diplomatic s5.tex line 12937, current 12933 at the batch extraction)''')]
for a, b in R:
    assert s.count(a) == 1, a
    s = s.replace(a, b)
p.write_text(s, encoding="utf-8", newline="")
print("patched", len(R))
