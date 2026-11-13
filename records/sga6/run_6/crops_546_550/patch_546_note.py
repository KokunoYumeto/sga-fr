"""Update the folio-546 marker note in build_findings.py: the move was applied in main.tex while this check ran."""
import pathlib

p = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\crops_546_550\build_findings.py")
t = p.read_text(encoding="utf-8")
old = 'r"\'appelle équivalence numérique ...\'. The checker of p. 545 may report the same boundary: apply once.")'
new = ('r"\'appelle équivalence numérique ...\'. ALREADY APPLIED: when this check ended, both layers of main.tex "\n'
       '    r"had the folio-546 marker above \'\\subsection*{4.5}\' (the p. 545 side of the same boundary); nothing "\n'
       '    r"left to do, do not run the command again.")')
assert t.count(old) == 1, t.count(old)
p.write_text(t.replace(old, new), encoding="utf-8")
print("patched")
