import pathlib
p = pathlib.Path("C:/Users/user/Documents/sga_scan_check_20261105/run_5/crops_271_275/make_findings.py")
s = p.read_text(encoding="utf-8")
a1 = 'here (renewed at the start of Exposé V, "\n      "s5.tex l. 6860, and not reset for Exposé VI).")'
b1 = 'here (renewed with the scoped definitions "\n      "before the heading of Exposé V and not reset for Exposé VI).")'
a2 = 'These are the first ¤R of Exposé VI (s5.tex l. 9115).")'
b2 = 'These are the first ¤R of Exposé VI.")'
assert s.count(a1) == 1 and s.count(a2) == 1
s = s.replace(a1, b1).replace(a2, b2)
p.write_text(s, encoding="utf-8", newline="\n")
print("ok")
