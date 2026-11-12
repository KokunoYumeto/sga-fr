import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II")
FOLDER = RUN / "b256_260"
OUT = RUN / "findings_256_260.json"

F = []


def add(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "confidence": confidence, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- page 256 ----------------
add(256,
    "Théorème 1.1, third line: 'et 𝔉 un ℤ_ℓ-faisceau (resp. ℚ_ℓ-faisceau) sur X'",
    "ℤ_ℓ-faisceau (resp. ℚ_ℓ-faisceau): the underline covers only the word faisceau, both times; "
    "the hyphens and the closing parenthesis are not underlined (checked at 3x)",
    r"$\mathbb{Z}_\ell$\underline{-faisceau} (resp. $\mathbb{Q}_\ell$\underline{-faisceau)}",
    "underline", "high",
    {"old": r"$\mathbb{Z}_\ell$\underline{-faisceau} (resp. $\mathbb{Q}_\ell$\underline{-faisceau)}",
     "new": r"$\mathbb{Z}_\ell$-\underline{faisceau} (resp. $\mathbb{Q}_\ell$-\underline{faisceau})"},
    "The TeX starts the underline with the hyphen after the math letter and takes the closing parenthesis "
    "into it; the typescript underlines only the word (as SGA 7 I, global item 17).")

add(256,
    "Théorème 1.1, line after (1.1.1): 'soit un isomorphisme de ℤ_ℓ-faisceaux(resp. de ℚ_ℓ-faisceaux) sur S'",
    "only the word faisceaux is underlined, both times; the hyphens and the closing parenthesis are not "
    "(checked at 3x)",
    r"$\mathbb{Z}_\ell$\underline{-faisceaux}(resp. \underline{de} $\mathbb{Q}_\ell$\underline{-faisceaux)}",
    "underline", "high",
    {"old": r"$\mathbb{Z}_\ell$\underline{-faisceaux}(resp. \underline{de} $\mathbb{Q}_\ell$\underline{-faisceaux)}",
     "new": r"$\mathbb{Z}_\ell$-\underline{faisceaux}(resp. \underline{de} $\mathbb{Q}_\ell$-\underline{faisceaux})"},
    "Same convention as the previous finding. The x of the first faisceaux is overtyped in the print; the "
    "reading faisceaux stands.")

add(256,
    "Théorème 1.1, lines 2-3: 'u ∈ H^2(X,ℤ_ℓ(1)) (resp. u ∈ H^2(X,ℚ_ℓ(1)) une classe de cohomologie sur X'",
    "(resp. u ∈ H^2(X,ℚ_ℓ(1)) followed directly by 'une classe': only two closing parentheses (checked at 2x)",
    r"(resp. $u \in H^2(X,\mathbb{Q}_\ell(1))$",
    "misprint_in_print", "high", None,
    "The parenthesis opened by 'resp.' is never closed (compare '(resp. ℚ_ℓ-faisceau)' on the next line). "
    "The TeX keeps the printed reading; the corrected layer too.",
    corrected=r"(resp. $u \in H^2(X,\mathbb{Q}_\ell(1))$)")

# ---------------- page 257 ----------------
add(257,
    "(1.2.2), range under the ⊕",
    "0≤j≤n (checked at 2x)",
    r"\underset{0 \leq j \leq n}{\oplus}",
    "misprint_in_print", "high", None,
    "n is not a variable of Théorème 1.2 (ℰ has rank 1 + r, the fibres are ℙ^r); p. 258 writes the same sum "
    "over 0 ≤ j ≤ r. The TeX keeps the printed reading; the corrected layer already reads r "
    "(SGA7II-FR-XVIII-003).",
    corrected=r"\underset{0 \leq j \leq r}{\oplus}")

add(257,
    "(1.2.2), degree of the source group",
    "H^{q-2-j} (checked at 2x)",
    r"H^{q-2-j}",
    "misprint_in_print", "high", None,
    "The map is defined on τ_{q-2j} ↦ Σ f^*(τ_{q-2j}) ∧ u^j (next line), and p. 258 writes ⊕ H^{q-2j}(X,ℤ_ℓ(-j)). "
    "The TeX keeps the printed reading; the corrected layer already reads q-2j (SGA7II-FR-XVIII-004).",
    corrected=r"H^{q-2j}")

add(257,
    "(1.2.2), source group H^{q-2-j}(X,ℤ_ℓ(-j)",
    "(X,ℤ_ℓ(-j) ⟶ : one closing parenthesis only (checked at 2x)",
    r"\mathbb{Z}_\ell(-j) \ \longrightarrow",
    "misprint_in_print", "high", None,
    "Missing closing parenthesis of H^{q-2-j}(X, ...). The TeX keeps the printed reading; the corrected layer "
    "already has it (SGA7II-FR-XVIII-004).",
    corrected=r"\mathbb{Z}_\ell(-j)) \ \longrightarrow")

add(257,
    "b), line after (1.2.2): 'défini par ⊕ τ_{q-2j} ⟶ Σ f*(τ_{q-2j}) ∧ u^j'",
    "défini par (underlined; checked at 1.6x)",
    r"\underline{défini par}",
    "misprint_in_print", "medium", None,
    "Agreement slip: the participle refers to 'la flèche' (b) la flèche (1.2.2) définie par ... est un "
    "isomorphisme). The TeX keeps the printed reading; the corrected layer too.",
    corrected=r"\underline{définie par}")

# ---------------- page 258 ----------------
add(258,
    "filtration F^i on ⊕ H^{q-2j}(X,ℤ_ℓ(-j)), second line of the range under the ⊕",
    "q-2j≤i",
    r"q-2j \leq i",
    "misprint_in_print", "medium", None,
    "Inequality reversed. The summand H^{q-2j}(X,ℤ_ℓ(-j)) goes to f^*(τ) ∧ u^j, which lies in F^{q-2j} of the "
    "decreasing Leray filtration (f^*(τ) in F^{q-2j}, u^j in F^0). The arrow 1.2.2 is compatible with the "
    "filtrations and induces the identity on the graded pieces only for F^i = ⊕ over q-2j ≥ i; with ≤, F^q "
    "would be the whole sum while F^q H^q is the image of H^q(X). The TeX keeps the printed reading; the "
    "corrected layer too.",
    corrected=r"q-2j \geq i")

# ---------------- page 259 ----------------
add(259,
    "2.1.5, display: 'x ∈ X - Δ ⟶ (g_o(x),...,g_r(x) ∈ ℙ^r ,'",
    "(g_o(x),...,g_r(x) ∈ ℙ^r: the tuple is not closed (checked at 1.4x)",
    r"g_r(x) \in \mathbb{P}^r",
    "misprint_in_print", "high", None,
    "Missing closing parenthesis of the coordinate tuple (2.1.6 prints (G_o(x),...,G_r(x)) closed). The TeX "
    "keeps the printed reading; the corrected layer already has it (SGA7II-FR-XVIII-005).",
    corrected=r"g_r(x)) \in \mathbb{P}^r")

add(259,
    "(2.1.4), top right node ℙ̌ (N_{Δ|X})",
    "N with subscript Δ|X, a vertical bar (checked at 1.3x)",
    r"\check{\mathbb{P}}\,(\underline{N}_{\Delta|X}) \arrow[ld",
    "misprint_in_print", "low", None,
    "The same normal bundle is N_{Δ/X} in the line above the diagram, on p. 258 and twice on p. 260; the bar "
    "is probably a slip for the slash (it can also be read as a variant notation, in which case it stands). "
    "The TeX keeps the printed reading and its STRUCTURE comment records the bar; the corrected layer too. "
    "If corrected, the STRUCTURE comment there mentions the bar twice.",
    corrected=r"\check{\mathbb{P}}\,(\underline{N}_{\Delta/X}) \arrow[ld")

# ---------------- page 260 ----------------
add(260,
    "(2.1.6.2), end of the display",
    "a full stop far right, level with the bottom node Δ",
    "{} & \\Delta &\n{} \\end{tikzcd} (no full stop; the STRUCTURE comment says it cannot be carried inside "
    "the tikzcd)",
    "punctuation", "high",
    {"old": "{} & \\Delta &\n{} \\end{tikzcd}",
     "new": "{} & \\Delta & .\n\\end{tikzcd}"},
    "Set in the bottom-right cell, as the TeX does for the full stop of (2.1.4) on p. 259. Apply together with "
    "the next finding (STRUCTURE comment).")

add(260,
    "STRUCTURE comment under (2.1.6.2), last sentence",
    "full stop printed after the display",
    "it cannot be carried inside the tikzcd block and is recorded here.",
    "other", "high",
    {"old": "; it cannot be\n%   carried inside the tikzcd block and is recorded here.",
     "new": "; it is set in\n%   the bottom-right cell of the tikzcd block."},
    "Goes with the previous fix; without it the comment says the full stop is left out.")

add(260,
    "(2.1.6.3), end of the display",
    "a comma far right, level with the bottom row Δ ↪ X",
    "{} & \\Delta \\arrow[r, hook] & X &\n{} \\end{tikzcd} (no comma; the STRUCTURE comment says it cannot be "
    "carried inside the tikzcd)",
    "punctuation", "high",
    {"old": "& X &\n{} \\end{tikzcd}",
     "new": "& X & ,\n\\end{tikzcd}"},
    "The sentence runs on into 'et l'inclusion composée ...'. Apply together with the next finding "
    "(STRUCTURE comment).")

add(260,
    "STRUCTURE comment under (2.1.6.3), last sentence",
    "comma printed after the display",
    "and cannot be carried inside the tikzcd block, so it is recorded here.",
    "other", "high",
    {"old": "and cannot be carried inside the tikzcd\n%   block, so it is recorded here.",
     "new": "and is set in the bottom-right\n%   cell of the tikzcd block."},
    "Goes with the previous fix; without it the comment says the comma is left out.")

add(260,
    "(2.1.6.2), label of the arrow Δ × ℙ^r ⟶ Δ",
    "pr_i, subscript a dotted i (checked at 3x); (2.1.6.3) prints pr_1 with the digit",
    r'\arrow[dl, "\mathrm{pr}_i"]',
    "misprint_in_print", "high", None,
    "The arrow is the first projection of Δ × ℙ^r onto Δ; (2.1.6.3) labels the same map pr_1. The TeX keeps "
    "the printed reading (its STRUCTURE comment records the dotted i); the corrected layer already reads pr_1 "
    "(SGA7II-FR-XVIII-006).",
    corrected=r'\arrow[dl, "\mathrm{pr}_1"]')

add(260,
    "(2.2.1), E_2 term 'H^p(X,R^q f_* ℤ_ℓ'",
    "H^p(X,R^qf_*ℤ_ℓ ⟹ : no closing parenthesis (checked at 1.6x)",
    r"H^p(X, R^q f_* \mathbb{Z}_\ell \quad",
    "misprint_in_print", "high", None,
    "Missing closing parenthesis. The TeX keeps the printed reading. The corrected layer already has it, but "
    "records it as a transcription repair (see the next finding).",
    corrected=r"H^p(X, R^q f_* \mathbb{Z}_\ell) \quad")

add(260,
    "(2.2.1), abutment 'H^{p+q}(X̃_o ℤ_ℓ)'",
    "(X̃_o ℤ_ℓ): a small subscript o after X̃ and no comma (checked at 4x)",
    r"H^{p+q}(\widetilde{X}_o \;\; \mathbb{Z}_\ell)",
    "misprint_in_print", "medium", None,
    "The abutment is H^{p+q}(X̃, ℤ_ℓ) (compare (1.2.1)); the o stands where the comma belongs. The TeX keeps the "
    "printed reading. The corrected layer reads H^{p+q}(\\widetilde{X},\\mathbb{Z}_\\ell), but its comment "
    "('Réparation de transcription : parenthèses et virgule rétablies; X-tilde sans indice o.', "
    "current/expose_XVIII_body.tex) and corrections.md SGA7II-FR-XVIII-007 (classed transcription_repair) "
    "treat the missing parenthesis, the o and the missing comma as transcription errors; the scan has all "
    "three, so the entry corrects misprints of the print and its record should say so.",
    corrected=r"H^{p+q}(\widetilde{X}, \mathbb{Z}_\ell)")

# ---------------- checks ----------------
ok = True
for f in F:
    text = (FOLDER / f"page_{f['page']}.tex").read_text(encoding="utf-8")
    if f["fix"]:
        n = text.count(f["fix"]["old"])
        if n != 1:
            ok = False
            print("FIX OLD NOT UNIQUE", f["page"], n, repr(f["fix"]["old"]))
        if "%%%%%%%%%%  scan idx" in f["fix"]["old"]:
            ok = False
            print("FIX TOUCHES MARKER", f["page"])
    if f["kind"] == "misprint_in_print":
        n = text.count(f["tex"])
        if n != 1:
            print("note: misprint tex count", f["page"], n, repr(f["tex"]))
print("all fixes unique:", ok, "| findings:", len(F))
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("written", OUT)
