"""Write findings_101_105.json and check every fix: 'old' occurs exactly once in its page_NNN.tex, never touches a
marker line, and the fixes of a page still apply one after another in JSON order (dependencies noted in the notes).
usage: python -I make_findings.py"""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(__file__).resolve().parents[1]
PAGES = RUN / "b101_105"
OUT = RUN / "findings_101_105.json"

F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- p. 101
add(101, "first line, end of Proposition 2.7 b) (statement begun on p. 100)",
    "'est pleinement fidèle et a pour image essentielle' underlined; 'D(C̲)_{C̲o-coh} .' not (both scans)",
    "plain 'est pleinement fidèle et a pour image essentielle'",
    "underline", "high",
    {"old": "est\npleinement fidèle et a pour image essentielle",
     "new": "\\emph{est\npleinement fidèle et a pour image essentielle}"},
    "End of the statement 2.7 b), whose first part (p. 100) is in \\emph, closed before the display.")

add(101, "Preuve of 2.7 a), triangle (E_i, E_{i-1}, F), end",
    "a comma to the right of the diagram, on the line of F (both scans)",
    "tikzcd without punctuation",
    "punctuation", "high",
    {"old": "\\arrow[dl,\"u_{i-1}\"]\\\\\nF &",
     "new": "\\arrow[dl,\"u_{i-1}\"]\\\\\nF & ,"},
    "Set in a cell of its own, as on pp. 93-94 and 98 (main.tex 'F & ,').")

add(101, "Proposition 2.7.1, statement before the diagram",
    "underlined by word groups: 'Sous les hypothèses de', 'soit', 'un n-quasi-isomorphisme de', 'avec', "
    "'pseudo-cohérent et', 'strictement pseudo-cohérent.', 'Il existe alors un triangle commutatif de' (both scans)",
    "no emphasis: the statement is in roman (2.4, 2.5, 2.7 have \\emph)",
    "underline", "high",
    {"old": "Sous les hypothèses de (2.7), soit \\(u:E\\to F\\) un \\(n\\)-quasi-isomorphisme de \\(\\Cpx(\\mathcal C)\\), "
            "avec \\(F\\) pseudo-cohérent et \\(E\\) strictement pseudo-cohérent. Il existe alors un triangle commutatif de",
     "new": "\\emph{Sous les hypothèses de (2.7), soit \\(u:E\\to F\\) un \\(n\\)-quasi-isomorphisme de \\(\\Cpx(\\mathcal C)\\), "
            "avec \\(F\\) pseudo-cohérent et \\(E\\) strictement pseudo-cohérent. Il existe alors un triangle commutatif de}"},
    "As Proposition 2.4 (p. 98). The final C(C̲) is not underlined (only the C̲ itself). The statement goes on after the "
    "diagram (entry below and p. 102).")

add(101, "Proposition 2.7.1, triangle (E, E', F), end",
    "a comma to the right of the diagram, on the line of F (both scans)",
    "tikzcd without punctuation",
    "punctuation", "high",
    {"old": "\\arrow[dl,\"u'\"]\\\\\nF &",
     "new": "\\arrow[dl,\"u'\"]\\\\\nF & ,"},
    "As the first diagram of the page.")

add(101, "Proposition 2.7.1, statement after the diagram (last line of the page)",
    "underlined: 'où', 'est strictement pseudo-cohérent', 'un quasi-isomorphisme', 'et', 'un' (both scans)",
    "no emphasis",
    "underline", "high",
    {"old": "où \\(E'\\) est strictement pseudo-cohérent, \\(u'\\) un quasi-isomorphisme, et \\(v\\) un",
     "new": "\\emph{où \\(E'\\) est strictement pseudo-cohérent, \\(u'\\) un quasi-isomorphisme, et \\(v\\) un}"},
    "The sentence ends on p. 102 (entry there); the \\emph closes before the page marker. The 'i' of "
    "'quasi-isomorphisme' is typed over an 'l' in both scans: the typist's correction, the TeX's 'isomorphisme' stands.")

# ---------------------------------------------------------------- p. 102
add(102, "first line, end of Proposition 2.7.1",
    "'monomorphisme induisant l'identité en degré' underlined; '≥ n.' not (both scans)",
    "no emphasis",
    "underline", "high",
    {"old": "monomorphisme induisant l'identité en degré",
     "new": "\\emph{monomorphisme induisant l'identité en degré}"},
    "End of the statement 2.7.1 (p. 101).")

add(102, "Définition 2.8, before the display",
    "underlined: 'Soient', 'et', 'Nous dirons que', 'est de', 'si l'ensemble des', 'au-dessus de', 'tels qu'il existe', "
    "'une suite exacte'; the defined term 'n-C̲o-présentation finie' is not underlined (its C̲ has its own short "
    "underline) (both scans)",
    "no emphasis",
    "underline", "high",
    {"old": "Soient \\(n\\in\\mathbb N\\) et \\(F\\in\\Ob\\mathcal C_S\\). Nous dirons que \\(F\\) est de "
            "\\(n\\)-\\(\\mathcal C_0\\)-présentation finie si l'ensemble des \\(X\\) au-dessus de \\(S\\) tels qu'il "
            "existe une suite exacte",
     "new": "\\emph{Soient \\(n\\in\\mathbb N\\) et \\(F\\in\\Ob\\mathcal C_S\\). Nous dirons que \\(F\\) est de} "
            "\\(n\\)-\\(\\mathcal C_0\\)-présentation finie \\emph{si l'ensemble des \\(X\\) au-dessus de \\(S\\) tels "
            "qu'il existe une suite exacte}"},
    "Defined term left out of the emphasis, as Définitions 2.1 and 2.3 (pp. 95, 98).")

add(102, "Définition 2.8, after the display",
    "underlined: 'avec', 'pour', 'est un raffinement de', 'Nous dirons que', 'est d'', 'si', 'est de n-', "
    "'-présentation finie pour tout'; the defined term '∞-C̲o-présentation finie' is not underlined (both scans)",
    "no emphasis",
    "underline", "high",
    {"old": "avec \\(E^i\\in\\Ob\\mathcal C_{0,X}\\) pour \\(-n\\leq i\\leq 0\\), est un raffinement de \\(S\\). Nous "
            "dirons que \\(F\\) est d'\\(\\infty\\)-\\(\\mathcal C_0\\)-présentation finie si \\(F\\) est de "
            "\\(n\\)-\\(\\mathcal C_0\\)-présentation finie pour tout",
     "new": "\\emph{avec \\(E^i\\in\\Ob\\mathcal C_{0,X}\\) pour \\(-n\\leq i\\leq 0\\), est un raffinement de \\(S\\). "
            "Nous dirons que \\(F\\) est d'}\\(\\infty\\)-\\(\\mathcal C_0\\)-présentation finie \\emph{si \\(F\\) est de "
            "\\(n\\)-\\(\\mathcal C_0\\)-présentation finie pour tout}"},
    "As the entry before. Apply before the C_{0X} entry below (this old contains \\mathcal C_{0,X}; JSON order).")

add(102, "Définition 2.8, 'avec E^i ∈ ob C_oX'",
    "C̲ with the indices o and X side by side, no comma (both scans)",
    "\\mathcal C_{0,X}",
    "punctuation", "high",
    {"old": "\\mathcal C_{0,X}", "new": "\\mathcal C_{0X}"},
    "As C_{0S} on p. 100 (applied). Apply after the underline entry before (JSON order).")

add(102, "Définition 2.8, display 'E^{-n} → ... → E^o → F_X → 0'",
    "three typed full stops on the baseline of the letters (witness: dots and E^{-n} end on the same pixel row); the "
    "hand-drawn arrows sit low here too, at about the height of the dots (both scans; crops_101_105/p102_seq1z.png)",
    "\\cdots",
    "symbol", "low",
    {"old": "E^{-n}\\longrightarrow\\cdots\\longrightarrow E^0",
     "new": "E^{-n}\\longrightarrow\\ldots\\longrightarrow E^0"},
    "Same kind of fix as pp. 79, 80, 86, 95 (typed baseline dots as \\ldots). Low: unlike there, the dots are not "
    "below the arrows.")

add(102, "'Nous dirons \"de présentation finie\" pour \"de 1-présentation finie\", ...'",
    "starts a new, indented paragraph after '... possible sur C̲o.' (both scans)",
    "runs on in the paragraph 'Bien entendu, ...'",
    "other", "high",
    {"old": "sur \\(\\mathcal C_0\\). Nous dirons", "new": "sur \\(\\mathcal C_0\\).\n\nNous dirons"},
    "Missing paragraph break.")

add(102, "Proposition 2.9, opening",
    "underlined: 'Soient', 'et', 'Conditions équivalentes'; the colon not (both scans)",
    "no emphasis",
    "underline", "high",
    {"old": "Soient \\(n\\in\\mathbb N\\) et \\(F\\in\\Ob\\mathcal C_S\\). Conditions équivalentes",
     "new": "\\emph{Soient \\(n\\in\\mathbb N\\) et \\(F\\in\\Ob\\mathcal C_S\\). Conditions équivalentes}"},
    "Statement of a proposition in roman, as 2.7.1.")

add(102, "Proposition 2.9 (i)",
    "underlined: 'est de', 'présentation finie', 'resp.', 'présentation finie' (both scans)",
    "no emphasis",
    "underline", "high",
    {"old": "\\(F\\) est de \\(n\\)-présentation finie (resp. d'\\(\\infty\\)-présentation finie)",
     "new": "\\(F\\) \\emph{est de \\(n\\)-présentation finie (resp. d'\\(\\infty\\)-présentation finie)}"},
    "Part of the statement 2.9.")

add(102, "Proposition 2.9 (ii)",
    "underlined: 'est', 'pseudo-cohérent', 'resp.', 'pseudo-cohérent' (both scans)",
    "no emphasis",
    "underline", "high",
    {"old": "\\(F\\) est \\((-n)\\)-pseudo-cohérent (resp. pseudo-cohérent)",
     "new": "\\(F\\) \\emph{est \\((-n)\\)-pseudo-cohérent (resp. pseudo-cohérent)}"},
    "Part of the statement 2.9.")

add(102, "Proposition 2.9, 'Dans le cas où S est un site ponctuel, ...'",
    "underlined: 'Dans le cas où', 'est un site ponctuel', 'est pseudo-cohérent si et seulement', "
    "'s'il existe une suite exacte'; the S̲ of the site has its own underline (both scans)",
    "no emphasis",
    "underline", "high",
    {"old": "Dans le cas où \\(S\\) est un site ponctuel, \\(F\\) est pseudo-cohérent si et seulement s'il existe une "
            "suite exacte",
     "new": "\\emph{Dans le cas où \\(S\\) est un site ponctuel, \\(F\\) est pseudo-cohérent si et seulement s'il existe "
            "une suite exacte}"},
    "Part of the statement 2.9.")

add(102, "Proposition 2.9, display '... → E^i → ... → E^o → F → 0'",
    "both groups of three dots are typed full stops on the baseline; the arrows sit low, as in the display of 2.8 "
    "(both scans)",
    "\\cdots twice",
    "symbol", "low",
    {"old": "\\cdots\\longrightarrow E^i\\longrightarrow\\cdots\\longrightarrow E^0",
     "new": "\\ldots\\longrightarrow E^i\\longrightarrow\\ldots\\longrightarrow E^0"},
    "As the display of Définition 2.8.")

add(102, "Proposition 2.9, end 'avec E^i ∈ ob C_o pour tout i.'",
    "underlined: 'avec', 'pour tout' (both scans)",
    "no emphasis",
    "underline", "high",
    {"old": "avec \\(E^i\\in\\Ob\\mathcal C_0\\) pour tout", "new": "\\emph{avec \\(E^i\\in\\Ob\\mathcal C_0\\) pour tout}"},
    "End of the statement 2.9.")

# ---------------------------------------------------------------- p. 103
add(103, "start of page",
    "p. 103 begins 'l'implication (ii) ⟹ (i) résulte aussitôt de (2.4)'; p. 102 ends '... est immédiate sur les "
    "définitions, et' (both scans)",
    "'l'' ends the last line of page_102.tex ('et l'%', under the folio-102 marker); page_103.tex begins 'implication'",
    "marker", "high", None,
    "Page 103 really begins with 'l'implication'. python -I move_marker.py 6 103 \"l'%\" --before (simulated on both "
    "layers, crops_101_105/sim_marker_103.py: '... et ', the marker, 'l'%', 'implication ...', which still renders "
    "'et l'implication').")

add(103, "Preuve of 2.10 b), triangle (F', F, H^n(F)[-n]), end",
    "a comma to the right of H^n(F)[-n], on its line (both scans)",
    "tikzcd without punctuation",
    "punctuation", "high",
    {"old": "\\Ho^n(F)[-n] \\arrow[ul]", "new": "\\Ho^n(F)[-n] \\arrow[ul] & ,"},
    "Set in a cell of its own, as p. 99 ('&& E \\arrow[ul] & .').")

# ---------------------------------------------------------------- p. 104
add(104, "Proposition 2.11 b), conclusion",
    "'alors F est pseudo-cohérent.' (both scans; crops_101_105/w104_b_end.png)",
    "alors \\(F\\) est pseudo-cohérent. (printed reading kept)",
    "misprint_in_print", "medium", None,
    "Under the hypotheses for i ≥ n alone F need not be pseudo-coherent; as in a), the conclusion is "
    "'n-pseudo-cohérent (resp. pseudo-cohérent)', and the proof of b) proves n-pseudo-cohérent (from 2.10 b)). "
    "The TeX keeps the printed reading (both layers).",
    corrected="alors \\(F\\) est \\(n\\)-pseudo-cohérent (resp. pseudo-cohérent)")

add(104, "Preuve of 2.11 a), 'On raisonne par récurrence sur N tel que F^i ≠ 0 pour i > n+N'",
    "F^i ≠ 0 (a clear ≠ in both scans; crops_101_105/p104_neq.png, w104_neq.png)",
    "\\(F^i\\neq0\\) (printed reading kept)",
    "misprint_in_print", "high", None,
    "The recurrence is on the N for which F^i = 0 for i > n+N (N = 0 gives F acyclic in degree > n, for 2.10 b); "
    "F' then vanishes above n+N-1), as in b): 'H^i(F) = 0 pour i > n+N'. The TeX keeps the printed reading (both "
    "layers).",
    corrected="\\(F^i=0\\)")

add(104, "Preuve of 2.11 b), triangle (F', F, H^{n+N}(F)[-n-N]), end",
    "a full stop to the right of H^{n+N}(F)[-n-N], on its line (both scans)",
    "tikzcd without punctuation",
    "punctuation", "high",
    {"old": "\\Ho^{n+N}(F)[-n-N] \\arrow[ul]", "new": "\\Ho^{n+N}(F)[-n-N] \\arrow[ul] & ."},
    "As the triangle of p. 103.")

# ---------------------------------------------------------------- p. 105
add(105, "Preuve of 2.12, 'Cela signifie, d'après (2.10 b)), que H^n(F'_{≤n} + F''_{≤n}) est de type fini.'",
    "H^n(F'_{≤n} + F''_{≤n}) in the running text, at the start of the line 'H^n(...) est de type fini. Mais on a' "
    "(both scans)",
    "a display \\[ \\Ho^n(F'_{\\leq n}+F''_{\\leq n}) \\]",
    "other", "medium",
    {"old": "que\n\\[\n  \\Ho^n(F'_{\\leq n}+F''_{\\leq n})\n\\]\nest de type fini.",
     "new": "que \\(\\Ho^n(F'_{\\leq n}+F''_{\\leq n})\\) est de type fini."},
    "The TeX makes an inline formula a display (same kind of fix as pp. 21, 34, 42, 80). The next formula "
    "(H^n(...) = H^n(...) + H^n(...) ,) is a display in the print too.")

# ---------------------------------------------------------------- checks
MARK = "%%%%%%%%%%  scan idx"
ok = True
by_page = {}
for f in F:
    by_page.setdefault(f["page"], []).append(f)
for page, items in by_page.items():
    t = (PAGES / f"page_{page:03d}.tex").read_text(encoding="utf-8")
    cur = t
    for f in items:
        fx = f["fix"]
        if fx is None:
            continue
        n = t.count(fx["old"])
        if n != 1:
            ok = False
            print("NOT UNIQUE in original", page, n, repr(fx["old"][:60]))
        if MARK in fx["old"] or MARK in fx["new"]:
            ok = False
            print("TOUCHES MARKER", page, repr(fx["old"][:60]))
        m = cur.count(fx["old"])
        if m != 1:
            ok = False
            print("NOT UNIQUE in sequence", page, m, repr(fx["old"][:60]))
        cur = cur.replace(fx["old"], fx["new"], 1)
    if cur.count("{") != cur.count("}"):
        ok = False
        print("UNBALANCED BRACES after all fixes on", page)
    (RUN / "crops_101_105" / f"applied_{page:03d}.tex").write_text(cur, encoding="utf-8", newline="\n")

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
counts = {}
for f in F:
    c = counts.setdefault(f["page"], [0, 0])
    c[1 if f["kind"] == "misprint_in_print" else 0] += 1
print("ok" if ok else "PROBLEMS", len(F), "findings", counts)
