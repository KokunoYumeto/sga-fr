import json
import pathlib

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
B = RUN / "b081_085"
OUT = RUN / "findings_081_085.json"

DASH_NOTE = ("The typescript has only the hyphen key (the same glyph as in s'avère-t-il); the TeX adds an en dash. "
             "One decision with the joint-name dash may cover it (main.tex has 5 '~--' and 18 ' -- ').")

F = []


def add(page, where, scan, tex, kind, confidence, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": confidence,
         "fix": None if old is None else {"old": old, "new": new}}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---- p. 81
add(81, "1st paragraph, 'Aussi s'avère-t-il commode - et utile'",
    "commode - et utile (typewriter hyphen, spaced, as dash)", r"commode~-- et utile",
    "punctuation", "medium", r"commode~-- et", r"commode~- et", DASH_NOTE)
add(81, "same sentence, 'notamment dans l'Exp. II - d'axiomatiser'",
    "l'Exp. II - d'axiomatiser (typewriter hyphen)", r"l'Exp.\ II~-- d'axiomatiser",
    "punctuation", "medium", r"II~-- d'axiomatiser", r"II~- d'axiomatiser", DASH_NOTE)

# ---- p. 82
add(82, "line 1, 'sont donnés dans l'Exp. II. On montre en particulier'",
    "the line runs on: 'sont donnés dans l'Exp. II. On montre en particulier qu'il existe des résolu-'",
    r"blank line (new paragraph) after 'sont donnés dans l'Exp.\ II.'",
    "other", "high", r"dans l'Exp.\ II." + "\n\n" + "On montre", r"dans l'Exp.\ II. On montre",
    "The transcription adds a paragraph break that the print does not have (the typescript indents its paragraphs).")
add(82, "'A titre d'illustration - et pour mettre en évidence'",
    "illustration - et pour (typewriter hyphen)", r"illustration~-- et pour",
    "punctuation", "medium", r"illustration~-- et", r"illustration~- et", DASH_NOTE)
add(82, "'des notions introduites - on donne en appendice'",
    "introduites - on donne (typewriter hyphen)", r"introduites~-- on donne",
    "punctuation", "medium", r"introduites~-- on", r"introduites~- on", DASH_NOTE)

# ---- p. 83
add(83, "lines 2-3, 'p^{-1}(O_S)). Le théorème central'",
    "the line runs on: '... d'anneaux p^{-1}(O_S)). Le' / 'théorème central de l'Exp. III ...'",
    r"blank line (new paragraph) before 'Le théorème central'",
    "other", "high", r"(\mathcal O_S)\))." + "\n\n" + "Le théorème", r"(\mathcal O_S)\)). Le théorème",
    "The transcription adds a paragraph break that the print does not have.")
add(83, "'le foncteur Rf_* transforme complexes pseudo-cohérents'",
    "double-struck R: ℝf_* (doubled stem, both scans)", r"\(Rf_*\)",
    "font", "high", r"\(Rf_*\)", r"\(\mathbb{R}f_*\)",
    "The print's derived-functor R is double-struck here; Exposé I's TeX writes it plain throughout "
    r"(\RHom = \mathrm R\!\Hom; the print has ℝHom on p. 116). See the message.")
add(83, "'a) S est localement noethérien' / 'b) f est projectif'",
    "a) and b) set on two lines; no punctuation after 'noethérien' (both scans)",
    r"a)~\(S\) est localement noethérien; b)~\(f\) est projectif;",
    "punctuation", "high", r"noethérien; b)", r"noethérien b)",
    "The TeX adds a semicolon to join the print's two-line list.")

# ---- p. 84
add(84, "1.1.1, last sentence, 'S-catégorie abe-/lienne plate'",
    "abe-/lienne without accent on the e (both scans; the OCR also reads 'abelienne')",
    r"abélienne \emph{plate}",
    "misprint_in_print", "high", r"abélienne \emph{plate}", r"abelienne \emph{plate}",
    "Missing accent in the print; the TeX silently corrects it.", corrected=r"abélienne \emph{plate}")
add(84, "1.1.2, '(SGA 1 VI 7,1)'",
    "7,1 with a comma (tail below the line in both scans; '6.1' in 1.1.1 has a round full stop)",
    r"(SGA 1 VI 7.1)",
    "misprint_in_print", "high", r"VI 7.1)", r"VI 7,1)",
    "The typist's comma for the full stop; the TeX silently corrects it.", corrected=r"VI 7.1)")
add(84, "1.1.3, 'S-foncteur additif (resp. exact)'",
    "only 'exact' is underlined, not 'resp.' (both scans)", r"(\emph{resp.\ exact})",
    "underline", "high", r"(\emph{resp.\ exact})", r"(resp.\ \emph{exact})", "")
add(84, "pp. 84-85 throughout: the base category / site S",
    "S underlined (S̲) everywhere it names the base category or site: 14 times on p. 84, 20 on p. 85",
    r"plain S: p. 84 'Soit \(S\) une catégorie', '\(f:X\to Y\) de \(S\)'; p. 85 'Soient \(S\) un site', "
    r"'de \(S_{/X}\)', '\(X\in\Ob S\)'",
    "underline", "high", None, None,
    "Convention of the transcription, not a page fix: the print's underline marks categories (S̲, C̲, O̲); the TeX "
    r"writes C̲ as \mathcal C and O̲ as \mathcal O but drops the underline of S̲ (main.tex has \underline S only "
    "in the index of notations). The print has S̲ elsewhere in Exposé I too (p. 116 '(S̲,A)'). One decision for "
    "the exposé.")

# ---- p. 85
add(85, "footnote (2), 'si a ∈ ob D(C_Y)(resp. Fl D(C_Y))'",
    "between F and D a short slanted stroke with a foot, squeezed in after typing (no type cell of its own; "
    "both scans): read 'Fl' (arrows), as the exposé types 'u ∈ Fl(S̲)' on p. 142",
    r"\(F/\Dpx(\mathcal C_Y)\)",
    "symbol", "medium", r"\(F/\Dpx(\mathcal C_Y)\)", r"\(\mathrm{Fl}\,\Dpx(\mathcal C_Y)\)",
    "'F/D(C_Y)' has no meaning here; the footnote covers an object (resp. an arrow) a of D(C_Y). "
    r"\mathrm{Fl} is the file's own form (p. 142). If the stroke is read as a typed slash, the print has a "
    "misprint and the corrected layer needs the same change.")
add(85, "1.2, 2nd paragraph, 'avec E ∈ ob C_oU est un crible'",
    "subscript 'oU' without a comma (both scans)", r"\mathcal C_{0,U}",
    "punctuation", "high", r"\mathcal C_{0,U}", r"\mathcal C_{0U}",
    "The TeX adds a comma between the two indices.")

# ---- checks
ok = True
for d in F:
    t = (B / f"page_{d['page']:03d}.tex").read_text(encoding="utf-8")
    if d["fix"] is not None:
        n = t.count(d["fix"]["old"])
        if n != 1:
            ok = False
            print("NOT UNIQUE", d["page"], repr(d["fix"]["old"]), n)
        if "%%%%%%%%%%" in d["fix"]["old"]:
            ok = False
            print("MARKER IN OLD", d["page"])
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
from collections import Counter
c = Counter((d["page"], d["kind"] == "misprint_in_print") for d in F)
for p in range(81, 86):
    print(p, c[(p, False)], "/", c[(p, True)])
print("all olds unique:", ok, "findings:", len(F))
