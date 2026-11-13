"""Check that the example strings quoted in the convention notes occur in the page files (read only)."""
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
B = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\b396_400")
ex = [
    (396, r"la classe de \(F_j\), et"),
    (396, r"la classe de \(E\). Enfin"),
    (400, r"Soient \(F_1,F_2\) les faisceaux"),
    (396, r"\(X=D_\pi(E)\)"),
    (397, r'D(E)=D(F) \arrow[r,"h"]'),
    (400, r"sera noté \(G_S^{n,\infty}\)"),
    (397, r"on considère alors \(\mathbb P(E)\)"),
    (397, r"\mathcal O_{\mathbb P(E)}(1)"),
    (397, r'& \mathbb P(E) \arrow[d,"g"]'),
    (397, r"localement de rang \(n\)"),
    (399, r"c'est homomorphisme"),
    (399, "grassmanienne"),
    (400, "leur classe"),
    (400, r"isomorphisme.~:"),
    (396, "étant effectués du poids"),
]
for page, s in ex:
    t = (B / f"page_{page}.tex").read_text(encoding="utf-8")
    print(page, t.count(s), s)
