"""Compare the extracted page files (b046_050, b041_045) with the current spans of s5.tex (read only)."""
import pathlib, re, sys, difflib
sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
t = (W / "sga5" / "diplomatic" / "s5.tex").read_text(encoding="utf-8")
ms = list(MARK.finditer(t))
span = {}
for i, m in enumerate(ms):
    end = ms[i + 1].start() if i + 1 < len(ms) else len(t)
    span[int(m.group(2))] = t[m.start():end]
for n in range(45, 51):
    d = "b041_045" if n <= 45 else "b046_050"
    p = (W / "run_5" / d / f"page_{n:03d}.tex").read_text(encoding="utf-8")
    body = p.split("\n", 1)[1]  # drop '% from s5.tex'
    s = span[n]
    same = body.rstrip("\n") == s.rstrip("\n")
    print(n, "same" if same else "DIFFERENT")
    if not same:
        for l in difflib.unified_diff(body.splitlines(), s.splitlines(), lineterm="", n=0):
            print("   ", l[:160])
