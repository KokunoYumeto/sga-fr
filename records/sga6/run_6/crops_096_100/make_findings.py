"""Build findings_096_100.json: check that every fix's old occurs exactly once in its page file, and that the fixes of
one page still apply in list order (each old unique at the moment it is applied).
usage: python -I make_findings.py"""
import json
import pathlib

here = pathlib.Path(__file__).parent
pages = here.parent / "b096_100"
out = here.parent / "findings_096_100.json"
N = "\n"

F = []


def add(page, where, scan, tex, kind, conf, old, new, note, corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, confidence=conf,
             fix=(dict(old=old, new=new) if old is not None else None))
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def emph(s):
    return r"\emph{" + s + "}"


BOLD_NOTE = ("As on pp. 87-88 (applied there): the accepted bold-label convention covers an underlined label word, "
             "not the plain item letters a), b). The TeX bolds the item letters of statements through Exposé I "
             "(see the message).")

# ---------------------------------------------------------------- p. 96
add(96, "Démonstration of 2.2 a), display 'H^j(M') ≃⟶ H^j(M'')   pour tout j'",
    "no punctuation after 'pour tout j' (both scans); the display's second line is 'et H^j(M') = 0 pour j ⩾ i.'",
    r"\qquad\text{pour tout }j,", "punctuation", "high",
    r"\text{pour tout }j,", r"\text{pour tout }j",
    "The TeX adds a comma at the end of the display.")
add(96, "Proposition 2.2, item label 'a)'",
    "plain a), neither underlined nor bold; the underline begins at 'Si' (both scans)",
    r"\textbf{a)}", "font", "medium", r"\textbf{a)}", "a)", BOLD_NOTE)
add(96, "Proposition 2.2, item label 'b)'",
    "plain b); the underline begins at 'Les' (both scans)",
    r"\textbf{b)}", "font", "medium", r"\textbf{b)}", "b)", "As a) above.")

# ---------------------------------------------------------------- p. 98
add(98, "Définition 2.3, first defined term: 'nous dirons que F ∈ ob D(C_S) est n-C_o-pseudo-cohérent si F vérifie ...'",
    "'-pseudo-cohérent' is not underlined, while 'est' before it and 'si' after it are (both scans; "
    "crops_096_100/p98_def23.png, w98_def23.png, p98_nC0.png). The n and the category letter C̲ carry short "
    "underlines of their own.",
    "one \\emph{...} over the whole definition, the defined terms included", "underline", "high",
    r"est \(n\)-\(\mathcal C_0\)-pseudo-cohérent si \(F\) vérifie",
    r"est} \(n\)-\(\mathcal C_0\)-pseudo-cohérent \emph{si \(F\) vérifie",
    "As Définitions 1.4.3 and 2.1 (pp. 93, 95): the defined terms are left out of the underline. Close the "
    "emphasis before the term and reopen it after. Independent of the next entry.")
add(98, "Définition 2.3, second defined term: 'Nous dirons que F est C_o-pseudo-cohérent si F est n-C_o-pseudo-cohérent pour tout n'",
    "'-pseudo-cohérent' after C̲_o is not underlined, while 'est' before it and 'si' after it are; in the later "
    "'n-C_o-pseudo-cohérent' (not a defined term) '-pseudo-cohérent' is underlined (both scans)",
    "inside the one \\emph{...} of the definition", "underline", "high",
    r"est \(\mathcal C_0\)-pseudo-cohérent si \(F\) est",
    r"est} \(\mathcal C_0\)-pseudo-cohérent \emph{si \(F\) est",
    "As the previous entry.")
p24a = (r"Soient \(n,i\in\mathbb Z\), et soit \(u:E\to F\) un \(i\)-quasi-isomorphisme de \(\Cpx(\mathcal C_S)\), "
        r"avec \(F\) \(n\)-pseudo-cohérent et \(E\) strictement \(n\)-pseudo-cohérent. Alors, quitte à raffiner "
        r"\(S\), il existe un triangle commutatif de \(\Cpx(\mathcal C_S)\)")
add(98, "Proposition 2.4, statement before the diagram",
    "underlined by word groups: 'Soient', 'et soit', 'un', 'quasi-isomorphisme', 'de', 'avec', "
    "'n-pseudo-cohérent et', 'strictement', 'pseudo-cohérent', 'Alors,', 'quitte à raffiner', "
    "'il existe un triangle commutatif de' (both scans)",
    "no emphasis: the statement is in roman (Proposition 2.2 and Définition 2.3 have \\emph)", "underline", "high",
    p24a, emph(p24a),
    "As Corollaire 1.4.5 (p. 93). The statement goes on after the diagram (entry below).")
add(98, "Proposition 2.4, diagram (E --v--> E', u, u'), end",
    "a comma to the right of the diagram, on the line of F (both scans)",
    "tikzcd without punctuation", "punctuation", "high",
    r"\\" + N + "F &" + N + r"\end{tikzcd}", r"\\" + N + "F & ," + N + r"\end{tikzcd}",
    "Set in a cell of its own, as on pp. 93-94.")
p24b = (r"où \(E'\) est strictement \(n\)-pseudo-cohérent, \(u'\) un quasi-isomorphisme et \(v\) un monomorphisme "
        r"induisant l'identité en degré \(\geq i\).")
add(98, "Proposition 2.4, end of the statement after the diagram",
    "underlined: 'où', 'est strictement', 'pseudo-cohérent', 'un quasi-isomorphisme et', 'un', "
    "'monomorphisme induisant l'identité en degré' (both scans)",
    "no emphasis", "underline", "high", p24b, emph(p24b),
    "Second part of the statement of the entry above.")
add(98, "Proposition 2.5, item label 'a)'",
    "plain a); the underline begins at 'Si' (both scans)",
    r"\textbf{a)}", "font", "medium", r"\textbf{a)}", "a)", "As on p. 96.")
p25a = (r"Si \(F\in\Ob\Dpx(\mathcal C_S)\) est \(n\)-pseudo-cohérent (resp. pseudo-cohérent), \(F[m]\) est "
        r"\((n-m)\)-pseudo-cohérent (resp. pseudo-cohérent).")
add(98, "Proposition 2.5 a), statement",
    "underlined: 'Si', 'est n-pseudo-cohérent', 'resp.', 'pseudo-cohérent', 'est', 'pseudo-cohérent', 'resp.', "
    "'pseudo-cohérent' (both scans)",
    "no emphasis", "underline", "high", p25a, emph(p25a),
    "Statement of a proposition in roman, as 2.4.")
add(98, "Proposition 2.5, item label 'b)' (printed at the top of p. 99)",
    "plain b) (p. 99, first line; both scans)",
    r"\textbf{b)}", "font", "medium", r"\textbf{b)}", "b)",
    "As a). The line belongs to p. 99 (marker entry there); the fix is given here, where the text stands now.")
add(98, "Proposition 2.5 b), 'Soit' (printed at the top of p. 99)",
    "'Soit' underlined (p. 99, first line; both scans)",
    "Soit, in roman", "underline", "high",
    "Soit" + N, r"\emph{Soit}" + N,
    "Start of the statement 2.5 b), which goes on after the diagram on p. 99 (entry there). Independent of the "
    "label entry before it; with both applied the line reads 'b) \\emph{Soit}'.")

# ---------------------------------------------------------------- p. 99
add(99, "start of page",
    "p. 99 begins 'b) Soit' (Proposition 2.5 b), 'Soit' underlined), then the triangle (*); p. 98 ends "
    "'F[m] est (n-m)-pseudo-cohérent (resp. pseudo-cohérent).' (both scans)",
    "the line '\\textbf{b)} Soit' is the last line of page_098.tex (under the folio-98 marker); page_099.tex "
    "begins with the diagram's \\[",
    "marker", "high", None, None,
    "Page 99 really begins with 'b) Soit'. Move the folio-99 marker above that line. After this file's p. 98 "
    "entries for '\\textbf{b)}' and 'Soit' (the line then reads 'b) \\emph{Soit}'): python -I move_marker.py 6 99 "
    "\"b) \\emph{Soit}\" --before. If the marker is moved first, use the anchor \"\\textbf{b)} Soit\" and apply "
    "those two fixes on p. 99. Simulated on both layers (crops_096_100/sim_markers.py): the end of 2.5 a), a "
    "blank line, the marker, 'b) \\emph{Soit}', '\\['.")
p25b = (r"un" + N + r"triangle distingué de \(\Dpx(\mathcal C_S)\). Si \(E\) et \(G\) sont \(n\)-pseudo-cohérents "
        r"(resp. pseudo-cohérents), alors \(F\) est \(n\)-pseudo-cohérent (resp. pseudo-cohérent).")
add(99, "Proposition 2.5 b), statement after the triangle (*)",
    "underlined: 'un triangle distingué de', 'Si', 'et', 'sont n-pseudo-cohérents', 'resp.', 'pseudo-cohérents', "
    "'alors', 'est', 'pseudo-cohérent', 'resp.', 'pseudo-cohérent' (both scans)",
    "no emphasis", "underline", "high", p25b, emph(p25b),
    "Statement of 2.5 b), begun by 'Soit' (entry on p. 98).")
add(99, "Preuve of 2.5 b), the rotated triangle (F, G[-1] --> E), end",
    "a full stop to the right of E, on its line (both scans)",
    "tikzcd without punctuation", "punctuation", "high",
    r"&& E \arrow[ul]" + N + r"\end{tikzcd}", r"&& E \arrow[ul] & ." + N + r"\end{tikzcd}",
    "Set in a cell of its own, as the commas of pp. 93-94. The triangle (*) has no punctuation in the print "
    "(the sentence goes on 'un triangle distingué'); the third diagram's comma is in the TeX.")

# ---------------------------------------------------------------- p. 100
add(100, "start of page",
    "p. 100 begins with the opening quote of '\"vraie\" flèche de C⁻(C̲_S)'; p. 99 ends '... où u est définie "
    "par une' (both scans)",
    "the opening guillemet ends the last line of page_099.tex ('définie par une «', under the folio-99 marker); "
    "page_100.tex begins 'vraie » flèche'",
    "marker", "high", None, None,
    "Page 100 really begins with the opening quote. python -I move_marker.py 6 100 \"«\" --before (the last « "
    "before the marker is this one; simulated on both layers: '... définie par une ', the marker, '«', "
    "'vraie » flèche ...', which still renders 'une « vraie » flèche').")
add(100, "'La catégorie D(C)_{C_o-coh} est, en vertu de (2.5), une sous-S̲-catégorie triangulée de D(C) (1.1).'",
    "only 'catégorie triangulée' (next line) is underlined; 'sous-S̲-' at the end of the line before has no "
    "underline except the S̲ of the site (both scans; crops_096_100/p100_sousS.png, w100_sousS.png)",
    r"une \emph{sous-\(S\)-catégorie triangulée}", "underline", "medium",
    r"une \emph{sous-\(S\)-catégorie triangulée}", r"une sous-\(S\)-\emph{catégorie triangulée}",
    "The emphasis covers only the second line of the term. Medium: the typist may have meant the whole term.")
add(100, "the site S̲: 'X ∈ ob S̲', 'une sous-S̲-catégorie', 'Supposons que S̲ soit un site ponctuel'",
    "S underlined where it names the site (both scans)",
    r"plain \(S\): '\(X\in\Ob S\)', 'sous-\(S\)-catégorie', 'Supposons que \(S\) soit un site ponctuel'",
    "underline", "high", None, None,
    "Convention of the transcription, as reported for pp. 84-85 and 93-95: one decision for the exposé, "
    "not a page fix.")
add(100, "label 'Proposition 2.7'",
    "'Proposition 2.7' with no full stop after the number (both scans; crops_096_100/p100_prop27.png, "
    "w100_prop27.png); every other label of pp. 96-100 has one",
    r"\textbf{Proposition 2.7.} (silently supplied)", "misprint_in_print", "high",
    r"\textbf{Proposition 2.7.}", r"\textbf{Proposition 2.7}",
    "The typist left out the label's full stop; the TeX silently supplies it (the bold label itself is accepted).",
    corrected=r"\textbf{Proposition 2.7.}")
p27 = (r"Supposons que \(S\) soit un site ponctuel, donc \(\mathcal C=\mathcal C_S\), "
       r"\(\mathcal C_0=\mathcal C_{0,S}\). Alors")
add(100, "Proposition 2.7, opening 'Supposons que S̲ soit un site ponctuel, donc C = C_S , C_o = C_oS . Alors :'",
    "underlined by word groups: 'Supposons que', 'soit un site ponctuel', 'donc', 'Alors'; S̲ and the C̲ have "
    "their own underlines (both scans)",
    "no emphasis", "underline", "high", p27, emph(p27),
    "Statement in roman, as 2.4 and 2.5. Apply before the C_{0S} entry below (this old contains "
    "\\mathcal C_{0,S}; JSON order).")
add(100, "Proposition 2.7, 'C_o = C_oS'",
    "C̲ with the indices o and S side by side, no comma (both scans; crops_096_100/w100_prop27.png)",
    r"\mathcal C_{0,S}", "punctuation", "high",
    r"\mathcal C_{0,S}", r"\mathcal C_{0S}",
    "As pp. 91-92 and 95: the TeX adds the comma between the indices throughout Exposé I.")
add(100, "Proposition 2.7, item label 'a)'",
    "plain a); the underline begins at 'Si' (both scans)",
    r"\textbf{a)}", "font", "medium", r"\textbf{a)}", "a)", "As on p. 96.")
p27a = (r"Si \(F\in\Ob\Dpx(\mathcal C)\) est pseudo-cohérent, il existe un quasi-isomorphisme "
        r"\(E\longrightarrow F\), avec \(E\) strictement pseudo-cohérent")
add(100, "Proposition 2.7 a), statement",
    "underlined: 'Si', 'est pseudo-cohérent,', 'il existe un quasi-isomorphisme', 'avec', 'strictement "
    "pseudo-cohérent'; the reference '(2.1).' is not (both scans)",
    "no emphasis", "underline", "high", p27a, emph(p27a),
    "The reference (2.1) and the full stop stay in roman.")
add(100, "Proposition 2.7, item label 'b)'",
    "plain b); the underline begins at 'Désignons' (both scans)",
    r"\textbf{b)}", "font", "medium", r"\textbf{b)}", "b)", "As on p. 96.")
p27b = (r"Désignons par \(\Kpx^{-,b}(\mathcal C_0)\) la sous-catégorie triangulée pleine de \(\Kpx^-(\mathcal C_0)\) "
        r"formée des complexes acycliques. Le foncteur canonique")
add(100, "Proposition 2.7 b), statement before the display",
    "underlined: 'Désignons par', 'la sous-catégorie triangulée pleine de', 'formée des complexes acycliques.', "
    "'Le foncteur canonique' (both scans)",
    "no emphasis", "underline", "high", p27b, emph(p27b),
    "The statement goes on after the display on p. 101. Apply before the two \\varnothing entries below "
    "(this old contains \\Kpx^{-,b}; JSON order).")
add(100, "Proposition 2.7 b), 'Désignons par K^{-,∅}(C_o)'",
    "the second index is the hand-drawn empty-set sign, a small loop crossed by a long slash, not a b (both "
    "scans; crops_096_100/p100_Kphi.png, w100_Kphi.png)",
    r"\Kpx^{-,b}", "symbol", "high",
    r"\(\Kpx^{-,b}", r"\(\Kpx^{-,\varnothing}",
    "K^{-,∅}(C_o) is the subcategory of the acyclic complexes (cohomology in no degree); b would be bounded "
    "cohomology. The same hand-drawn sign stands beside a typed b on p. 174 (Exposé II, 'K^{-,b}(L(S))/"
    "K^{-,∅}(L(S))'; crops_096_100/w174_full.png), where the TeX writes \\varnothing (main.tex line 4175).")
add(100, "Proposition 2.7 b), display 'K^-(C_o)/K^{-,∅}(C_o) ⟶ D(C)'",
    "the same hand-drawn ∅ (both scans; crops_096_100/w100_Kphi2.png)",
    r"\Kpx^-(\mathcal C_0)/\Kpx^{-,b}(\mathcal C_0)", "symbol", "high",
    r"/\Kpx^{-,b}", r"/\Kpx^{-,\varnothing}",
    "As the previous entry.")

# ---------------------------------------------------------------- checks
ok = True
texts = {}
for x in F:
    p = x["page"]
    if p not in texts:
        texts[p] = (pages / f"page_{p:03d}.tex").read_text(encoding="utf-8")
for x in F:
    if x["fix"]:
        old = x["fix"]["old"]
        n0 = (pages / f"page_{x['page']:03d}.tex").read_text(encoding="utf-8").count(old)
        if n0 != 1:
            ok = False
            print("ORIGINAL COUNT", n0, x["page"], repr(old[:60]))
for p in sorted(texts):  # sequential application in list order
    t = texts[p]
    for x in F:
        if x["page"] != p or not x["fix"]:
            continue
        old, new = x["fix"]["old"], x["fix"]["new"]
        n = t.count(old)
        if n != 1:
            ok = False
            print("SEQUENTIAL COUNT", n, p, repr(old[:60]))
            continue
        t = t.replace(old, new)
    if t.count("{") != t.count("}"):
        print("BRACES", p, t.count("{"), t.count("}"))
        ok = False
    (here / f"applied_{p:03d}.tex").write_text(t, encoding="utf-8", newline="")
print("all checks passed" if ok else "CHECK FAILED")
out.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="")
from collections import Counter
c = Counter((x["page"], x["kind"] == "misprint_in_print") for x in F)
print(sorted(c.items()), len(F))
