"""Find (re)definitions of given macros in both layers of main.tex (read only)."""
import pathlib, sys, re
sys.stdout.reconfigure(encoding='utf-8')
ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
names = sys.argv[1:]
for layer in ("diplomatic", "current"):
    t = (ROOT / layer / "main.tex").read_text(encoding="utf-8")
    lines = t.split("\n")
    print("=====", layer)
    for i, l in enumerate(lines, 1):
        for n in names:
            if re.search(r"(newcommand|renewcommand|providecommand|DeclareMathOperator|\def)\*?\s*\{?\\" + n + r"(?![A-Za-z])", l):
                print(i, l[:200])
