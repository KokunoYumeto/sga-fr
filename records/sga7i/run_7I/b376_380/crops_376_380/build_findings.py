import json, sys
B = chr(92)
def t(s):
    return s.replace("§", B)

F = []
def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": t(tex), "kind": kind,
         "confidence": conf,
         "fix": None if fix is None else {"old": t(fix[0]), "new": t(fix[1])}}
    if corrected is not None:
        d["corrected"] = t(corrected)
    d["note"] = note
    F.append(d)

add(377, "Théorème 5.4, first line: 'et A_K un schéma abélien sur S ayant une réduction semi-stable sur S'",
    "A_K un schéma abélien sur S ayant une réduction semi-stable sur S ('un schéma abélien sur' underlined, S plain)",
    "§underline{un schéma abélien sur} $S$",
    "misprint_in_print", "high", None,
    "A_K is an abelian scheme over the fraction field K (it has semi-stable reduction over S); the exposé writes 'A_K un schéma abélien sur K' in its other statements. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    corrected="§underline{un schéma abélien sur} $K$")

add(379, "line after (5.5.4): 'et on aura alors'",
    "et on aura alors: the second letter is typed over a u (the glyph shows both the arch and feet of n and the bowl of u) and the o is struck twice, i.e. the typist retyped 'ou' as 'on'",
    "et ou aura alors",
    "word", "medium", ("et ou aura alors", "et on aura alors"),
    "The TeX gives the reading before the typist's correction. If the overstrike is read as 'ou' instead, this becomes a misprint of the print that the TeX keeps (fix null, corrected 'et on aura alors').")

add(379, "(5.5.8), second line",
    "T_ℓ(A')/T_ℓ(A'_K)^f ≃ M'_K ⊗_Z Z_ℓ . (no index K on the first A')",
    "T_§ell(A')/T_§ell(A'_K)^f",
    "misprint_in_print", "high", None,
    "The index K is missing on the first A' (compare the first line of (5.5.8) and both lines of (5.5.9)). The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    corrected="T_§ell(A'_K)/T_§ell(A'_K)^f")

add(380, "first line: 'où on se rappelera que les groupes'",
    "où on se rappelera que les groupes",
    "se rappelera",
    "misprint_in_print", "medium", None,
    "Spelling error of the typescript (appeler doubles the l before a mute e), as on p. 283. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    corrected="se rappellera")

add(380, "Proposition 5.6: '(qui peut être égal à la caractéristique résiduelle de S)'",
    "(qui peut être égal à la carac-téristique résiduelle de S): the underline starts under 'qui'; the opening parenthesis is not underlined",
    "§underline{(qui peut être égal à la caractéristique résiduelle de} $S$)",
    "underline", "medium", ("§underline{(qui peut", "(§underline{qui peut"),
    "The TeX puts the opening parenthesis inside the underline; compare (§underline{fibre spéciale de la biextension} on p. 377, where it stays outside.".replace("§", B))

add(380, "Proposition 5.6: 'le pro-ℓ-groupe de Barsotti-Tate T_ℓ(A_K)^t'",
    "le pro-ℓ-groupe de Barsotti-Tate: 'le pro' and 'groupe de Barsotti-Tate' underlined; the handwritten ℓ and the hyphens on either side of it are not underlined",
    "§underline{le pro-$§ell$-groupe de Barsotti-Tate}",
    "underline", "medium",
    ("§underline{le pro-$§ell$-groupe de Barsotti-Tate}", "§underline{le pro}-$§ell$-§underline{groupe de Barsotti-Tate}"),
    "The TeX runs the underline under the handwritten ℓ, which the print, as with every other math symbol of the statement, leaves without underline.")

add(380, "5.6.1: 'cela signifie respectivement que S' déploye les groupes'",
    "respectivement que S' déploye les groupes",
    "déploye les",
    "misprint_in_print", "medium", None,
    "Spelling error of the typescript (verbs in -oyer take i before a mute e; the volume has 'qui déploie F_K' elsewhere). The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    corrected="déploie les")

add(380, "5.6.1: 'que S' déploye les groupes constants tordus M et M''",
    "les groupes constants tordus M et M' (M, M' underlined)",
    "tordus $§underline{M}$ et $§underline{M}'$",
    "misprint_in_print", "low", None,
    "The pairing contradicts 'respectivement': by (5.5.7) T_ℓ(A_K)^t is given by M' (T_ℓ(A^o)^t ≃ M̌' ⊗ Z_ℓ(1)), and by (5.5.8) T_ℓ(A_K)/T_ℓ(A_K)^f by M. Probably an authorial slip, harmless since M and M' are isogenous; the emendation is conjectural. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    corrected="tordus $§underline{M}'$ et $§underline{M}$")

add(380, "end of 5.6.1: 'qui fait l'affaire.'",
    "qui fait l'affaire. Between 'fait' and 'l'affaire' there is only a speck (about 4x4 px, above the baseline); the typewriter's full stop on the same line is about 11x12 px and sits on the baseline",
    "fait.l'affaire",
    "punctuation", "medium", ("fait.l'affaire", "fait l'affaire"),
    "The TeX turns a speck into a full stop. If the mark is judged a lightly typed stray stop, this becomes a misprint of the print that the TeX keeps (fix null, corrected 'fait l'affaire').")

out = sys.argv[1]
with open(out, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
    fh.write("\n")
print("wrote", len(F), "findings")
