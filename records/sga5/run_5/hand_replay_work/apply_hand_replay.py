"""Hand replay of the last set-aside SGA 5 fixes on the corrected layer (sga5/current/s5.tex).
Each edit replaces an old string that must occur exactly once between the marker of its folio
and the next marker.  usage: python -I apply_hand_replay.py [--write]
Without --write it only checks the counts."""
import json
import pathlib
import re
import sys
import datetime

root = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
cur = root / "sga5" / "current" / "s5.tex"
MARK = re.compile(r"^%{10}  scan idx (\d+)  \|  folio (\S+)  %{10}$", re.M)
BY = "Claude Opus 5.5 (effort high), hand replay"

# (replay item, page, source, old, new, what)
EDITS = [
    ("R2", 105, "findings_101_105.json",
     r"d_*d^!(P\otimes Q)",
     r"d_*d^!(P\overset{\mathrm{L}}{\otimes} Q)",
     "first diagram, lower right: derived L restored over the tensor sign (the prime of d'^! was already absent)"),
    ("R3", 85, "findings_081_085.json",
     r"\uRHom(P\otimes^LL,Q",
     r"\uRHom(P\overset{\mathrm{L}}{\otimes}L,Q",
     "second square, upper right: P\\otimes^LL written in the diagram's form P\\overset{L}{\\otimes}L (the letter L was already right)"),
    ("R4", 110, "findings_106_110.json",
     r"\Hom(\R f_{2*}A,\R f_{1*}A)",
     r"\Hom(Rf_{2*}A,Rf_{1*}A)",
     "Cor. 4.9: plain typed R for \\R (double-struck), keeping the corrected index f_{2*}"),
    ("R6", 147, "findings_146_150.json",
     r"(\text{resp. }v:b_{1*}b_2^*M",
     r"(\text{resp. }\underline{v}:b_{1*}b_2^*M",
     "resp. part of the display: underline of v restored"),
    ("R7", 171, "findings_171_175.json",
     r"$v\in\uHom_A(",
     r"$v\in\Hom_A(",
     "5.8.5 lead-in: Hom not underlined (the corrected layer's subscript A kept)"),
    ("R10", 190, "findings_186_190.json",
     r"u\in\uHom_A(c_1^*L,c_2^!L),\qquad v\in\uHom_B(d_1^*M,d_2^!M),",
     r"u\in\Hom_A(c_1^*L,c_2^!L),\qquad v\in\Hom_B(d_1^*M,d_2^!M),",
     "before 6.8.2: global Hom_A, Hom_B not underlined (the corrected v kept)"),
    ("R11", 201, "findings_201_205.json",
     r"où $\delta:Y\to Y\times_SY$ est la diagonale, la flèche horizontale supérieure est le produit tensoriel des flèches",
     r"\emph{où} $\delta:Y\to Y\times_SY$ \emph{est la diagonale}, la flèche horizontale supérieure \emph{est le produit tensoriel des flèches}",
     "Lemme 6.23.3: statement underline as \\emph, adapted to the corrected wording ('la flèche horizontale supérieure' for the print's '(1)', upright as '(1)')"),
    ("R12", 201, "findings_201_205.json",
     r"la flèche verticale est déduite du produit tensoriel externe par restriction selon la diagonale",
     r"la flèche verticale \emph{est déduite du produit tensoriel externe par restriction selon la diagonale}",
     "Lemme 6.23.3: statement underline as \\emph, adapted to the corrected wording ('la flèche verticale' for '(2)')"),
    ("R13", 201, "findings_201_205.json",
     r"et la flèche horizontale inférieure est composée de 6.5.3 (définie car",
     r"\emph{et} la flèche horizontale inférieure \emph{est composée de} 6.5.3 (\emph{définie car}",
     "Lemme 6.23.3: statement underline as \\emph, adapted to the corrected wording ('la flèche horizontale inférieure' for '(3)')"),
    ("R14", 284, "findings_281_285.json",
     r"\R_!^{2r}q(q^*L)\longrightarrow",
     r"\mathrm{R}_!^{2r}q(q^*L)\longrightarrow",
     "Prop. 1.3 (ii) c): plain typed R for \\R, keeping the corrected lower !"),
    ("R15", 289, "findings_286_290.json",
     r"est un morphisme injectif d'anneaux unitaires, et les éléments $1,\xi,\ldots,\xi^r$ forment une base du $A^*(S)$-module $A^*(P)$. En particulier, $A^*(P)$ est un $A^*(S)$-module libre de même rang que $E$.",
     r"\emph{est un morphisme injectif d'anneaux unitaires, et les éléments} $1,\xi,\ldots,\xi^r$ \emph{forment une base du} $A^*(S)$-\emph{module} $A^*(P)$. \emph{En particulier}, $A^*(P)$ \emph{est un} $A^*(S)$-\emph{module libre de même rang que} $E$.",
     "Cor. 2.2.6: statement underline as \\emph (the corrected layer's A^* kept)"),
    ("R16", 308, "findings_306_310.json",
     r"\alpha:A^*(S)[T_{ij_i}]_{1\le i\le m,\,1\le j_i\le p_i}\to A^*(X)",
     r"\alpha:A^{\bullet}(S)[T_{ij_i}]_{1\le i\le m,\,1\le j_i\le p_i}\to A^{\bullet}(X)",
     "display alpha: raised dot A^{\\bullet} for A^* (twice), keeping the corrected index p_i"),
    ("R17", 309, "findings_306_310.json",
     r"l'idéal de l'anneau de polynômes",
     r"\emph{l'idéal de l'anneau de polynômes}",
     "Lemme 5.4.1 a): underline as \\emph (the corrected layer already reads 'de l'anneau')"),
    ("R18", 309, "findings_306_310.json",
     r"$j_i$-ème fonction symétrique élémentaire des éléments",
     r"$j_i^{\text{ème}}$ \emph{fonction symétrique élémentaire des éléments}",
     "Lemme 5.4.1 b): raised 'ème' and underline as \\emph (the corrected 'fonction' and index j_i kept)"),
    ("R20", 331, "findings_331_335.json",
     r"g^*(g_*(\cdot))c_{d-1}(\check F),",
     r"g^*[g_*(\cdot)]c_{d-1}(\check F),",
     "(8.5.4): square brackets of the print, at the corrected place of the closing bracket"),
    ("R21", 323, "findings_321_325.json",
     r"Soient $X$ un $k$-schéma projectif, lisse, connexe, de dimension $n$, et $Y$",
     r"\emph{Soient} $X$ \emph{un} $k$-\emph{schéma projectif, lisse, connexe, de dimension} $n$ \emph{et} $Y$",
     "Cor. 7.4: no comma after n; statement underline as \\emph (the corrected 'projectif' kept)"),
    ("R22", 323, "findings_321_325.json",
     r" une section hyperplane lisse de $X$, définie par une section d'un",
     r" \emph{une section hyperplane lisse de} $X$, \emph{définie par une section d'un}",
     "Cor. 7.4: statement underline as \\emph, adapted to the corrected hypothesis (smooth hyperplane section)"),
    ("R23", 323, "findings_321_325.json",
     r"$\mathcal O_X$-module ample $L$. Notant",
     r"$\mathcal O_X$-\emph{Module ample} $L$. \emph{Notant}",
     "Cor. 7.4: the typescript's capital M of Module; underline as \\emph (the corrected 'ample' kept)"),
    ("R24", 365, "findings_361_365.json",
     r"\mathbf L\Phi_{X^\bullet}:D^-({}_A\cC)",
     r"\underline{\underline{L}}^{-}\Phi_{X^\bullet}:D^-({}_A\cC)",
     "display of the left derived functor: doubly underlined L with superscript minus, as in the three places below"),
    ("R25", 367, "findings_366_370.json",
     r"\emph{Démonstration de la proposition 8.1.}",
     r"Démonstration de la proposition 8.1.",
     "proof label typed plain, not underlined (the corrected 8.1 kept)"),
    ("R27", 390, "findings_386_390.json",
     "(3.2), l'homomorphisme trace\n",
     "(3.2) l'homomorphisme trace:\n",
     "no comma after the reference, colon after 'trace' (the corrected layer's reference (3.2) kept)"),
    ("R32", 396, "findings_396_400.json",
     r"une sous-catégorie triangulée de $D^+(A)$ stable par facteurs directs, $F$ un complexe de faisceaux de $A$-modules tel que les conditions i), ii) de 6.1 soient remplies. Sous ces conditions on a",
     r"\emph{une sous-catégorie triangulée de} $D^+(A)$ \emph{stable par facteurs directs}, $F$ \emph{un complexe de faisceaux de} $A$-\emph{modules tel que les conditions} i), ii) \emph{de} 6.1 \emph{soient remplies}. \emph{Sous ces conditions on a}",
     "Thm 7.1: statement underline as \\emph (the corrected reference 6.1 kept)"),
    ("R34", 402, "findings_401_405.json",
     r"$W$),",
     r"$W$)",
     "Lemme 7.14: no comma after '(eta le point générique de W)' (the corrected W kept)"),
    ("R35", 466, "findings_466_470.json",
     "L_F=\\prod_i\\bigl(L_{\\R^i_!u(F)}\\bigr)^{(-1)^i}\n =\\prod_i\\prod_j\\bigl(L_{\\R^j_!v(\\R^i_!u(F))}",
     "L_F=\\prod_i\\bigl(L_{\\mathrm{R}^i_!u(F)}\\bigr)^{(-1)^i}\n =\\prod_i\\prod_j\\bigl(L_{\\mathrm{R}^j_!v(\\mathrm{R}^i_!u(F))}",
     "'En effet' display: plain typed R for \\R three times (the corrected exponents kept)"),
]


def region(text, page):
    ms = list(MARK.finditer(text))
    for i, m in enumerate(ms):
        if m.group(2) == str(page):
            end = ms[i + 1].start() if i + 1 < len(ms) else len(text)
            return m.end(), end
    raise KeyError(page)


def main():
    write = "--write" in sys.argv
    raw = cur.read_bytes()
    assert b"\r\n" not in raw
    text = raw.decode("utf-8")
    nmark = len(MARK.findall(text))
    ok = True
    for key, page, src, old, new, what in EDITS:
        a, b = region(text, page)
        n = text[a:b].count(old)
        print(key, page, "count", n)
        if n != 1:
            ok = False
            continue
        i = text.index(old, a, b)
        text = text[:i] + new + text[i + len(old):]
    assert len(MARK.findall(text)) == nmark
    if not ok:
        print("NOT WRITTEN: a count is not 1")
        return
    if write:
        with open(cur, "w", encoding="utf-8", newline="") as f:
            f.write(text)
        t = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        # HANDFIX_5.jsonl has CRLF line ends: keep them
        with open(root / "HANDFIX_5.jsonl", "a", encoding="utf-8", newline="\r\n") as f:
            for key, page, src, old, new, what in EDITS:
                rec = {"t": t, "vol": "5", "page": page,
                       "file": "C:/Users/user/Documents/sga_scan_check_20261105/sga5/current/s5.tex",
                       "what": what, "source": f"{src} (REPLAY_MANUAL_5.json, set aside: old occurs 0 times on the current page)",
                       "by": BY}
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        print("written", len(EDITS), "edits at", t)
    else:
        print("dry run ok")


main()
