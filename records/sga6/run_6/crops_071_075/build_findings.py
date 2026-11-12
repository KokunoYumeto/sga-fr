"""Build findings_071_075.json and check that every fix's old occurs exactly once in its page file."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
B = RUN / "b071_075"
NL = "\n"


def fx(old, new):
    return {"old": old, "new": new}


F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- page 71 ----------------
add(71, "heading of the bibliography",
    "Références bibliographiques : (underlined heading followed by a colon; both scans)",
    r"\subsection*{Références bibliographiques}",
    "punctuation", "medium",
    fx(r"\subsection*{Références bibliographiques}", r"\subsection*{Références bibliographiques~:}"),
    "The colon after the heading is missing; the heading form without the underline is accepted typesetting.")
add(71, "reference [1]",
    "Hirzebruch : Neue topologischen Methoden in der algebraischen Geometrie. (both scans)",
    "Neue topologischen Methoden",
    "misprint_in_print", "high", None,
    "Typing error: the title of Hirzebruch's book is 'Neue topologische Methoden in der algebraischen Geometrie'. "
    "The TeX keeps the printed reading.",
    corrected="Neue topologische Methoden")
add(71, "heading 'Rappel de notations'",
    "* Rappel de notations: an asterisk (normal typing height) before the underlined heading. It opens the "
    "copyist's interpolation that closes with the lowered asterisk after 'f_!(G) = Σ (-1)^p R^p f_*(G).' at the "
    "top of p. 73. The footnote at the foot of the page has no call mark of its own (both scans).",
    r"\subsection*{Rappel de notations\footnotemark}: no asterisk; the footnote hangs on a numbered "
    r"\footnotemark after the heading",
    "missing", "medium",
    fx(r"\subsection*{Rappel de notations\footnotemark}", r"\subsection*{* Rappel de notations\footnotemark}"),
    r"The TeX keeps the closing asterisk on p. 73 ('\quad*') but drops this opening one. The \footnotemark has "
    "no counterpart in the print (its footnote is unmarked); the fix leaves it as the attachment of the footnote.")
add(71, "footnote",
    "Les passages entre astériques * ... * sont des interpolations du copiste. (both scans)",
    "Les passages entre astériques",
    "misprint_in_print", "high", None,
    "Typing error for 'astérisques'; the TeX keeps the printed reading. (For the raised and lowered asterisks of "
    "this footnote see the interpolation-asterisk entry under p. 73.)",
    corrected="astérisques")
add(71, "[Ce sont celles du \"rapport sur Riemann-Roch\", cité R.R.R. dans ce qui suit.]",
    "cité R.R.R. dans ce qui suit (letters with full stops; both scans)",
    r"cité \(\RRR\) dans: \RRR is \newcommand{\RRR}{\mathrm{RRR}} (main.tex l. 29) and prints 'RRR'; the later "
    r"\providecommand{\RRR}{\mathrm{R.R.R.}} (l. 1517) has no effect",
    "punctuation", "high",
    fx(r"cité \(\RRR\) dans", r"cité R.R.R. dans"),
    "The full stops are lost through the macro. Same on p. 73; only the running head prints RRR without stops.")
add(71, "last line: 'resp. une sous-' / p. 72 'variété Y de X)'",
    "'sous-variété' is divided at the page break after its own hyphen: 'une sous-' ends p. 71, 'variété' begins "
    "p. 72",
    r"page_071.tex ends 'resp.\ une sous-' and the folio-72 marker line follows: the line end after 'sous-' prints "
    "as a space, so the output reads 'sous- variété'",
    "other", "high",
    fx(r"resp.\ une sous-", r"resp.\ une sous-%"),
    "The folio-72 marker itself stands right (p. 72 begins 'variété'). The % joins the two halves as at folio 18 "
    "('cet ex%'). The same line stands before the folio-72 marker in the current layer: apply there too.")

# ---------------- page 72 ----------------
add(72, "'On note A(X) l'anneau gradué des classes de cylces de X'",
    "cylces (both scans)", "cylces",
    "misprint_in_print", "high", None,
    "Typing error; the TeX keeps the printed reading.",
    corrected="cycles")
add(72, "'(pour l'équivalence rationnelle -cf. Chow)'",
    "rationnelle -cf. Chow): a hyphen joined to 'cf.' (both scans)",
    r"rationnelle~-- cf.\ Chow",
    "punctuation", "medium",
    fx(r"rationnelle~-- cf.\ Chow", r"rationnelle -cf.\ Chow"),
    "The TeX's en dash (tied before, spaced after) is not in the print.")
add(72, "after '... est formé des cycles de codimension i.'",
    "'Si E est un fibré à fibre vectoriel, on note ...' begins a new, indented paragraph (both scans)",
    r"'... de codimension \(i\). Si \(E\) est un fibré ...' runs on in one paragraph",
    "other", "high",
    fx(r"codimension \(i\). Si \(E\)", r"codimension \(i\)." + NL + NL + r"Si \(E\)"),
    "Missing paragraph break.")
add(72, "'Si E est un fibré à fibre vectoriel, on note C(E) = Σ C^i(E)'",
    "fibré à fibre vectoriel, (both scans)", "fibré à fibre vectoriel,",
    "misprint_in_print", "medium", None,
    "Agreement error ('fibre' is feminine; 'fibré à fibre vectorielle' two paragraphs below and throughout). "
    "The TeX keeps the printed reading.",
    corrected="fibre vectorielle")
add(72, "after 'Ce sont des éléments de A(X) ⊗ Q .'",
    "'Lorsque y est le fibré tangent à X, ...' is a new, indented paragraph (both scans)",
    r"'... \(A(X)\otimes\mathbb Q\). Lorsque \(y\) ...' in one paragraph",
    "other", "high",
    fx(r"\otimes\mathbb Q\). Lorsque", r"\otimes\mathbb Q\)." + NL + NL + "Lorsque"),
    "Missing paragraph break. 'Ce sont des éléments' starts at the margin and rightly continues the paragraph "
    "of the display.")
add(72, "after the display f* : A(X) -> A(Y) et f_* : A(Y) -> A(X)",
    "'Le premier est homogène de degré 0 et multiplicatif.' begins an indented paragraph after the display "
    "(both scans)",
    r"\] followed directly by 'Le premier est homogène' (the text continues the paragraph of the display)",
    "other", "high",
    fx(r"\]" + NL + "Le premier", r"\]" + NL + NL + "Le premier"),
    "Missing paragraph break (text that continues after a display starts at the margin, as 'Ce sont des "
    "éléments' above).")
add(72, "'Le second est homogène de degré dim.X - dim.Y.'",
    "dim.X - dim.Y (a full stop after each 'dim'; both scans)",
    r"\(\dim X-\dim Y\)",
    "punctuation", "high",
    fx(r"\(\dim X-\dim Y\)", r"\(\dim.X-\dim.Y\)"),
    "The stops of the abbreviation are dropped in the TeX.")
add(72, "after '... de degré dim.X - dim.Y.'",
    "'On définit également des homomorphismes :' is a new, indented paragraph (both scans)",
    r"'... \(\dim X-\dim Y\). On définit également ...' in one paragraph",
    "other", "high",
    fx(". On définit également", "." + NL + NL + "On définit également"),
    "Missing paragraph break. Does not overlap the dim. fix; the two apply in either order.")
add(72, "after the display f^! : K(X) -> K(Y) et f_! : K(Y) -> K(X).",
    "'Si F est un faisceau cohérent sur X, ...' begins an indented paragraph (both scans)",
    r"\] followed directly by 'Si \(\underline F\) est un faisceau cohérent' (continues the paragraph of the "
    "display)",
    "other", "high",
    fx(r"\]" + NL + r"Si \(\underline F\) est un faisceau", r"\]" + NL + NL + r"Si \(\underline F\) est un faisceau"),
    "Missing paragraph break.")

# ---------------- page 73 ----------------
add(73, "start of page",
    "p. 73 begins 'Si G est un faisceau cohérent sur Y, f_*(G) est cohérent sur X.' (indented); p. 72 ends "
    "'... c'est simplement l'opération d'image réciproque.' (both scans; witness pp. 83-84)",
    r"'Si \(G\) est un' is the last line of page_072.tex (under the folio-72 marker); page_073.tex begins "
    "'faisceau cohérent sur'",
    "marker", "high", None,
    r"Page 73 really begins with 'Si \(G\) est un'. Move the folio-73 marker up one line, above it: "
    r"python -I move_marker.py 6 73 'Si \(G\) est un' --before (single quotes; simulated on both layers with "
    r"crops_071_075/sim_markers.py, nothing written: '... d'image réciproque.' / blank line / marker / "
    r"'Si \(G\) est un' / 'faisceau cohérent sur \(Y\), ...').")
add(73, "label of the theorem",
    "THEOREME DE RIEMANN-ROCH. (typed capitals, not underlined; both scans)",
    r"\textbf{Théorème de Riemann--Roch.}",
    "word", "medium",
    fx(r"\textbf{Théorème de Riemann--Roch.}", r"\textbf{THÉORÈME DE RIEMANN--ROCH.}"),
    "Capitals against the TeX's small letters (the bold is accepted). Accents and the joint-name dash keep the "
    "TeX's forms (global rules). All labels of pp. 73-75 are typed in capitals: LEMME 1-4, COROLLAIRE.")
add(73, "formula (1)",
    "f_*(ch(y)T(Y)) = ch(f_!(y))T(X)  dans A(X) ⊗ Q . with 'dans' underlined (both scans)",
    r"\quad\text{dans } A(X)\otimes\mathbb Q.",
    "underline", "high",
    fx(r"\text{dans } A(X)", r"\text{\emph{dans} } A(X)"),
    r"The statement's word inside the display is underlined in the print and plain in the TeX (the file's "
    r"\emph, as in the statement).")
add(73, "label of Lemme 1",
    "LEMME 1. (typed capitals; both scans)",
    r"\textbf{Lemme 1.}",
    "word", "medium",
    fx(r"\textbf{Lemme 1.}", r"\textbf{LEMME 1.}"),
    "Capitals against small letters.")
add(73, "'moyennant la proposition 2.13 (\"décomposition cellulaire\") de R.R.R. On va donc'",
    "de R.R.R. On (both scans)",
    r"de \(\RRR\). On -- prints 'RRR.' (\RRR = \mathrm{RRR}, see p. 71)",
    "punctuation", "high",
    fx(r"de \(\RRR\). On va", "de R.R.R. On va"),
    "As on p. 71. The last stop of R.R.R. also ends the sentence.")
add(73, "the copyist's interpolation asterisks (pp. 71, 73, 75)",
    "The print raises the opening asterisk and lowers the closing one, as its own footnote shows "
    "('astériques ^* ... _*', p. 71): p. 73 '(^* application régulière _*)', '(^* abrégée _*)', "
    "'(^* En fait, ... est vrai pour f. _*)' and the lowered '_*' closing the Rappel after "
    "'R^p f_*(G).'; p. 75 '... et g^* . * Dans la formule (7), ... dans K(Y')._*]' (opening at normal height, "
    "closing lowered); p. 71 '* Rappel de notations' (normal height). Both scans.",
    r"every asterisk on the line: p. 71 footnote 'astériques *\dots* sont'; p. 73 '\).\quad*', "
    r"'(* application régulière *)', '(* abrégée *)', '(* En fait, ... *)'; p. 75 '{*}Dans la formule (7) ... "
    r"\(K(Y')\).{*}]'",
    "symbol", "medium", None,
    r"Convention of the transcription, reported once and not itemized. If the volume follows the print: raised "
    r"= \textsuperscript{*}, lowered = \textsubscript{*}, normal height = *; e.g. '(\textsuperscript{*} "
    r"application régulière \textsubscript{*})', footnote 'astériques \textsuperscript{*}\dots\textsubscript{*} "
    r"sont', p. 75 '* Dans la formule (7) ... \(K(Y')\).\textsubscript{*}]'.")

# ---------------- page 74 ----------------
add(74, "label of Lemme 2",
    "LEMME 2. (typed capitals; both scans)",
    r"\textbf{Lemme 2.}",
    "word", "medium",
    fx(r"\textbf{Lemme 2.}", r"\textbf{LEMME 2.}"),
    "Capitals against small letters.")
add(74, "formula (4)",
    "y = i^!(x) , avec x ∈ K(X) , with 'avec' underlined (both scans)",
    r"\text{avec }x\in K(X)",
    "underline", "high",
    fx(r"\text{avec }x", r"\text{\emph{avec} }x"),
    "The statement's word inside the display is underlined in the print, plain in the TeX.")
add(74, "label of the Corollaire",
    "COROLLAIRE. (typed capitals; both scans)",
    r"\textbf{Corollaire.}",
    "word", "medium",
    fx(r"\textbf{Corollaire.}", r"\textbf{COROLLAIRE.}"),
    "Capitals against small letters.")
add(74, "label of Lemme 3",
    "LEMME 3. (typed capitals; both scans)",
    r"\textbf{Lemme 3.}",
    "word", "medium",
    fx(r"\textbf{Lemme 3.}", r"\textbf{LEMME 3.}"),
    "Capitals against small letters.")
add(74, "Lemme 3: 'soit l'injection u -> (u,v_o) v_o ∈ P'",
    "u → (u,v_o): a plain arrow, no bar at its tail (both scans)",
    r"\(u\mapsto (u,v_0)\)",
    "symbol", "high",
    fx(r"u\mapsto", r"u\longrightarrow"),
    r"\mapsto is not in the print.")
add(74, "Lemme 3: '(u,v_o) v_o ∈ P. Alors'",
    "(u,v_o) v_o ∈ P. -- no comma between (u,v_o) and v_o (both scans)",
    r"\(u\mapsto (u,v_0)\), \(v_0\in P\)",
    "punctuation", "high",
    fx(r",v_0)\), \(v_0\in", r",v_0)\) \(v_0\in"),
    "Comma added by the TeX. Does not overlap the arrow fix.")
add(74, "diagram, bottom arrow Y' -> X'",
    "label j above the bottom arrow (both scans)",
    r"\arrow[r,\"j\"'] (the ' sets the label below the arrow)".replace('\\"', '"'),
    "formula", "medium",
    fx('\\arrow[r,"j"\']', '\\arrow[r,"j"]'),
    "Label on the wrong side of the arrow; the other three labels stand as printed (i above, g left, f right).")

# ---------------- page 75 ----------------
add(75, "label of Lemme 4",
    "LEMME 4. (typed capitals; both scans)",
    r"\textbf{Lemme 4.}",
    "word", "medium",
    fx(r"\textbf{Lemme 4.}", r"\textbf{LEMME 4.}"),
    "Capitals against small letters.")
add(75, "formula (8)",
    "f_*(1) = 1 , d'où f_*f^* = 1 . with 'd'où' underlined (both scans)",
    r"\text{d'où }f_*f^*=1.",
    "underline", "high",
    fx(r"\text{d'où }f_*f^*", r"\text{\emph{d'où} }f_*f^*"),
    "Underlined in the print, plain in the TeX.")
add(75, "formula (9)",
    "... mod.Ker f_*  pour tout α ∈ A(Y) . with 'pour tout' underlined (both scans)",
    r"\text{pour tout }\alpha\in A(Y).",
    "underline", "high",
    fx(r"\text{pour tout }\alpha", r"\text{\emph{pour tout} }\alpha"),
    "Underlined in the print, plain in the TeX.")
add(75, "after the formulas (6)-(9) and the footnote text",
    "'[Pour simplifier l'écriture, ...' begins an indented paragraph (both scans)",
    r"\end{align}, \footnotetext{...} and '[Pour simplifier' on the next line: the text continues the "
    "paragraph of the display",
    "other", "high",
    fx("VII 4.1.}" + NL + "[Pour", "VII 4.1.}" + NL + NL + "[Pour"),
    "Missing paragraph break.")
add(75, "after the display (6 bis)",
    "'La formule (7) résulte des formules' is a new, indented paragraph (both scans)",
    r"\end{equation} followed directly by 'La formule (7) résulte des formules'",
    "other", "high",
    fx(r"\end{equation}" + NL + "La formule (7)", r"\end{equation}" + NL + NL + "La formule (7)"),
    "Missing paragraph break ('La formule (6)' and 'La formule (8)' have theirs).")
add(75, "'elles-mêmes conséquences de Künneth'",
    "KÜnneth: the u-umlaut typed at capital height, the same form as on p. 70 ('la formule de KÜnneth'); both "
    "scans",
    "Künneth",
    "misprint_in_print", "low",
    fx("de Künneth et", "de KÜnneth et"),
    "If the capital Ü counts as a typing slip, the TeX silently corrects it and the diplomatic layer should read "
    "KÜnneth. It may instead be the typewriter's only form of ü (then one volume decision with p. 70, not a page "
    "fix).",
    corrected="Künneth")
add(75, "after 'avec ξ = C^1(L) ∈ A^1(Y').'",
    "'[En fait, (9) est très vraisemblablement une identité, ...]' is a new, indented paragraph (both scans)",
    r"'... \in A^1(Y')\). [En fait, ...' in one paragraph",
    "other", "high",
    fx(r"A^1(Y')\). [En fait", r"A^1(Y')\)." + NL + NL + "[En fait"),
    "Missing paragraph break.")

# ---------------- checks ----------------
ok = True
for d in F:
    f = d["fix"]
    if f is None:
        continue
    t = (B / f"page_{d['page']:03d}.tex").read_text(encoding="utf-8")
    n = t.count(f["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE", d["page"], n, repr(f["old"]))
    if "%%%%%%%%%%" in f["old"]:
        ok = False
        print("MARKER IN OLD", d["page"], repr(f["old"]))
# overlap check: apply all fixes of a page in sequence on a copy
for p in sorted({d["page"] for d in F}):
    t = (B / f"page_{p:03d}.tex").read_text(encoding="utf-8")
    for d in F:
        if d["page"] == p and d["fix"]:
            if t.count(d["fix"]["old"]) != 1:
                ok = False
                print("FAILS AFTER EARLIER FIXES", p, repr(d["fix"]["old"]))
            t = t.replace(d["fix"]["old"], d["fix"]["new"], 1)
out = RUN / "findings_071_075.json"
out.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
from collections import Counter
c = Counter((d["page"], d["kind"] == "misprint_in_print") for d in F)
for p in sorted({d["page"] for d in F}):
    print(p, c[(p, False)], "/", c[(p, True)])
print("all fixes unique and non-overlapping:", ok, "| written", out, len(F), "findings")
