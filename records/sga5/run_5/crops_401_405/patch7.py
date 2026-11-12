"""Make the old of the (**) '!' fix on p. 401 unique across pp. 401-405 (edits build_findings.py only)."""
p = "C:/Users/user/Documents/sga_scan_check_20261105/run_5/crops_401_405/build_findings.py"
s = open(p, encoding="utf-8").read()
a = r'''  r"(\RG_{!V}", r"(\R_!\Gamma_V",'''
b = r'''  r"(**)\qquad¶\clK{\Delta}(\RG_{!V}", r"(**)\qquad¶\clK{\Delta}(\R_!\Gamma_V",'''
assert s.count(a) == 1, s.count(a)
s = s.replace(a, b)
open(p, "w", encoding="utf-8", newline="\n").write(s)
print("patched")
