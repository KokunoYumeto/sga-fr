"""One-off patch of build_findings.py: make two olds unique across pages 391-395."""
p = "C:/Users/user/Documents/sga_scan_check_20261105/run_5/crops_391_395/build_findings.py"
s = open(p, encoding="utf-8").read()
a = r'''"symbol", "high", r"\lambda_n^*(\sigma_2)", r"\lambda_n^\natural(\sigma_2)",'''
b = r'''"symbol", "high", r"=" + NL + r"\lambda_n^*(\sigma_2)", r"=" + NL + r"\lambda_n^\natural(\sigma_2)",'''
c = r'''"punctuation", "high", r"si $g\ne e$,", r"si $g\ne e$:", "The TeX has a comma for the colon.")'''
d = r'''"punctuation", "high", r"donne, si $g\ne e$,", r"donne, si $g\ne e$:", "The TeX has a comma for the colon.")'''
assert s.count(a) == 1 and s.count(c) == 1, (s.count(a), s.count(c))
s = s.replace(a, b).replace(c, d)
open(p, "w", encoding="utf-8", newline="\n").write(s)
print("patched")
