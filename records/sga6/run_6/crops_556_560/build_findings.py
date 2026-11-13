"""build_findings.py: build findings_556_560.json, check every fix's old (exactly once in its page file,
no marker line), and simulate applying each page's fixes in order (read only on the page files)."""
import json, pathlib, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
B = HERE.parent / "b556_560"
OUT = HERE.parent / "findings_556_560.json"
F = []


def add(page, where, scan, tex, kind, conf, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
         "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- page 556 ----------------
add(556, "heading 6.4, 'Démonstration de 6.2.2.'",
    "'6.4. Démonstration de 6.2.2. Il suffit de montrer ...': the run-in heading ends with a full stop after 6.2.2 (both scans; b556_560/page_556_s1.png)",
    r"\subsection*{6.4. Démonstration de 6.2.2}", "punctuation", "low",
    r"\subsection*{6.4. Démonstration de 6.2.2}", r"\subsection*{6.4. Démonstration de 6.2.2.}",
    r"As the p. 529 entry for \subsection*{1.6} (findings_526_530), which notes that Exposé X writes its headings without the print's final full stop: one decision for the exposé. The run-in text and the plain title are accepted typesetting.")

add(556, "'Soient p l'idéal premier de y'",
    "p̲: a typed p, underlined (both scans; crops_556_560/c556_p.png)",
    r"Soient \(\mathfrak p\) l'idéal", "font", "medium",
    r"Soient \(\mathfrak p\) l'idéal", r"Soient \(\underline{p}\) l'idéal",
    r"The print's underlined letter, not Fraktur, as the applied edits of p. 530 (\underline{m}, findings_526_530) and pp. 185-186 (\underline{p}). The same p̲ eight more times on p. 557 (seven entries); \mathfrak p occurs only on pp. 556-557 in main.tex: apply all eight edits or none.")

add(556, "display 'c_{h,k} : G_a → Sℓ(n)  (h,k = 1,...,n ; h ≠ k).'",
    "G_a with a plain typed G (not underlined, not double-struck; both scans; crops_556_560/c556_Ga.png)",
    r"c_{h,k}:\mathbb G_a", "font", "low",
    r"c_{h,k}:\mathbb G_a", r"c_{h,k}:G_a",
    r"The typist's plain G for the group scheme, as G_m on pp. 558-559 (\Gm, \mathbb G_{m,S}) and the plain G of p. 508 (findings_506_510). Same class as the typist's plain Q (volume decision with SGA 7 II issue 61): low. Apply with the five G_m edits of pp. 558-559 or none.")

add(556, "'La démonstration se fait alors en deux pas.'",
    "runs on at the left margin after '... h ≠ k) inversible.' (both scans; crops_556_560/wit_556_small.png); the paragraphs of these pages are indented ('Pour le premier', 'Supposant', 'On suppose donc' on p. 557)",
    "a blank line before 'La démonstration' (new paragraph)", "other", "medium",
    "inversible.\n\nLa démonstration se fait", "inversible.\nLa démonstration se fait",
    "Spurious paragraph break.")

add(556, "equation number of 'c_{h,k,λ} c_{h,k,μ} = c_{h,k,λ+μ}' in 6.4",
    "(6.3.1) (both scans)",
    r"\tag{6.3.1} (printed reading kept)", "misprint_in_print", "low",
    None, None,
    r"The formula stands in 6.4 (Démonstration de 6.2.2); §6.3 (p. 555) has no numbered formula, and the numbers run by section elsewhere ((6.1.x), (6.2.x), then (6.5.4), (6.5.5) after the remarks 6.5.1-6.5.3): a number left over from an older numbering (cf. GLOBAL_ISSUES 31). Corrected edition only, together with the reference 'de (6.3.1)' on p. 558: both or neither.",
    corrected=r"\tag{6.4.1}")

add(556, "letters the print underlines on pp. 556-559 (convention of the Exposé X transcription, reported once)",
    "underlined in the print (both scans): p. 556 the n of Sℓ(n)(Y) and of Gℓ(n)(Y') and the first n of 'et n constant égal à n'; the matrix a in all five places ('Pour toute matrice a = (a_ij)', 'c_{h,k,λ} a en ajoutant', 'colonne de a', 'la matrice ac_{h,k,λ}', 'ligne de a'); p. 559 both e ('Soient e l'objet final', Spec(O(e))). Plain in the print: the n of the display Sℓ(n), of Gℓ(n) at the foot of p. 556, of (i,j=1,...,n) and of p. 559 ('entier positif n', Gℓ(n)_X, (6.5.4), (6.5.5)); the a of p. 558 ('une matrice inversible a = (a_ij)', the display a c = c a); s, y, Y, A, k, u (crops_556_560/c556_Sln.png, c556_GlnY.png, c556_ncst.png, c556_a1.png, c556_a23.png, c556_a4.png, c556_a5.png, c556_Gln.png, c558_amat.png)",
    "all plain", "underline", "high",
    None, None,
    r"Convention of the Exposé X transcription (findings_521_525, findings_526_530): not itemized. The TeX of p. 555 already writes this rank as \underline n ('on peut supposer que \(\underline n\) est constant sur \(X\), soit \(\underline n=n\in\mathbb Z\)'), so on p. 556 the print's distinction between n̲ and the integer n ('et n̲ constant égal à n') is lost. The ten edits, if the diplomatic layer reproduces the underline: p. 556 '\(s\in\operatorname{S\ell}(n)(Y)\)' -> '\(s\in\operatorname{S\ell}(\underline n)(Y)\)'; '\(\operatorname{G\ell}(n)(Y')\)' -> '\(\operatorname{G\ell}(\underline n)(Y')\)'; 'et \(n\) constant' -> 'et \(\underline n\) constant'; 'matrice \(a=(a_{ij})' -> 'matrice \(\underline a=(a_{ij})'; '\(c_{h,k,\lambda}a\) en ajoutant' -> '\(c_{h,k,\lambda}\underline a\) en ajoutant'; 'colonne de \(a\)' -> 'colonne de \(\underline a\)'; 'la matrice \(ac_{h,k,\lambda}\)' -> 'la matrice \(\underline ac_{h,k,\lambda}\)'; 'ligne de \(a\)' -> 'ligne de \(\underline a\)'; p. 559 'Soient \(e\) l'objet' -> 'Soient \(\underline e\) l'objet'; '\Spec(\mathcal O(e))' -> '\Spec(\mathcal O(\underline e))' (each once in its page file). The underlined O written \mathcal O falls under the pending volume decision.")

# ---------------- page 557 ----------------
add(557, "'la matrice unité 1 = (δ_ij)'",
    "1 doubly underlined (both scans; crops_556_560/c557_unite.png)",
    r"unité \(1=(\delta_{ij})\)", "font", "medium",
    r"unité \(1=(\delta_{ij})\)", r"unité \(\mathbf{1}=(\delta_{ij})\)",
    r"The unit matrix carries the typescript's double underline, which the volume writes bold (the doubly underlined D and Gl of Exposé VI as \mathbf, findings_386_390 and findings_391_395; \Sym prints a bold S); the scalar 1 of 's_11 = 1', 's'_nn = 1' is plain. If the volume prefers the underline form: \underline{\underline{1}}. Apply with the next entry.")

add(557, "'de sorte que s'_nn = 1 , s' = 1 , et on a gagné.'",
    "the second 1 doubly underlined, the first plain (both scans; crops_556_560/c557_gagne.png)",
    r"\(s'=1\), et on a gagné", "font", "medium",
    r"\(s'=1\), et on a gagné", r"\(s'=\mathbf{1}\), et on a gagné",
    "As the unit matrix of the first line.")

P557 = "p̲: a typed p, underlined (both scans; crops_556_560/c557_si1.png, w557_si1.png)"
NOTE_P = r"As 'Soient p l'idéal premier' on p. 556 (\underline{p} for the print's underlined p): apply the eight p edits of pp. 556-557 together."
add(557, "'Si s_11 ≠ 1 et s_21 ∈ p'", P557, r"et \(s_{21}\in\mathfrak p\)", "font", "medium",
    r"et \(s_{21}\in\mathfrak p\)", r"et \(s_{21}\in\underline{p}\)", NOTE_P)
add(557, "'ait s'_21 ∉ p. Puisque det(s) = 1 ∉ p'", P557 + "; two places",
    r"ait \(s'_{21}\notin\mathfrak p\). Puisque \(\det(s)=1\notin\mathfrak p\)", "font", "medium",
    r"ait \(s'_{21}\notin\mathfrak p\). Puisque \(\det(s)=1\notin\mathfrak p\)",
    r"ait \(s'_{21}\notin\underline{p}\). Puisque \(\det(s)=1\notin\underline{p}\)", NOTE_P)
add(557, "'il existe au moins un indice i tel que s_i1 ∉ p'", P557,
    r"tel que \(s_{i1}\notin\mathfrak p\)", "font", "medium",
    r"tel que \(s_{i1}\notin\mathfrak p", r"tel que \(s_{i1}\notin\underline{p}",
    NOTE_P + r" The old stops before '\)' so that it does not overlap the misprint entry of the same formula.")
add(557, "'Alors on a s_21 + s_i1 ∉ p'", P557, r"\(s_{21}+s_{i1}\notin\mathfrak p\)", "font", "medium",
    r"\(s_{21}+s_{i1}\notin\mathfrak p\)", r"\(s_{21}+s_{i1}\notin\underline{p}\)", NOTE_P)
add(557, "'On peut donc supposer s_21 ∉ p'", P557, r"supposer \(s_{21}\notin\mathfrak p\)", "font", "medium",
    r"supposer \(s_{21}\notin\mathfrak p\)", r"supposer \(s_{21}\notin\underline{p}\)", NOTE_P)
add(557, "'Si s_11 - 1 ∈ p, alors dans s' = (s'_ij) = sc_{1,2,1}'", P557, r"\(s_{11}-1\in\mathfrak p\)", "font", "medium",
    r"\(s_{11}-1\in\mathfrak p\)", r"\(s_{11}-1\in\underline{p}\)", NOTE_P)
add(557, "'s'_11 - 1 = (s_11 + s_21)-1 ∉ p'", P557, r"(s_{11}+s_{21})-1\notin\mathfrak p\)", "font", "medium",
    r"-1\notin\mathfrak p\)", r"-1\notin\underline{p}\)", NOTE_P)

add(557, "'il existe au moins un indice i tel que s_i1 ∉ p' / 'Alors on a'",
    "no full stop after p̲ at the end of the line; 'Alors' (capital) begins the next line (both scans; crops_556_560/c557_si1.png, w557_si1.png)",
    r"\(s_{i1}\notin\mathfrak p\). Alors on a (silently corrected)", "misprint_in_print", "medium",
    r"\). Alors on a", r"\) Alors on a",
    r"The typist left out the full stop (the stops of this page are heavy dots, e.g. 's'_21 ∉ p.' on the line above). The TeX supplies it silently; the fix restores the print. The old does not overlap the \underline{p} entry of the same formula (that old ends before '\)').",
    corrected=r"\). Alors on a")

add(557, "'en multipliant s à gauche (resp. à droite) par des matrices c_{i,1,λ} (resp. c_{i,1,λ})'",
    "c_{i,1,λ} twice (both scans; crops_556_560/c557_resp.png, w557_resp.png)",
    r"\(c_{i,1,\lambda}\) (resp. \(c_{i,1,\lambda}\)) (printed reading kept)", "misprint_in_print", "low",
    None, None,
    r"'resp.' joins two different operations: clearing the first column (s_i1) and the first row (s_1i) needs c_{i,1,λ} on one side and c_{1,i,λ} on the other. With the usual matrix product the second is the wrong one (as given in 'corrected'); with the column/row rule stated on p. 556 it would be the first. The indices of this proof are loose elsewhere too (c = c_{h,1,λ} and c_{i,1,1} for adding row i to row 2), so the corrected edition may leave it: low.",
    corrected=r"\(c_{i,1,\lambda}\) (resp. \(c_{1,i,\lambda}\))")

add(557, "'Reste à voir que celles-ci sont des produits de commutateurs'",
    "runs on at the left margin after the indented paragraph 'On suppose donc que s soit déjà sur Y un produit de matrices c_{h,k,λ}.' (both scans; b556_560/page_557_s4.png, crops_556_560/wit_557_small.png)",
    "a blank line before 'Reste à voir' (new paragraph)", "other", "medium",
    r"\(c_{h,k,\lambda}\)." + "\n\nReste à voir", r"\(c_{h,k,\lambda}\)." + "\nReste à voir",
    "Spurious paragraph break.")

# ---------------- page 558 ----------------
add(558, "first line, 'c_{h,k,λ} et c_{h,k,μ} sont conjugées'",
    "'conjugées': no u after the g, whose lower part is faint in both scans (crops_556_560/c558_conj.png, w558_conj.png)",
    "sont conjugées (printed reading kept)", "misprint_in_print", "high",
    None, None, "Spelling slip of the print; the TeX keeps it.", corrected="conjuguées")

add(558, "'on tire de ceci et de (6.3.1) que β(c_{h,k,λ})=0'",
    "(6.3.1) (both scans; the 6 faint; crops_556_560/c558_631.png, w558_631.png)",
    "de (6.3.1) que (printed reading kept)", "misprint_in_print", "low",
    None, None, "Goes with the tag (6.3.1) of p. 556 (see there): both or neither, corrected edition only.",
    corrected="de (6.4.1) que")

add(558, "'dans un faisceau de groupes abéliens B, on a'",
    "the letter is an overstrike of B and H (the two stems and serifs of H with the bowls of B; both scans; crops_556_560/c558_B_zoom.png, w558_B.png)",
    r"abéliens \(B\), on a", "other", "low",
    None, None,
    "A typist's correction whose last letter the scans do not show; the TeX reads B. Four lines below B is the ring of U = Spec(B), which may favour H for the sheaf of groups. No edit proposed; for the corrected edition's notes.")

F2SCAN = "F̲_2: a typed F, underlined, with the subscript 2 (both scans; crops_556_560/c558_F2.png, wit_558_small.png)"
F2NOTE = r"As the first F_2 entry of this page (low; apply the seven F edits together)."
add(558, "'n'est pas le corps premier F_2 = {0,1}'", F2SCAN, r"premier \(\mathbb F_2=\{0,1\}\)", "font", "low",
    r"premier \(\mathbb F_2=\{0,1\}\)", r"premier \(\underline{F}_2=\{0,1\}\)",
    r"The print writes the prime field as an underlined typed F in all nine places of this page (the typist's form for the double-struck F); the TeX has \mathbb F_2. Same class as the typist's plain Q (volume decision with SGA 7 II issue 61; GLOBAL_ISSUES 78 kept \mathbb in SGA 7 II): low. The form of the underlined G of p. 507 (findings_506_510, \underline{G}). Apply all seven F edits of this page or none.")
add(558, "'Si k = F_2, alors V = Spec(A[T]/(T^2+T+1))'", F2SCAN, r"Si \(k=\mathbb F_2\)", "font", "low",
    r"Si \(k=\mathbb F_2\)", r"Si \(k=\underline{F}_2\)", F2NOTE)
add(558, "'dont le corps résiduel est différent de F_2. On a gagné.'", F2SCAN, r"différent de \(\mathbb F_2\)", "font", "low",
    r"différent de \(\mathbb F_2\)", r"différent de \(\underline{F}_2\)", F2NOTE)
add(558, "6.5.1, 'sont tous non isomorphes à F_2'", F2SCAN, r"isomorphes à \(\mathbb F_2\)", "font", "low",
    r"isomorphes à \(\mathbb F_2\)", r"isomorphes à \(\underline{F}_2\)", F2NOTE)
add(558, "6.5.1, 'S = Spec(F_2), Sℓ(2,F_2) = Gℓ(2,F_2)'", F2SCAN + "; three places",
    r"\(S=\Spec(\mathbb F_2)\), \(\operatorname{S\ell}(2,\mathbb F_2)=\operatorname{G\ell}(2,\mathbb F_2)\)", "font", "low",
    r"\(S=\Spec(\mathbb F_2)\), \(\operatorname{S\ell}(2,\mathbb F_2)=\operatorname{G\ell}(2,\mathbb F_2)\)",
    r"\(S=\Spec(\underline{F}_2)\), \(\operatorname{S\ell}(2,\underline{F}_2)=\operatorname{G\ell}(2,\underline{F}_2)\)", F2NOTE)
add(558, "6.5.1, 'du groupe des commutateurs de Gℓ(2,F_2)'", F2SCAN, r"commutateurs de \(\operatorname{G\ell}(2,\mathbb F_2)\)", "font", "low",
    r"commutateurs de \(\operatorname{G\ell}(2,\mathbb F_2)\)", r"commutateurs de \(\operatorname{G\ell}(2,\underline{F}_2)\)", F2NOTE)
add(558, "6.5.1, 'tandis que l'ordre de Sℓ(2,F_2) est 6'", F2SCAN, r"l'ordre de \(\operatorname{S\ell}(2,\mathbb F_2)\)", "font", "low",
    r"l'ordre de \(\operatorname{S\ell}(2,\mathbb F_2)\)", r"l'ordre de \(\operatorname{S\ell}(2,\underline{F}_2)\)", F2NOTE)

add(558, "6.5.1, 'pour le topos annelé des faisceaux zariskiens sur S'",
    "'zariskiens' underlined (both scans; b556_560/page_558_s3.png, crops_556_560/wit_558_small.png)",
    "faisceaux zariskiens sur (no emphasis)", "underline", "high",
    "faisceaux zariskiens sur", r"faisceaux \emph{zariskiens} sur",
    r"\emph is the Exposé X command for underlined words (\emph{algébrique} on p. 559).")

add(558, "6.5.2, 'que toute représentation G_m → G_m soit définie par une'",
    "G_m twice with a plain typed G (both scans; crops_556_560/c558_Gm.png)",
    r"\(\Gm\to\Gm\) (\Gm = \mathbb G_m, main.tex line 13838)", "font", "low",
    r"représentation \(\Gm\to\Gm\) soit", r"représentation \(G_m\to G_m\) soit",
    r"As G_a on p. 556 (same class as the typist's plain Q: low). If the print's G_m is plain throughout Exposé X, a redefinition of \Gm for the exposé would replace the \Gm edits.")

# ---------------- page 559 ----------------
GSCAN = "a plain typed G (not underlined, not double-struck; both scans; b556_560/page_559_s1.png, page_559_s3.png)"
GNOTE = "As p. 558 (low; apply with the other G edits of pp. 556-559)."
add(559, "'la représentation G_m → G_m définie par'", GSCAN + "; two places",
    r"\(\Gm\to\Gm\)", "font", "low",
    r"la représentation \(\Gm\to\Gm\) définie", r"la représentation \(G_m\to G_m\) définie", GNOTE)
add(559, "'pour n'importe quelle représentation α : G → G_m.'", GSCAN,
    r"\(\alpha:G\to\Gm\)", "font", "low",
    r"\(\alpha:G\to\Gm\)", r"\(\alpha:G\to G_m\)", GNOTE)
add(559, "(6.5.4) 'α : Gℓ(n) → G_m'", GSCAN,
    r"\alpha:\operatorname{G\ell}(n)\longrightarrow\Gm", "font", "low",
    r"\alpha:\operatorname{G\ell}(n)\longrightarrow\Gm", r"\alpha:\operatorname{G\ell}(n)\longrightarrow G_m", GNOTE)
add(559, "(6.5.5) 'α_S : Gℓ(n)_S → G_{m,S}'", GSCAN,
    r"\longrightarrow\mathbb G_{m,S}", "font", "low",
    r"\longrightarrow\mathbb G_{m,S}", r"\longrightarrow G_{m,S}", GNOTE)

add(559, "'La représentation α dans (6.5.4) est bien entendu complètement déterminée par α_S.'",
    "begins a new, indented paragraph after 'pour tout Y ∈ Ob(C), s ∈ Gℓ(n)(Y) = Gℓ(n)_S(u(Y)).' (both scans; b556_560/page_559_s3.png, crops_556_560/wit_559_small.png)",
    "runs on in the same paragraph", "other", "high",
    r"(u(Y))\). La représentation", r"(u(Y))\)." + "\n\nLa représentation",
    "Missing paragraph break.")

add(559, "the category of the ringed topos: 'X = (C,O)', 'u : C → (Sch/S)', 'Y ∈ Ob(C)' twice, 'sur C est composé'",
    "a plain typed C (no underline, not double-struck) in all five places (both scans; crops_556_560/c559_XCO.png, c559_uC.png, c559_ObC.png)",
    r"\mathcal C (5 places)", "font", "high",
    None, None,
    r"Category letter, pending volume decision: not itemized; named in the message. The underlined O of (C,O), Spec(O(e)), Spec(O(Y)) is written \mathcal O, as the pending \cO decision.")

# ---------------- page 560 ----------------
add(560, "author line of the Appendice",
    "'par A. Grothendieck', the whole line underlined (both scans; b556_560/page_560_s1.png)",
    "par A. Grothendieck (no underline)", "underline", "medium",
    "par A. Grothendieck", r"\underline{par A. Grothendieck}",
    r"As the author line of Exposé X (p. 519, findings_516_520: \underline{par O. Jussila}) and the applied \underline{par P. BERTHELOT}. The title above (underlined 'Appendice' and 'Spécialisation en théorie des intersections') is accepted typesetting.")

add(560, "'Soit d'autre part N le faisceau conormal pour i'",
    "N struck twice, the typist's double-struck N (both scans; crops_556_560/c560_N.png, w560_N.png); the same N with a clear second stem in the two displays",
    r"\(N\)", "font", "medium",
    r"Soit d'autre part \(N\)", r"Soit d'autre part \(\mathbb N\)",
    r"The conormal sheaf is a double-struck N in all three places of this page (next two entries); the TeX has a plain N. The volume writes the print's double-struck letters as \mathbb. p. 561 has the same N ('dont le faisceau conormal N est libre', 'λ_{-1}(N) = 0') for its checker. Apply the three N edits together.")
add(560, "display 'λ_{-1}(N) ∈ K˙(Y) .'",
    "double-struck N, an N with a second left stem (both scans; crops_556_560/c560_lamN.png, w560_lamN.png)",
    r"\lambda_{-1}(N)\in K^\circ(Y).", "font", "medium",
    r"\lambda_{-1}(N)\in", r"\lambda_{-1}(\mathbb N)\in",
    r"As the first N entry. The old does not contain K^\circ (convention entry below).")
add(560, "display 'i*i_*(x) = x λ_{-1}(N)  pour x ∈ K.(Y) ,'",
    "double-struck N (both scans; crops_556_560/c560_formula.png)",
    r"x\lambda_{-1}(N)\qquad", "font", "medium",
    r"x\lambda_{-1}(N)\qquad", r"x\lambda_{-1}(\mathbb N)\qquad",
    "As the first N entry.")

add(560, "'Considérons aussi l'nomomorphisme image directe (IV 2.11)'",
    "'l'nomomorphisme': n for h (no ascender, against the h of 'morphisme' in the same word; both scans; crops_556_560/c560_nomo.png, w560_nomo.png)",
    "l'nomomorphisme (printed reading kept)", "misprint_in_print", "high",
    None, None, "Typing error of the print; the TeX keeps it.", corrected="l'homomorphisme")

add(560, "K˙ on p. 560 (4 places: the display 'λ_{-1}(N) ∈ K˙(Y)', 'structure de K˙(Y)-module', 'avec K˙(X), K˙(Y)')",
    "K with a raised dot in every place (both scans; crops_556_560/c560_lamN.png, c560_Kdot.png)",
    r"K^\circ (4 places)", "symbol", "high",
    None, None,
    r"The Exposé X convention reported in findings_521_525 (one script K^\circ -> K^{\bullet} for Exposé X, both layers); the Appendice follows it: not itemized. Three examples: '\in K^\circ(Y).' -> '\in K^{\bullet}(Y).'; 'structure de \(K^\circ(Y)\)-module' -> 'structure de \(K^{\bullet}(Y)\)-module'; 'avec \(K^\circ(X)\), \(K^\circ(Y)\)' -> 'avec \(K^{\bullet}(X)\), \(K^{\bullet}(Y)\)'. No old string of this file contains K^\circ.")

add(560, "statements of p. 560: Lemme 7.1 (to '... définie dans (IV 2.10).') and Corollaire 7.2",
    "underlined word group by word group (both scans): Lemme 7.1 'Soit', 'une immersion fermée régulière', 'de codimension bornée', 'de sorte que', 'est un morphisme parfait', 'et qu'on peut donc définir le morphisme', 'Soit d'autre part', 'le faisceau conormal pour', 'qui est un faisceau localement libre de type fini sur', 'de sorte qu'on peut former', 'Considérons aussi l'nomomorphisme image directe', 'Ceci posé', 'on a la formule', 'où le produit du deuxième membre est relatif à la structure de', 'module', 'de', 'définie dans'; Corollaire 7.2 'Soient', 'un morphisme plat', 'avec', 'un trait', 'i.e.', 'le spectre d'un anneau de valuation discrète', 'le point fermé de', 'son point générique', 'l'inclusion canonique', 'Alors', 'est de tor-dimension finie donc', 'on peut définir'; letters, formulas, references and punctuation plain; the labels underline only the word",
    "the statements in roman", "underline", "high",
    None, None,
    "Exposé X follows the Exposé II pattern of GLOBAL_ISSUES 82 (pending volume decision; findings_521_525, findings_526_530): not itemized. 'La démonstration est, essentiellement sans changement, ...' is plain in the print.")

# ---------------- checks ----------------
ok = True
pages = {}
for n in range(556, 561):
    pages[n] = (B / f"page_{n}.tex").read_bytes().decode("utf-8")
    assert "\r" not in pages[n], n
for i, d in enumerate(F):
    fx = d["fix"]
    if fx is None:
        continue
    t = pages[d["page"]]
    c = t.count(fx["old"])
    if c != 1 or "%%%%%%%%%%" in fx["old"] or "%%%%%%%%%%" in fx["new"]:
        print("BAD", i, d["page"], c, repr(fx["old"]))
        ok = False
    for ch in fx["new"]:
        if ord(ch) < 32 and ch != "\n":
            print("CTRL", i, repr(fx["new"])); ok = False
# simulate: apply each page's fixes in order, each old once at the time of application
for n in range(556, 561):
    t = pages[n]
    for i, d in enumerate(F):
        if d["page"] != n or d["fix"] is None:
            continue
        o, w = d["fix"]["old"], d["fix"]["new"]
        if t.count(o) != 1:
            print("SIM-BAD", n, i, t.count(o), repr(o)); ok = False
            continue
        t = t.replace(o, w)
    # reverse order too
    t = pages[n]
    for i, d in reversed(list(enumerate(F))):
        if d["page"] != n or d["fix"] is None:
            continue
        o, w = d["fix"]["old"], d["fix"]["new"]
        if t.count(o) != 1:
            print("SIM-REV-BAD", n, i, t.count(o), repr(o)); ok = False
            continue
        t = t.replace(o, w)
cnt = {}
for d in F:
    k = cnt.setdefault(d["page"], [0, 0])
    k[1 if d["kind"] == "misprint_in_print" else 0] += 1
print("entries", len(F), "per page (normal/misprint):", {p: f"{a}/{b}" for p, (a, b) in sorted(cnt.items())})
print("OK" if ok else "PROBLEMS")
if ok:
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(F, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    print("written", OUT)
