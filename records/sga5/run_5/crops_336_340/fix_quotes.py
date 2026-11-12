import pathlib, sys
sys.stdout.reconfigure(encoding="utf-8")

p = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\crops_336_340\build_findings.py")
lines = p.read_text(encoding="utf-8").split("\n")
targets = [134, 137, 160, 165, 170, 175, 181, 183, 224, 229, 234, 239]
BS = chr(92)
for n in targets:
    s = lines[n - 1]
    a = s.index('r"')
    j = a + 2
    while True:
        k = s.index('"', j)
        if s[k - 1] != BS:
            break
        j = k + 1
    content = s[a + 2:k]
    new_content = content.replace(BS + '"', '"')
    assert not new_content.endswith("'"), n
    lines[n - 1] = s[:a] + "r'''" + new_content + "'''" + s[k + 1:]
    print(n, lines[n - 1].strip()[:160])
p.write_text("\n".join(lines), encoding="utf-8", newline="\n")
