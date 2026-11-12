import json
import sys

OUT = sys.argv[1]

findings = [
    {
        "page": 142,
        "where": "first line: '(l'identité des deux derniers membres dans cette formule ayant déjà été noté avec la construction de 1_E)'",
        "scan": "noté",
        "tex": "ayant déjà été noté avec",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "ayant déjà été notée avec",
        "note": "Agreement slip: the participle refers to 'l'identité' (feminine). The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    },
    {
        "page": 142,
        "where": "(1.1.5.10), the isomorphism deduced from phi_{p,p^{-1}} used for the inverse of x in E(S) over p",
        "scan": "P_{p^{-1}} ≃ (P_p)^o: capital P (closed bowl, no arms) in both places, not E",
        "tex": "P_{p^{-1}} \\;\\simeq\\; (P_p)^{o}",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "E_{p^{-1}} \\;\\simeq\\; (E_p)^{o}",
        "note": "The inverse of x over p lies in the fibre bitorseur E_{p^{-1}}; phi_{p,p^{-1}} : E_p E_{p^{-1}} ≃ E_1 with (1.1.5.4) gives E_{p^{-1}} ≃ (E_p)^o. The typescript writes P_p for the fibre E_p (also on p. 144 and pp. 136-138, e.g. 'phi : P_p x P_{p'} -> P_{pp'}' right after E_p is defined). The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    },
    {
        "page": 143,
        "where": "second paragraph: 'avec le foncteur image inverse f* par un morphisme de topos'",
        "scan": "f followed by the typewriter asterisk raised to superscript height, the same glyph and position as in 'f*(phi)' four lines below",
        "tex": "$f*$",
        "kind": "symbol",
        "confidence": "medium",
        "fix": {"old": "$f*$", "new": "$f^*$"},
        "note": "$f*$ sets a centred binary asterisk on the line; the same printed symbol is $f^*(\\varphi)$ at the end of the paragraph.",
    },
    {
        "page": 144,
        "where": "1.2, line 5: 'que les opérations gauches et droites de G sur P_p coîncident'",
        "scan": "P_p (capital P with a subscript small p)",
        "tex": "de $G$ sur $P_p$",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "de $G$ sur $E_p$",
        "note": "G operates on the fibre bitorseurs E_p named in the same sentence ('les bitorseurs E_p (p ∈ P(S)) soient des torseurs ordinaires'); same P_p-for-E_p slip as (1.1.5.10) on p. 142. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    },
    {
        "page": 144,
        "where": "1.2, same sentence: 'coîn-cident'",
        "scan": "coîncident: circumflex over the i (checked at high zoom), not a diaeresis",
        "tex": "coîncident",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "coïncident",
        "note": "Spelling slip, circumflex for diaeresis (the same circumflex is printed on p. 145). The TeX keeps the printed reading.",
    },
    {
        "page": 144,
        "where": "diagram (1.2.1), to the right of the bottom-right node E_{p'p}",
        "scan": "a comma on the base line well to the right of E_{p'p}",
        "tex": "\\end{tikzcd}",
        "kind": "punctuation",
        "confidence": "high",
        "fix": {"old": "\\end{tikzcd}", "new": "\\end{tikzcd}\\quad ,"},
        "note": "The sentence continues after the diagram ('... diagrammes suivants (où p,p' ∈ P(S)) : [diagram] , où la première flèche verticale ...'). The STRUCTURE comment records the comma; the tikzcd leaves it out. Placed after the tikzcd as in the earlier diagram fixes of this volume (pp. 21, 99, 100).",
    },
    {
        "page": 144,
        "where": "1.3.1.0, first line: 'Soient P un objet de T muni d'une section e_P, G un Groupe de T'",
        "scan": "the first T has no underline; the T of 'G un Groupe de T' in the same line is underlined",
        "tex": "objet de $T$ muni",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "objet de \\underline{$T$} muni",
        "note": "The topos letter lost its underline (underlined everywhere else on pp. 141-145). An omitted underline, not a wrong character. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    },
    {
        "page": 145,
        "where": "1.3.2, 'si les sections alpha et beta coîncident sur e_P x e_Q'",
        "scan": "coîncident: circumflex over the i, as on p. 144 (checked at high zoom)",
        "tex": "coïncident",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": {"old": "coïncident", "new": "coîncident"},
        "corrected": "coïncident",
        "note": "The TeX silently corrects the printed circumflex to the diaeresis; the fix restores the print (p. 144 already keeps 'coîncident'). 'corrected' is the current TeX.",
    },
]

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(findings, fh, ensure_ascii=False, indent=1)
    fh.write("\n")
print("wrote", len(findings), "findings to", OUT)
