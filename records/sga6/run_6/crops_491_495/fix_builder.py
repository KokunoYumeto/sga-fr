import pathlib
p = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\crops_491_495\build_findings.py")
t = p.read_text(encoding="utf-8")
NL = chr(10)
BS = chr(92)
bad1 = 'newline="' + NL + '").write(t)'
good1 = 'newline="' + BS + 'n").write(t)'
bad2 = 'newline="' + NL + '").write(json.dumps(findings, ensure_ascii=False, indent=1) + "' + NL + '")'
good2 = 'newline="' + BS + 'n").write(json.dumps(findings, ensure_ascii=False, indent=1) + "' + BS + 'n")'
assert t.count(bad1) == 1 and t.count(bad2) == 1, (t.count(bad1), t.count(bad2))
t = t.replace(bad1, good1).replace(bad2, good2)
open(p, "w", encoding="utf-8", newline=NL).write(t)
print("fixed")
