"""Second one-off patch of build_findings.py: longer, file-unique olds for five fixes."""
import pathlib

p = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\crops_381_385\build_findings.py")
s = p.read_text(encoding="utf-8")
R = [
    (r'''    "\\otimes_\\Lambda^{\\mathbf L}", "\\otimes_\\Lambda^{\\mathbb{L}}",''',
     r'''    "=\\R\\Gamma^G(\\check P^\\bullet\\otimes_\\Lambda^{\\mathbf L}",
    "=\\R\\Gamma^G(\\check P^\\bullet\\otimes_\\Lambda^{\\mathbb{L}}",'''),
    (r'''"font", "high", "\\R\\Gamma^G(\\check P", "\\mathrm{R}\\Gamma^G(\\check P", "")''',
     r'''"font", "high", "\\[" + NL + "\\R\\Gamma^G(\\check P",
    "\\[" + NL + "\\mathrm{R}\\Gamma^G(\\check P", "")'''),
    (r'''"high", "multiplicité $v_x(g)$", "multiplicité $\\nu_x(g)$", "As Lemme 4.1.")''',
     r'''"high", "multiplicité $v_x(g)$ du point $\\delta(x)$", "multiplicité $\\nu_x(g)$ du point $\\delta(x)$",
    "As Lemme 4.1.")'''),
    (r'''"punctuation", "high", "$-module, ", "$-module,- ",''',
     r'''"punctuation", "high", "\\mathbb Q_\\ell[G_{y'}]$-module, ",
    "\\mathbb Q_\\ell[G_{y'}]$-module,- ",'''),
    (r'''"punctuation", "high", "On a donc", "On a donc:", "")''',
     r'''"punctuation", "high",
    "On a donc" + NL + "\\[" + NL + "a_{y'}(s)=", "On a donc:" + NL + "\\[" + NL + "a_{y'}(s)=", "")'''),
]
for a, b in R:
    n = s.count(a)
    assert n == 1, (n, a)
    s = s.replace(a, b)
p.write_text(s, encoding="utf-8", newline="")
print("patched", len(R))
