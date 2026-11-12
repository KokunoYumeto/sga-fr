"""Write run_6/findings_031_035.json (SGA 6, pp. 31-35)."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
F = []


def add(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, confidence=confidence, fix=fix)
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def fx(old, new):
    return {"old": old, "new": new}


NL = "\n"

# ---------------- page 31 ----------------
add(31, "after (1.22 bis), 'et par suite, la composante x^n s'obtient'",
    "et par suite, la composante x^n ...: the underline starts at 'composante'; 'la' is not underlined (both scans)",
    r"\emph{la composante}", "underline", "high",
    fx(r"\emph{la composante}", r"la \emph{composante}"),
    "The article stands outside the underline, as the math between the underlined words.")
add(31, "(1.26)",
    "ch : Ã ——— \\widehat{A ⊗ Q} . : one wide hat spans A ⊗ Q (both scans)",
    r"\ch:\widetilde A\longrightarrow \Ahat\otimes\Q. (\Ahat = \widehat A: the hat over A only)",
    "formula", "high",
    fx(r"\Ahat\otimes\Q.", r"\widehat{A\otimes\Q}."),
    "The print completes A ⊗ Q (the target of ch, which has denominators in every degree); the three places of "
    "p. 32 have the same wide hat, while 1 + Â^+ on p. 32 has a small hat over A alone. \\Ahat\\otimes\\Q occurs "
    "only on pp. 31-32 of main.tex (4 places, all reported). Independent of the arrow fix below (no overlap).")
add(31, "(1.26), the sign between Ã and the target",
    "Ã ——— : a plain typed rule with no arrowhead; it ends cleanly in both scans",
    r"\widetilde A\longrightarrow", "misprint_in_print", "medium",
    fx(r"\widetilde A\longrightarrow", r"\widetilde A\relbar\joinrel\relbar\joinrel\relbar"),
    "ch : Ã -> (A⊗Q)^ is a map, and the typed arrows of p. 32 (1 + Â^+ ⟶ ...) and p. 33 ((a_1,...,a_p) ⟶ ...) "
    "have their heads: the head was never typed. The TeX silently supplies it; the fix restores the printed "
    "headless rule in the form used for such rules in SGA 7 I (\\relbar\\joinrel...). 'corrected' is the "
    "current TeX.",
    corrected=r"\widetilde A\longrightarrow")
add(31, "'on va définir un homomorphisme d'anneaux augnentés'", "augnentés",
    "augnentés (printed reading kept)", "misprint_in_print", "high", None,
    "n for m in the print; the TeX keeps it. The corrected layer still reads 'augnentés'.",
    corrected="augmentés")
add(31, "'Cet homomorphisme est défini sans ambiguité'",
    "ambiguité: the i has only its dot, no diaeresis (both scans)",
    "ambiguïté", "misprint_in_print", "medium",
    fx("ambiguïté", "ambiguité"),
    "On p. 33 the typist marks this i ('sans ambiguïté un élément'); here the mark is missing. The TeX silently "
    "corrects; the fix restores the printed reading. The OCR also reads 'ambiguité' on pp. 102, 109, 122, 250, "
    "276 and 294 (not checked on the scans), where main.tex has 'ambiguïté'.",
    corrected="ambiguïté")

# ---------------- page 32 ----------------
add(32, "'soit η l'endomorphisme additif de Â⊗Q défini pour x^i'",
    "\\widehat{A ⊗ Q}: one wide hat over A ⊗ Q (both scans)",
    r"additif de $\Ahat\otimes\Q$ défini", "formula", "high",
    fx(r"additif de $\Ahat\otimes\Q$ défini", r"additif de $\widehat{A\otimes\Q}$ défini"),
    "As (1.26) on p. 31.")
add(32, "'on a un isomorphisme ch de l'anneau Ã⊗Q sur l'anneau Â⊗Q'",
    "sur l'anneau \\widehat{A ⊗ Q} (one wide hat, both scans)",
    r"\emph{sur l'anneau} $\Ahat\otimes\Q$", "formula", "high",
    fx(r"\emph{sur l'anneau} $\Ahat\otimes\Q$", r"\emph{sur l'anneau} $\widehat{A\otimes\Q}$"),
    "As (1.26) on p. 31.")
add(32, "'un homomorphisme additif 1 + Â^+ ⟶ 1 + (Â⊗Q)^+'",
    "1 + (\\widehat{A ⊗ Q})^+ : the hat spans A ⊗ Q inside the parentheses; the hat of 1 + Â^+ covers A only "
    "(both scans)",
    r"1+(\Ahat\otimes\Q)^+", "formula", "high",
    fx(r"1+(\Ahat\otimes\Q)^+", r"1+(\widehat{A\otimes\Q})^+"),
    "As (1.26) on p. 31; \\Ahp (\\widehat A^{+}) on the left is right.")
add(32, "(1.28), end of the display",
    "η(x^i) = 1/(-1)^{i-1}(i-1)! x^i with no full stop (both scans); the sentence runs on 'on a alors'",
    r"(i-1)!\,x^i.", "punctuation", "high",
    fx(r"(i-1)!\,x^i.", r"(i-1)!\,x^i"),
    "The TeX adds a full stop at the end of (1.28).")
add(32, "line after (1.28)", "on a alors (small o, both scans)", "On a alors", "word", "high",
    fx("On a alors", "on a alors"),
    "The sentence continues after (1.28) ('soit η ... défini ... par (1.28) on a alors'); the TeX starts a new "
    "sentence with a capital, together with its added full stop (previous entry).")
add(32, "Proposition 1.3, '(on a N^i = 0 pour i > q). Si l'on pose :'",
    "underlined: 'Soit', 'de la forme', 'Si l'on pose'; the remark '(on a N^i = 0 pour i > q).' is not "
    "underlined (both scans)",
    "one \\emph{...} from 'Soit' to 'Si l'on pose~:', the remark included", "underline", "high",
    fx(r"$[q,1+N^1+\cdots+N^q]$ (on a $N^i=0$ pour $i>q$). Si l'on pose~:}",
       r"$[q,1+N^1+\cdots+N^q]$} (on a $N^i=0$ pour $i>q$). \emph{Si l'on pose~:}"),
    "Close the emphasis before the remark and reopen it at 'Si l'on pose', as done for Proposition 1.2 "
    "on p. 30.")
add(32, "Proposition 1.3, display defining λ_{-1}(N), second sum",
    "Σ_{i=0}^{n} (upper limit n, both scans)",
    r"\sum_{i=0}^{n} (printed reading kept)", "misprint_in_print", "medium", None,
    "N = [q, 1 + N^1 + ... + N^q] has rank q, so λ^i(N) = 0 for i > q and the finite sum ends at q; n is not "
    "defined in the statement (a carry-over from Proposition 1.2). The TeX keeps the printed n; the corrected "
    "layer also reads n.",
    corrected=r"\sum_{i=0}^{q}")
add(32, "throughout Exposé 0 App (here: 'noté 𝒯_f', '𝒯_f = 𝒯 (𝒯 est l'initiale de Todd)', '𝒯(x)', (1.30))",
    "a hand-drawn script T (wavy top stroke opening with a loop, stem curved like a C); the text itself calls "
    "it 'l'initiale de Todd'",
    r"\mathcal C (six times on this page)", "symbol", "medium", None,
    "Convention of the transcription, not a page fix: the handwritten Todd letter is written \\mathcal C. "
    "Examples: p. 32 '$\\mathcal C_f=\\mathcal C$ ($\\mathcal C$ est l'initiale de Todd)', p. 32 (1.30) "
    "'(-1)^q N^q\\mathcal C(\\check N)^{-1}', p. 33 (1.30 bis) 'N^q\\mathcal C(N)^{-1}'. In main.tex the same "
    "letter is \\mathcal C in 15 places of Exposé 0 App: pp. 32 (6), 33 (1), 67 (1), 68 (1), 69 (4), 70 (2) "
    "(on pp. 67-70 the Todd classes \\check{\\mathcal C}(...)); the letters for categories (\\cC on pp. 42-45, "
    "\\mathcal C on pp. 84-99) are not concerned. One replacement \\mathcal C -> \\mathcal T in those 15 places, "
    "both layers.")

# ---------------- page 33 ----------------
add(33, "'on peut donc définir sans ambiguïté un élément λ^p(N,x) de A en posant'",
    "de A en posant (no colon, both scans)", "en posant~:", "punctuation", "high",
    fx("en posant~:", "en posant"),
    "The TeX adds a colon before (1.32).")
add(33, "(1.32), end of the display",
    "λ^p(N,x)λ_{-1}(N) = λ^p(xλ_{-1}(N)) with no full stop (both scans)",
    r"\lambda^p(x\lambda_{-1}(N)).", "punctuation", "high",
    fx(r"\lambda^p(x\lambda_{-1}(N)).", r"\lambda^p(x\lambda_{-1}(N))"),
    "The TeX adds a full stop at the end of (1.32).")
add(33, "'notre anneau A en est un complèté)'",
    "complèté (grave accent on the first e, acute on the last; both scans)",
    "complèté (printed reading kept)", "misprint_in_print", "high", None,
    "Grave for acute accent in the print; the TeX keeps it. The corrected layer still reads 'complèté'.",
    corrected="complété")
add(33, "Théorème 1.4, 'est un polynôme, isobare de poids p'",
    "est un polynôme, isobare de: 'est un' and 'isobare de' are underlined, 'polynôme,' is not (both scans)",
    "one \\emph{...} over the whole statement, 'polynôme' included", "underline", "high",
    fx("est un polynôme, isobare", r"est un} polynôme, \emph{isobare"),
    "Every other word of the statement is underlined; probably a slip of the typist, but the print does not "
    "underline it.")
add(33, "end of page, '... a_1 + ... + a_p de N^p dans N. On'",
    "de N^p dans N.: only 'dans' is underlined; 'de' is not (both scans)",
    r"\emph{de $N^p$ dans $N$.}", "underline", "high",
    fx(r"\emph{de $N^p$ dans $N$.}", r"de $N^p$ \emph{dans} $N$."),
    "The following 'On' (last word of the page, see the marker entry of p. 34) is not underlined either.")

# ---------------- page 34 ----------------
add(34, "start of page",
    "p. 33 ends '... de N^p dans N. On'; p. 34 begins 'fait opérer le groupe symétrique' (both scans)",
    "page_034.tex begins '\\emph{On fait opérer' under the folio-34 marker", "marker", "high", None,
    "Page 34 really begins with 'fait opérer'; 'On' belongs to p. 33. Apply the underline fix of the next entry "
    "first ('\\emph{On fait opérer' -> 'On \\emph{fait opérer', both layers), then move the marker forward "
    "(no --before): python -I move_marker.py 6 34 \"\\emph{fait opérer\" (simulated on both layers: "
    "'... dans $N$.}' / 'On ' / marker / '\\emph{fait opérer ...').")
add(34, "first line, 'On fait opérer le groupe symétrique'",
    "'On' (end of p. 33) is not underlined; the underline starts at 'fait' (both scans)",
    r"\emph{On fait opérer", "underline", "high",
    fx(r"\emph{On fait opérer", r"On \emph{fait opérer"),
    "Apply before the folio-34 marker move (previous entry), whose anchor is the '\\emph{fait opérer' this "
    "edit creates.")
add(34, "first line, 'sur N^p, donc sur N^(p) donc sur Λ(N^(p))'",
    "donc sur N^(p) donc sur (no comma after N^(p), both scans; the other items have theirs)",
    r"donc sur $N^{(p)}$, donc sur", "punctuation", "high",
    fx(r"donc sur $N^{(p)}$, donc sur", r"donc sur $N^{(p)}$ donc sur"),
    "The TeX adds the comma.")
add(34, "Démonstration, 'A priori, le quotient λ^p(N,1) = ... est une série formelle'",
    "λ^p(N,1) = λ^p(λ_{-1}(N))/λ_{-1}(N) in the running text, followed on the same line by 'est une série "
    "formelle' (both scans)",
    "\\[ \\lambda^p(N,1)=\\lambda^p(\\lambda_{-1}(N))/\\lambda_{-1}(N) \\] (a display)", "other", "medium",
    fx(NL.join(["le quotient", r"\[", r"\lambda^p(N,1)=\lambda^p(\lambda_{-1}(N))/\lambda_{-1}(N)", r"\]",
                "est une série"]),
       r"le quotient $\lambda^p(N,1)=\lambda^p(\lambda_{-1}(N))/\lambda_{-1}(N)$ est une série"),
    "The print sets the formula inline; the TeX makes it a display (same fix as on p. 21, applied).")
add(34, "Démonstration, 'considérons l'élément ℓ^p(N) = E_G(...) ∈ K(G) , où maintenant' (opening)",
    "ℓ^p(N) = E_G((Λ(N^(p))^alt) ∈ K(G) in the running text, followed on the same line by ', où maintenant' "
    "(both scans)",
    "\\[ \\ell^p(N)=...\\in \\underline{K}(G), \\] (a display)", "other", "medium",
    fx(NL.join(["l'élément", r"\[", r"\ell^p(N)="]), r"l'élément $\ell^p(N)="),
    "The print sets the formula inline. Goes with the next entry (closing): the two edits leave the formula, "
    "whose parentheses differ between the layers (misprint entry below), untouched.")
add(34, "Démonstration, 'considérons l'élément ℓ^p(N) = E_G(...) ∈ K(G) , où maintenant' (closing)",
    "... ∈ K(G) , où maintenant (inline, both scans)",
    "\\in \\underline{K}(G),\\n\\]\\noù maintenant", "other", "medium",
    fx(NL.join([r"\in \underline{K}(G),", r"\]", "où maintenant"]), r"\in \underline{K}(G)$, où maintenant"),
    "Goes with the previous entry; apply both or neither.")
add(34, "Démonstration, 'l'élément ℓ^p(N) = E_G((Λ(N^(p))^alt) ∈ K(G)'",
    "E_G((Λ(N^(p))^alt): three opening and two closing parentheses (both scans)",
    r"\underline{E}_G((\Lambda(N^{(p)})^{\mathrm{alt}}) (printed reading kept)", "misprint_in_print", "high",
    None,
    "The alternating part of Λ(N^(p)) is meant, as in (1.33). The TeX keeps the printed reading; the corrected "
    "layer already reads ((\\Lambda(N^{(p)}))^{\\mathrm{alt}}).",
    corrected=r"\underline{E}_G((\Lambda(N^{(p)}))^{\mathrm{alt}})")

# ---------------- page 35 ----------------
add(35, "start of page",
    "p. 34 ends '... que K(G) s'identifie'; p. 35 begins 'au sous-anneau de K engendré' (both scans)",
    "'au' is the last word of page_034.tex (under the folio-34 marker); page_035.tex begins 'sous-anneau'",
    "marker", "high", None,
    "Page 35 really begins with 'au'. Move the folio-35 marker before it: python -I move_marker.py 6 35 \"au\" "
    "--before (the last 'au' before the marker is that word; simulated on both layers: '... s'identifie ' / "
    "marker / 'au' / 'sous-anneau ...').")
add(35, "'on vérifie facilement dans cet anneau que l'on a ℓ^p(N) λ_{-1}(N) = λ^p(λ_{-1}(N)). Comme'",
    "a ℓ^p(N) λ_{-1}(N) = λ^p(λ_{-1}(N)). Comme on est ...: inline, in the running text (both scans)",
    "\\[ \\ell^p(N)\\lambda_{-1}(N)=\\lambda^p(\\lambda_{-1}(N)). \\] (a display)", "other", "medium",
    fx(NL.join(["que l'on a", r"\[", r"\ell^p(N)\lambda_{-1}(N)=\lambda^p(\lambda_{-1}(N)).", r"\]",
                "Comme on est"]),
       r"que l'on a $\ell^p(N)\lambda_{-1}(N)=\lambda^p(\lambda_{-1}(N))$. Comme on est"),
    "The print sets the formula inline; the TeX makes it a display.")

out = RUN / "findings_031_035.json"
out.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("wrote", out, len(F))
