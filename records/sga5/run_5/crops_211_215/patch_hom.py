"""One-off: itemize the underlined functor-category Hom (\\uHom) in make_findings.py."""
import pathlib

p = pathlib.Path(__file__).with_name("make_findings.py")
s = p.read_text(encoding="utf-8")

reps = [
    # A: Definition 2.4.2, first sentence
    (r'''    r"\emph{à translations près, et on note} $\Hom",
    "Underlined statement. The Hom of Hom_AR(N°,C) is underlined too (see the coordinator message on underlined Hom).")''',
     r'''    r"\emph{à translations près, et on note} $\uHom",
    "Underlined statement; the Hom of the functor category Hom_AR(N°,C) is underlined too (\\uHom, as on pp. 207-208).")'''),
    # B: item (i)
    (r'''    r"\item \emph{Les objets de} $\Hom_{AR}(\NN^\circ,\cC)$ \emph{sont les objets de} $\Hom(\NN^\circ,\cC)$.",
    "Underlined statement; the final full stop is not underlined.")''',
     r'''    r"\item \emph{Les objets de} $\uHom_{AR}(\NN^\circ,\cC)$ \emph{sont les objets de} $\uHom(\NN^\circ,\cC)$.",
    "Underlined statement, with the underlined Hom of both functor categories (\\uHom); the final full stop is not "
    "underlined.")'''),
    # C: item (ii)
    (r'''    r"\item \emph{Si} $X$ \emph{et} $Y$ \emph{sont deux objets de} $\Hom(\NN^\circ,\cC)$, \emph{un morphisme de} $X$ "
    r"\emph{dans} $Y$ \emph{dans la catégorie} $\Hom_{AR}(\NN^\circ,\cC)$ \emph{est un élément de l'ensemble}",
    "Underlined statement.")''',
     r'''    r"\item \emph{Si} $X$ \emph{et} $Y$ \emph{sont deux objets de} $\uHom(\NN^\circ,\cC)$, \emph{un morphisme de} $X$ "
    r"\emph{dans} $Y$ \emph{dans la catégorie} $\uHom_{AR}(\NN^\circ,\cC)$ \emph{est un élément de l'ensemble}",
    "Underlined statement, with the underlined Hom of the functor categories (\\uHom).")'''),
    # D + E: 'et' and the two underlined Hom of the P = ... display
    (r'''    r"P=\Hom(\NN^\circ,\cC),\qquad P_{AR}", r"P=\Hom(\NN^\circ,\cC)\quad\text{et}\quad P_{AR}",
    "The print joins the two definitions with 'et' (run in the text); the TeX replaces the word by a comma "
    "(display against run-in text is not reported).")''',
     r'''    r",\qquad P", r"\quad\text{et}\quad P",
    "The print joins the two definitions with 'et' (run in the text); the TeX replaces the word by a comma "
    "(display against run-in text is not reported).")
add(215, "Dans la suite ...", "P = Hom(N°,C) with Hom underlined", r"P=\Hom(\NN^\circ,\cC)", "underline", "high",
    r"P=\Hom(", r"P=\uHom(",
    "The print underlines the Hom of the functor categories Hom(N°,C), Hom_AR(N°,C) on pp. 212-215 (as on p. 207, "
    "written \\uHom there); the Hom of morphism sets (Hom_AR(X,Y), Hom(X[r],Y), Hom_P) is plain in print and TeX.")
add(215, "Dans la suite ...", "P_AR = Hom_AR(N°,C) with Hom underlined", r"P_{AR}=\Hom_{AR}(\NN^\circ,\cC)",
    "underline", "high", r"_{AR}=\Hom_{AR}", r"_{AR}=\uHom_{AR}", "As the preceding finding.")'''),
    # F: heading 2.4 on p. 212
    (r'''    "Underlined title ending with a full stop in the print; the TeX drops it.")''',
     r'''    "Underlined title ending with a full stop in the print; the TeX drops it.")
add(212, "heading 2.4", "Hom_AR(N°,C) with Hom underlined (functor category)", r"$P_{AR}=\Hom_{AR}(\NN^\circ,\cC)$",
    "underline", "high", r"P_{AR}=\Hom", r"P_{AR}=\uHom",
    "The print underlines the Hom of the functor categories Hom(N°,C), Hom_AR(N°,C) on pp. 212-215 (as on pp. "
    "207-208, where \\uHom was used). The underline of 'La catégorie' is the accepted title underline.")'''),
]
for a, b in reps:
    print(s.count(a), a[:70].replace("\n", " "))
    s = s.replace(a, b)
p.write_text(s, encoding="utf-8")
