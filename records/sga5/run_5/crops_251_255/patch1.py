import pathlib

p = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\crops_251_255\make_findings.py")
t = p.read_text(encoding="utf-8")
anchor = 'add(255, "\'Soit maintenant X un préschéma localement noethérien connexe.\'",'
assert t.count(anchor) == 1, t.count(anchor)
item = r'''add(255, "Rappels 1.2.3, 'revêtements étales de T munis d'une structure de X-groupe abélien'",
    "X-groupe abélien (a typed X; the sentence is about a préschéma T)",
    r"\(X\)-groupe abélien", "misprint_in_print", "medium",
    None,
    "Wrong letter: the étale coverings and the sheaves are on T, so the group structure is over T. The TeX keeps "
    "the printed X.",
    corrected=r"\(T\)-groupe abélien")

'''
t = t.replace(anchor, item + anchor, 1)
p.write_text(t, encoding="utf-8")
print("patched")
