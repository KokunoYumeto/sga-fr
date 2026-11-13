import sys
sys.stdout.reconfigure(encoding='utf-8')
base = r"C:\Users\user\Documents\sga_scan_check_20261105\sga6"
M643 = "%%%%%%%%%%  scan idx 656  |  folio 643  %%%%%%%%%%"
M646 = "%%%%%%%%%%  scan idx 659  |  folio 646  %%%%%%%%%%"
pairs = [
    ("643 old", "ainsi (ii) implique (i). D'%\n" + M643 + "\nautre part,"),
    ("643 new", "ainsi (ii) implique\n" + M643 + "\n(i). D'autre part,"),
    ("646 old", "on a}\n\\[\n  \\chi(F\\otimes L)=\\chi(F);\n\\]\n\\item\n" + M646 + "\n"),
    ("646 new", "on a}\n" + M646 + "\n\\[\n  \\chi(F\\otimes L)=\\chi(F);\n\\]\n\\item\n"),
]
for layer in ("diplomatic", "current"):
    txt = open(base + "\\" + layer + "\\main.tex", encoding="utf-8").read()
    for name, s in pairs:
        print(layer, name, txt.count(s))
