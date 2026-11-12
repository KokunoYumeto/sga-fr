import pathlib

p = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\crops_176_180\build_findings.py")
t = p.read_text(encoding="utf-8")
bad = 'r"\\arrow[d,""M\\lten\\Tr_{B/A}""]".replace(\'""\', \'"\')'
good = 'r\'\\arrow[d,"M\\lten\\Tr_{B/A}"]\''
print("occurrences:", t.count(bad))
t = t.replace(bad, good)
p.write_text(t, encoding="utf-8", newline="\n")
print([l for l in t.splitlines() if "Tr_{B/A}" in l])
