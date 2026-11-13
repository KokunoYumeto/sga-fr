"""check_conv.py: the forms quoted in the convention entries occur once in their page files (read only)."""
import pathlib, sys
sys.stdout.reconfigure(encoding="utf-8")
B = pathlib.Path(__file__).resolve().parent.parent / "b556_560"
forms = {
    556: [r"\(s\in\operatorname{S\ell}(n)(Y)\)", r"\(\operatorname{G\ell}(n)(Y')\)", r"et \(n\) constant",
          r"matrice \(a=(a_{ij})", r"\(c_{h,k,\lambda}a\) en ajoutant", r"colonne de \(a\)",
          r"la matrice \(ac_{h,k,\lambda}\)", r"ligne de \(a\)"],
    559: [r"Soient \(e\) l'objet", r"\Spec(\mathcal O(e))"],
    560: [r"\in K^\circ(Y).", r"structure de \(K^\circ(Y)\)-module", r"avec \(K^\circ(X)\), \(K^\circ(Y)\)"],
}
for n, fs in forms.items():
    t = (B / f"page_{n}.tex").read_text(encoding="utf-8")
    for f in fs:
        print(n, t.count(f), f)
    if n == 560:
        print(560, "K^\\circ total", t.count("K^\\circ"))
