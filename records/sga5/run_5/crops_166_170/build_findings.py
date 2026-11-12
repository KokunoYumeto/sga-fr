"""Build findings_166_170.json and check that every fix's old occurs exactly once (also when applied in order)."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
B = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\b166_170")
OUT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\findings_166_170.json")

EMPH = ("\\emph is the file's command for the print's underline in Exposé III, whose typescript III B continues "
        "(as in the findings of pp. 141-150); Exposé III B has no underline markup of its own.")


def F(page, where, scan, tex, kind, conf, fix, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
         "fix": None if fix is None else {"old": fix[0], "new": fix[1]}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


L = []

# ---------------- page 166 ----------------
L += [
    F(166, "first sentence, 'se factorise (de manière unique) à travers 5.3.3'",
      "'(de manière unique)' between parentheses",
      "se factorise de manière unique (no parentheses)", "punctuation", "high",
      ("se factorise de manière unique", "se factorise (de manière unique)")),
    F(166, "(5.3.4), end of the display",
      "a comma after the display: '(E ⊗_K F) ⊗_{A^e} A   ,'",
      "no comma", "punctuation", "high",
      (r"(E\lten_KF)\lten_{A^e}A", r"(E\lten_KF)\lten_{A^e}A,")),
    F(166, "'D'autre part, 5.3.3 se dérive en une flèche de D(K), dite flèche d'évaluation,'",
      "'flèche d'évaluation' underlined ('dite' not)",
      "not underlined", "underline", "high",
      ("dite flèche d'évaluation,", r"dite \emph{flèche d'évaluation},"), EMPH),
    F(166, "'tel que RHom_A(E,F) ∈ ob D^b(A°) : on dérive d'abord 5.3.2'",
      "' : on dérive' (colon, small o)",
      "'. On dérive' (full stop, capital O)", "punctuation", "high",
      (r"(A^\circ)$. On dérive", r"(A^\circ)$ : on dérive")),
    F(166, "'d'abord 5.3.2 en une flèche de D^-((A^e)°)', before (5.3.6)",
      "no comma after D^-((A^e)°) (clear at 2x)",
      "$D^-((A^e)^\\circ)$, (comma added)", "punctuation", "high",
      (r"$D^-((A^e)^\circ)$,", r"$D^-((A^e)^\circ)$")),
    F(166, "number of no. 5.4",
      "'5.4.' with a full stop",
      "\\subsubsection*{5.4}", "punctuation", "high",
      (r"\subsubsection*{5.4}", r"\subsubsection*{5.4.}"), "As '1.1.' on p. 140."),
    F(166, "'La flèche 5.4.1 se dérive en une flèche de D(K)'",
      "begins a new, indented paragraph",
      "runs on after '... E ⊗_K Hom_A(E,F) → F.' in the same paragraph", "other", "high",
      (r"\to F$. La flèche 5.4.1", r"\to F$." + "\n\n" + "La flèche 5.4.1")),
    F(166, "'dite flèche de produit tensoriel,'",
      "'flèche de produit tensoriel' underlined (across the break 'pro-/duit')",
      "not underlined", "underline", "high",
      ("dite flèche de produit tensoriel,", r"dite \emph{flèche de produit tensoriel},")),
]

# ---------------- page 167 ----------------
L += [
    F(167, "'le premier membre de 5.4.2 s'identifie en effet à Hom^•_A(E,F) ⊗_A G'",
      "Hom underlined (as in 5.4.1)",
      "\\Hom_A^\\bullet (no underline)", "underline", "high",
      (r"$\Hom_A^\bullet(E,F)\otimes_AG$", r"$\uHom_A^\bullet(E,F)\otimes_AG$")),
    F(167, "'la flèche naturelle Hom^•_A(E,F ⊗_A G) ⟶ RHom_A(E,F ⊗_A G) = ...'",
      "Hom underlined",
      "\\Hom_A^\\bullet (no underline)", "underline", "high",
      (r"\Hom_A^\bullet(E,F\otimes_AG)\longrightarrow", r"\uHom_A^\bullet(E,F\otimes_AG)\longrightarrow")),
    F(167, "'La flèche 5.4.2 n'est pas en général un isomorphisme.'",
      "begins a new, indented paragraph after the formula",
      "no blank line after \\]: runs on", "other", "high",
      (r"\]" + "\n" + "La flèche 5.4.2", r"\]" + "\n\n" + "La flèche 5.4.2")),
    F(167, "'Elle l'est cependant certains cas importants'",
      "'cepen-/dant certains cas importants': no 'dans' (clear at 1.2x)",
      "cependant dans certains (silently corrected)", "misprint_in_print", "high",
      ("cependant dans certains", "cependant certains"),
      "Missing word. The TeX silently supplies it; the fix restores the printed reading (diplomatic layer only).",
      "cependant dans certains"),
    F(167, "'par exemple si E est parfait (comme on le vérifie'",
      "'parfait' underlined",
      "not underlined", "underline", "high",
      ("est parfait (comme", r"est \emph{parfait} (comme")),
    F(167, "'b) F = M ⊗_K A , avec M ∈ ob D^+(K) (au n° 6, M sera un complexe dualisant, ...'",
      "an opening parenthesis before 'au n° 6'",
      "'$; au numéro 6,' (semicolon, no parenthesis)", "punctuation", "high",
      (r"D^+(K)$; au", r"D^+(K)$ (au"),
      "Apply together with the closing parenthesis after '6.5.6' (two findings below)."),
    F(167, "same place, 'au n° 6'",
      "'n°' (abbreviation)",
      "numéro (written out)", "word", "high",
      ("numéro 6", r"n\textsuperscript{o}~6"),
      "The file writes n\\textsuperscript{o}~5 in the introduction of Exposé III B."),
    F(167, "'voir notamment 6.3.2 , 6.4.1, 6.5.6).'",
      "a closing parenthesis before the full stop",
      "6.5.6. (no parenthesis)", "punctuation", "high",
      ("6.5.6.", "6.5.6)."),
      "Pairs with the opening parenthesis before 'au n° 6'."),
    F(167, "number of no. 5.5",
      "'5.5.' with a full stop",
      "\\subsubsection*{5.5}", "punctuation", "high",
      (r"\subsubsection*{5.5}", r"\subsubsection*{5.5.}")),
    F(167, "5.5, 'Notons DF(A) la cétégorie dérivée des complexes'",
      "'cétégorie' (é for a), clear at 2x",
      "catégorie (silently corrected)", "misprint_in_print", "high",
      ("la catégorie dérivée", "la cétégorie dérivée"),
      "Typing error. The TeX silently corrects; the fix restores the printed reading (diplomatic layer only).",
      "la catégorie dérivée"),
    F(167, "5.5, 'on a des flèches \"dérivées filtrées\" analogues à 5.3.4'",
      "'dérivées filtrées' between typewriter double quotes",
      "no quotes", "punctuation", "high",
      ("flèches dérivées filtrées analogues", "flèches ``dérivées filtrées'' analogues")),
    F(167, "number of no. 5.6",
      "'5.6.' with a full stop",
      "\\subsubsection*{5.6}", "punctuation", "high",
      (r"\subsubsection*{5.6}", r"\subsubsection*{5.6.}")),
    F(167, "5.6, 'complexes d'amplitude parfaite finie, i.e. parfaits et de tor-dimension finie'",
      "'i.e.'",
      "c'est-à-dire (abbreviation written out)", "word", "high",
      ("finie, c'est-à-dire parfaits", "finie, i.e. parfaits")),
    F(167, "'On définit une flèche canonique, dite trace,'",
      "'trace' underlined",
      "not underlined", "underline", "high",
      ("dite trace,", r"dite \emph{trace},")),
    F(167, "(5.6.1), end of the display",
      "a comma after '⊗_{A^e} A'",
      "no comma", "punctuation", "high",
      (r"\longrightarrow F\lten_{A^e}A", r"\longrightarrow F\lten_{A^e}A,")),
    F(167, "(5.6.1), 'Tr_A = RHom_A(E,F ⊗_A E) ⟶ F ⊗_{A^e} A'",
      "'Tr_A =' with an equals sign (clear at 2x)",
      "\\Tr_A=\\uRHom_A (keeps the printed reading)", "misprint_in_print", "medium",
      None,
      "Tr_A is the map RHom_A(E,F⊗E) → F⊗_{A^e}A; the traces 5.6.2-5.6.4 (p. 168) and Tr_K (pp. 168-169) are "
      "written 'Tr :'. The TeX keeps the printed reading.",
      r"\Tr_A:\uRHom_A(E,F\lten_AE)"),
]

# ---------------- page 168 ----------------
L += [
    F(168, "(5.6.2) 'Tr_A : Hom_A(E,F ⊗_A E) ⟶ H^0(T,F ⊗_{A^e} A)'",
      "plain Hom, not underlined (clear at 2x)",
      "\\uHom_A (underlined)", "underline", "high",
      (r"\uHom_A(E,F\lten_AE)\longrightarrow H^0", r"\Hom_A(E,F\lten_AE)\longrightarrow H^0"),
      "The global Hom (H^0 of the target), as Hom_{DF(A)} below; the print underlines only RHom in 5.6.3."),
    F(168, "(5.6.4) 'Tr_A : Hom_A(E,E) ⟶ H^0(T,A_♮)'",
      "plain Hom, not underlined (clear at 2x)",
      "\\uHom_A (underlined)", "underline", "high",
      (r"\uHom_A(E,E)", r"\Hom_A(E,E)")),
    F(168, "'Cette formule entraîne notamment que, pour E ∈ ..., u ∈ Hom_A(E,F ⊗_A E) , on a'",
      "plain Hom, not underlined (clear at 2x)",
      "\\uHom_A (underlined)", "underline", "high",
      (r"u\in\uHom_A(E,F\lten_AE)", r"u\in\Hom_A(E,F\lten_AE)")),
    F(168, "'tandis que 5.6.3 est une flèche \"sérieuse\", de nature globale'",
      "'sérieuse' between typewriter double quotes",
      "no quotes", "punctuation", "high",
      ("flèche sérieuse,", "flèche ``sérieuse'',")),
    F(168, "'d'où des flèches analogue à 5.6.2, 5.6.3, 5.6.4'",
      "'analogue' without s (clear at 2x)",
      "analogues (silently corrected)", "misprint_in_print", "high",
      ("des flèches analogues à 5.6.2", "des flèches analogue à 5.6.2"),
      "Agreement error. The TeX silently corrects; the fix restores the printed reading (diplomatic layer only).",
      "des flèches analogues à 5.6.2"),
    F(168, "'compatible avec le passage au gradué associé (cf. ([3] V 3.7.2))'",
      "'(cf.' at the end of the line, '([3] V 3.7.2)),' on the next: the reference has its own parentheses",
      "(cf. [3] V 3.7.2)", "punctuation", "high",
      ("(cf. [3] V 3.7.2)", "(cf. ([3] V 3.7.2))")),
    F(168, "'et on en déduit, comme en (loc. cit.), que'",
      "'(loc. cit.)' between parentheses",
      "comme en loc. cit., que", "punctuation", "high",
      ("comme en loc. cit., que", "comme en (loc. cit.), que")),
    F(168, "(5.6.5) 'Tr_A(u) = Σ_i Tr_A gr^i u'",
      "'Tr_A gr^i u' without parentheses",
      "\\Tr_A(\\operatorname{gr}^i u) (parentheses added)", "formula", "high",
      (r"\Tr_A(\operatorname{gr}^i u)", r"\Tr_A\operatorname{gr}^i u")),
    F(168, "number of no. 5.7",
      "'5.7.' with a full stop",
      "\\subsubsection*{5.7}", "punctuation", "high",
      (r"\subsubsection*{5.7}", r"\subsubsection*{5.7.}")),
    F(168, "5.7, 'les traces commutatives \"usuelles\" ((SGA 6 I), ([3] V 3))'",
      "'usuelles' between typewriter double quotes",
      "no quotes", "punctuation", "high",
      ("commutatives usuelles", "commutatives ``usuelles''")),
    F(168, "5.7, '([3] V 3)), et les traces'",
      "a comma after '([3] V 3))'",
      "no comma", "punctuation", "high",
      ("([3] V 3)) et les", "([3] V 3)), et les")),
    F(168, "5.7, 'les traces \"non commutatives\" de Stallings [5]'",
      "'non commutatives' between typewriter double quotes (the a of 'commutatives' overtyped)",
      "no quotes", "punctuation", "high",
      ("traces non commutatives", "traces ``non commutatives''")),
    F(168, "'a) Supposons A = K .'",
      "'a)' with a closing parenthesis only",
      "(a)", "punctuation", "high",
      ("(a) Supposons", "a) Supposons")),
]

# ---------------- page 169 ----------------
L += [
    F(169, "first sentence, 'définie en ([3] V 3.7.1) (dans le cas particulier où ...'",
      "a parenthesis opens before 'dans le cas particulier'",
      "'([3] V 3.7.1), dans le cas' (comma, no parenthesis)", "punctuation", "high",
      ("([3] V 3.7.1), dans le cas", "([3] V 3.7.1) (dans le cas"),
      "Apply together with the closing parenthesis after 'réduit à A' (two findings below)."),
    F(169, "'où le complexe K de (loc. cit.) est réduit à A'",
      "'(loc. cit.)' between parentheses",
      "de loc. cit. est", "punctuation", "high",
      ("de loc. cit. est", "de (loc. cit.) est")),
    F(169, "'est réduit à A ). En particulier,'",
      "a closing parenthesis after A",
      "réduit à $A$. (no parenthesis)", "punctuation", "high",
      ("réduit à $A$. En", "réduit à $A$). En"),
      "Pairs with the opening parenthesis before 'dans le cas particulier'."),
    F(169, "'b) On suppose à nouveau'",
      "'b)' with a closing parenthesis only",
      "(b)", "punctuation", "high",
      ("(b) On suppose", "b) On suppose")),
    F(169, "'une K-algèbre plate (non nécessairement commutative).'",
      "'(non nécessairement commutative)' between parentheses",
      "'plate, non nécessairement commutative.'", "punctuation", "high",
      ("plate, non nécessairement commutative.", "plate (non nécessairement commutative).")),
    F(169, "'pour E strictement parfait (i.e. borné, ...'",
      "a parenthesis opens before 'i.e.'",
      "'parfait, c'est-à-dire' (comma)", "punctuation", "high",
      ("$E$ strictement parfait, ", "$E$ strictement parfait ("),
      "Apply together with the closing parenthesis after 'de type fini' (three findings below)."),
    F(169, "same place, '(i.e. borné,'",
      "'i.e.'",
      "c'est-à-dire (abbreviation written out)", "word", "high",
      ("c'est-à-dire borné", "i.e. borné")),
    F(169, "'à composantes localement facteurs directs de modules libre de type fini'",
      "'libre' without s (clear at 1x)",
      "libres (silently corrected)", "misprint_in_print", "high",
      ("modules libres", "modules libre"),
      "Agreement error. The TeX silently corrects; the fix restores the printed reading (diplomatic layer only).",
      "modules libres"),
    F(169, "'de modules libre de type fini). Tout d'abord'",
      "a closing parenthesis after 'fini'",
      "type fini. (no parenthesis)", "punctuation", "high",
      ("type fini. Tout", "type fini). Tout"),
      "Pairs with the opening parenthesis before 'i.e.'."),
    F(169, "'que nous noterons a ⟼ a_♮ , donc si d_a désigne'",
      "a comma after a_♮",
      "a semicolon", "punctuation", "high",
      (r"a_\natural$; donc si", r"a_\natural$, donc si")),
    F(169, "'L'isomorphisme 5.4.2 pour F = A , G = E s'écrit'",
      "no comma after '5.4.2' and none after 'G = E'",
      "'5.4.2, pour $F=A$, $G=E$, s'écrit' (two commas added)", "punctuation", "high",
      ("5.4.2, pour $F=A$, $G=E$, s'écrit", "5.4.2 pour $F=A$, $G=E$ s'écrit")),
    F(169, "(5.7.2) 'Tr_A(u) = Σ_i u_{ii♮}'",
      "no parentheses: the hand-drawn ♮ stands lower right of the index ii",
      "(u_{ii})_\\natural (parentheses added)", "formula", "high",
      (r"\sum_i (u_{ii})_\natural", r"\sum_i u_{ii_\natural}"),
      "The ♮ sits below the level of ii, as a subscript of the subscript."),
    F(169, "'est un homomorphisme de complexes, on a, par 5.6.5, 5.6.6,'",
      "'par 5.6.5, 5.6.6,' (comma, no 'et')",
      "par 5.6.5 et 5.6.6, ('et' added)", "word", "high",
      ("par 5.6.5 et 5.6.6,", "par 5.6.5, 5.6.6,")),
    F(169, "(5.7.4) 'Tr_A(u) = Σ(-1)^i Tr_A(u^i)'",
      "Σ without an index (clear at 3x)",
      "\\sum_i (index added)", "formula", "high",
      (r"\sum_i(-1)^i", r"\sum(-1)^i")),
]

# ---------------- page 170 ----------------
L += [
    F(170, "'d'un homomorphisme de complexes Hom^•_A(E,E) ⟶ A (5.6.3)'",
      "target 'A' with no ♮ (clear at 2.5x)",
      "\\uHom_A^\\bullet(E,E)\\to A (keeps the printed reading)", "misprint_in_print", "medium",
      None,
      "5.6.3 is Tr_A : RHom_A(E,E) → A_♮, and a trace is defined only modulo commutators (5.7.1: Tr_A(d_a) = a_♮); "
      "the hand-drawn ♮ seems left out here. The TeX keeps the printed reading.",
      r"\uHom_A^\bullet(E,E)\to A_\natural"),
    F(170, "'pour tout endomorphisme u de E dans D(A) , et, combinées à 5.7.5,'",
      "a comma after D(A)",
      "no comma", "punctuation", "high",
      ("dans $D(A)$ et, combinées", "dans $D(A)$, et, combinées")),
    F(170, "'on retrouve la définition de (SGA 4^{1/2} Rapport 4.3).'",
      "no comma after 4^{1/2}",
      "(SGA $4^{1/2}$, Rapport 4.3) (comma added)", "punctuation", "high",
      (r"$4^{1/2}$, Rapport", r"$4^{1/2}$ Rapport")),
    F(170, "number of no. 5.8",
      "'5.8.' with a full stop",
      "\\subsubsection*{5.8}", "punctuation", "high",
      (r"\subsubsection*{5.8}", r"\subsubsection*{5.8.}")),
    F(170, "(5.8.1), the three isomorphism signs",
      "each sign is a long horizontal line with a tilde above it and no arrowhead (a stretched ≃; clear at 4x)",
      "\\xrightarrow{\\sim} (arrows)", "symbol", "high",
      (r"A\xrightarrow{\sim}P\otimes_{A^e}Q\xrightarrow{\sim}(Q\otimes_AP)\otimes_{A^e}A\xrightarrow{\sim}A",
       r"A\simeq P\otimes_{A^e}Q\simeq(Q\otimes_AP)\otimes_{A^e}A\simeq A"),
      "The other arrows of the page have their heads; 5.8.2 has the short ≃ (\\simeq in the TeX)."),
    F(170, "'pour y ∈ P , y ∈ Q , a, b ∈ K'",
      "'y ∈ P' (clear at 1.2x)",
      "$y\\in P$ (keeps the printed reading)", "misprint_in_print", "high",
      None,
      "The generators are axb ⊗ y - x ⊗ bya with x in P and y in Q. The TeX keeps the printed reading.",
      r"$x\in P$"),
    F(170, "same line, 'a, b ∈ K'",
      "'a, b ∈ K' (clear at 1.2x)",
      "$a,b\\in K$ (keeps the printed reading)", "misprint_in_print", "high",
      None,
      "For a, b in K (central) axb ⊗ y - x ⊗ bya is 0, so the quotient would be P ⊗_K Q, not P ⊗_{A^e} Q: "
      "a, b run through A. The TeX keeps the printed reading.",
      r"$a,b\in A$"),
    F(170, "'D'autre part, la flèche de composition au niveau des modules,'",
      "a comma after 'modules' ('mo-/dules,')",
      "no comma", "punctuation", "high",
      ("au niveau des modules" + "\n" + r"\[", "au niveau des modules," + "\n" + r"\[")),
    F(170, "first line of the composition display, '... ⟶ Hom_A(E,P ⊗_A Q ⊗_A E)'",
      "no comma at the end of the line (the comma follows 'f ⊗ g ⟼ (P ⊗_A g)f' on the next line)",
      "comma after the first line", "punctuation", "high",
      (r"P\otimes_AQ\otimes_AE),", r"P\otimes_AQ\otimes_AE)")),
]

# ---------------- checks ----------------
ok = True
texts = {p: (B / f"page_{p}.tex").read_text(encoding="utf-8") for p in range(166, 171)}
work = dict(texts)
for i, x in enumerate(L):
    if x["fix"] is None:
        continue
    old, new = x["fix"]["old"], x["fix"]["new"]
    n = texts[x["page"]].count(old)
    m = work[x["page"]].count(old)
    if "%%%%%%%%%%" in old:
        print("MARKER IN OLD", i)
        ok = False
    if n != 1 or m != 1:
        print(f"COUNT {i} page {x['page']}: original {n}, in sequence {m}: {old!r}")
        ok = False
    else:
        work[x["page"]] = work[x["page"]].replace(old, new, 1)
for p in range(166, 171):
    norm = sum(1 for x in L if x["page"] == p and x["kind"] != "misprint_in_print")
    mis = sum(1 for x in L if x["page"] == p and x["kind"] == "misprint_in_print")
    print(p, f"{norm}/{mis}")
print("all olds unique:", ok)
if ok:
    OUT.write_text(json.dumps(L, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("written", OUT)
