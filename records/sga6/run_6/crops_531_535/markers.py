"""markers.py: print the lines around the folio markers 531-536 in sga6/<layer>/main.tex (read only)."""
import pathlib, re, sys
sys.stdout.reconfigure(encoding='utf-8')
ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
for layer in ("diplomatic", "current"):
    lines = (ROOT / layer / "main.tex").read_text(encoding="utf-8").split("\n")
    print("=====", layer, len(lines))
    for i, l in enumerate(lines, 1):
        m = MARK.search(l)
        if m and 531 <= int(m.group(2)) <= 536:
            for j in range(max(1, i - 3), min(len(lines), i + 2) + 1):
                print(j, "|", lines[j - 1][:200])
            print("--")
