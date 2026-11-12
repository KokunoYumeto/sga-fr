import pathlib
p = pathlib.Path(r'C:\Users\user\Documents\sga_scan_check_20261105\run_6\crops_241_245\write_findings.py')
s = p.read_text(encoding='utf-8')
old = "Per-page \\\\ob edits of later batches stay harmless after this change."
assert s.count(old) == 1, s.count(old)
new = old + " The same line recurs in main.tex for later exposés (lines 6540, 7189, 13288, 17025): apply this edit inside the folio-245 span only."
p.write_text(s.replace(old, new), encoding='utf-8')
print('patched')
