import re, sys, pathlib
sys.stdout.reconfigure(encoding="utf-8")
BS = chr(92)
for layer in ("diplomatic", "current"):
    t = pathlib.Path(rf"C:\Users\user\Documents\sga_scan_check_20261105\sga6\{layer}\main.tex").read_text(encoding="utf-8")
    a = t.find("|  folio 498  ")
    b = t.find("X. Formalisme des intersections")
    v7 = t.find("VII. Immersions r")
    ix = t[a:b]
    vii = t[v7:a]
    print(layer, "IX span chars", a, b)
    print("  IX K^circ:", ix.count("K^" + BS + "circ"), " IX K^{bullet}:", ix.count("K^{" + BS + "bullet}"), " IX K_bullet:", ix.count("K_" + BS + "bullet"))
    print("  VII..VIII K^circ:", vii.count("K^" + BS + "circ"), " K^{bullet}:", vii.count("K^{" + BS + "bullet}"))
    fol = re.findall(r"folio (\d+)", ix)
    print("  IX folios:", fol[0] if fol else None, "-", fol[-1] if fol else None)
    print("  IX D(E):", len(re.findall(r"(?<![A-Za-z\\])D\(E\)", ix)), " D_pi:", ix.count("D_" + BS + "pi"))
    print("  IX mathrm{GL}:", ix.count(BS + "mathrm{GL}"))
    s = t.find("|  folio 511  ")
    e = t.find("|  folio 516  ")
    seg = t[s:e]
    print("  folios 511-515 K^circ:", seg.count("K^" + BS + "circ"), " K^{bullet}:", seg.count("K^{" + BS + "bullet}"))
    print("  folios 511-515 underline:", seg.count(BS + "underline"), " textbf:", seg.count(BS + "textbf"))
