"""marker_check.py: count the old strings of the proposed main.tex marker edits in both layers and
simulate the edits in memory (read only; nothing is written)."""
import pathlib, re, sys
sys.stdout.reconfigure(encoding='utf-8')
ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
M532 = "%%%%%%%%%%  scan idx 545  |  folio 532  %%%%%%%%%%"
M534 = "%%%%%%%%%%  scan idx 547  |  folio 534  %%%%%%%%%%"
M536 = "%%%%%%%%%%  scan idx 549  |  folio 536  %%%%%%%%%%"
EDITS = [
    ("532", "divisible par un\n" + M532 + "\nnombre premier",
            "divisible par\n" + M532 + "\nun nombre premier"),
    ("534a", "(où $j(x)=x\\otimes1$) est une\n" + M534 + "\napplication polynôme.",
             "(où $j(x)=x\\otimes1$) est une application polynôme."),
    ("534b", "Alors l'application composée\n\\[",
             "Alors l'application composée\n" + M534 + "\n\\["),
    ("536a", "d'Euler-\n" + M536 + "\nPoincaré",
             "d'Euler-Poincaré"),
    ("536b", "immédiatement :\n\n\\textbf{Proposition 2.3.1.}",
             "immédiatement :\n\n" + M536 + "\n\\textbf{Proposition 2.3.1.}"),
]
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
for layer in ("diplomatic", "current"):
    txt = (ROOT / layer / "main.tex").read_text(encoding="utf-8")
    for name, old, new in EDITS:
        print(layer, name, "count", txt.count(old))
    sim = txt
    for name, old, new in EDITS:
        assert sim.count(old) == 1, (layer, name)
        sim = sim.replace(old, new)
    lines = sim.split("\n")
    print("== simulated", layer, "marker counts:",
          {f: sum(1 for l in lines if MARK.search(l) and MARK.search(l).group(2) == f) for f in ("532", "534", "536")})
    for i, l in enumerate(lines):
        m = MARK.search(l)
        if m and m.group(2) in ("532", "534", "536"):
            for j in range(max(0, i - 2), min(len(lines), i + 2)):
                print("   ", j + 1, "|", lines[j][:150])
            print("   --")
