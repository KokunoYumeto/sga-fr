"""Build findings_111_115.json and check every fix against the page files (nothing else is written).
Checks: each old occurs exactly once in its page_NNN.tex; the fixes of a page apply one after another in JSON order;
braces stay balanced; no old/new touches a marker line."""
import json
import pathlib
import re

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
B = RUN / "b111_115"
OUT = RUN / "findings_111_115.json"
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
pages = {p: (B / f"page_{p}.tex").read_text(encoding="utf-8") for p in range(111, 116)}


def span(page, start, end):
    """The exact text of the page from the first occurrence of start to the end of the next occurrence of end."""
    t = pages[page]
    i = t.index(start)
    j = t.index(end, i) + len(end)
    return t[i:j]


def emph(s):
    return "\\emph{" + s + "}"


F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, confidence=conf, fix=fix)
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- p. 111
add(111, "the site/topos S (underlined in the print) throughout pp. 111-115",
    "X ∈ ob S̲, S̲ par S̲/X, D⁻(_A S̲) (p. 111); Soient S̲ un topos, de S̲ (p. 112)",
    "\\(X\\in\\Ob S\\), \\(S\\) par \\(S_{/X}\\), \\(\\Dpx^-(_A S)\\); Soient \\(S\\) un topos",
    "underline", "high", None,
    "Convention of the transcription, as reported for pp. 84-85, 93-95 and 100: one decision for the exposé, "
    "not a page fix. The underline is distinctive here: the print leaves the final object S plain (p. 111 "
    "'on peut supposer X = S', p. 113 'U au-dessus de S', 'U = S', p. 112 'pour tout U au-dessus de S'), "
    "and the TeX writes both as S.")

old = span(111, "le\nfoncteur dérivé", "f^{-1}(E)\\).")
add(111, "Corollaire 2.16 (statement continued from p. 110): 'le foncteur dérivé du produit tensoriel (E',E) ⟼ ...'",
    "underlined statement: 'le foncteur dérivé du produit tensoriel' underlined",
    "roman", "underline", "high", dict(old=old, new=emph(old)),
    "The statement of 2.16 is in roman in the TeX (its beginning on p. 110 too), where the print underlines it, "
    "as Lemme 2.15.1 and Corollaire 2.14 are in \\emph. Block form as for pp. 98-100.")

old = span(111, "Soient \\(X\\in\\Ob S\\)", "en degré \\(>n+n'\\).")
add(111, "Corollaire 2.16, 'Soient X ∈ ob S, X' = u(X), ... acyclique en degré > n+n'.'",
    "underlined statement (Soient, Alors si, est, pseudo-cohérent, comme objet de, et acyclique en degré, ...)",
    "roman", "underline", "high", dict(old=old, new=emph(old)),
    "Second sentence of the statement. Apply before the D⁻(_{A'}S') entry below (this old contains its text; "
    "JSON order).")

add(111, "Corollaire 2.16, '(comme objet de D⁻(_{A'}S̲'))'",
    "D⁻(_{A'}S̲') (subscript A' with its prime, both scans)", "\\Dpx^-(_A S')",
    "formula", "high",
    dict(old="(comme objet de \\(\\Dpx^-(_A S')\\))", new="(comme objet de \\(\\Dpx^-(_{A'}S')\\))"),
    "E' is a complex of left A'-modules on S'; the same subscript stands in the proof (D⁻(_{A'}S̲')) and in a). "
    "After the block entry above (JSON order); this old is still unique after it.")

add(111, "Corollaire 2.16, 'X' = u(X)'",
    "X' = u(X)", "\\(X'=u(X)\\) (printed reading kept)", "misprint_in_print", "medium", None,
    "The reading is certain (both scans). u is not defined in 2.16: the morphism is given by the functor "
    "f^{-1}: S → S', and in the proof u denotes E'⊗^L_A (applied to (2.13)); X' must be f^{-1}(X), as "
    "U' = f^{-1}(U) in the proof. An author's slip rather than a typing error; for the corrected edition to decide.",
    corrected="\\(X'=f^{-1}(X)\\)")

add(111, "Preuve of 2.16, 'd'autre part si E = (A_U)^p , on a E' ⊗^L_A E = (E'|U')^p'",
    "on a", "alors", "word", "high",
    dict(old="\\), alors \\(E'", new="\\), on a \\(E'"),
    "'on' at the end of the line, 'a E' ⊗ E' at the start of the next (both scans, OCR 'on a').")

add(111, "Corollaire 2.16.1, 'Sous les hypothèses de (2.16), on a :'",
    "'Sous les hypothèses de' and 'on a' underlined", "roman", "underline", "high",
    dict(old="Sous les hypothèses de (2.16), on a :",
         new="\\emph{Sous les hypothèses de} (2.16), \\emph{on a} :"),
    "The reference and the colon are not underlined.")

old = span(111, "Le foncteur \\(\\mathrm Lf^*", ") induit un foncteur")
add(111, "Corollaire 2.16.1 a), 'Le foncteur 𝕃f* : ... (qui n'est autre que le foncteur A' ⊗^L_A) induit un foncteur'",
    "'Le foncteur', 'qui n'est autre que le foncteur', 'induit un foncteur' underlined", "roman",
    "underline", "high", dict(old=old, new=emph(old)),
    "Apply before the 𝕃f* entry below (this old contains it; JSON order).")

add(111, "Corollaire 2.16.1 a), 'Le foncteur 𝕃 f* : D⁻(_A S̲) ⟶ D⁻(_{A'}S̲')'",
    "𝕃 f* (double-struck L, doubled stem, both scans)", "\\mathrm Lf^*", "font", "high",
    dict(old="\\mathrm Lf^*: \\Dpx^-(_A S)\\to", new="\\mathbb{L}f^*: \\Dpx^-(_A S)\\to"),
    "The derived functor of f* is double-struck here and in the display; the L over the tensor sign is a plain "
    "typed L (\\mathrm L right). After the block entry above (JSON order).")

add(111, "Corollaire 2.16.1 a), display '𝕃f* : D⁻(_A S̲)_coh ⟶ D⁻(_{A'}S̲')_coh'",
    "𝕃f* (double-struck)", "\\mathrm Lf^*", "font", "high",
    dict(old="\\mathrm Lf^*: \\Dpx^-(_A S)_{\\coh}", new="\\mathbb{L}f^*: \\Dpx^-(_A S)_{\\coh}"),
    "As the previous entry.")

add(111, "Corollaire 2.16.1 a), '(notation de (2.6)).'",
    "'notation de' underlined", "roman", "underline", "high",
    dict(old="(notation de (2.6)).", new="(\\emph{notation de} (2.6))."), "")

old = span(111, "Si \\(A\\) est commutatif", "\\Dpx^-(S)\\) induit un foncteur")
add(111, "Corollaire 2.16.1 b), 'Si A est commutatif, le foncteur ⊗^L_A : ... induit un foncteur'",
    "'Si', 'est commutatif', 'le foncteur', 'induit un foncteur' underlined", "roman", "underline", "high",
    dict(old=old, new=emph(old)), "")

# ---------------------------------------------------------------- p. 112
add(112, "Exercice 2.16.2, 'Montrer que E ∈ ob D⁻(_A S̲) est n-pseudo-oohérent (resp. pseudo-cohérent)'",
    "n-pseudo-oohérent", "\\(n\\)-pseudo-cohérent (silently corrected)", "misprint_in_print", "high",
    dict(old="\\(n\\)-pseudo-cohérent (resp. pseudo-cohérent) si",
         new="\\(n\\)-pseudo-oohérent (resp. pseudo-cohérent) si"),
    "Typing error, 'oohérent' in both scans (OCR the same); the TeX silently corrects it.",
    corrected="\\(n\\)-pseudo-cohérent (resp. pseudo-cohérent) si")

add(112, "Définition 3.1, first defined term: 'Nous dirons que F est précohérent (relativement à C_o)'",
    "'précohérent' not underlined (the words before and after are)", "\\emph over the whole definition",
    "underline", "high",
    dict(old="est précohérent (relativement", new="est} précohérent \\emph{(relativement"),
    "As Définitions 1.4.3, 2.1 and 2.3 (pp. 93, 95, 98): the defined term is left out of the underline. "
    "Independent of the next two entries.")

add(112, "Définition 3.1, 'où E ∈ ob C_oU, Ker(u) ...'",
    "C̲_{oU} (no comma between the indices; the comma after U belongs to the sentence)", "\\mathcal C_{0,U}",
    "punctuation", "high",
    dict(old="\\mathcal C_{0,U}", new="\\mathcal C_{0U}"),
    "As pp. 91-92, 95 and 100: the TeX adds the comma between the indices.")

add(112, "Définition 3.1, second defined term: 'Nous dirons que F est cohérent (relativement à C_o)'",
    "'cohérent' not underlined", "\\emph over the whole definition", "underline", "high",
    dict(old="est cohérent (relativement", new="est} cohérent \\emph{(relativement"),
    "As the first defined term.")

add(112, "label 'Lemme 3.3'",
    "Lemme 3.3 (no full stop; then 'a) Soit')", "\\textbf{Lemme 3.3.}", "misprint_in_print", "medium",
    dict(old="\\textbf{Lemme 3.3.}", new="\\textbf{Lemme 3.3}"),
    "The typist left out the label's full stop (both scans); the TeX silently supplies it (the bold label itself is "
    "accepted), as 'Proposition 2.7' on p. 100.",
    corrected="\\textbf{Lemme 3.3.}")

add(112, "Lemme 3.3 a), 'Soit'",
    "'Soit' underlined", "roman", "underline", "high",
    dict(old="Soit\n\\[", new="\\emph{Soit}\n\\["),
    "Start of the statement of 3.3 a), which goes on at the top of p. 113 (entry there).")

# ---------------------------------------------------------------- p. 113
old = span(113, "une\nsuite exacte de", "\\(F\\) est de type fini.")
add(113, "Lemme 3.3 a), 'une suite exacte de C_S. Si G est de type fini et H précohérent, F est de type fini.'",
    "underlined statement", "roman", "underline", "high", dict(old=old, new=emph(old)),
    "Statement of a lemma in roman (3.3 a), b), c) all), as 2.4 and 2.5 on pp. 98-99.")

add(113, "Lemme 3.3 b), 'Soit'", "'Soit' underlined", "roman", "underline", "high",
    dict(old="Soit\n\\[\n  F\\longrightarrow", new="\\emph{Soit}\n\\[\n  F\\longrightarrow"), "")

old = span(113, "une suite exacte de \\(\\mathcal C_S\\). Si \\(F\\) est de type fini", "\\(H\\) est précohérent.")
add(113, "Lemme 3.3 b), 'une suite exacte de C_S. Si F est de type fini et G précohérent, H est précohérent.'",
    "underlined statement", "roman", "underline", "high", dict(old=old, new=emph(old)), "")

add(113, "Lemme 3.3 c), 'Soit'", "'Soit' underlined", "roman", "underline", "high",
    dict(old="Soit\n\\[\n  0\\longrightarrow", new="\\emph{Soit}\n\\[\n  0\\longrightarrow"), "")

old = span(113, "une suite exacte de \\(\\mathcal C_S\\). Si \\(F\\) et \\(H\\)", "l'est aussi.")
add(113, "Lemme 3.3 c), 'une suite exacte de C_S. Si F et H sont précohérents (resp. de type fini), G l'est aussi.'",
    "underlined statement", "roman", "underline", "high", dict(old=old, new=emph(old)), "")

add(113, "Preuve of 3.3 b), 'H' ∈ ob C_oU.'",
    "C̲_{oU}", "\\mathcal C_{0,U}", "punctuation", "high",
    dict(old="\\mathcal C_{0,U}", new="\\mathcal C_{0U}"), "As p. 112.")

# ---------------------------------------------------------------- p. 115
add(115, "start of page",
    "p. 114 ends '... il existe des épimorphismes F' --u--> F, H' --v--> H, avec'; p. 115 begins 'F' ∈ ob C_o, H' ∈ ob C_o.'",
    "folio-115 marker before 'avec \\(F'\\in\\Ob\\mathcal C_0\\)'", "marker", "high", None,
    "Page 115 really begins with \\(F'\\in\\Ob\\mathcal C_0\\); 'avec' is the last word of p. 114 (both scans, OCR). "
    "Fix: python -I move_marker.py 6 115 \"\\(F'\\in\\Ob\\mathcal C_0\\)\" (simulated on both layers: "
    "'... \\(H'\\xrightarrow{v}H\\),' / 'avec ' / marker / '\\(F'\\in\\Ob\\mathcal C_0\\), \\(H'...'). "
    "No other fix of this file touches these lines.")

add(115, "Preuve of 3.3 c), diagram, the vertical arrow v: H' → H",
    "dashed arrow (both scans; the arrows u and w beside it are solid)", "\\arrow[d,\"v\"] (solid)",
    "symbol", "medium",
    dict(old="\\arrow[d,\"v\"]", new="\\arrow[d,dashed,\"v\"]"),
    "The dashes have the same pattern in both scans, so the break is in the print itself; medium because a faint "
    "hand-drawn stroke could reproduce like this.")

add(115, "'On en déduit immédiatement le'",
    "no colon after 'le' (both scans, OCR)", "le :", "punctuation", "high",
    dict(old="immédiatement le :", new="immédiatement le"),
    "The TeX adds the colon.")

old = span(115, "La sous-catégorie (strictement)", "cohérents. Soit")
add(115, "Corollaire 3.4, statement before the display",
    "underlined statement (La sous-catégorie, (strictement), pleine de, formée des objets cohérents est stable "
    "par limites projectives, ... sont cohérents. Soit)", "roman", "underline", "high",
    dict(old=old, new=emph(old)),
    "The plural s of 'limites', 'inductives', 'finies' are the typist's added letters (overtyped): the TeX's plural "
    "is the corrected wording.")

old = span(115, "une suite exacte de \\(\\mathcal C_S\\). Si \\(E^0", "\\(E^2\\) aussi.")
add(115, "Corollaire 3.4, after the display: 'une suite exacte de C_S. Si E^o, E^1, E^3, E^4 sont cohérents, E^2 aussi.'",
    "underlined statement", "roman", "underline", "high", dict(old=old, new=emph(old)), "")

old = span(115, "Supposons que les objets de", "sous les conditions de")
add(115, "Corollaire 3.5, 'Supposons que les objets de C_o sont C_o-cohérents (ce qui implique ... sous les conditions de (2.0)).'",
    "underlined statement; the closing reference (2.0)) not", "roman", "underline", "high",
    dict(old=old, new=emph(old)), "The reference and the closing parentheses stay in roman.")

add(115, "Corollaire 3.5 a), 'Conditions équivalentes sur F ∈ ob C_S :'",
    "'Conditions équivalentes sur' underlined", "roman", "underline", "high",
    dict(old="Conditions équivalentes sur \\(F", new="\\emph{Conditions équivalentes sur} \\(F"), "")

old = span(115, "\\item \\(F\\) est de présentation finie;", "finie (2.8).")
new = (old.replace("\\(F\\) est de présentation finie;", "\\(F\\) \\emph{est de présentation finie};")
       .replace("\\(F\\) est cohérent;", "\\(F\\) \\emph{est cohérent};")
       .replace("\\(F\\) est d'\\(\\infty\\)-présentation finie (2.8).",
                "\\(F\\) \\emph{est d'\\(\\infty\\)-présentation finie} (2.8)."))
add(115, "Corollaire 3.5 a), items (i)-(iii)",
    "'est de présentation finie', 'est cohérent', 'est d'∞-présentation finie' underlined", "roman",
    "underline", "high", dict(old=old, new=new), "F and the reference (2.8) stay in roman.")

add(115, "Corollaire 3.5 b), 'Soient F ∈ ob D⁻(C_S), n ∈ Z. On a :'",
    "'Soient' and 'On a' underlined", "roman", "underline", "high",
    dict(old="Soient \\(F\\in\\Ob\\Dpx^-(\\mathcal C_S)\\), \\(n\\in\\mathbb Z\\). On a :",
         new="\\emph{Soient} \\(F\\in\\Ob\\Dpx^-(\\mathcal C_S)\\), \\(n\\in\\mathbb Z\\). \\emph{On a} :"), "")

old = span(115, "F\\ n\\text{-pseudo-cohérent}", "\\text{ de type fini.}")
new = (old.replace("\\text{-pseudo-cohérent}", "\\text{-\\emph{pseudo-cohérent}}")
       .replace("\\text{ cohérent pour }", "\\text{ \\emph{cohérent pour} }")
       .replace("\\text{et }", "\\text{\\emph{et} }")
       .replace("\\text{ de type fini.}", "\\text{ \\emph{de type fini}.}"))
add(115, "Corollaire 3.5 b), display 'F n-pseudo-cohérent ⟺ H^i(F) cohérent pour i ≥ n+1, et H^n(F) de type fini.'",
    "'pseudo-cohérent', 'cohérent pour', 'et', 'de type fini' underlined in the display", "no underline",
    "underline", "high", dict(old=old, new=new),
    "Words inside the display, as \\text{\\emph{...}} on pp. 73-75.")

# ---------------------------------------------------------------- checks
ok = True
for p in range(111, 116):
    t = pages[p]
    seq = t
    for d in [d for d in F if d["page"] == p]:
        fx = d["fix"]
        if not fx:
            continue
        o, n = fx["old"], fx["new"]
        c0 = t.count(o)
        c1 = seq.count(o)
        if c0 != 1 or c1 != 1:
            ok = False
            print("COUNT", p, c0, c1, repr(o[:60]))
        if MARK.search(o) or MARK.search(n):
            ok = False
            print("MARKER", p, repr(o[:60]))
        if o.count("{") - o.count("}") != n.count("{") - n.count("}"):
            ok = False
            print("BRACES", p, repr(o[:60]))
        seq = seq.replace(o, n, 1)
    (RUN / "crops_111_115" / f"applied_{p}.tex").write_text(seq, encoding="utf-8", newline="")
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")
counts = {}
for d in F:
    k = counts.setdefault(d["page"], [0, 0])
    k[1 if d["kind"] == "misprint_in_print" else 0] += 1
print("ok" if ok else "PROBLEMS", len(F), counts)
