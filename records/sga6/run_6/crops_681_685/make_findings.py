"""Write findings_681_685.json and check that every fix's old string occurs exactly once on its page."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
B = RUN / "b681_685"
OUT = RUN / "findings_681_685.json"
C = "crops_681_685/"


def F(page, where, scan, tex, kind, conf, fix, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
         "fix": None if fix is None else {"old": fix[0], "new": fix[1]}}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    return d


SECOND = "second reading (sga6_fr_r1/src/fr.tex)"
f = []

# ---------------- p. 681 ----------------
f.append(F(681, "5.1, the display 'g˙: Gr˙(X) -> H^{2*}(X,Z_l(*))'",
           "g with the raised typed dot, the same dot as in Gr˙ (both scans; " + C + "c681_gdisp.png)",
           r"g':\operatorname{Gr}^\bullet(X)", "symbol", "high",
           (r"g':\operatorname{Gr}", r"g^\bullet:\operatorname{Gr}"),
           "The prime stands for the print's raised dot (as K' did in Exposés IV and VI, now K^{\\bullet}); the "
           + SECOND + " has g' too. Two more on this page (next entries); apply the three together."))
f.append(F(681, "end of 5.1, 'on voit en tous cas que g˙ est uniquement déterminé'",
           "g˙, raised dot (both scans; " + C + "c681_gdot1.png)",
           r"que $g'$ est", "symbol", "high",
           (r"que $g'$ est", r"que $g^\bullet$ est"), "As the display of 5.1."))
f.append(F(681, "5.2, 'la question de l'existence de g˙ se résoud affirmativement'",
           "g˙, raised dot (both scans; " + C + "c681_gdot2.png)",
           r"de $g'$ se résoud", "symbol", "high",
           (r"de $g'$ se", r"de $g^\bullet$ se"), "As the display of 5.1."))
f.append(F(681, "5.2, 'par division à partir des psi^i, un homomorphisme d'anneaux :' before the display of g_Q",
           "'d'anneaux :' with a colon (both scans; " + C + "c681_anneaux.png, w_692_small.png)",
           r"un homomorphisme d'anneaux (no colon), then the display", "punctuation", "high",
           (r"des $\psi^i$, un homomorphisme d'anneaux", r"des $\psi^i$, un homomorphisme d'anneaux :"),
           "The " + SECOND + " also lacks the colon."))
f.append(F(681, "display of g_Q, subscript of the tensor product '(x)_{Z_l} Q_l'",
           "a plain typed Z with a hand-drawn l: no double stroke, no underline, whereas the Q above it and the other "
           "Z's of the display are double-struck (both scans; " + C + "c681_Zsub.png, c681_tensZ.png, w681_gQ.png)",
           r"\otimes_{\Zell}\Qell (\Zell is \mathbb Z_\ell)", "font", "low",
           (r"\otimes_{\Zell}", r"\otimes_{Z_\ell}"),
           "Reported like the typist's plain Q (volume decision with SGA 7 II issue 61)."))
f.append(F(681, "5.1, after the display: 'tels que pour tout Module localement libre E sur X'",
           "tels que (both scans)", r"tels que pour tout Module", "misprint_in_print", "medium", None,
           "The antecedent is 'un homomorphisme d'anneaux g˙' (singular). The TeX keeps the printed reading; the "
           + SECOND + " has 'tel que' (SGA-SRC-001421).", corrected="tel que"))
f.append(F(681, "5.2, 'et tel que l'image du premier membre soit contenue dans celle de H^2(X,Z_l(*))'",
           "H^2 with nothing after the 2 (both scans; " + C + "c681_H2.png)",
           r"celle de $H^2(X,\Zell(\bullet))$", "misprint_in_print", "medium", None,
           "The image of Gr˙(X) lies in the image of the whole H^{2*}(X,Z_l(*)), whose quotient by torsion the next "
           "clause takes. The TeX keeps the printed H^2; the " + SECOND + " has H^{2\\bullet}. Write * for \\bullet "
           "here if the asterisk entry below is applied.",
           corrected=r"H^{2\bullet}(X,\Zell(\bullet))"))
f.append(F(681, "5.2, 'la question de l'existence de g˙ se résoud affirmativement'",
           "résoud (both scans; " + C + "c681_gdot2.png)", r"se résoud affirmativement", "misprint_in_print",
           "medium", None,
           "As in SGA 7 I and II (MISPRINTS_7I, MISPRINTS_7II). The TeX keeps the printed reading; the " + SECOND
           + " has 'résout'. Again on p. 684.", corrected="résout"))
f.append(F(681, "5.2, 'les composantes g^i de l'hypothètique homomorphisme g'",
           "hypothètique, grave accent (both scans; " + C + "c681_hypoth.png)", r"l'hypothètique homomorphisme",
           "misprint_in_print", "high", None,
           "The TeX keeps the printed reading; the " + SECOND + " has 'hypothétique'.", corrected="hypothétique"))
f.append(F(681, "throughout pp. 681-685: H^{2*}(X,Z_l(*)) and its variants; e.g. p. 681 the title of no. 5, "
                "p. 682 'Gr˙(X) -> H^{2*}(X,Z)', p. 685 'H_Y^*(X, - ) -> H^*(X, - )'",
           "a typed asterisk (the six-armed typewriter star) in the degree and in the twist: H^{2*}, Z_l(*), Q_l(*), "
           "H_Y^*, H^*; the raised dot occurs only in Gr˙, K˙, g˙ (both scans; " + C + "c681_gdisp.png, "
           "c683_d63_full.png, c682_61.png)",
           r"\bullet for all of them: \(H^{2\bullet}(X,\Zell(\bullet))\), H^{2\bullet}(X,\Z), "
           r"H_Y^\bullet(X,-)\longrightarrow H^\bullet(X,-)", "symbol", "high", None,
           "Convention of this transcription (the " + SECOND + " has it too); not itemized. On pp. 681-685 every "
           "H^{2\\bullet}, every (\\bullet) after \\Zell or \\Qell and the two H^\\bullet of the last display of "
           "p. 685 are the print's *; \\operatorname{Gr}^\\bullet, K^\\bullet and L^\\bullet are not. One pass for "
           "Exposé XIV: H^{2\\bullet} -> H^{2*}, \\Zell(\\bullet) -> \\Zell(*), \\Qell(\\bullet) -> \\Qell(*), "
           "H_Y^\\bullet(X,-) -> H_Y^*(X,-), H^\\bullet(X,-) -> H^*(X,-); the other pages of the exposé to be "
           "checked against the scan first."))
f.append(F(681, "throughout pp. 681-682: the locally free Module E and the invertible sheaves L_1, L_2, L_3; e.g. "
                "p. 681 'Module localement libre E sur X', '(L_1-1)(L_2-1)(L_3-1) = 0', p. 682 "
                "'c_1(L_1)c_1(L_2)c_1(L_3) != 0'",
           "E and L underlined in every place (E, c_i(E), c^i(E), psi(c_i(E)), c_i^l(E) twice, L_1,L_2,L_3 twice on "
           "p. 681; c_1(L_1)c_1(L_2)c_1(L_3), 'libre E', c_i(E) on p. 682; both scans)",
           r"plain $E$, $c_i(E)$, $L_1,L_2,L_3$, c_1(L_1)c_1(L_2)c_1(L_3)", "underline", "high", None,
           "Convention of the Exposé XIV TeX (no \\underline{E} or \\underline{L} in the exposé; the volume writes "
           "\\underline{E} elsewhere, e.g. Exposé X); not itemized. The underlined O of O_X (p. 684) belongs to the "
           "pending O decision."))

# ---------------- p. 682 ----------------
f.append(F(682, "6.1, 'on n'a pas à distinguer entre le K˙(X) naif et l'autre'",
           "K˙(X), raised dot (both scans; " + C + "c682_Knaif.png)", r"le $K'(X)$ naif", "symbol", "high",
           (r"le $K'(X)$ naif", r"le $K^\bullet(X)$ naif"),
           "p. 681 writes K^\\bullet for the same K˙; K' again in (6.1) (next entry) and on p. 685 (main.tex also on "
           "folio 689)."))
f.append(F(682, "(6.1), 'K˙(X) -> Ch(H^{2*}(X,Z_l(*)))'",
           "K˙(X), raised dot (both scans; " + C + "c682_61.png)", r"K'(X)\longrightarrow \Ch", "symbol", "high",
           (r"K'(X)\longrightarrow \Ch", r"K^\bullet(X)\longrightarrow \Ch"), "As the entry before."))
f.append(F(682, "5.3, 'et on peut répéter à ce propos les reflexions qui précèdent'",
           "reflexions, no accent on the first e (both scans; " + C + "c682_reflex.png)",
           r"les reflexions qui précèdent", "misprint_in_print", "medium", None,
           "The TeX keeps the printed reading; the " + SECOND + " has 'réflexions'.", corrected="réflexions"))
f.append(F(682, "end of 5.3, 'à défaut de g^i lui-même'",
           "no full stop after 'lui-même'; 5.4 follows (both scans; " + C + "c682_luimeme.png, w682_luimeme.png)",
           r"lui-même.", "misprint_in_print", "high", ("lui-même.", "lui-même"),
           "The typist left the sentence without its stop; the TeX silently supplies it (so does the " + SECOND
           + "). The fix restores the printed reading.", corrected="lui-même."))

# ---------------- p. 683 ----------------
f.append(F(683, "(6.2), the source 'H^n(X,Q (i))' of the Gysin homomorphism",
           "underlined Q, then a blank and (i): no l, the place for the hand-drawn l left empty (both scans; "
           + C + "c683_62.png, w683_62.png)",
           r"H^n(X,\Qell(i))", "misprint_in_print", "high", (r"H^n(X,\Qell(i))", r"H^n(X,\Q(i))"),
           "The l was never written in (the other hand-drawn l of the page are dark in both scans). The TeX "
           "silently supplies it; apply together with the next entry.", corrected=r"H^n(X,\Qell(i))"))
f.append(F(683, "(6.2), the target 'H^{n-2d}(Y,Q (i-d))'",
           "underlined Q, a blank, (i-d): no l (both scans; " + C + "c683_62.png, w683_62.png)",
           r"H^{n-2d}(Y,\Qell(i-d))", "misprint_in_print", "high", (r"(Y,\Qell(i-d))", r"(Y,\Q(i-d))"),
           "As the entry before (same display, same omission).", corrected=r"(Y,\Qell(i-d))"))
f.append(F(683, "after (6.2), 'où d est la dimension relative virtuelle de d.'",
           "'virtuelle de d.' (both scans)", r"dimension relative virtuelle de $d$.", "misprint_in_print", "high",
           None,
           "d is the virtual relative dimension of the morphism f of 6.1. The TeX keeps the printed reading; the "
           + SECOND + " has 'de $f$'.", corrected=r"de $f$"))
f.append(F(683, "'à valeurs dans Gr˙(Y)_Q , on constate que'",
           "Gr˙(Y)_Q, raised dot (both scans; " + C + "c683_GrY.png)", r"$\operatorname{Gr}'(Y)_{\Q}$", "symbol",
           "high", (r"dans $\operatorname{Gr}'(Y)_{\Q}$", r"dans $\operatorname{Gr}^\bullet(Y)_{\Q}$"),
           "The print's raised dot in Gr is \\bullet elsewhere (handled globally); here a prime, also twice in the "
           "diagram (6.3) (next entries; main.tex has one more on folio 686). The " + SECOND + " has the prime too."))
f.append(F(683, "diagram (6.3), top left 'Gr˙(X)_Q'",
           "Gr˙(X)_Q, raised dot (both scans; " + C + "c683_d63_full.png, w683_d63full.png)",
           r"\operatorname{Gr}'(X)_{\Q} \arrow[r]", "symbol", "high",
           (r"\operatorname{Gr}'(X)_{\Q} \arrow[r]", r"\operatorname{Gr}^\bullet(X)_{\Q} \arrow[r]"),
           "As the entry before."))
f.append(F(683, "diagram (6.3), bottom left 'Gr˙(Y)_Q'",
           "Gr˙(Y)_Q, raised dot (both scans; " + C + "c683_d63_full.png, w683_d63.png)",
           r"\operatorname{Gr}'(Y)_{\Q} \arrow[r]", "symbol", "high",
           (r"\operatorname{Gr}'(Y)_{\Q} \arrow[r]", r"\operatorname{Gr}^\bullet(Y)_{\Q} \arrow[r]"),
           "As the entry before."))
f.append(F(683, "after (6.3), 'où les flêches horizontales se définissent'",
           "flêches with a circumflex (both scans; " + C + "c683_fl1.png, w683_fleches.png)",
           r"flèches horizontales", "misprint_in_print", "high",
           ("flèches horizontales", "flêches horizontales"),
           "Wrong accent; the TeX silently corrects it, the fix restores the printed reading. Twice more in the "
           "sentence (next entries).", corrected="flèches horizontales"))
f.append(F(683, "same sentence, 'et où les fl?hes verticales sont respectivement'",
           "'fl', then a c carrying the circumflex, then 'hes': six letters, the e missing (both scans; "
           + C + "c683_fl2.png, w683_fl2.png)",
           r"flèches verticales", "misprint_in_print", "medium",
           ("flèches verticales", r"fl\^{c}hes verticales"),
           "Typing slip (the circumflex struck on the c, the e left out). If the glyph is read as ê overstruck by c, "
           "write 'flêhes' instead. The TeX silently corrects it.", corrected="flèches verticales"))
f.append(F(683, "same sentence, 'la flê-che de Exp. VIII'",
           "flê- / che, circumflex (both scans; " + C + "c683_fl3.png, w683_fleches.png)",
           r"la flèche de Exp. VIII", "misprint_in_print", "high", ("flèche de Exp", "flêche de Exp"),
           "As the two entries before.", corrected="flèche de Exp"))
f.append(F(683, "end of 6.2, 'résulte alors de la commutativité du diagramme analogue à (6.3) :'",
           "'analogue à (6.3) :' with a colon before the diagram (6.4) (both scans; " + C + "w683_colon.png)",
           r"analogue à (6.3) followed by \begin{equation}, no colon", "punctuation", "high",
           ("analogue à (6.3)\n\\begin{equation}", "analogue à (6.3) :\n\\begin{equation}"),
           "The " + SECOND + " also lacks the colon."))

# ---------------- p. 684 ----------------
f.append(F(684, "first line, '(mod. équivalence ra-/tionelle)'",
           "rationelle, one n (both scans)", r"(mod. équivalence rationelle)", "misprint_in_print", "high", None,
           "As elsewhere in the volume (MISPRINTS_6). The TeX keeps the printed reading; the " + SECOND
           + " has 'rationnelle'.", corrected="rationnelle"))
f.append(F(684, "6.3, 'comme il est expliqué au n° 3.'",
           "n° with the typed degree sign (both scans; " + C + "c684_no3.png)", r"au no. 3", "symbol", "high",
           ("au no. 3", "au n° 3"),
           "The Exposé XIV TeX writes n° as 'no.' or 'no' (main.tex also on folios 667, 671, 674, 675, 676, 687, "
           "688; those prints not checked here); the volume has n° elsewhere ('n°20')."))
f.append(F(684, "6.4, 'de façon à tranformer intersections'",
           "tranformer, without the s (both scans; " + C + "c684_tranf.png)", r"de façon à tranformer",
           "misprint_in_print", "high", None,
           "The TeX keeps the printed reading; the " + SECOND + " has 'transformer'.", corrected="transformer"))
f.append(F(684, "6.4, 'Cette dernière question se résoud affirmativement'",
           "résoud (both scans)", r"question se résoud affirmativement", "misprint_in_print", "medium", None,
           "As on p. 681. The TeX keeps the printed reading (so does the " + SECOND + " here).",
           corrected="résout"))
f.append(F(684, "6.4, 'et en particulier la classe de Chern est elle nulle dans H^6(Y,Z/2Z) ?'",
           "'est elle' without the hyphen, in the middle of the line (both scans; " + C + "c684_estelle.png)",
           r"la classe de Chern est elle nulle", "misprint_in_print", "medium", None,
           "Interrogative inversion needs the hyphen (the page has 'est-il' twice). The TeX keeps the printed "
           "reading; the " + SECOND + " has 'est-elle'.", corrected="est-elle"))

# ---------------- p. 685 ----------------
f.append(F(685, "7.1, 'pour un ccmplexe de Modules parfait L.'",
           "ccmplexe: the second letter is a c, the same glyph as the first, while the o of 'pour' and 'Modules' on "
           "the line are whole (both scans; " + C + "c685_ccm.png, w685_ccm.png)",
           r"un complexe de Modules", "misprint_in_print", "medium",
           ("un complexe de Modules", "un ccmplexe de Modules"),
           "Typing error silently corrected by the TeX; the fix restores the printed reading.",
           corrected="un complexe de Modules"))
LDOT = ("L. with the dot on the baseline (lower dot), unlike the raised dot of K˙(X) on the same page (both scans; "
        + C + "%s)")
LNOTE = ("The print's L. is L_\\bullet (as p. 18, FIXLOG_6 '\\det^*(L_\\bullet)'); the TeX writes L^\\bullet in all "
         "five places of p. 685 (the " + SECOND + " too): apply the five together.")
f.append(F(685, "7.1, 'pour un complexe de Modules parfait L. sur un schéma X'", LDOT % "c685_L1.png",
           r"parfait $L^\bullet$ sur", "symbol", "high",
           (r"parfait $L^\bullet$ sur", r"parfait $L_\bullet$ sur"), LNOTE))
f.append(F(685, "7.1, display 'c_i(L.) in H^{2i}(X,Z_l(i))'", LDOT % "c685_ciL.png",
           r"c_i(L^\bullet)\in H^{2i}(X,\Zell(i))", "symbol", "high",
           (r"c_i(L^\bullet)\in", r"c_i(L_\bullet)\in"), "As the entry before."))
f.append(F(685, "7.1, 'on sait que le K˙(X) construit avec les complexes parfaits'",
           "K˙(X), raised dot (both scans; " + C + "c685_K.png)", r"le $K'(X)$ construit", "symbol", "high",
           (r"le $K'(X)$ construit", r"le $K^\bullet(X)$ construit"), "As p. 682 (K' for K˙)."))
f.append(F(685, "7.2, 'telle que L.|(X-Y) soit nul'", LDOT % "c685_Lrestr.png",
           r"$L^\bullet|(X-Y)$", "symbol", "high",
           (r"$L^\bullet|(X-Y)$", r"$L_\bullet|(X-Y)$"), "As the first L entry of the page."))
f.append(F(685, "7.2, 'les faisceaux de cohomologie de L. soient à supports dans Y'", LDOT % "c685_Lrestr.png",
           r"de $L^\bullet$ soient", "symbol", "high",
           (r"de $L^\bullet$ soient", r"de $L_\bullet$ soient"), "As the first L entry of the page."))
f.append(F(685, "7.2, display 'c_i^Y(L.) in H_Y^{2i}(X,Z_l(i)) resp. H_Y^{2i}(X,Z)'", LDOT % "c685_ciY.png",
           r"c_i^Y(L^\bullet)\in H_Y^{2i}", "symbol", "high",
           (r"c_i^Y(L^\bullet)", r"c_i^Y(L_\bullet)"), "As the first L entry of the page."))

# ---------------- checks ----------------
pages = {p: (B / f"page_{p}.tex").read_text(encoding="utf-8") for p in range(681, 686)}
bad = 0
for d in f:
    if d["fix"] is None:
        continue
    t = pages[d["page"]]
    old = d["fix"]["old"]
    n = t.count(old)
    marker = any("scan idx" in line for line in old.split("\n"))
    if n != 1 or marker:
        bad += 1
        print("BAD", d["page"], n, repr(old))
    new_t = t.replace(old, d["fix"]["new"], 1)
    if new_t == t:
        print("NOCHANGE", d["page"], repr(old))
# overlapping olds on the same page
for p in pages:
    spans = []
    for d in f:
        if d["page"] == p and d["fix"]:
            i = pages[p].find(d["fix"]["old"])
            spans.append((i, i + len(d["fix"]["old"]), d["fix"]["old"]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            print("OVERLAP", p, repr(a[2]), repr(b[2]))
OUT.write_text(json.dumps(f, ensure_ascii=False, indent=1), encoding="utf-8")
from collections import Counter
cnt = Counter((d["page"], d["kind"] == "misprint_in_print") for d in f)
for p in range(681, 686):
    print(p, "normal", cnt[(p, False)], "misprint", cnt[(p, True)])
print("entries", len(f), "bad", bad)
