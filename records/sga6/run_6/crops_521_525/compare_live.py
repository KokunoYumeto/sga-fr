"""compare_live.py: compare page_521..525.tex with the live main.tex (both layers) between the folio-521 and folio-526 markers (read only)."""
import pathlib, re, sys, difflib
sys.stdout.reconfigure(encoding='utf-8')
ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
B = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\b521_525")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
pl = []
for n in range(521, 526):
    t = B.joinpath(f"page_{n}.tex").read_text(encoding="utf-8").split("\n")[1:]
    if t and t[-1] == "":
        t.pop()
    pl += t
for layer in ("diplomatic", "current"):
    lines = (ROOT / layer / "main.tex").read_text(encoding="utf-8").split("\n")
    a = next(i for i, l in enumerate(lines) if (m := MARK.search(l)) and m.group(2) == "521")
    b = next(i for i, l in enumerate(lines) if (m := MARK.search(l)) and m.group(2) == "526")
    seg = lines[a:b]
    d = list(difflib.unified_diff(pl, seg, "pages", layer, lineterm="", n=0))
    print(layer, "lines", a + 1, "-", b, "identical" if not d else "DIFFERS")
    for x in d[:40]:
        print("   ", x[:220])
