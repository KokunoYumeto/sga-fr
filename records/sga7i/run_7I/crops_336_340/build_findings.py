"""Build findings_336_340_recheck.json and check every fix 'old' (exactly once) and 'tex' (present) per page."""
import json
import pathlib
import sys

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I")
B = RUN / "b336_340"
OUT = RUN / "findings_336_340_recheck.json"

F = [
    {
        "page": 336,
        "where": "Prouvons 2.2.9, sentence 'Les conditions envisagées impliquent évidemment ...'",
        "scan": "(iii), (iv) (iv°), qui impliquent chacune (iii°) — no comma between (iv) and (iv°)",
        "tex": "(iii), (iv) (iv$^o$),",
        "kind": "misprint_in_print",
        "confidence": "low",
        "fix": None,
        "corrected": "(iii), (iv), (iv$^o$),",
        "note": "Comma missing in the list of conditions. The TeX keeps the printed reading; the corrected layer also "
                "still lacks the comma. 'corrected' replaces the 'tex' substring.",
    },
    {
        "page": 337,
        "where": "first line, 'appelée la partie torique de T_ℓ(A°),'",
        "scan": "appelée",
        "tex": "appelée la \\underline{partie torique de}",
        "kind": "misprint_in_print",
        "confidence": "low",
        "fix": None,
        "corrected": "appelé la \\underline{partie torique de}",
        "note": "Agreement slip: the participle refers to 'un sous-faisceau ℓ-adique constant tordu canonique' at the "
                "foot of p. 336 (cf. 'caractérisé' after (2.3.2)). The TeX keeps the printed reading; the corrected "
                "layer already reads 'appelé'. 'corrected' replaces the 'tex' substring.",
    },
    {
        "page": 337,
        "where": "last paragraph, 'des modules de Tate de A(K̄) , (A'(K̄) comme les modules d'invariants'",
        "scan": "A(K̄) , (A'(K̄) — a parenthesis opened before A' and never closed",
        "tex": "$(A'(\\overline{K})$ comme",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "$A'(\\overline{K})$ comme",
        "note": "Stray '(' in the print. The TeX keeps the printed reading; the corrected layer already drops it. "
                "'corrected' replaces the 'tex' substring.",
    },
    {
        "page": 337,
        "where": "last paragraph, 'les modules d'invariants sous le groupe d'inertie I (1.6.5)'",
        "scan": "(1.6.5)",
        "tex": "d'inertie $I$ (1.6.5)",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "d'inertie $I$ (2.2.5)",
        "note": "Wrong reference number in the print: Exposé IX has no 1.6.5 (§1 ends with Proposition 1.5 and its "
                "proof). The fact cited, that the parties fixes are the modules of invariants under the inertia group "
                "I, is Proposition 2.2.5 (folio 332), which the proof of 2.2.9 on p. 336 cites for the same fact "
                "('compte tenu de 2.2.5'). The TeX keeps the printed reading; the corrected layer already reads "
                "(2.2.5). 'corrected' replaces the 'tex' substring.",
    },
    {
        "page": 338,
        "where": "first line, 'grace au théorème suivant'",
        "scan": "graĉe (the circumflex stands over the c; crop crops_336_340/p338_grace.png)",
        "tex": "gra\\^ce",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "grâce",
        "note": "Accent typed on the wrong letter. The TeX keeps the printed reading; the corrected layer already "
                "reads 'grâce'. 'corrected' replaces the 'tex' substring.",
    },
    {
        "page": 338,
        "where": "heading of Théorème 2.4",
        "scan": "Thoérème (underlined)",
        "tex": "\\underline{Thoérème}",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "\\underline{Théorème}",
        "note": "Typing error. The TeX keeps the printed reading; the corrected layer already reads Théorème. "
                "'corrected' replaces the 'tex' substring.",
    },
    {
        "page": 338,
        "where": "Démonstration a), 'prolongement canonique de la biextension W_K de (A_K;A'_K) par G_mK'",
        "scan": "(A_K;A'_K) — a semicolon between the two factors (crop crops_336_340/p338_AK.png)",
        "tex": "$(A_K ; A'_K)$",
        "kind": "misprint_in_print",
        "confidence": "low",
        "fix": None,
        "corrected": "$(A_K , A'_K)$",
        "note": "The pair is written with a comma elsewhere, e.g. '(A°,A'°)' in the same sentence and '(A_K,A'_K)' "
                "in 1.0. The TeX keeps the printed reading; the corrected layer already reads '$(A_K , A'_K)$'. "
                "'corrected' replaces the 'tex' substring.",
    },
    {
        "page": 338,
        "where": "(2.4.1)",
        "scan": "φ_w — a lowercase w (as tall as the m of G_mS, not the S; crop crops_336_340/p338_phiW.png)",
        "tex": "\\varphi_w :",
        "kind": "other",
        "confidence": "medium",
        "fix": None,
        "note": "No difference and no misprint: the TeX matches the print, and the print is right. The class of the "
                "biextension W is written w in (1.4.3) and (1.4.4) ('w = w° ∈ Biext^1(A°,A'°;G_mS)'), and φ_w is "
                "the pairing VIII 2.2 attaches to it. The earlier misprint entry for this spot "
                "(findings_336_340.json, in MISPRINTS_7I with correct '\\varphi_W') should be withdrawn, and the "
                "corrected layer, which reads \\varphi_W, should read \\varphi_w as printed.",
    },
    {
        "page": 339,
        "where": "(2.4.5)",
        "scan": "T_ℓ(T_o) × T_ℓ(A_o°) — no prime on the A of the second factor (crops crops_336_340/p339_245.png "
                "and p339_243.png)",
        "tex": "T_{\\ell}(T_{o}) \\times T_{\\ell}(A_{o}^{\\,o})",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "T_{\\ell}(T_{o}) \\times T_{\\ell}({A'}^{o}_{o})",
        "note": "(2.4.5) is the special fibre of (2.4.4), whose second factor T_ℓ(A'°)^f has special fibre "
                "T_ℓ(A'_o°), and it is induced by (2.4.3), whose second factor is T_ℓ(A'_o°); cf. also (2.4.7). The "
                "TeX keeps the printed reading; the corrected layer already has the prime. 'corrected' replaces the "
                "'tex' substring.",
    },
    {
        "page": 340,
        "where": "'Comme il s'agit encore de relations antre faisceaux ℓ-adiques constants tordus'",
        "scan": "entre — the first letter is an overstrike, a and e typed on the same spot (the typist's correction)",
        "tex": "antre",
        "kind": "word",
        "confidence": "medium",
        "fix": {"old": "relations antre", "new": "relations entre"},
        "note": "At full resolution the first letter is not a plain a: the closed round top and cross-stroke of an e "
                "lie over the bowl and foot of an a (crop crops_336_340/p340_compare.png, beside a plain a and e of "
                "the same line). The a/e overstrike in 'partie' on p. 337 and the e/s overstrike in 'résulte' on "
                "p. 336 are given in the TeX as the corrected words. This supersedes the earlier misprint entry "
                "'antre' -> 'entre' (findings_336_340.json). The corrected layer already reads 'entre', so the replay "
                "there finds nothing to change.",
    },
    {
        "page": 340,
        "where": "'l'annulateur du deuxième facteur, ... est égale à cette dernière'",
        "scan": "égale (underlined)",
        "tex": "est \\underline{égale} à",
        "kind": "misprint_in_print",
        "confidence": "low",
        "fix": None,
        "corrected": "est \\underline{égal} à",
        "note": "Agreement slip: the subject is 'l'annulateur' (masculine). The TeX keeps the printed reading; the "
                "corrected layer already reads \\underline{égal}. 'corrected' replaces the 'tex' substring.",
    },
    {
        "page": 340,
        "where": "'i.e. que l'inclusion déjà obtenue (1.10)', before (2.4.7)",
        "scan": "(1.10)",
        "tex": "déjà obtenue (1.10)",
        "kind": "misprint_in_print",
        "confidence": "low",
        "fix": None,
        "corrected": "déjà obtenue (VIII 4.10)",
        "note": "Wrong reference number in the print: Exposé IX has no 1.10 (§1 ends with Proposition 1.5). The "
                "inclusion T_ℓ(T_o) ⊂ T_ℓ(A'_o°)^⊥ was obtained in a) (p. 339) from VIII 4.10, and VIII 4.11 says "
                "that by 4.10 the left annihilator contains T_ℓ(T). The print slips 1 for 4 likewise in VIII 4.11 "
                "('(1.11.1)' for (4.11.1), p. 274). Low: the intended form of the reference is inferred. The TeX "
                "keeps the printed reading. The corrected layer reads '(2.4.7)' here (the number of the display "
                "that follows), which is neither the printed reading nor a recorded correction. 'corrected' "
                "replaces the 'tex' substring.",
    },
]

ok = True
for x in F:
    t = (B / f"page_{x['page']:03d}.tex").read_text(encoding="utf-8")
    body = t.split("\n", 2)[2]  # skip the source line and the marker line
    n_tex = body.count(x["tex"])
    if n_tex < 1:
        ok = False
        print("TEX NOT FOUND", x["page"], repr(x["tex"]))
    if x["fix"]:
        n = t.count(x["fix"]["old"])
        if n != 1:
            ok = False
            print("OLD COUNT", n, x["page"], repr(x["fix"]["old"]))
        if "%%%%%%%%%%" in x["fix"]["old"] or "%%%%%%%%%%" in x["fix"]["new"]:
            ok = False
            print("MARKER IN FIX", x["page"])
    print(x["page"], x["kind"], "tex x%d" % n_tex, "fix" if x["fix"] else "-")

if not ok:
    sys.exit("check failed")
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
print("wrote", OUT, len(F))
