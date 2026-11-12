"""Add the 'resolved' key to the 33 set-aside items (REPLAY_MANUAL_5.json and
MANUAL_5_findings_231_235.json), keeping the files' structure (indent 1, UTF-8, CRLF, no final newline).
usage: python -I resolve_items.py"""
import json
import pathlib

root = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
D = "12 Nov 2026"
H = f"placed by hand {D} (HANDFIX_5.jsonl, hand replay)"
A = f"already as the fix wants in the current layer (checked {D} ~16:30 UTC"

R = {
    0: f"{A}: current reads '\\dim.\\mathrm{{top}}_{{\\bar{{x}}}}(K)$ la borne', no comma)",
    1: f"{A}: current reads c_*c^!(P\\overset{{L}}{{\\otimes}} Q), no prime)",
    2: f"{H}: current had d_*d^!(P\\otimes Q) (prime already gone); the derived L restored as d_*d^!(P\\overset{{\\mathrm{{L}}}}{{\\otimes}} Q)",
    3: f"{H}: current already reads L (not 1) in the upper right corner; only the form changed, P\\otimes^LL to P\\overset{{\\mathrm{{L}}}}{{\\otimes}}L, as the finding's note asks",
    4: f"{H}: \\Hom(\\R f_{{2*}}A,\\R f_{{1*}}A) to \\Hom(Rf_{{2*}}A,Rf_{{1*}}A); the corrected index 2 (misprint Rf_*A) kept",
    5: f"{A}: current reads 'l'isomorphisme 6.8.3 est')",
    6: f"{H}: current had v without underline; now \\underline{{v}}:b_{{1*}}b_2^*M",
    7: f"{H}: current read $v\\in\\uHom_A($; underline removed ($v\\in\\Hom_A($), the current layer's subscript A kept",
    8: f"{A}: current reads (P) R^qj_*(Z/l)=0 pour q>1)",
    9: (f"open ({D}): the corrected layer recasts the sentence (inherited from ref_c4): 'où \\[...\\]. Il s'en déduit, comme en (III 1.6), "
        "qu'elle est un isomorphisme', with no parenthesis and without the print's 'dont on déduit de (loc. cit.)'; the printed comma "
        "after ')' has no place in that wording. Whether to restore the printed sentence (and 'de (loc. cit.)') is an editorial decision; "
        "no misprint record covers it"),
    10: f"{H}: underlines removed in the corrected wording 'u\\in\\Hom_A(c_1^*L,c_2^!L),\\qquad v\\in\\Hom_B(d_1^*M,d_2^!M),' (v for the printed c kept)",
    11: (f"{H}, adapted: the corrected layer (from ref_c4) writes 'la flèche horizontale supérieure' for the print's '(1)'; "
         "\\emph on 'où', 'est la diagonale', 'est le produit tensoriel des flèches'; the words standing for '(1)' left upright, as '(1)' is in the print"),
    12: f"{H}, adapted: 'la flèche verticale \\emph{{est déduite du produit tensoriel externe par restriction selon la diagonale}}' (the corrected layer's words for '(2)' upright)",
    13: f"{H}, adapted: '\\emph{{et}} la flèche horizontale inférieure \\emph{{est composée de}} 6.5.3 (\\emph{{définie car}}' (the corrected layer's words for '(3)' upright)",
    14: f"{H}: \\R_!^{{2r}}q to \\mathrm{{R}}_!^{{2r}}q; the corrected lower ! kept",
    15: f"{H}: statement underline as \\emph in Cor. 2.2.6; the current layer's A^* kept (it writes A^* where the print and the diplomatic layer have A^\\bullet on this page)",
    16: f"{H}: A^* to A^{{\\bullet}} twice in the display alpha; the corrected index p_i (misprint p_m) kept",
    17: f"{H}: current already reads 'de l'anneau' (letter and apostrophe corrected); now \\emph{{l'idéal de l'anneau de polynômes}}",
    18: f"{H}: '$j_i$-ème fonction' to '$j_i^{{\\text{{ème}}}}$ \\emph{{fonction symétrique élémentaire des éléments}}'; the corrected singular 'fonction' and index j_i kept",
    20: f"{H}: (8.5.4) g^*(g_*(\\cdot))c_{{d-1}}(\\check F) to g^*[g_*(\\cdot)]c_{{d-1}}(\\check F): the print's square brackets at the corrected place, as the finding's note asks",
    21: (f"{H}, adapted: Cor. 7.4 in the current layer carries the accepted correction SGA-SRC-000366 (X projective, L ample, Y a smooth hyperplane section); "
         "comma after n removed and \\emph on 'Soient', 'un', 'schéma projectif, lisse, connexe, de dimension', 'et'"),
    22: f"{H}, adapted to the corrected hypothesis: ' \\emph{{une section hyperplane lisse de}} $X$, \\emph{{définie par une section d'un}}'",
    23: f"{H}, adapted: '$\\mathcal O_X$-\\emph{{Module ample}} $L$. \\emph{{Notant}}' (the typescript's capital M; the corrected 'ample' kept)",
    24: f"{H}: the first display had \\mathbf L\\Phi_{{X^\\bullet}}; now \\underline{{\\underline{{L}}}}^{{-}}\\Phi_{{X^\\bullet}}, as in the three places below",
    25: f"{H}: '\\emph{{Démonstration de la proposition 8.1.}}' to plain 'Démonstration de la proposition 8.1.' (the corrected 8.1 kept)",
    26: f"{A}: current reads $Y'=p^{{-1}}(Y)=C'-U'$)",
    27: f"{H}: '(3.2), l'homomorphisme trace' to '(3.2) l'homomorphisme trace:'; the current layer's reference (3.2) (print 3.3.1, inherited from ref_c4) kept",
    31: f"{A}: current reads $\\nu_y(f)=1$ pour tout $y\\in Y$)",
    32: f"{H}: statement underline as \\emph in Thm 7.1; the corrected reference 6.1 kept",
    33: f"{A}: current reads \\alpha_{{x'}}(f'/G_{{x'}}, v, f', G_{{x'}}, \\varphi_{{x'}}))",
    34: f"{H}: '$W$),' to '$W$)' (the corrected W for the printed S kept)",
    35: f"{H}: plain R for \\R three times in the 'En effet' display; the current layer's corrected exponent form kept",
}
M = (f"{A}: p. 230 already reads '\\emph{{Preuve}} : L'équivalence' and p. 231 has no \\end{{prooftext}} after "
     "'l'assertion (ii).' (begin/end prooftext balance 6/6 in the file); both halves of the paired fix are in place)")


def ser(data):
    return json.dumps(data, ensure_ascii=False, indent=1).replace("\n", "\r\n").encode("utf-8")


def dump(path, data):
    path.write_bytes(ser(data))


for f in ("REPLAY_MANUAL_5.json", "MANUAL_5_findings_231_235.json"):
    assert ser(json.load(open(root / f, encoding="utf-8"))) == (root / f).read_bytes(), f"format differs: {f}"


p = root / "REPLAY_MANUAL_5.json"
items = json.load(open(p, encoding="utf-8"))
todo = [i for i, x in enumerate(items) if "resolved" not in x]
assert sorted(todo) == sorted(R), (todo, sorted(R))
for i in todo:
    items[i]["resolved"] = R[i]
dump(p, items)

q = root / "MANUAL_5_findings_231_235.json"
m = json.load(open(q, encoding="utf-8"))
assert len(m) == 1 and "resolved" not in m[0]
m[0]["resolved"] = M
dump(q, m)
print("resolved", len(todo), "+ 1")
