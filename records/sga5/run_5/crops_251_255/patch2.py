import pathlib

p = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\crops_251_255\make_findings.py")
t = p.read_text(encoding="utf-8")
pairs = [
    ("(s5.tex line 8490 diplomatic)", "(s5.tex line 8491 diplomatic, 8490 current)"),
    ("simulated in memory on both layers: line 8490 then ends", "simulated in memory on both layers: the line before the marker then ends"),
]
for a, b in pairs:
    assert t.count(a) == 1, (a, t.count(a))
    t = t.replace(a, b, 1)
p.write_text(t, encoding="utf-8")
print("patched")
