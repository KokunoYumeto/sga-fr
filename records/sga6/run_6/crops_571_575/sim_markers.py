"""Simulate the three marker moves (folios 571, 572, 575) in memory on both layers of main.tex (no file is written);
print the count of each old string, its line, and the result around the marker. '§' stands for a backslash."""
import pathlib, sys
sys.stdout.reconfigure(encoding='utf-8')
BS = chr(92)
ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
M571 = "%%%%%%%%%%  scan idx 584  |  folio 571  %%%%%%%%%%"
M572 = "%%%%%%%%%%  scan idx 585  |  folio 572  %%%%%%%%%%"
M575 = "%%%%%%%%%%  scan idx 588  |  folio 575  %%%%%%%%%%"
EDITS = [
    ("§textbf{7.11.} On\n" + M571 + "\npeut, pour un schéma",
     M571 + "\n§textbf{7.11.} On peut, pour un schéma"),
    ("et en\n" + M572 + "\nnotant que",
     "et\n" + M572 + "\nen notant que"),
    ("la connexité de §(C_s§), qui\n" + M575 + "\nrésulte de",
     "la connexité\n" + M575 + "\nde §(C_s§), qui résulte de"),
]
EDITS = [(o.replace("§", BS), n.replace("§", BS)) for o, n in EDITS]
for layer in ("diplomatic", "current"):
    t = (ROOT / layer / "main.tex").read_text(encoding="utf-8")
    for old, new in EDITS:
        n = t.count(old)
        pos = t.find(old)
        line = t[:pos].count("\n") + 1 if pos >= 0 else None
        print(layer, "count", n, "starts at line", line)
        if n == 1:
            t = t.replace(old, new, 1)
            p2 = t.find(new)
            print("   ->", repr(t[p2 - 60:p2 + len(new) + 40]))
print("old strings as JSON-ready text:")
import json
for o, n in EDITS:
    print(json.dumps(o, ensure_ascii=False)); print(json.dumps(n, ensure_ascii=False))
