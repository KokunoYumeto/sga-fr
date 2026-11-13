import json, sys, pathlib
sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
RUN = HERE.parent
B = RUN / "b511_515"
OUT = RUN / "findings_511_515.json"
NL = chr(0xB6)  # placeholder for a real line break in old/new


def fx(old, new):
    return {"old": old.replace(NL, "\n"), "new": new.replace(NL, "\n")}


M512 = "%%%%%%%%%%  scan idx 525  |  folio 512  %%%%%%%%%%"
M514 = "%%%%%%%%%%  scan idx 527  |  folio 514  %%%%%%%%%%"
M515 = "%%%%%%%%%%  scan idx 528  |  folio 515  %%%%%%%%%%"

F = []

# ---------------- page 511 ----------------
F.append({"page": 511,
  "where": "first display, end of its first line: K˙(𝔻) before '→ K.(X)'",
  "scan": "K˙(𝔻): the double-struck D alone, without (E) (both scans; crops_511_515/c511_disp1.png, w511_disp1.png). p. 510 writes 𝔻(E̲) in full; this page abbreviates it to 𝔻 (three times in the display, once in the text)",
  "tex": r"K^\circ(D(E))",
  "kind": "extra", "confidence": "high",
  "fix": fx(r"(D(E))¶\longrightarrow K_\bullet(X)", r"(\mathbb D)¶\longrightarrow K_\bullet(X)"),
  "note": r"The TeX writes out the print's abbreviation 𝔻 as D(E), with a plain D for the double-struck letter (\mathbb D, as pp. 510 and 516 now have it). Same in the next two entries. The old string avoids K^\circ, so the entry applies before or after a K-dot script."})
F.append({"page": 511,
  "where": "first display, second and third 𝔻: '⊗ K˙(𝔻) → K.(𝔻)'",
  "scan": "K˙(𝔻) → K.(𝔻): 𝔻 alone, double-struck (both scans)",
  "tex": r"K^\circ(D(E))\n\longrightarrow K_\bullet(D(E))",
  "kind": "extra", "confidence": "high",
  "fix": fx(r"(D(E))¶\longrightarrow K_\bullet(D(E))", r"(\mathbb D)¶\longrightarrow K_\bullet(\mathbb D)"),
  "note": "As the previous entry."})
F.append({"page": 511,
  "where": "'K˙(𝔻) est libre sur K˙(X)'",
  "scan": "K˙(𝔻): 𝔻 alone, double-struck (both scans; crops_511_515/c511_Kdot.png)",
  "tex": r"$K^\circ(D(E))$ est libre",
  "kind": "extra", "confidence": "high",
  "fix": fx(r"(D(E))$ est libre", r"(\mathbb D)$ est libre"),
  "note": "As the first entry."})
F.append({"page": 511,
  "where": "'Soit donc X = 𝔻(E). On procède par'",
  "scan": "𝔻(E̲) with a double-struck D, as ℙ and 𝕍 (both scans)",
  "tex": r"$X=D(E)$",
  "kind": "font", "confidence": "high",
  "fix": fx(r"$X=D(E)$", r"$X=\mathbb D(E)$"),
  "note": r"After this entry and the three above, no plain D of the flag scheme is left in Exposé IX (pp. 510 and 516 were given \mathbb D by their batches)."})
F.append({"page": 511,
  "where": "'On introduit alors P = ℙ(E), et le noyau F'",
  "scan": "a comma after ℙ(E̲) (both scans; crops_511_515/c511_PE_comma.png, w511_PE_comma.png)",
  "tex": r"$P=\mathbb P(E)$ et le noyau",
  "kind": "punctuation", "confidence": "high",
  "fix": fx(r"$P=\mathbb P(E)$ et le noyau", r"$P=\mathbb P(E)$, et le noyau"),
  "note": "The TeX drops the print's comma."})
F.append({"page": 511,
  "where": "after the display K.(S) ⊗ K˙(X) → K.(X): 'Soit donc X = 𝔻(E)'",
  "scan": "'Soit donc' is indented: a new paragraph (both scans)",
  "tex": r"no blank line after \]: 'Soit donc' continues the paragraph",
  "kind": "other", "confidence": "medium",
  "fix": fx(r"\]¶Soit donc", r"\]¶¶Soit donc"),
  "note": "Missing paragraph break (the typescript indents its new paragraphs: 'On a déjà vu' on this page)."})
F.append({"page": 511,
  "where": "'On procède par réccurrence sur le rang de E'",
  "scan": "réccurrence, with a double c (both scans)",
  "tex": "réccurrence (the printed reading kept)",
  "kind": "misprint_in_print", "confidence": "high",
  "fix": None, "corrected": "récurrence",
  "note": "Typing error kept by the diplomatic TeX; the corrected layer already reads 'récurrence', as the print itself does three lines below ('l'hypothèse de récurrence')."})
F.append({"page": 511,
  "where": "K˙ on pp. 511-515 (33 places: 13 on p. 511, 8 on p. 513, 12 on p. 514)",
  "scan": "K with a raised filled dot in every place, the K˙ of Exposés IV, VI and VII (both scans; crops_511_515/c511_Kdot.png, c511_disp1.png, w511_disp1.png); the K. with a lower dot is K_\\bullet in the TeX, as it should be",
  "tex": r"K^\circ",
  "kind": "symbol", "confidence": "high",
  "fix": None,
  "note": r"Convention of the Exposé IX TeX: K^\circ for the print's K˙ throughout (88 in folios 498-518, the whole exposé, no K^{\bullet}), the form Exposé VI §1 and Exposé VII had before their passes. Not itemized: one script for IX (K^\circ -> K^{\bullet}, both layers). Three examples: p. 511 'base de $K^\circ(X)$ sur $K^\circ(S)$' -> 'base de $K^{\bullet}(X)$ sur $K^{\bullet}(S)$'; p. 513 'entre les $K^\circ$ par' -> 'entre les $K^{\bullet}$ par'; p. 514 'la classe de $E$ dans $K^\circ(S)$' -> 'la classe de $E$ dans $K^{\bullet}(S)$'. No old string of the other entries contains K^\circ."})
F.append({"page": 511,
  "where": "letters of sheaves and Modules on pp. 511-515",
  "scan": "underlined in the print (both scans): p. 511 E (rang de E, P(E) twice, p*(E), 𝔻(E), 'E un O_S-Module' of Cor. 3.2), F ('le noyau F', 'drapeaux de F'); p. 512 E ('E un O_S-Module', V(E), 'associé à E', 'extensions F de E', both Ě, 'de E'), F (extensions F, the F and E of (3.3.1), every V(F)); p. 513 F, E ('extension F de E'), the A of A(P), every F and E inside S(F), P(F), P(E), V(E); p. 514 every E, F inside P(E), P(F), S(F), S(E), 'sous-Module de F', I in 'Si I est l'idéal', 'I est un idéal inversible', 'I est défini', 'I ≃ O(-1)', E of 'et E le O_S-Module' and of 'la classe de E'; p. 515 every E_o (E_o = (O_S)^n, base de E_o, E_o^(i), sous-Module de E_o, E_oS', E_oS'^(i), drapeaux de E_o, image inverse de E_o, E_oX_o, E_oS'' three times), G/B, L_o^(i), G_o^(i), G_o^(i-1), F_o^(i), G_oS''^(i+1), F_oS''^(i). Plain in the print: 'contravariant en E !' (p. 512), the class I of 'i_*(1) = 1-I' and the ideal J (p. 514), the class E of 'On note E la classe' (p. 514), G/U, B, U, T, X_o, Y_o (p. 515)",
  "tex": r"all plain, except \underline P (p. 512) as printed",
  "kind": "underline", "confidence": "high",
  "fix": None,
  "note": r"Convention of the Exposé IX transcription (as reported for Exposés VI and VII and for pp. 506-510): not itemized; no blind script, the same letters stand plain in the print where they are classes. Two places where the plain letter merges two printed letters: p. 514 'On note $E$ la classe de $E$' (class E, sheaf E̲) and the I of '$i_*(1)=1-I$' (class) against the sheaf I̲ of the same sentence. The underlined O written \mathcal O falls under the pending structure-sheaf decision. Three examples, in the form to use if the diplomatic layer reproduces the underline: p. 511 'le noyau $F$ de' -> 'le noyau $\underline{F}$ de'; p. 513 'L'algèbre $A(P)$ de' -> 'L'algèbre $\underline{A}(P)$ de'; p. 514 'Si $I$ est l'idéal' -> 'Si $\underline{I}$ est l'idéal'."})
F.append({"page": 511,
  "where": "statements of pp. 511-515: Corollaire 3.2 (p. 511), Proposition 3.4 (p. 513), Proposition 4.1 (pp. 514-515)",
  "scan": "underlined word group by word group (both scans): Cor. 3.2 'Soient', 'un schéma noethérien', 'un', '-Module localement', 'libre de rang', 'le fibré projectif associé', 'le morphisme', 'structural de', 'et', 'la classe dans', 'du faisceau', 'Alors', 'l'homomorphisme', 'défini par', 'est un isomorphisme'; Prop. 3.4 'Soient', 'un schéma noethérien', 'un', '-Module localement', 'libre de rang', 'le fibré vectoriel associé', 'un torseur sous', 'le morphisme structural de', 'Alors l'homomorphisme canonique', 'est un isomorphisme'; Prop. 4.1 'Soient', 'un schéma noethérien', 'le', 'groupe' (S- plain), 'un torseur sous', 'et', 'le', '-Module localement libre de rang', 'corres-/pondant à', 'On note', 'la classe de', 'dans', 'et', 'le', 'idéal engendré' (λ- plain), p. 515 'par', 'Si', 'est le morphisme structural de', 'alors', 'défini/car', 'est plat', 'est surjectif et définit un isomorphisme'; letters, formulas and punctuation plain; the labels underline only the word",
  "tex": r"the statements in roman (no \underline, no \emph)",
  "kind": "underline", "confidence": "high",
  "fix": None,
  "note": "Exposé IX follows the Exposé II pattern of GLOBAL_ISSUES 82 (pending volume decision): not itemized; the word groups are listed for the scripted pass. No emphasized defined terms and no category letter on pp. 511-515."})

# ---------------- page 512 ----------------
F.append({"page": 512,
  "where": "start of page (folio-512 marker)",
  "scan": "p. 511 ends '... on utilise l'homomorphisme f_*, défini car f est projectif.'; p. 512 begins 'On a alors, d'après IV (2.12.4) :' at the margin (both scans; crops_511_515/wit_511_half.png, wit_512_half.png)",
  "tex": "'On a' stands at the end of page_511.tex, above the folio-512 marker; page_512.tex begins 'alors, d'après IV (2.12.4) :'",
  "kind": "marker", "confidence": "high",
  "fix": None,
  "note": "Page 512 really begins at 'On a alors'. Exact edit in main.tex, both layers (each string occurs once in each layer): replace 'défini car $f$ est projectif. On a\\n" + M512 + "\\nalors, d'après IV (2.12.4) :' by 'défini car $f$ est projectif.\\n" + M512 + "\\nOn a alors, d'après IV (2.12.4) :'. The comment line keeps the sentence in one paragraph, as the print has it."})
F.append({"page": 512,
  "where": "first display, left side: f_*( Σ_{i=0}^{n-1} ξ^{-1} f*(x_i) )",
  "scan": "ξ^{-1}: the exponent is the digit 1 (flag, no dot; the same glyph as in n-1 above the sums), while the right side has f_*(ξ^{-i}) with a dotted i (both scans; crops_511_515/c512_disp.png, w512_disp.png)",
  "tex": r"\xi^{-i}f^*(x_i) (silently corrected)",
  "kind": "misprint_in_print", "confidence": "high",
  "fix": fx(r"\left(\sum_{i=0}^{n-1}\xi^{-i}f^*", r"\left(\sum_{i=0}^{n-1}\xi^{-1}f^*"),
  "corrected": r"\xi^{-i}f^*(x_i)",
  "note": "The sum is φ((x_i)) = Σ ξ^{-i} f*(x_i) of Corollaire 3.2 (p. 511), so -1 is a typing error for -i; the diplomatic TeX silently corrects it. The fix changes only the exponent; the old string is long enough to be unique in main.tex as well (p. 511 has the same \\xi^{-i}f^*)."})
F.append({"page": 512,
  "where": "'En sens inverse, soit P un torseur sous V.'",
  "scan": "indented: a new paragraph (both scans)",
  "tex": r"single line break after '... sur $\mathbb V(F)$.': the same paragraph",
  "kind": "other", "confidence": "medium",
  "fix": fx(r"$\mathbb V(F)$.¶En sens inverse", r"$\mathbb V(F)$.¶¶En sens inverse"),
  "note": "Missing paragraph break."})

# ---------------- pages 513-514: the symmetric algebra ----------------
S_SCAN = "an S with a vertical stroke through it, the typist's double-struck S (typed like a dollar sign), as on p. 507 (both scans; crops_511_515/c513_S.png, w513_S.png)"
S_NOTE = r"The TeX writes the print's 𝕊 as a plain S; written \mathbb S as the p. 507 entries of findings_506_510 (applied). After these five entries no plain S of the symmetric algebra is left in Exposé IX. The underline of F, E inside is the underlined-letter convention."
for page, where, old, new in [
  (513, "'L'algèbre A(P) de P sur O_S est 𝕊(F) ⊗_{𝕊(O_S)} O_S'",
   r"est $S(F)\otimes_{S(\mathcal O_S)}\mathcal O_S$", r"est $\mathbb S(F)\otimes_{\mathbb S(\mathcal O_S)}\mathcal O_S$"),
  (513, "'soit 𝕊(F)/(s-1)𝕊(F)'",
   r"soit $S(F)/(s-1)S(F)$", r"soit $\mathbb S(F)/(s-1)\mathbb S(F)$"),
  (513, "'fractions homogènes de degré 0 𝕊(F)_(s)'",
   r"$0$ $S(F)_{(s)}$", r"$0$ $\mathbb S(F)_{(s)}$"),
  (513, "'est alors Proj(𝕊(F)/s.𝕊(F))'",
   r"\operatorname{Proj}(S(F)/s\cdot S(F))", r"\operatorname{Proj}(\mathbb S(F)/s\cdot \mathbb S(F))"),
  (514, "'I est défini par l'idéal J de 𝕊(F) noyau de 𝕊(F) → 𝕊(E)'",
   r"de $S(F)$ noyau de $S(F)\to S(E)$", r"de $\mathbb S(F)$ noyau de $\mathbb S(F)\to \mathbb S(E)$"),
]:
    F.append({"page": page, "where": where, "scan": S_SCAN, "tex": old.strip("$"),
      "kind": "font", "confidence": "high", "fix": fx(old, new), "note": S_NOTE})

# ---------------- page 514 ----------------
F.append({"page": 514,
  "where": "start of page (folio-514 marker)",
  "scan": "p. 513 ends '... il suffit pour le voir de montrer que pour a ∈ K.(S) et'; p. 514 begins 'b∈K˙(ℙ(E)), on a' (both scans; crops_511_515/wit_514_half.png)",
  "tex": r"'$b\in K^\circ(\mathbb P(E))$, on a' stands at the end of page_513.tex, above the folio-514 marker; page_514.tex begins with the display i_*(b\cdot h^*(a)) = ...",
  "kind": "marker", "confidence": "high",
  "fix": None,
  "note": "Page 514 really begins at '$b\\in K^\\circ(\\mathbb P(E))$, on a'. Exact edit in main.tex, both layers, as two replacements made together (neither old string contains K^\\circ, so they apply before or after a K-dot script; each occurs once in each layer): replace 'pour $a\\in K_\\bullet(S)$ et $b\\in' by 'pour $a\\in K_\\bullet(S)$ et\\n" + M514 + "\\n$b\\in', and ', on a\\n" + M514 + "\\n\\[' by ', on a\\n\\['."})
F.append({"page": 514,
  "where": "§4 title 'Fibrés principaux sous les groupes 𝔾l(n)_S'",
  "scan": "a double-struck G followed by a double-struck small l: '𝔾l(n)_S' (both scans; crops_511_515/c514_Gl_title.png, w514_Gl2.png)",
  "tex": r"$\mathrm{GL}(n)_S$ (roman, capital L)",
  "kind": "symbol", "confidence": "high",
  "fix": fx(r"groupes $\mathrm{GL}(n)_S$}", r"groupes $\mathbf{Gl}(n)_S$}"),
  "note": r"The print's 'Gl' with a small l (the volume's \Gl and \GL print Gl), both letters doubled; \mathbf{Gl} as main.tex writes R_{\mathbb Z}(\mathbf{Gl}(n)) elsewhere, since \mathbb has no small l. Corollaire 4.3 on p. 517 types a plain 'Gl(n)_S' (witness crops_511_515/w517_Gl.png), rightly \mathrm{Gl} after findings_516_520: the doubled letters are p. 514's own."})
F.append({"page": 514,
  "where": "Proposition 4.1, 'G le S-groupe 𝔾l(n)_S'",
  "scan": "double-struck 'Gl' with a small l, as in the §4 title (both scans; crops_511_515/c514_Gl_prop.png, w514_Gl2.png)",
  "tex": r"$\mathrm{GL}(n)_S$",
  "kind": "symbol", "confidence": "high",
  "fix": fx(r"$S$-groupe $\mathrm{GL}(n)_S$", r"$S$-groupe $\mathbf{Gl}(n)_S$"),
  "note": "As the title."})
F.append({"page": 514,
  "where": "'L'homomorphisme K˙(S) → K˙(ℙ(F))/Im(K˙(ℙ(E))) est donc un isomorphisme' (1 of 2)",
  "scan": "the map stands in the running text at the start of a line, followed on the same line by 'est donc un isomorphisme, et par suite,' (both scans)",
  "tex": "a display between 'L'homomorphisme' and 'est donc un isomorphisme'",
  "kind": "other", "confidence": "high",
  "fix": fx(r"L'homomorphisme¶\[¶", r"L'homomorphisme $"),
  "note": r"The TeX makes an inline formula a display. Apply together with the next entry, which closes the $: split in two so that neither old string contains K^\circ."})
F.append({"page": 514,
  "where": "same formula, its end before 'est donc un isomorphisme' (2 of 2)",
  "scan": "as the previous entry",
  "tex": r"\] before 'est donc un isomorphisme'",
  "kind": "other", "confidence": "high",
  "fix": fx(r"¶\]¶est donc un isomorphisme", r"$ est donc un isomorphisme"),
  "note": "Apply together with the previous entry."})

# ---------------- page 515 ----------------
F.append({"page": 515,
  "where": "start of page (folio-515 marker)",
  "scan": "p. 514 ends '... et J le λ-idéal engendré'; p. 515 begins 'par (E - n). Si f est le morphisme structural de P, ...' (both scans; crops_511_515/wit_514_half.png, wit_515_half.png)",
  "tex": "'par $(E-n)$. Si $f$ est le' stands at the end of page_514.tex, above the folio-515 marker",
  "kind": "marker", "confidence": "high",
  "fix": None,
  "note": "Page 515 really begins at 'par $(E-n)$'. Exact edit in main.tex, both layers (once in each): replace 'engendré par $(E-n)$. Si $f$ est le\\n" + M515 + "\\nmorphisme structural' by 'engendré\\n" + M515 + "\\npar $(E-n)$. Si $f$ est le morphisme structural'."})
F.append({"page": 515,
  "where": "display K.(S)/J.K.(S) ⥲ K.(P)",
  "scan": "one full stop after K.(P) (both scans)",
  "tex": r"K_\bullet(P)..",
  "kind": "punctuation", "confidence": "high",
  "fix": fx(r"K_\bullet(P)..", r"K_\bullet(P)."),
  "note": "The TeX doubles the full stop."})
F.append({"page": 515,
  "where": "'et F_o^(i) = G_o^(i-1)/G_o^(i) ≃ Ker(L_o^(i) → L_o^(i-1)).'",
  "scan": "the formula stands in the running text, on the line that begins 'E_oX_o → L_o^(i), et', and ends with one full stop (both scans)",
  "tex": "a display ending in '..'",
  "kind": "other", "confidence": "high",
  "fix": fx(r"$, et¶\[¶F_0^{(i)}=G_0^{(i-1)}/G_0^{(i)}\simeq \Ker(L_0^{(i)}\to L_0^{(i-1)})..¶\]",
            r"$, et $F_0^{(i)}=G_0^{(i-1)}/G_0^{(i)}\simeq \Ker(L_0^{(i)}\to L_0^{(i-1)})$."),
  "note": "The TeX makes an inline formula a display and doubles its full stop. The blank line after it stays: 'Par ailleurs' begins an indented paragraph in the print."})

sub = [
  ("'le sous-groupe des automorphismes de E_oS', qui'", r"automorphismes de $E_{0,S'}$", r"automorphismes de $E_{0S'}$"),
  ("'les sous-modules E_oS'^(i) pour tout i'", r"$E_{0,S'}^{(i)}$", r"$E_{0S'}^{(i)}$"),
  ("'le noyau de E_oX_o → L_o^(i)'", r"$E_{0,X_0}\to", r"$E_{0X_0}\to"),
  ("'d'un automorphisme de E_oS'' modulo'", r"automorphisme de $E_{0,S''}$", r"automorphisme de $E_{0S''}$"),
  ("'c'est-à-dire d'un drapeau de E_oS'', les sous-modules'", r"drapeau de $E_{0,S''}$, les", r"drapeau de $E_{0S''}$, les"),
  ("'f_i^α - f_i^β ∈ G_oS''^(i+1)'", r"G_{0,S''}^{(i+1)}", r"G_{0S''}^{(i+1)}"),
  ("'d'un drapeau de E_oS'' et pour tout i'", r"drapeau de $E_{0,S''}$ et pour", r"drapeau de $E_{0S''}$ et pour"),
  ("'d'une base de F_oS''^(i)'", r"F_{0,S''}^{(i)}", r"F_{0S''}^{(i)}"),
]
for where, old, new in sub:
    F.append({"page": 515, "where": where,
      "scan": "the two indices typed together, o and then S' (S'', X_o), without a comma (both scans; crops_511_515/c515_EoS.png, c515_EoSi.png)",
      "tex": old.strip("$"),
      "kind": "punctuation", "confidence": "high",
      "fix": fx(old, new),
      "note": "The TeX adds a comma between the two indices (as on pp. 85-87). These eight on p. 515 are all of Exposé IX's."})

# ---------------- checks ----------------
pages = {p: (B / f"page_{p}.tex").read_text(encoding="utf-8") for p in range(511, 516)}
bad = 0
for k, f in enumerate(F):
    fx_ = f.get("fix")
    if fx_ is None:
        continue
    t = pages[f["page"]]
    n = t.count(fx_["old"])
    if n != 1:
        bad += 1
        print("NOT UNIQUE", k, f["page"], n, repr(fx_["old"]))
    if "%%%%%%%%%%" in fx_["old"] or "%%%%%%%%%%" in fx_["new"]:
        bad += 1
        print("MARKER IN FIX", k)
    if any(ord(c) < 32 and c != "\n" for c in fx_["old"] + fx_["new"]):
        bad += 1
        print("CONTROL CHAR", k)
    if NL in fx_["old"] + fx_["new"]:
        bad += 1
        print("PLACEHOLDER LEFT", k)
# overlapping olds on the same page
for p in pages:
    spans = []
    for k, f in enumerate(F):
        if f["page"] == p and f.get("fix"):
            i = pages[p].find(f["fix"]["old"])
            spans.append((i, i + len(f["fix"]["old"]), k))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            bad += 1
            print("OVERLAP", p, a, b)
# main.tex: strings named in the marker notes, and every page-level old
BS = chr(92)
for layer in ("diplomatic", "current"):
    t = pathlib.Path(rf"C:\Users\user\Documents\sga_scan_check_20261105\sga6\{layer}\main.tex").read_text(encoding="utf-8")
    olds = [
      "défini car $f$ est projectif. On a\n" + M512 + "\nalors, d'après IV (2.12.4) :",
      "pour $a" + BS + "in K_" + BS + "bullet(S)$ et $b" + BS + "in",
      ", on a\n" + M514 + "\n" + BS + "[",
      "engendré par $(E-n)$. Si $f$ est le\n" + M515 + "\nmorphisme structural",
    ]
    print(layer, "marker-edit old counts:", [t.count(o) for o in olds])
    cnt = [(k, t.count(f["fix"]["old"])) for k, f in enumerate(F) if f.get("fix")]
    print(layer, "page-fix olds in main.tex with count != 1:", [(k, c) for k, c in cnt if c != 1])

counts = {}
for f in F:
    c = counts.setdefault(f["page"], [0, 0])
    c[1 if f["kind"] == "misprint_in_print" else 0] += 1
print("counts", counts, "total", len(F), "bad", bad)
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
print("written", OUT)
