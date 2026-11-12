"""Build findings_091_095.json and check that every fix's 'old' occurs exactly once in its page file."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(__file__).resolve().parent.parent
B = RUN / "b091_095"
OUT = RUN / "findings_091_095.json"
KINDS = {"word", "formula", "symbol", "font", "underline", "missing", "extra", "number", "punctuation", "accent",
         "misprint_in_print", "marker", "other"}
F = []


def add(**kw):
    F.append(kw)


NL = "\n"

# ---------------- page 91 ----------------
add(page=91, where="start of page",
    scan="p. 91 begins 'que l'hypothèse de finitude sur H^n(G) est conservée'; p. 90 ends '... rendre H^{n+1}(u) "
         "injectif; on vérifie' (both scans)",
    tex="'que l'%' ends the last line of page_090.tex (under the folio-90 marker); page_091.tex begins "
        "'hypothèse de finitude'",
    kind="marker", confidence="high", fix=None,
    note="Page 91 really begins with 'que l''. Move the folio-91 marker before it: python -I move_marker.py 6 91 "
         "\"que l'\" --before (it takes the last 'que l'' before the marker, the one in 'on vérifie que l'%'; "
         "simulated on both layers: '... on vérifie ', the marker, 'que l'%', 'hypothèse de finitude ...', which "
         "still renders 'on vérifie que l'hypothèse').")
add(page=91, where="'avec M ∈ ob C_oX , est un raffinement de S'",
    scan="C̲ with the two indices o and X side by side, no comma (both scans; crops_091_095/p91_C0X.png)",
    tex="\\mathcal C_{0,X}",
    kind="punctuation", confidence="high",
    fix={"old": r"\mathcal C_{0,X}", "new": r"\mathcal C_{0X}"},
    note="The TeX adds a comma between the indices, as \\mathcal C_{0,U} on p. 85. Same on pp. 92 and 95; the TeX "
         "writes C_{0,X} throughout Exposé I (see the message).")
add(page=91, where="'B^{n+1}(F_X) = Im(F_X^n --d^n--> F_X^{n+1})'",
    scan="Im (typed I and m, both scans)",
    tex="\\Im\\!\\left(...\\right): \\Im is LaTeX's built-in ℑ (Fraktur I); the \\providecommand{\\Im}"
        "{\\operatorname{Im}} of main.tex line 1851 does nothing because \\Im is already defined",
    kind="symbol", confidence="high",
    fix={"old": r"=\Im\!\left(", "new": r"=\operatorname{Im}\!\left("},
    note="The TeX's own macro renders ℑ(F_X^n → F_X^{n+1}) where the print has Im. Every \\Im of main.tex "
         "renders ℑ (p. 90 twice, pp. 139, 445, 461): \\renewcommand{\\Im}{\\operatorname{Im}} at line 1851 "
         "would fix all of them at once (see the message).")

# ---------------- page 92 ----------------
add(page=92, where="octahedron diagram ('l'octaèdre' de K(C_X)), end",
    scan="a full stop to the right of F_X, on its line (both scans; crops_091_095/p92_diagram.png, w92_diagram.png)",
    tex="tikzpicture without punctuation",
    kind="punctuation", confidence="high",
    fix={"old": r"  \draw[->] (FX) to[bend right=42] (GX);" + NL + r"\end{tikzpicture}",
         "new": r"  \draw[->] (FX) to[bend right=42] (GX);" + NL
                + r"  \node[anchor=base] at (6.3,0 |- FX.base) {.};" + NL + r"\end{tikzpicture}"},
    note="Set as a node on the baseline of F_X: the picture's baseline is G_X (baseline=(GX.base)), so a '\\;.' "
         "after \\end{tikzpicture} would stand at the top of the diagram. Independent of the u' entry below.")
add(page=92, where="octahedron diagram, bottom row 'E' --u'-- F_X'",
    scan="the line from E' to F_X, labelled u', is drawn without an arrowhead (both scans; crops_091_095/"
         "p92_diagram.png, w92_diagram.png); every other arrow of the diagram has its head",
    tex="\\draw[->] (Ep) -- node[below] {$u'$} (FX);",
    kind="misprint_in_print", confidence="medium",
    fix={"old": r"\draw[->] (Ep) -- node[below] {$u'$} (FX);", "new": r"\draw (Ep) -- node[below] {$u'$} (FX);"},
    corrected=r"\draw[->] (Ep) -- node[below] {$u'$} (FX);",
    note="The head of u' : E' → F_X (p. 91, 'le cône de u' : E' → F_X') was not drawn; the TeX silently supplies it.")
add(page=92, where="equation number '(.)' of 'H^n(E) → H^n(F) → H^n(G) → 0 .'",
    scan="(.) at the left of the display (both scans)",
    tex="\\tag{(.)}: amsmath sets a \\tag in parentheses, so it renders ((.))",
    kind="number", confidence="high",
    fix={"old": r"\tag{(.)}", "new": r"\tag{.}"},
    note="\\tag{.} renders (.), as printed; the reference 'la suite exacte (.)' later on the page is right. "
         "The only \\tag{(...)} of main.tex.")
add(page=92, where="'avec M ∈ ob C_oX est, par définition, un raffinement de S'",
    scan="C̲ with the indices o and X side by side, no comma (both scans; crops_091_095/p92_C0X.png)",
    tex="\\mathcal C_{0,X}",
    kind="punctuation", confidence="high",
    fix={"old": r"\mathcal C_{0,X}", "new": r"\mathcal C_{0X}"},
    note="As p. 91.")

# ---------------- page 93 ----------------
add(page=93, where="start of page",
    scan="p. 93 begins with the display 'H^n(u') : H^n(E_X) ⊕ M → H^n(F_X)', then 'est un épimorphisme. Cela "
         "termine la démonstration de (1.4.1).'; p. 92 ends '... à partir de la suite exacte (.), que' (both scans)",
    tex="the display \\[ \\Ho^n(u'):\\Ho^n(E_X)\\oplus M\\longrightarrow \\Ho^n(F_X) \\] and the line 'est un' are "
        "the last lines of page_092.tex (under the folio-92 marker); page_093.tex begins 'épimorphisme.'",
    kind="marker", confidence="high", fix=None,
    note="Page 93 really begins with that display. Move the folio-93 marker above its \\[: python -I move_marker.py "
         "6 93 \"\\[\" --before (the last \\[ before the marker is this display's; simulated on both layers: '... "
         "la suite exacte (.), que', the marker, '\\[', the display, '\\]', 'est un', 'épimorphisme. Cela termine "
         "...').")
add(page=93, where="Lemme 1.4.2, 'Soient C une catégorie abélienne, u : E → F un morphisme de complexes de C "
                   "(resp. une flèche de D(C̲))'",
    scan="the first two C are plain typed C without the underline that marks the category letter; only D(C̲) has "
         "it (both scans; crops_091_095/p93_lemme.png). Corollaire 1.4.5 on the same page underlines all three C.",
    tex="\\(\\mathcal C\\) all three times",
    kind="misprint_in_print", confidence="medium",
    fix={"old": r"Soient \(\mathcal C\) une catégorie abélienne, \(u:E\to F\) un morphisme de complexes de "
                r"\(\mathcal C\) (resp.",
         "new": r"Soient \(C\) une catégorie abélienne, \(u:E\to F\) un morphisme de complexes de \(C\) (resp."},
    corrected=r"Soient \(\mathcal C\) une catégorie abélienne, \(u:E\to F\) un morphisme de complexes de "
              r"\(\mathcal C\) (resp.",
    note="The typist left out the underline of C̲ (\\mathcal C) twice; the TeX silently supplies it.")
add(page=93, where="Définition 1.4.3, the defined terms",
    scan="the statement is underlined by word groups ('Nous dirons que', 'est un', 'resp. un', 'si', 'vérifie les "
         "conditions équivalentes de'), but the defined terms 'n-quasi-isomorphisme' and 'n-isomorphisme' are not "
         "underlined (both scans)",
    tex="one \\emph{...} over the whole definition, the defined terms included",
    kind="underline", confidence="high",
    fix={"old": r"\emph{Nous dirons que \(u\) est un \(n\)-quasi-isomorphisme (resp.\ un \(n\)-isomorphisme) si",
         "new": r"\emph{Nous dirons que \(u\) est un} \(n\)-quasi-isomorphisme (\emph{resp.\ un} "
                r"\(n\)-isomorphisme) \emph{si"},
    note="Not the block-underline decision (formulas and punctuation): whole words are left out to set off the "
         "defined terms. Close the emphasis before each defined term and reopen it after. Same in Définition 2.1 "
         "(p. 95).")
add(page=93, where="Corollaire 1.4.5, statement",
    scan="the statement is underlined by word groups: 'Soient', 'une catégorie abélienne', 'un', "
         "'quasi-isomorphisme de complexes de', 'Il existe un diagramme commutatif de' (both scans)",
    tex="no emphasis: the statement is in roman (Lemme 1.4.2, Définition 1.4.3 and Corollaire 1.4.4 have \\emph)",
    kind="underline", confidence="high",
    fix={"old": r"Soient \(\mathcal C\) une catégorie abélienne, \(n\in\mathbb Z\), et \(u:E\to F\) un "
                r"\(n\)-quasi-isomorphisme de complexes de \(\mathcal C\). Il existe un diagramme commutatif de "
                r"\(\Cpx(\mathcal C)\)",
         "new": r"\emph{Soient \(\mathcal C\) une catégorie abélienne, \(n\in\mathbb Z\), et \(u:E\to F\) un "
                r"\(n\)-quasi-isomorphisme de complexes de \(\mathcal C\). Il existe un diagramme commutatif de "
                r"\(\Cpx(\mathcal C)\)}"},
    note="The statement goes on after the diagram on p. 94 ('où u' est un quasi-isomorphisme ... en degré ≥ n'), "
         "also without emphasis in the TeX (entry for p. 94).")
add(page=93, where="diagram of Corollaire 1.4.5 (E --v--> E', u, u'), end",
    scan="a comma to the right of the diagram, on the line of F (both scans)",
    tex="tikzcd without punctuation",
    kind="punctuation", confidence="high",
    fix={"old": "\\arrow[dl,\"u'\"]\\\\" + NL + "F &", "new": "\\arrow[dl,\"u'\"]\\\\" + NL + "F & ,"},
    note="Set in the last cell, as on pp. 7, 59 and 80.")
add(page=93, where="pp. 93-95: the site S̲",
    scan="S underlined where it names the site, plain where it names the object S: p. 93 Corollaire 1.4.4 "
         "'Soient S̲, S, C̲, C̲_o comme en (1.4.1)'; p. 94 'dans le cas où S̲ est le site ponctuel'; p. 95 2.0 "
         "'S̲ désigne un site, S un objet de S̲, C̲ une S̲-catégorie ... une sous-S̲-catégorie', Définition 2.1 "
         "'X ∈ ob S̲' (both scans)",
    tex="plain \\(S\\) for both: 'Soient \\(S,S,\\mathcal C,\\mathcal C_0\\)', 'le cas où \\(S\\) est le site "
        "ponctuel', '\\(S\\) désigne un site, \\(S\\) un objet de \\(S\\)', '\\(X\\in\\Ob S\\)'",
    kind="underline", confidence="high", fix=None,
    note="Convention of the transcription, as reported for pp. 84-85 (S̲ underlined in the print, plain in the "
         "TeX): one decision for the exposé, not a page fix. Where both stand together the TeX reads 'S, S'.")

# ---------------- page 94 ----------------
add(page=94, where="lines 1-2, end of Corollaire 1.4.5, 'où u' est un quasi-isomorphisme et v un monomorphisme "
                   "induisant l'identité en degré ≥ n (i.e. ...)'",
    scan="underlined: 'où', 'est un quasi-isomorphisme et', 'un monomorphisme induisant l'identité', 'en degré'; "
         "the parenthesis '(i.e. tel que E'^i = E^i et v^i = Id(E^i) pour i ≥ n).' is not underlined (both scans)",
    tex="no emphasis",
    kind="underline", confidence="high",
    fix={"old": "où \\(u'\\) est un" + NL + "quasi-isomorphisme et \\(v\\) un monomorphisme induisant l'identité "
                "en degré \\(\\geq n\\) (i.e.",
         "new": "\\emph{où \\(u'\\) est un" + NL + "quasi-isomorphisme et \\(v\\) un monomorphisme induisant "
                "l'identité en degré} \\(\\geq n\\) (i.e."},
    note="End of the statement begun on p. 93 (entry there); the parenthesis stays in roman.")
add(page=94, where="first triangle (E --v_{n-1}--> E'_{n-1}, u, u'_{n-1}), end",
    scan="a comma to the right of the diagram, on the line of F (both scans)",
    tex="tikzcd without punctuation",
    kind="punctuation", confidence="high",
    fix={"old": "\\arrow[dl,\"u'_{n-1}\"]\\\\" + NL + "F &", "new": "\\arrow[dl,\"u'_{n-1}\"]\\\\" + NL + "F & ,"},
    note="Set in the last cell, as on p. 93.")
add(page=94, where="second triangle (E'_i --v_{i-1}--> E'_{i-1}, u'_i, u'_{i-1}), end",
    scan="a comma to the right of the diagram, on the line of F (both scans)",
    tex="tikzcd without punctuation",
    kind="punctuation", confidence="high",
    fix={"old": "\\arrow[dl,\"u'_{i-1}\"]\\\\" + NL + "F &", "new": "\\arrow[dl,\"u'_{i-1}\"]\\\\" + NL + "F & ,"},
    note="As the first triangle.")

# ---------------- page 95 ----------------
add(page=95, where="Définition 2.1, the defined terms",
    scan="'strictement C̲_o-n-pseudo-cohérent (resp. C̲_o-pseudo-cohérent, resp. C̲_o-parfait)' is not underlined "
         "(only the category letters carry their own underline); the rest of the statement is underlined by word "
         "groups: 'Soient', 'un complexe de', 'et', 'Nous dirons que', 'est', 'si', 'pour', ... (both scans; "
         "crops_091_095/p95_def21.png)",
    tex="one \\emph{...} over the whole definition, the defined terms included",
    kind="underline", confidence="high",
    fix={"old": r"est strictement \(\mathcal C_0\)-\(n\)-pseudo-cohérent (resp.\ \(\mathcal C_0\)-pseudo-cohérent, "
                r"resp.\ \(\mathcal C_0\)-parfait) si",
         "new": r"est} strictement \(\mathcal C_0\)-\(n\)-pseudo-cohérent (resp.\ \(\mathcal C_0\)-pseudo-cohérent, "
                r"resp.\ \(\mathcal C_0\)-parfait) \emph{si"},
    note="As Définition 1.4.3 (p. 93): the defined terms are left out of the underline.")
add(page=95, where="Définition 2.1, 'E^i ∈ ob C_oS pour i ≥ n'",
    scan="C̲ with the indices o and S side by side, no comma (both scans; crops_091_095/p95_C0S.png)",
    tex="\\mathcal C_{0,S}",
    kind="punctuation", confidence="high",
    fix={"old": r"\mathcal C_{0,S}", "new": r"\mathcal C_{0S}"},
    note="As pp. 91-92. Apply before the misprint entry that follows (its corrected reading assumes it).")
add(page=95, where="Définition 2.1, 'E^i ∈ ob C_oS pour i ≥ n'",
    scan="index S (both scans)",
    tex="\\mathcal C_{0,S}: keeps the printed S (the current layer too)",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"\mathcal C_{0X}",
    note="E is a complex of C_X with X ∈ ob S̲ arbitrary (same sentence), so its components lie in C_X and the "
         "condition is E^i ∈ ob C_{0X}; C_{0S} is the fibre at the fixed object S of 2.0. The TeX keeps the "
         "printed reading; the corrected layer needs \\mathcal C_{0X} (or \\mathcal C_{0,X} if the comma "
         "entry is not applied).")
add(page=95, where="Preuve of Lemme 2.1.1, display '0 → Z^n(E) → E^n → E^{n+1} → ... → 0'",
    scan="three typed full stops on the baseline, below the level of the arrows (both scans; crops_091_095/"
         "p95_dots.png)",
    tex="\\cdots",
    kind="symbol", confidence="medium",
    fix={"old": r"E^{n+1}\longrightarrow\cdots\longrightarrow 0", "new": r"E^{n+1}\longrightarrow\ldots\longrightarrow 0"},
    note="\\cdots sets the dots at mid-height (same kind of fix as pp. 49, 79, 80).")

# ---------------- checks ----------------
pages = {p: (B / f"page_{p:03d}.tex").read_text(encoding="utf-8") for p in range(91, 96)}
ok = True
for x in F:
    assert x["kind"] in KINDS, x["kind"]
    assert x["confidence"] in ("high", "medium", "low")
    if x["kind"] == "misprint_in_print":
        assert "corrected" in x, x["where"]
    else:
        assert "corrected" not in x
    fx = x.get("fix")
    if fx:
        n = pages[x["page"]].count(fx["old"])
        if n != 1:
            print("NOT UNIQUE", x["page"], n, repr(fx["old"][:80]))
            ok = False
        if "%%%%%%%%%%" in fx["old"] or "%%%%%%%%%%" in fx["new"]:
            print("MARKER IN FIX", x["page"])
            ok = False
        if fx["old"] == fx["new"]:
            print("NO-OP FIX", x["page"])
            ok = False
counts = {}
for x in F:
    c = counts.setdefault(x["page"], [0, 0])
    c[1 if x["kind"] == "misprint_in_print" else 0] += 1
print("counts", counts, "total", len(F), "ok" if ok else "PROBLEMS")
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("written", OUT)
