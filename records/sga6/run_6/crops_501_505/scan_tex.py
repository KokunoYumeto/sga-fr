"""Locate Exposé IX in both layers of main.tex; count K^\circ and show the folio markers around pp. 498-510."""
import re, sys, pathlib
sys.stdout.reconfigure(encoding='utf-8')
ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
for layer in ("diplomatic", "current"):
    lines = (ROOT / layer / "main.tex").read_text(encoding="utf-8").split("\n")
    print("==", layer, len(lines), "lines")
    marks = {}
    for i, l in enumerate(lines, 1):
        m = re.search(r"folio (\d+) ", l)
        if m:
            marks[int(m.group(1))] = i
        if re.search(r"\\(chapter|section)\*?\{", l) and i > 11000 and i < 14000:
            print("  head", i, l[:140])
    for f in (497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 510, 520, 530):
        print("  folio", f, "line", marks.get(f))
    # count K^\circ between folio 498 and folio 530
    a, b = marks.get(497, 1), marks.get(530, len(lines))
    seg = lines[a - 1:b]
    n = sum(l.count("K^\\circ") for l in seg)
    nb = sum(l.count("K^{\\bullet}") + l.count("K^\\bullet") for l in seg)
    print("  K^\\circ in folios 497-529:", n, "  K^bullet:", nb)
