import sys, re, pathlib
p = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex")
t = p.read_text(encoding="utf-8")
for pat in sys.argv[1:]:
    ms = [m.start() for m in re.finditer(re.escape(pat), t)]
    print(repr(pat), len(ms))
    for s in ms[:4]:
        print("   ", repr(t[max(0, s - 70):s + 70]))
