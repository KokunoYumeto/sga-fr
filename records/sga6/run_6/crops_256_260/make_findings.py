import json, sys, os

RUN = r"C:\Users\user\Documents\sga_scan_check_20261105\run_6"
OUT = os.path.join(RUN, "findings_256_260.json")
N = "\n"
M256 = "%%%%%%%%%%  scan idx 269  |  folio 256  %%%%%%%%%%"
M257 = "%%%%%%%%%%  scan idx 270  |  folio 257  %%%%%%%%%%"
M260 = "%%%%%%%%%%  scan idx 273  |  folio 260  %%%%%%%%%%"
M261 = "%%%%%%%%%%  scan idx 274  |  folio 261  %%%%%%%%%%"

F = []

def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "confidence": conf, "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)

# ---------------- page 256
# (folio-256 marker: already moved in main.tex at 20:52 from batch 251-255; not reported)
add(256, "Corollaire 4.6.1, first line of the display",
    "tor.amp(E_{X_s})_x ⊂ [a,b] (one pair of parentheses, index x outside)",
    r"\tamp((E_{X_s})_x)\subset[a,b]",
    "formula", "high",
    {"old": r"\tamp((E_{X_s})_x)", "new": r"\tamp(E_{X_s})_x"},
    "The TeX adds a second pair of parentheses around (E_{X_s})_x.")

# ---------------- page 257
add(257, "page start",
    "p. 257 begins 'b) parf.amp_{f_i}(E_i) ⊂ [a_i,b_i] pour i = 1, 2'; p. 256 ends '... et acyclique en degré extérieur à [a,b].'",
    r"page_257.tex begins 'extérieur à \([a,b]\).' (end of Prop. 4.7 a), printed on p. 256)",
    "marker", "high", None,
    "The folio-257 marker stands one TeX line too early. Exact fix in main.tex (both layers): replace "
    "'acyclique en degré\\n" + M257 + "\\nextérieur à \\([a,b]\\).\\n\\item' by "
    "'acyclique en degré\\nextérieur à \\([a,b]\\).\\n" + M257 + "\\n\\item', so that page 257 begins with "
    r"'\item \(\parfamp_{f_i}(E_i)'.")

add(257, "Corollaire 4.7.1, first line",
    "Sous les hypothèses de (4.6),",
    "Sous les hypothèses de (4.6),",
    "misprint_in_print", "medium", None,
    "Wrong reference number in the print: f_1, f_2 and f = f_1 x_S f_2 are those of Proposition 4.7 (4.6 has no f_i). "
    "The TeX keeps the printed (4.6). The same one-step slip occurs twice on p. 259 ((4.8) for (4.9)).",
    corrected="Sous les hypothèses de (4.7),")

# ---------------- page 258
add(258, "Proposition 4.8, last sentence ('Par suite, le foncteur Rf_* envoie ...')",
    "D(X)_{S-parf} dans D(Y)_{S-parf} with both 'parf' underlined (not the 'S-')",
    r"envoie \(D(X)_{S\text{-}\parf}\) dans \(D(Y)_{S\text{-}\parf}\)",
    "underline", "high",
    {"old": r"envoie \(D(X)_{S\text{-}\parf}\) dans \(D(Y)_{S\text{-}\parf}\)",
     "new": r"envoie \(D(X)_{S\text{-}\uparf}\) dans \(D(Y)_{S\text{-}\uparf}\)"},
    "The underlined parf of (4.2) (\\uparf), not the statement underline: footnote (1) then states that this category "
    "equals the one with plain parf because X and Y are quasi-compact. In Cor. 4.7.2 and 4.9.1 the typist leaves "
    "plain parf without underline inside underlined statements.")

add(258, "footnote (1)",
    "on a d'ailleurs D(X)_{S-parf (underlined)} = D(X)_{S-parf (plain)}",
    r"\(D(X)_{S\text{-}\parf}=D(X)_{S\text{-}\uparf}\)",
    "underline", "high",
    {"old": r"\(D(X)_{S\text{-}\parf}=D(X)_{S\text{-}\uparf}\)",
     "new": r"\(D(X)_{S\text{-}\uparf}=D(X)_{S\text{-}\parf}\)"},
    "The print underlines the first parf and not the second; the TeX has them the other way round.")

add(258, "Corollaire 4.8.1, end ('le foncteur Rf_* envoie ...')",
    "D(X)_{parf} dans D(Y)_{parf} with both 'parf' underlined",
    r"envoie \(D(X)_{\parf}\) dans \(D(Y)_{\parf}\)",
    "underline", "high",
    {"old": r"envoie \(D(X)_{\parf}\) dans \(D(Y)_{\parf}\)",
     "new": r"envoie \(D(X)_{\uparf}\) dans \(D(Y)_{\uparf}\)"},
    "Footnote (2), D(X)_{underlined parf} = D(X)_{parf}, is already right in the TeX.")

add(258, "Proposition 4.9, end of the statement",
    "RHom(E,f^!(F)) with Hom underlined, R plain",
    r"\RHom(E,f^!(F))",
    "underline", "high",
    {"old": r"\RHom(E,f^!(F))", "new": r"\mathrm R\underline{\Hom}(E,f^!(F))"},
    "\\RHom prints a plain Hom.")

add(258, "Preuve of 4.9, last line",
    "f_*RHom(E,f^!F) with Hom underlined",
    r"f_*\RHom(E,f^!F)",
    "underline", "high",
    {"old": r"f_*\RHom(E,f^!F)", "new": r"f_*\mathrm R\underline{\Hom}(E,f^!F)"},
    "")

# ---------------- page 259
add(259, "first display (théorème de dualité), left side",
    "f_*RHom(E,f^!F) with Hom underlined",
    r"f_*\RHom(E,f^!F)",
    "underline", "high",
    {"old": r"f_*\RHom(E,f^!F)", "new": r"f_*\mathrm R\underline{\Hom}(E,f^!F)"},
    "")

add(259, "first display, the sign between the two sides",
    "≃ (a typed tilde over a dash, no arrowhead)",
    r"\xrightarrow{\sim}",
    "symbol", "high",
    {"old": r"f^!F)\xrightarrow{\sim}", "new": r"f^!F)\simeq"},
    "The same typed sign as in f^! ≃ i^!f'^! on p. 258, which the TeX writes \\simeq.")

add(259, "first display, right side",
    "RHom(f_*(E),F) with Hom underlined",
    r"\RHom(f_*(E),F).",
    "underline", "high",
    {"old": r"\RHom(f_*(E),F).", "new": r"\mathrm R\underline{\Hom}(f_*(E),F)."},
    "")

add(259, "second display (d'après (I 7.7)), left side",
    "RHom(f_*(E),F) with Hom underlined",
    r"\RHom(f_*(E),F)\xrightarrow{\sim}",
    "underline", "high",
    {"old": r"\[" + N + r" \RHom(f_*(E),F)", "new": r"\[" + N + r" \mathrm R\underline{\Hom}(f_*(E),F)"},
    "Independent of the next edit (the two do not change the same characters).")

add(259, "second display, the sign between the two sides",
    "≃ (tilde over a dash, no arrowhead)",
    r"\xrightarrow{\sim}",
    "symbol", "high",
    {"old": r"F)\xrightarrow{\sim}(f_*(E))", "new": r"F)\simeq(f_*(E))"},
    "")

add(259, "Corollaire 4.9.1, first line",
    "Sous les hypothèses de (4.8),",
    "Sous les hypothèses de (4.8),",
    "misprint_in_print", "medium", None,
    "Wrong reference number in the print: the corollary is Prop. 4.9 with E = O_X (its proof: 'Faire E = O_X'); "
    "f^! and the noetherian, compactifiable setting are those of 4.9, not of 4.8. The TeX keeps (4.8).",
    corrected="Sous les hypothèses de (4.9),")

add(259, "Corollaire 4.9.2, 'Posons ... RHom(.,K_X) = D_X'",
    "RHom(.,K_X) with Hom underlined",
    r"\(\RHom(\,\cdot\,,K_X)=D_X\)",
    "underline", "high",
    {"old": r"\(\RHom", "new": r"\(\mathrm R\underline{\Hom}"},
    "")

add(259, "Corollaire 4.9.2, 'Posons ... RHom(.,K_X) = D_X'",
    "(.,K_X): a full stop on the line as the empty place",
    r"(\,\cdot\,,K_X)",
    "symbol", "high",
    {"old": r"(\,\cdot\,,K_X)", "new": r"(.,K_X)"},
    "As the earlier fixes (P,\\cdot) -> (P,.) and (\\cdot,I) -> (.,I) in this volume.")

add(259, "Corollaire 4.9.2, 'Posons ... = D_X'",
    "D_X with the D underlined",
    r"=D_X",
    "underline", "high",
    {"old": r"K_X)=D_X", "new": r"K_X)=\underline{D}_X"},
    "The duality functor D_X, D_S is underlined everywhere on this page (statement, displays, proof); the TeX writes a plain D.")

add(259, "Corollaire 4.9.2, 'on a D_X(E) ∈ ob D(f)_parf'",
    "D_X(E) with the D underlined",
    r"on a \(D_X(E)",
    "underline", "high",
    {"old": r"on a \(D_X(E)", "new": r"on a \(\underline{D}_X(E)"},
    "")

add(259, "Corollaire 4.9.2, display",
    "E ⟶ D_X D_X(E) with both D underlined",
    r"E\longrightarrow D_XD_X(E)",
    "underline", "high",
    {"old": r"D_XD_X(E)", "new": r"\underline{D}_X\underline{D}_X(E)"},
    "")

add(259, "Preuve of 4.9.2, first sentence",
    "appliquer (4.8) avec Y = S, F = O_S",
    r"appliquer (4.8) avec \(Y=S\)",
    "misprint_in_print", "medium", None,
    "Wrong reference number in the print: the first assertion is Prop. 4.9 with Y = S, F = O_S (4.8 has no F and no f^!). "
    "The TeX keeps (4.8).",
    corrected="appliquer (4.9) avec")

add(259, "proof of 4.9.2, display (dualité globale)",
    "f_*D_X ≃ D_S f_* with both D underlined and the sign ≃ (tilde over a dash, no arrowhead)",
    r"f_*D_X\xrightarrow{\sim}D_Sf_*.",
    "formula", "high",
    {"old": r"f_*D_X\xrightarrow{\sim}D_Sf_*.", "new": r"f_*\underline{D}_X\simeq\underline{D}_Sf_*."},
    "One edit for the three differences of this short display (two underlined D, \\simeq for the print's sign).")

add(259, "proof of 4.9.2, second display",
    "f_*(E) ⟶ D_S D_S f_*(E) with both D underlined",
    r"D_SD_Sf_*(E)",
    "underline", "high",
    {"old": r"D_SD_Sf_*(E)", "new": r"\underline{D}_S\underline{D}_Sf_*(E)"},
    "")

# ---------------- page 260
add(260, "page start",
    "p. 260 begins 'a) Le foncteur M ↦ H^p(E ⊗ M) ...'; p. 259 ends 'Considérons les conditions suivantes :' (and the footnote)",
    r"'\begin{enumerate}[label=\alph*)]' and '\item Le' stand at the end of page_259.tex, above the folio-260 marker; page_260.tex begins 'foncteur'",
    "marker", "high", None,
    "The folio-260 marker stands one TeX line too late (two lines with the list opening). Exact fix in main.tex (both layers): replace "
    "'Considérons les conditions suivantes :\\n\\begin{enumerate}[label=\\alph*)]\\n\\item Le\\n" + M260 + "\\nfoncteur' by "
    "'Considérons les conditions suivantes :\\n" + M260 + "\\n\\begin{enumerate}[label=\\alph*)]\\n\\item Le\\nfoncteur'.")

add(260, "page end",
    "p. 260 ends '... où M^0 et M^1 sont sommes directes de faisceaux'; p. 261 begins 'du type O_{U,X}, où U est un objet de X.'",
    r"page_260.tex ends 'sont sommes directes de faisceaux du'; page_261.tex begins 'type \(\mathcal O_{U,X}\)'",
    "marker", "high", None,
    "The folio-261 marker stands one word too late: 'du' belongs to p. 261. Exact fix in main.tex (both layers): replace "
    "'sommes directes de faisceaux du\\n" + M261 + "\\ntype' by 'sommes directes de faisceaux\\n" + M261 + "\\ndu type'.")

add(260, "Lemme 5.1 b'), display (*)",
    "Hom(H^{-p-1}(E^∨),M) with Hom underlined",
    r"\Hom(H^{-p-1}(E^{\vee}),M)\tag{$*$}",
    "underline", "high",
    {"old": r"\Hom(H^{-p-1}(E^{\vee}),M)\tag{$*$}", "new": r"\underline{\Hom}(H^{-p-1}(E^{\vee}),M)\tag{$*$}"},
    "")

add(260, "'Définition de (*) :'",
    "only 'Définition de' is underlined; '(*)' is not",
    r"\emph{Définition de \((*)\)}",
    "underline", "medium",
    {"old": r"\emph{Définition de \((*)\)}", "new": r"\emph{Définition de} \((*)\)"},
    "")

add(260, "'Définition de (*)', first line",
    "E^∨ = RHom(E,O_X) with Hom underlined",
    r"\RHom(E,\mathcal O_X)",
    "underline", "high",
    {"old": r"\RHom(E,\mathcal O_X)", "new": r"\mathrm R\underline{\Hom}(E,\mathcal O_X)"},
    "")

add(260, "display (**)",
    "RHom(E^∨,M) with Hom underlined",
    r"\RHom(E^{\vee},M)",
    "underline", "high",
    {"old": r"\RHom(E^{\vee},M)", "new": r"\mathrm R\underline{\Hom}(E^{\vee},M)"},
    "")

add(260, "display (***), left side",
    "Ext^{p+1}(E^∨,M) with Ext underlined",
    r"\Ext^{p+1}(E^{\vee},M)",
    "underline", "high",
    {"old": r"\Ext^{p+1}(E^{\vee},M)", "new": r"\underline{\Ext}^{p+1}(E^{\vee},M)"},
    "")

add(260, "display (***), right side",
    "Hom(H^{-p-1}(E^∨),M) with Hom underlined",
    r"\Hom(H^{-p-1}(E^{\vee}),M),\tag{$***$}",
    "underline", "high",
    {"old": r"\Hom(H^{-p-1}(E^{\vee}),M),\tag", "new": r"\underline{\Hom}(H^{-p-1}(E^{\vee}),M),\tag"},
    "")

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
print("wrote", len(F), "findings to", OUT)
