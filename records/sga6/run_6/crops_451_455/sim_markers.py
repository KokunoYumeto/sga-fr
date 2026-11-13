"""State of the two marker moves (folios 451, 456) in both layers of main.tex, simulated in memory; prints counts,
line numbers and the result. Also compares the text of folios 451-455 in main.tex with the page files."""
import pathlib, sys
sys.stdout.reconfigure(encoding='utf-8')
ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
B = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\b451_455")
NL = "\n"
M451 = "%%%%%%%%%%  scan idx 464  |  folio 451  %%%%%%%%%%"
M456 = "%%%%%%%%%%  scan idx 469  |  folio 456  %%%%%%%%%%"
EDITS = [
    ("en appliquant la formule de" + NL + M451 + NL + "projection :" + NL + r"\[",
     "en appliquant la formule de" + NL + "projection :" + NL + M451 + NL + r"\["),
    (r"\subsection*{4.7}" + NL + NL + "On" + NL + M456 + NL + "revient à la situation",
     M456 + NL + r"\subsection*{4.7}" + NL + NL + "On" + NL + "revient à la situation"),
]
pages = "".join((B / f"page_{p}.tex").read_text(encoding="utf-8").split(NL, 1)[1] for p in range(451, 456))
for layer in ("diplomatic", "current"):
    t = (ROOT / layer / "main.tex").read_text(encoding="utf-8")
    for old, new in EDITS:
        n_old, n_new = t.count(old), t.count(new)
        pos = t.find(old if n_old else new)
        line = t[:pos].count(NL) + 1
        print(layer, "old count", n_old, "new count", n_new, "at lines", line, "-", line + old.count(NL))
        if n_old == 1:
            t = t.replace(old, new, 1)
    # text of folios 451-455 after both moves, against the page files after the same moves
    p2 = pages
    for old, new in EDITS:
        p2 = p2.replace(old, new, 1)
    a = t.find(M451)
    b = t.find(M456)
    seg = t[a:b]
    p2seg = p2[p2.find(M451):p2.find(M456)]
    print("   folios 451-455 equal to page files (after the moves):", seg == p2seg)
    if seg != p2seg:
        import difflib
        for l in difflib.unified_diff(p2seg.split(NL), seg.split(NL), lineterm="", n=0):
            print("   ", l)
