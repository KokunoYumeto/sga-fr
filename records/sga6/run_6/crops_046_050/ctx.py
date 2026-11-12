"""Print the context of literal patterns in both layers of SGA 6 main.tex.
usage: python -I ctx.py PATTERN_FILE   (one literal pattern per line; <NL> stands for a line break)"""
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
pats = [p.replace("<NL>", "\n") for p in pathlib.Path(sys.argv[1]).read_text(encoding="utf-8").splitlines() if p]
for layer in ("diplomatic", "current"):
    t = (W / layer / "main.tex").read_text(encoding="utf-8")
    print("==", layer)
    for p in pats:
        i = t.find(p)
        n = t.count(p)
        if i < 0:
            print("  NOT FOUND:", repr(p))
            continue
        line = t.count("\n", 0, i) + 1
        print(f"  [{n}x, line {line}]", repr(t[max(0, i - 70):i + len(p) + 70]))
