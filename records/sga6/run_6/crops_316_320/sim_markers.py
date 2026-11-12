"""Simulate (in memory only) the marker moves and the joint display edit proposed in findings_316_320.json
on both layers of SGA 6 main.tex; print the regions after the edit. Writes nothing."""
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
M317 = "%%%%%%%%%%  scan idx 330  |  folio 317  %%%%%%%%%%"
M319 = "%%%%%%%%%%  scan idx 332  |  folio 319  %%%%%%%%%%"
M320 = "%%%%%%%%%%  scan idx 333  |  folio 320  %%%%%%%%%%"
M316 = "%%%%%%%%%%  scan idx 329  |  folio 316  %%%%%%%%%%"

EDITS = [
    ("marker 317",
     "pour la théorie générale des \\(\\lambda\\)-anneaux.\n\\item\n" + M317 + "\nSoit \\(A\\)",
     "pour la théorie générale des\n" + M317 + "\n\\(\\lambda\\)-anneaux.\n\\item\nSoit \\(A\\)"),
    ("marker 319",
     "pour éviter des confusions,\n" + M319 + "\nnous choisirons",
     "pour éviter des confusions, nous\n" + M319 + "\nchoisirons"),
    ("marker 320",
     "la valeur de \\(Q_{2,2}\\) :\n\\[\n  Q_{2,2}(X_1,X_2,X_3,X_4)=X_1X_3-X_4.\n\\]\n\n" + M320 + "\nIndiquons",
     "la valeur de \\(Q_{2,2}\\) :\n" + M320 + "\n\\[\n  Q_{2,2}(X_1,X_2,X_3,X_4)=X_1X_3-X_4.\n\\]\n\nIndiquons"),
    ("display 315 part",
     "\\text{si } p\\geq n,\\\\\n" + M316 + "\n",
     "\\text{si } p\\geq n,\n\\end{gathered}\n\\]\n" + M316 + "\n"),
    ("display 316 part",
     "  F^p\\Lambda^n(E)=\\Lambda^n(E),\\quad \\text{et si } p<0,\\quad F^p\\Lambda^n(E)=0.\n\\end{gathered}\n\\]\nCeci définit",
     "\\(F^p\\Lambda^n(E)=\\Lambda^n(E)\\), et si \\(p<0\\), \\(F^p\\Lambda^n(E)=0\\). Ceci définit"),
]

for layer in ("diplomatic", "current"):
    t = (ROOT / layer / "main.tex").read_text(encoding="utf-8")
    for name, old, new in EDITS:
        n = t.count(old)
        print(layer, name, "occurrences:", n)
        if n == 1:
            t = t.replace(old, new)
    if layer == "diplomatic":
        for key in (M316, M317, M319, M320):
            k = t.find(key)
            print("-----", key[-12:-11], key)
            print(t[k - 260:k + 200])
