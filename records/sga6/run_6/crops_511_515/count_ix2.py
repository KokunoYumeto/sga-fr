import sys, pathlib, re
sys.stdout.reconfigure(encoding="utf-8")
BS = chr(92)
for layer in ("diplomatic", "current"):
    t = pathlib.Path(rf"C:\Users\user\Documents\sga_scan_check_20261105\sga6\{layer}\main.tex").read_text(encoding="utf-8")
    a = t.find("|  folio 498  ")
    b = t.find("|  folio 519  ")
    ix = t[a:b]
    print(layer, "folios 498-518:")
    for key in ["K^" + BS + "circ", "K^{" + BS + "bullet}", BS + "mathbb S", BS + "mathbb D", "_{0,"]:
        print("  ", key, ix.count(key))
    print("   plain S( :", len(re.findall(r"(?<![A-Za-z\\_^{])S\((?!\))", ix)) , " {S( :", ix.count("{S("))
    print("   plain D( :", len(re.findall(r"(?<![A-Za-z\\])D\(E\)", ix)))
    seg = t[t.find("|  folio 519  "):t.find("|  folio 520  ")]
    print("   folio 519 starts:", repr(seg[:200]))
