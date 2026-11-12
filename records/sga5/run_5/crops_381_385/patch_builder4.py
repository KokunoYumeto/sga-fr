"""Fourth one-off patch of build_findings.py: file-unique olds for two paragraph findings on p. 384."""
import pathlib

p = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\crops_381_385\build_findings.py")
s = p.read_text(encoding="utf-8")
R = [
    (r'''"other", "high", "\\]" + NL + "Les ", "\\]" + NL + NL + "Les ",''',
     r'''"other", "high", "\\tag{4.2.2}" + NL + "\\]" + NL + "Les ",
    "\\tag{4.2.2}" + NL + "\\]" + NL + NL + "Les ",'''),
    (r'''"other", "high", "\\]" + NL + "Le caractère",
    "\\]" + NL + NL + "Le caractère",''',
     r'''"other", "high", "\\]" + NL + "Le caractère $\\sigma'_{y'}$",
    "\\]" + NL + NL + "Le caractère $\\sigma'_{y'}$",'''),
]
for a, b in R:
    n = s.count(a)
    assert n == 1, (n, a)
    s = s.replace(a, b)
p.write_text(s, encoding="utf-8", newline="")
print("patched", len(R))
