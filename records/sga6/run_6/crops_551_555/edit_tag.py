import pathlib
p = pathlib.Path(r'C:\Users\user\Documents\sga_scan_check_20261105\run_6\findings_551_555.json')
s = p.read_text(encoding='utf-8')
BS = chr(92)
old = '"tex": "' + BS + BS + 'tag{6.1.3} (on p. 552 and here)",'
new = '"tex": "' + BS + BS + 'tag{6.1.3}",'
assert s.count(old) == 1, s.count(old)
s = s.replace(old, new)
old2 = 'The TeX keeps the printed reading. The print numbers two formulas (6.1.3)'
new2 = 'The TeX keeps the printed reading (' + BS + BS + 'tag{6.1.3} here and on p. 552). The print numbers two formulas (6.1.3)'
assert s.count(old2) == 1, s.count(old2)
s = s.replace(old2, new2)
p.write_text(s, encoding='utf-8')
print('done')
