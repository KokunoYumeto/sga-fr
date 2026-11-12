import json
import os

RUN = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II"
BATCH = os.path.join(RUN, "b201_205")
OUT = os.path.join(RUN, "findings_201_205.json")

P204_OLD = (r"\underline{Proposition 2.1. Soient $S$ une courbe projective lisse et connexe sur un corps "
            r"algébriquement clos $k$, $X$ une variété propre et lisse sur $k$, purement de dimension $n+1$, "
            r"et $f:X\to S$ un morphisme lisse en dehors d'un ensemble fini $F$ de points de $X$. Les "
            r"caractéristiques d'Euler-Poincaré (en cohomologie étale) de $S$, $X$ et de la fibre générique "
            r"géométrique $X_{\bar\eta}$ de $f$ vérifient alors}")
P204_NEW = (r"\underline{Proposition} 2.1. \underline{Soient} $S$ \underline{une courbe projective lisse et "
            r"connexe sur un corps algébriquement clos} $k$, $X$ \underline{une variété propre et lisse sur} "
            r"$k$, \underline{purement de dimension} $n+1$, \underline{et} $f:X\to S$ \underline{un morphisme "
            r"lisse en dehors d'un ensemble fini} $F$ \underline{de points de} $X$. \underline{Les "
            r"caractéristiques d'Euler-Poincaré (en cohomologie étale) de} $S$, $X$ \underline{et de la fibre "
            r"générique géométrique} $X_{\bar\eta}$ \underline{de} $f$ \underline{vérifient alors}")

findings = [
    {
        "page": 201,
        "where": "paragraph before the display, list of characters: 'a_I , le caractère de la représentation d'Artin'",
        "scan": "a_I: subscript I without a prime (checked at 2x); u_{I'} later in the same sentence has a clear prime",
        "tex": r"$a_I$ , le caractère de la représentation d'Artin",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": r"$a_{I'}$ , le caractère de la représentation d'Artin",
        "note": "Missing prime: all the characters of the sentence live on the finite quotient I' = I/H' (the display below uses a_{I'}; p. 202: a_{I'} = u_{I'} + Sw_{I'}). The TeX keeps the printed reading. Corrected edition: together with Sw_I of the same sentence (both or neither).",
    },
    {
        "page": 201,
        "where": "same sentence: 'Sw_I , celui de la représentation de Swan'",
        "scan": "Sw_I: subscript I without a prime (checked at 2x)",
        "tex": r"$\mathrm{Sw}_I$ , celui de la représentation de Swan",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": r"$\mathrm{Sw}_{I'}$ , celui de la représentation de Swan",
        "note": "Missing prime, as for a_I (p. 202 uses Sw_{I'} throughout). The TeX keeps the printed reading. Corrected edition: together with a_I (both or neither).",
    },
    {
        "page": 201,
        "where": "display at the foot of the page: mu = (a_{I'},s_{I/H}) = |I'|^{-1} sum_{i in I'} a_{I'}(i)s_{I/H}(i)",
        "scan": "a full stop typed after the display, well to the right (checked at 1.5x)",
        "tex": "a_{I'}(i)s_{I/H}(i)\n\\end{equation*}",
        "kind": "punctuation",
        "confidence": "high",
        "fix": {"old": "a_{I'}(i)s_{I/H}(i)\n\\end{equation*}",
                "new": "a_{I'}(i)s_{I/H}(i) \\quad .\n\\end{equation*}"},
        "note": "The TeX leaves out the full stop; written like the full stops of the displays on p. 202 ('\\quad .').",
    },
    {
        "page": 202,
        "where": "first display block, third line: (Sw_{I'},s_{I/H}) = dim_{Z/l} Hom_I(S(I') (x)_{Z_l} Z/l, Z/l^{I/H})",
        "scan": "no full stop typed after the closing parenthesis: only a tiny dot (3x5 px, 12 px of ink, against 5x5 px and 18-23 px for the typed full stops of the page) under the parenthesis, below the line of subscripts (checked at 3x, pixel-measured)",
        "tex": r"\ \mathbb{Z}/\ell^{I/H}) \quad .",
        "kind": "extra",
        "confidence": "low",
        "fix": {"old": r"\ \mathbb{Z}/\ell^{I/H}) \quad .",
                "new": r"\ \mathbb{Z}/\ell^{I/H})"},
        "note": "The chain of equalities continues on the next line ('= dim ... Coker(...))'), so no full stop belongs here and the dot reads as a speck. If it is taken as a lightly struck full stop instead, it is a stray one (misprint): keep it in the diplomatic and drop it in the corrected edition.",
    },
    {
        "page": 202,
        "where": "Cas 1, first paragraph: 'On peut donc supposer que X_s est le sous-schéma de E^{n+1}_S défini par une équation f'",
        "scan": "X_s, the subscript s clearly printed",
        "tex": r"supposer que $X_s$ est le sous-schéma",
        "kind": "misprint_in_print",
        "confidence": "low",
        "fix": None,
        "corrected": r"supposer que $X$ est le sous-schéma",
        "note": "Author's slip: the equation sum x_i x_{i+m} + a = 0, a in the maximal ideal of V (a uniformizer when X is regular), defines X over S, not its special fibre; Cas 2 and Cas 3 (p. 203) read 'on peut prendre X ⊂ E^{n+1}_S défini par une équation f'. The TeX keeps the printed reading. Review before using in the corrected edition.",
    },
    {
        "page": 202,
        "where": "Cas 1, first paragraph: 'le sous-schéma de E^{n+1}_S'",
        "scan": "a plain typed capital E with a single stem (checked at 8x), whereas the E of O_{E_S^{2m}} in the display at the foot of the page and the E of E^{n+1}_S (twice) and E^1_S on p. 203 are double-struck (double stem)",
        "tex": r"sous-schéma de $\mathbb{E}_S^{n+1}$",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": {"old": r"sous-schéma de $\mathbb{E}_S^{n+1}$",
                "new": r"sous-schéma de $E_S^{n+1}$"},
        "corrected": r"sous-schéma de $\mathbb{E}_S^{n+1}$",
        "note": "The typist left out the second stem of the double-struck E (affine space). The TeX silently corrects; the fix restores the print; 'corrected' is the current TeX.",
    },
    {
        "page": 202,
        "where": "heading 'Cas 1. n = dim(X_s) = 2m - 1'",
        "scan": "a full stop after '2m - 1': a compact dot of 7x7 px without a tail (checked at 8x and pixel-measured); the commas of the page are 10-12 px tall with a tail curving down to the left; the headings Cas 2 and Cas 3 on p. 203 also end with a full stop",
        "tex": r"2m - 1$} ,",
        "kind": "punctuation",
        "confidence": "medium",
        "fix": {"old": r"2m - 1$} ,", "new": r"2m - 1$} ."},
        "note": "The TeX has a comma for the printed full stop.",
    },
    {
        "page": 203,
        "where": "Cas 2, paragraph after the equation: 'Phi^i_{x_o} = 0 pour i ≠ n et Phi^i_{x_o} est de dimension un'",
        "scan": "the second Phi also has the superscript i (checked at 2.5x)",
        "tex": r"et $\Phi^i_{x_o}$ est de dimension un",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": r"et $\Phi^n_{x_o}$ est de dimension un",
        "note": "Wrong index: the only non-zero group is in degree n (Phi^i = 0 for i ≠ n), as in the parallel sentences of Cas 1 (top of the page) and Cas 3. The TeX keeps the printed reading.",
    },
    {
        "page": 204,
        "where": "section heading '2. Le cas \"géométrique\"'",
        "scan": "the underline starts under 'Le'; the number '2.' is not underlined (checked at 2.5x); single underline",
        "tex": r"\underline{2. Le cas ``géométrique''}",
        "kind": "underline",
        "confidence": "high",
        "fix": {"old": r"\underline{2. Le cas", "new": r"2. \underline{Le cas"},
        "note": "As the file writes the heading of section 1 ('1. \\underline{Enoncé du problème}', p. 197).",
    },
    {
        "page": 204,
        "where": "Proposition 2.1, the statement",
        "scan": "the typescript underlines only the words: 'Proposition', 'Soient', 'une courbe projective lisse et connexe sur un corps / algébriquement clos', 'une variété propre et lisse sur', 'purement de di-/mension', 'et', 'un morphisme lisse en dehors d'un ensemble fini', 'de points de', 'Les caractéristiques d'Euler-Poincaré (en cohomologie étale) de', 'et de la fibre générique géométrique', 'de', 'vérifient alors'; the number 2.1., the symbols S, k, X, n+1, f : X → S, F, X_eta-bar, f and the commas and full stop between them are not underlined (checked at 1.5x)",
        "tex": r"\underline{Proposition 2.1. Soient $S$ une courbe ... de $f$ vérifient alors}",
        "kind": "underline",
        "confidence": "high",
        "fix": {"old": P204_OLD, "new": P204_NEW},
        "note": "The TeX puts one underline over the whole statement; the file elsewhere follows the typescript's segments (Propositions 1.12 and 1.13, pp. 201-202).",
    },
    {
        "page": 204,
        "where": "display after 'la dernière classe de Chern du fibré tangent': chi(X) = int c_{n+1}(Theta_X) = (-1)^{n+1} int c_{n+1}(Omega^1_X)",
        "scan": "both integral signs are written without a subscript (checked at 2x)",
        "tex": r"\chi(X)=\int_X c_{n+1}(\Theta_X)=(-1)^{n+1}\int_X c_{n+1}(\Omega_X^1)",
        "kind": "formula",
        "confidence": "high",
        "fix": {"old": r"\chi(X)=\int_X c_{n+1}(\Theta_X)=(-1)^{n+1}\int_X c_{n+1}(\Omega_X^1)",
                "new": r"\chi(X)=\int c_{n+1}(\Theta_X)=(-1)^{n+1}\int c_{n+1}(\Omega_X^1)"},
        "note": "The TeX adds _X to both integrals; the integrals of p. 205 do carry X and X_s in print.",
    },
    {
        "page": 204,
        "where": "last line: 'de la classe totale de Chern de Omega^1_S sur S'",
        "scan": "no punctuation after 'sur S' (checked at 3x); the sentence runs on into the display at the top of p. 205 and 'et les cup-puissances de c^1 sont nulles :'",
        "tex": r"de $\Omega_S^1$ sur $S$.",
        "kind": "punctuation",
        "confidence": "high",
        "fix": {"old": r"de $\Omega_S^1$ sur $S$.", "new": r"de $\Omega_S^1$ sur $S$"},
        "note": "The TeX adds a full stop that the print does not have.",
    },
]

# every fix's old must occur exactly once in its page file (LF line breaks)
ok = True
for f in findings:
    if f["fix"] is None:
        continue
    path = os.path.join(BATCH, "page_%03d.tex" % f["page"])
    with open(path, encoding="utf-8", newline="") as fh:
        text = fh.read()
    n = text.count(f["fix"]["old"])
    if n != 1:
        ok = False
    # an old must not cross a marker line
    if "%%%%%%%%%%" in f["fix"]["old"]:
        ok = False
        print("marker in old:", f["page"])
    print(f["page"], f["kind"], "occurrences:", n)

for f in findings:
    if f["kind"] != "misprint_in_print":
        f.pop("corrected", None)

if ok:
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(findings, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    print("written", OUT, len(findings))
else:
    print("NOT written: an old string is not unique")
