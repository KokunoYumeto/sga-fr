"""Build findings_136_140.json and check every fix: sequentially on the page files (old must occur exactly once
at its turn), and on the page spans of main.tex in both layers (as process_sga.py applies them; misprint fixes are
not replayed on the corrected layer). Also simulates the two marker moves on in-memory copies. Writes only the JSON.
usage: python -I make_findings.py"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).parent
RUN = HERE.parent
W = RUN.parent
sys.path.insert(0, str(W))
from sga_config import MARK  # noqa: E402

OUT = RUN / "findings_136_140.json"
PAGES = RUN / "b136_140"

F = []


def add(page, where, scan, tex, kind, conf, old=None, new=None, note="", corrected=None):
    x = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, confidence=conf,
             fix=None if old is None else dict(old=old, new=new))
    if corrected is not None:
        x["corrected"] = corrected
    x["note"] = note
    F.append(x)


# ---------------------------------------------------------------- p. 136
add(136, "Lemme 5.8.3, first line of the statement",
    "underlined by word groups: 'Soit', 'un', 'Module à gauche', 'Conditions équivalentes'; E, 'A-', the full stop "
    "and the colon not (both scans)",
    r"Soit \(E\) un \(A\)-Module à gauche. Conditions équivalentes : (roman, no emphasis)",
    "underline", "high",
    r"Soit \(E\) un \(A\)-Module à gauche. Conditions équivalentes :",
    r"\emph{Soit \(E\) un \(A\)-Module à gauche. Conditions équivalentes} :",
    "The statement is in roman in the TeX, as Corollaire 1.4.5 and 2.4-2.7 (pp. 93-100, fixed singly). The formulas "
    "inside the emphasis are left to the volume decision on block underlines.")
add(136, "Lemme 5.8.3, items (i) and (ii)",
    "(i) 'est localement facteur direct d'un Module libre de type fini', (ii) 'est plat et de présentation finie' "
    "underlined; E and the final ; and . not (both scans)",
    r"\item \(E\) est localement ... fini; / \item \(E\) est plat et de présentation finie. (roman)",
    "underline", "high",
    r"\item \(E\) est localement facteur direct d'un Module libre de type fini;" + "\n"
    + r"\item \(E\) est plat et de présentation finie.",
    r"\item \(E\) \emph{est localement facteur direct d'un Module libre de type fini};" + "\n"
    + r"\item \(E\) \emph{est plat et de présentation finie}.",
    "Rest of the statement of the entry above.")
add(136, "proof of 5.8.3, 'le foncteur Hom_A(E,.) est exact'",
    "Hom underlined (the Module Hom; both scans)",
    r"\(\Hom_A(E,\cdot)\) (\Hom = \operatorname{Hom}, plain)",
    "underline", "high",
    r"foncteur \(\Hom_A(E",
    r"foncteur \(\underline{\Hom}_A(E",
    r"All ten Hom of this page are underlined in the print; the TeX writes plain \Hom (main.tex line 2847). The "
    r"lemma cited in this sentence, (1.3.1), is written \underline{\Hom}(P,.) in main.tex (line 1939), as are "
    r"Notation 4.5 and its formulas. See the message.")
add(136, "same formula, 'Hom_A(E,.)'",
    "a typed full stop on the baseline (both scans)",
    r"(E,\cdot)",
    "symbol", "low",
    r"(E,\cdot)",
    r"(E,.)",
    r"As (P,\cdot) -> (P,.) on p. 89 (findings_086_090, applied: main.tex line 1939). Independent of the "
    r"underline entry before it.")
add(136, "display after 'On doit montrer que la suite'",
    "Hom_A(E,F) -> Hom_A(E,F\") -> 0 with both Hom underlined (both scans)",
    r"\Hom_A(E,F)\longrightarrow \Hom_A(E,F'')\longrightarrow 0",
    "underline", "high",
    r"\Hom_A(E,F)\longrightarrow \Hom_A(E,F'')",
    r"\underline{\Hom}_A(E,F)\longrightarrow \underline{\Hom}_A(E,F'')",
    "As the entry above.")
add(136, "'la suite déduite par application du foncteur Hom(.,I)'",
    "Hom underlined (both scans)",
    r"\(\Hom_{\mathbb Z_S}(\cdot,I)\)",
    "underline", "high",
    r"foncteur \(\Hom_{\mathbb Z_S}",
    r"foncteur \(\underline{\Hom}_{\mathbb Z_S}",
    "As above. Apply before the misprint entry for the same formula (its old is the text this entry and the next "
    "one leave).")
add(136, "same formula, '(.,I)'",
    "a typed full stop on the baseline (both scans)",
    r"(\cdot,I)",
    "symbol", "low",
    r"(\cdot,I)",
    r"(.,I)",
    r"As (E,\cdot) above. Apply before the misprint entry that follows.")
add(136, "same formula, the index of Hom",
    "Hom_Z(.,I): the index is a double-struck Z alone, no S (both scans; crops_136_140/p136_homZ.png, "
    "w136_homZ.png)",
    r"\Hom_{\mathbb Z_S}(\cdot,I) (silently corrected)",
    "misprint_in_print", "medium",
    r"\underline{\Hom}_{\mathbb Z_S}(.,I)",
    r"\underline{\Hom}_{\mathbb Z}(.,I)",
    r"The functor is the Hom of Z_S-Modules into the Z_S-Module injectif I of the same sentence; the diagram below "
    r"has Hom_{Z_S} four times. The typist left out the index S; the TeX silently supplies it. The old is the text "
    r"left by the two entries before this one (apply in JSON order); the edit removes only the S.",
    corrected=r"\underline{\Hom}_{\mathbb Z_S}(.,I)")
add(136, "diagram (3.17.1), upper row",
    "Hom_{Z_S}(F\",I) (x)_A E -> Hom_{Z_S}(F,I) (x)_A E, both Hom underlined (both scans)",
    r"0&\to&\Hom_{\mathbb Z_S}(F'',I)\otimes_A E&\to&\Hom_{\mathbb Z_S}(F,I)\otimes_A E",
    "underline", "high",
    r"0&\to&\Hom_{\mathbb Z_S}(F'',I)\otimes_A E&\to&\Hom_{\mathbb Z_S}(F,I)\otimes_A E",
    r"0&\to&\underline{\Hom}_{\mathbb Z_S}(F'',I)\otimes_A E&\to&\underline{\Hom}_{\mathbb Z_S}(F,I)\otimes_A E",
    "As above.")
add(136, "diagram (3.17.1), lower row",
    "Hom_{Z_S}(Hom_A(E,F\"),I) -> Hom_{Z_S}(Hom_A(E,F),I) . with all four Hom underlined (both scans)",
    r"0&\to&\Hom_{\mathbb Z_S}(\Hom_A(E,F''),I)&\to&\Hom_{\mathbb Z_S}(\Hom_A(E,F),I).",
    "underline", "high",
    r"0&\to&\Hom_{\mathbb Z_S}(\Hom_A(E,F''),I)&\to&\Hom_{\mathbb Z_S}(\Hom_A(E,F),I).",
    r"0&\to&\underline{\Hom}_{\mathbb Z_S}(\underline{\Hom}_A(E,F''),I)&\to&"
    r"\underline{\Hom}_{\mathbb Z_S}(\underline{\Hom}_A(E,F),I).",
    "As above.")
add(136, "'Preuve de (5.8).'",
    "only 'Preuve de' underlined; '(5.8).' not (both scans; crops_136_140/w136_preuvede.png)",
    r"\emph{Preuve de (5.8).}",
    "underline", "high",
    r"\emph{Preuve de (5.8).}",
    r"\emph{Preuve de} (5.8).",
    "The emphasis covers the reference and the full stop, which the print leaves plain.")

# ---------------------------------------------------------------- p. 137
add(137, "start of the page",
    "p. 137 begins 'flèche de troncature' (both scans; OCR page_137.txt agrees); p. 136 ends '... en degré < m, la'",
    r"page_136.tex ends '... acyclique en degré \(<m\), la flèche de'; the folio-137 marker stands before "
    r"'troncature'",
    "marker", "high", None, None,
    "Page 137 really begins with 'flèche de'. Move the marker up: python -I move_marker.py 6 137 'flèche de' "
    "--before (simulated on both layers: '... en degré \\(<m\\), la' / marker / 'flèche de' / 'troncature').")
add(137, "diagram of the truncation, upper row",
    "the row begins with an arrow: '-> E^{m-1} -> E^m -> E^{m+1} -> ...', no dots before it (both scans)",
    r"\cdots&\to&E^{m-1}&\to&E^m&\to&E^{m+1}\to\cdots\\",
    "extra", "high",
    r"\cdots&\to&E^{m-1}",
    r"&\to&E^{m-1}",
    "The TeX adds leading dots that the print does not have. Independent of the entry for the final dots.")
add(137, "diagram of the truncation, lower row",
    "the row begins with an arrow: '-> 0 -> E^m/B^m -> E^{m+1} -> ...', no dots before it (both scans)",
    r"\cdots&\to&0&\to&E^m/B^m&\to&E^{m+1}\to\cdots",
    "extra", "high",
    r"\cdots&\to&0",
    r"&\to&0",
    "As the upper row.")
add(137, "diagram of the truncation, end of the upper row",
    "three typed full stops on the baseline after the last arrow (both scans)",
    r"E^{m+1}\to\cdots\\",
    "symbol", "medium",
    r"E^{m+1}\to\cdots\\",
    r"E^{m+1}\to\ldots\\",
    r"\cdots sets the dots at mid-height (same kind of fix as pp. 49, 79, 80, 86, 95).")
add(137, "diagram of the truncation, end of the lower row",
    "three typed full stops on the baseline after the last arrow (both scans)",
    r"E^{m+1}\to\cdots",
    "symbol", "medium",
    r"E^{m+1}\to\cdots" + "\n" + r"\end{array}",
    r"E^{m+1}\to\ldots" + "\n" + r"\end{array}",
    "As the upper row.")
add(137, "distinguished triangle E\" -> E' -> E'^m[-m]",
    "a comma to the right of the triangle, on the line of E\" -> E' (both scans)",
    "tikzcd without punctuation",
    "punctuation", "high",
    r"E' \arrow[ul]" + "\n" + r"\end{tikzcd}",
    r"E' \arrow[ul] & ," + "\n" + r"\end{tikzcd}",
    "Set in a cell of its own, as the full stop after the triangle on p. 99 (findings_096_100).")
add(137, "'donc que l'on a parf.amp(E) ⊂ [m,n]'",
    "parf.amp(E) (both scans; crops_136_140/p137_parfamp.png)",
    r"\perfamp(E), which prints perf.amp (\providecommand{\perfamp}{\operatorname{perf.amp}}, main.tex line 2852)",
    "word", "high",
    r"\perfamp(E)",
    r"\operatorname{parf.amp}(E)",
    r"The print types parf.amp throughout Exposé I (also p. 128 on the witness; the OCR of pp. 121-149 reads "
    r"parf.amp), and parf.dim where \perfdim (line 2853) prints perf.dim. Changing the two definitions repairs all "
    r"16 \perfamp and 4 \perfdim; with that change this page edit is unnecessary but harmless "
    r"(\operatorname{parf.amp} is the file's own form, line 4360).")
add(137, "Remarques 5.8.4 b), 'Notons D(_AS)_parf'",
    "the index 'parf' underlined (both scans)",
    r"\Dpx({}_A S)_{\mathrm{parf}}",
    "underline", "high",
    r"Notons \(\Dpx({}_A S)_{\mathrm{parf}}\)",
    r"Notons \(\Dpx({}_A S)_{\underline{\mathrm{parf}}}\)",
    "The underlined index is the notation defined here (complexes parfaits et de tor-dimension finie), distinct "
    "from the plain parf of D^b(_AX)_parf (5.10, p. 138, not underlined); the volume's index of notations writes "
    r"the same distinction as \Dcat(f)_{\underline{\parf}} (III 4.2).")
add(137, "display after 'induit un foncteur'",
    "D(S)_parf with the index 'parf' underlined; 'coh' not (both scans)",
    r"\Dpx(S)_{\mathrm{parf}}\times_S \Dpx^b(S)_{\mathrm{coh}}",
    "underline", "high",
    r"\Dpx(S)_{\mathrm{parf}}\times_S",
    r"\Dpx(S)_{\underline{\mathrm{parf}}}\times_S",
    "As the entry above.")
add(137, "the site S, pp. 137-139",
    "S underlined (S̲) wherever it names the site: p. 137 'D(_AS̲)', 'si S̲ est de type fini', 'sous-S̲-catégorie', "
    "'D(S̲)_parf x_S̲ D^b(S̲)_coh'; p. 138 'S̲ = (Ens)', 'où S est l'objet final de S̲' (the object S plain), "
    "'S̲_/X'; p. 139 'objet s-ponctué U de S̲', '(S̲,A)' (both scans)",
    r"plain \(S\): 'C'est cependant le cas si \(S\) est de type fini' (p. 137), 'où \(S\) est l'objet final de "
    r"\(S\)' (p. 138), '\((S,A)\) est défini' (p. 139)",
    "underline", "high", None, None,
    "Convention of the transcription, reported for pp. 84-100 (findings_081_085 to 096_100): one decision for the "
    "exposé, not itemized.")

# ---------------------------------------------------------------- p. 138
add(138, "Corollaire 5.9, statement before the display",
    "underlined by word groups from 'Supposons que' to 'voir', then 'et' and 'Alors on a'; the references "
    "'(MULT VI 2.6)' and '(EGA O_IV 17.2.8)).' are not underlined (both scans)",
    "no emphasis: the statement is in roman",
    "underline", "high",
    r"Supposons que \(S=(\mathrm{Ens})\) (donc \(A\) «~est~» un anneau ordinaire) et que tout \(A\)-module à gauche "
    r"soit de tor-dimension finie (c'est le cas par exemple si \(A\) est de dimension cohomologique globale finie, "
    r"voir (MULT VI 2.6) et (EGA \(0_{\mathrm{IV}}\) 17.2.8)). Alors on a",
    r"\emph{Supposons que \(S=(\mathrm{Ens})\) (donc \(A\) «~est~» un anneau ordinaire) et que tout \(A\)-module "
    r"à gauche soit de tor-dimension finie (c'est le cas par exemple si \(A\) est de dimension cohomologique "
    r"globale finie, voir} (MULT VI 2.6) \emph{et} (EGA \(0_{\mathrm{IV}}\) 17.2.8)). \emph{Alors on a}",
    "One edit, so that the braces stay balanced; the references stay in roman as the print has them.")
add(138, "Corollaire 5.9 (i)",
    "', et' after (i) with 'et' underlined (both scans)",
    r"\quad\text{et}",
    "underline", "high",
    r"\text{et}",
    r"\text{\emph{et}}",
    "The statement's word inside the display (as pp. 73-74).")
add(138, "Corollaire 5.9 (ii)",
    "D(_AS)_parf with the index 'parf' underlined (both scans; crops_136_140/w138_i_ii.png); 'torf' and 'coh' not",
    r"\Dpx({}_A S)_{\mathrm{parf}}",
    "underline", "high",
    r"=\Dpx({}_A S)_{\mathrm{parf}}",
    r"=\Dpx({}_A S)_{\underline{\mathrm{parf}}}",
    "The notation of 5.8.4 b) (p. 137): perfect and of finite tor-dimension, as the paraphrase 'Autrement dit' says.")
add(138, "Corollaire 5.9, 'Autrement dit ...'",
    "underlined by word groups from 'Autrement dit' to 'pseudo-cohérent)'; the final full stop not (both scans)",
    "no emphasis",
    "underline", "high",
    r"Autrement dit, pour que \(E\in\Ob\Dpx({}_A S)\) soit de tor-dimension finie (resp. de tor-dimension finie et "
    r"parfait) il faut et il suffit que \(E\) soit à cohomologie bornée (resp. à cohomologie bornée et "
    r"pseudo-cohérent).",
    r"\emph{Autrement dit, pour que \(E\in\Ob\Dpx({}_A S)\) soit de tor-dimension finie (resp. de tor-dimension "
    r"finie et parfait) il faut et il suffit que \(E\) soit à cohomologie bornée (resp. à cohomologie bornée et "
    r"pseudo-cohérent)}.",
    "End of the statement of Corollaire 5.9.")
add(138, "'Preuve.' (p. 138; p. 139 twice)",
    "only the word underlined, the full stop after the underline (both scans; crops_136_140/w138_preuve.png)",
    r"\emph{Preuve.} (stop inside the emphasis)",
    "underline", "medium", None, None,
    r"Convention: main.tex has \emph{Preuve.} 132 times; p. 90 reported \emph{Démonstration.} the same way "
    r"(findings_086_090). A scripted pass \emph{Preuve.} -> \emph{Preuve}. would follow the print here. Not "
    r"itemized.")
add(138, "label of Corollaire 5.10",
    "'Corollaire 5.10' with no full stop after the number (both scans; crops_136_140/p138_cor510.png, "
    "w138_cor510.png)",
    r"\textbf{Corollaire 5.10.}",
    "punctuation", "high",
    r"\textbf{Corollaire 5.10.}",
    r"\textbf{Corollaire 5.10}",
    "The TeX adds the full stop (5.9, 5.10.1 and 5.11 have theirs in the print).")
add(138, "Corollaire 5.10, statement",
    "underlined by word groups: 'Soit', S̲, 'Supposons que', 'ait assez de points', then 'et que', 'pour tout point', "
    "'de', 'tout', 'module à gauche soit de tor-dimension finie', 'Alors on a'; the reference '(SGA 4 IV 6.4.1.)' "
    "is not (both scans)",
    "no emphasis: the statement is in roman",
    "underline", "high",
    r"Soit \(X\in\Ob S\). Supposons que \(S_{/X}\) ait assez de points (SGA 4 IV 6.4.1.) et que, pour tout point "
    r"\(s\) de \(S_{/X}\), tout \(A_s\)-module à gauche soit de tor-dimension finie. Alors on a",
    r"\emph{Soit \(X\in\Ob S\). Supposons que \(S_{/X}\) ait assez de points} (SGA 4 IV 6.4.1.) \emph{et que, pour "
    r"tout point \(s\) de \(S_{/X}\), tout \(A_s\)-module à gauche soit de tor-dimension finie. Alors on a}",
    "One edit (balanced braces). Independent of the label entry. The display after it is not underlined, and the "
    "sentence 'Autrement dit ...' at the top of p. 139 is not underlined either (as the TeX).")

# ---------------------------------------------------------------- p. 140
add(140, "Définition 6.1, statement before the diagram",
    "underlined by word groups: 'Soient', 'une catégorie additive (resp. triangulée)', 'et', 'un groupe abélien', "
    "'On dit qu'une fonction f', 'est une', then 'si pour tous', 'tels que l'on ait', '(resp. un triangle "
    "distingué'; the defined term 'fonction additive de C dans F' is not underlined (both scans; "
    "crops_136_140/w140_def61.png)",
    "no emphasis: the definition is in roman",
    "underline", "high",
    r"Soient \(\mathcal C\) une catégorie additive (resp. triangulée) et \(F\) un groupe abélien. On dit qu'une "
    r"fonction \(f:\Ob(\mathcal C)\longrightarrow F\) est une fonction additive de \(\mathcal C\) dans \(F\) si pour "
    r"tous \(L,L',L''\in\Ob(\mathcal C)\) tels que l'on ait \(L\simeq L'+L''\) (resp. un triangle distingué",
    r"\emph{Soient \(\mathcal C\) une catégorie additive (resp. triangulée) et \(F\) un groupe abélien. On dit "
    r"qu'une fonction \(f:\Ob(\mathcal C)\longrightarrow F\) est une} fonction additive de \(\mathcal C\) dans \(F\) "
    r"\emph{si pour tous \(L,L',L''\in\Ob(\mathcal C)\) tels que l'on ait \(L\simeq L'+L''\) (resp. un triangle "
    r"distingué}",
    "As Définitions 1.4.3 and 2.1 (pp. 93, 95): the defined term stays out of the underline. One edit (balanced "
    "braces).")
add(140, "Définition 6.1, after the diagram",
    "'on a' underlined; 'f(L) = f(L') + f(L\")' and the full stop not (both scans)",
    "no emphasis",
    "underline", "high",
    r") on a \(f(L)=f(L')+f(L'')\).",
    r") \emph{on a} \(f(L)=f(L')+f(L'')\).",
    "")
add(140, "'Les fonctions additives de C dans F forment ...'",
    "underlined by word groups: 'Les fonctions additives de', 'dans', 'forment un groupe abélien,', 'noté'; "
    "'Add(C,F).' not (both scans)",
    "no emphasis",
    "underline", "high",
    r"Les fonctions additives de \(\mathcal C\) dans \(F\) forment un groupe abélien, noté \(\Add(\mathcal C,F)\).",
    r"\emph{Les fonctions additives de \(\mathcal C\) dans \(F\) forment un groupe abélien, noté} "
    r"\(\Add(\mathcal C,F)\).",
    "Last sentence of the definition; the notation Add(C,F) stays in roman as printed.")
add(140, "the category letter C of §6",
    "a plain typed C, neither underlined nor double-struck: 'Soient C une catégorie additive', 'ob(C)', "
    "'Add(C,F)' (both scans; also p. 141 '6.2. Soient C une catégorie triangulée' on the witness)",
    r"\mathcal C (6 times on p. 140)",
    "font", "high", None, None,
    "Pending volume decision on the category letter (NOTE_6), not itemized: in §6 the category is an arbitrary "
    "additive or triangulated category, not an S-category, and the typist leaves it plain.")
add(140, "end of the page",
    "p. 140 ends with 'noté Add(C,F).'; the paragraph number '6.2.' is the first line of p. 141 (both scans; "
    "witness p. 141)",
    r"page_140.tex ends with '\textbf{6.2.}'; the folio-141 marker stands after it",
    "marker", "high", None, None,
    "Page 141 really begins with '6.2.' (a heading at the top of a page, which the script did not move). Move the "
    "folio-141 marker up: python -I move_marker.py 6 141 '\\textbf{6.2.}' --before (simulated on both layers: "
    "'... \\(\\Add(\\mathcal C,F)\\).' / blank line / marker / '\\textbf{6.2.}' / 'Soient ...').")


# ---------------------------------------------------------------- checks
def page_spans(t):
    ms = list(MARK.finditer(t))
    out = {}
    for i, m in enumerate(ms):
        end = ms[i + 1].start() if i + 1 < len(ms) else len(t)
        out.setdefault(int(m.group(2)), (m.start(), end))
    return out


def apply_seq(texts, layer, skip_misprints):
    """texts: dict name->text; layer 'page' uses page files, else main.tex spans."""
    ok = True
    for x in F:
        fx = x["fix"]
        if not fx:
            continue
        if skip_misprints and x["kind"] == "misprint_in_print":
            continue
        p = x["page"]
        old, new = fx["old"], fx["new"]
        if MARK.search(old) or MARK.search(new):
            print("touches marker", p, old[:40]); ok = False
        if layer == "page":
            t = texts[p]
            n = t.count(old)
            if n != 1:
                print(f"[page] p{p}: old occurs {n} times: {old[:60]!r}"); ok = False
                continue
            texts[p] = t.replace(old, new, 1)
        else:
            t = texts["main"]
            s, e = page_spans(t)[p]
            seg = t[s:e]
            n = seg.count(old)
            if n != 1:
                print(f"[{layer}] p{p}: old occurs {n} times: {old[:60]!r}"); ok = False
                continue
            k = s + seg.find(old)
            texts["main"] = t[:k] + new + t[k + len(old):]
    return ok


def braces_ok(s):
    s = s.replace("\\{", "").replace("\\}", "")
    d = 0
    for ch in s:
        d += ch == "{"
        d -= ch == "}"
        if d < 0:
            return False
    return d == 0


pages_txt = {p: (PAGES / f"page_{p}.tex").read_text(encoding="utf-8") for p in range(136, 141)}
orig = dict(pages_txt)
ok = apply_seq(pages_txt, "page", False)
for p in range(136, 141):
    body = pages_txt[p]
    if not braces_ok(body):
        print("unbalanced braces after fixes on page", p); ok = False
for edition, skip in (("diplomatic", False), ("current", True)):
    t = (W / "sga6" / edition / "main.tex").read_text(encoding="utf-8")
    texts = {"main": t}
    ok &= apply_seq(texts, edition, skip)


def move_marker(t, folio, anchor, before):
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    j = t2.find(line)
    return t2[j - 120:j + len(line) + 60]


for edition in ("diplomatic", "current"):
    t = (W / "sga6" / edition / "main.tex").read_text(encoding="utf-8")
    print(f"--- {edition} 137:", repr(move_marker(t, 137, "flèche de", True)))
    print(f"--- {edition} 141:", repr(move_marker(t, 141, r"\textbf{6.2.}", True)))

if ok:
    OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")
    print("wrote", OUT, len(F), "findings")
    for p in range(136, 141):
        n = sum(1 for x in F if x["page"] == p and x["kind"] != "misprint_in_print")
        m = sum(1 for x in F if x["page"] == p and x["kind"] == "misprint_in_print")
        print(p, f"{n}/{m}")
else:
    print("NOT WRITTEN: fix the errors above")
