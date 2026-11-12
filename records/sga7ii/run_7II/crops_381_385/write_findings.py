import json, io
out = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II\findings_381_385_recheck.json"
BS = chr(92)
def L(s):
    # '@' stands for one backslash in the LaTeX strings below
    return s.replace("@", BS)
F = []
F.append({
 "page": 383,
 "where": "first line, before Théorème 4.2",
 "scan": "on trouve de meme .",
 "tex": "on trouve de meme .",
 "kind": "misprint_in_print",
 "confidence": "high",
 "fix": None,
 "corrected": "de même",
 "note": "The typescript omits the circumflex (p. 385 prints 'De même' with it). The TeX keeps the printed reading."
})
F.append({
 "page": 384,
 "where": "5.0, second line",
 "scan": "d'un corps de nombresen une place",
 "tex": "d'un corps de nombresen une place",
 "kind": "misprint_in_print",
 "confidence": "high",
 "fix": None,
 "corrected": "nombres en",
 "note": "Missing word space: measured on the scan, the e of 'en' follows the s at the typewriter's normal letter pitch (about 20 px), with no space cell. The TeX keeps the printed reading."
})
F.append({
 "page": 384,
 "where": "paragraph 'Soient k un corps fini à q' éléments', second line",
 "scan": "𝔊 = 𝔊al(k̄/k): the G of 'Gal' is the same hand-drawn Fraktur G as the group symbol before the equals sign",
 "tex": L("@mathfrak{G} = @operatorname{Gal}(@bar{k}/k)"),
 "kind": "font",
 "confidence": "high",
 "fix": {"old": L("@operatorname{Gal}(@bar{k}/k)"), "new": L("@mathfrak{G}@mathrm{al}(@bar{k}/k)")},
 "note": "Checked at 4x: both G's are the hand-drawn Fraktur letter with a descending tail; 'Galois' on the same line is typed roman. This is the case held for one volume decision in GLOBAL_ISSUES_SGA item 61 (pp. 384, 389); apply if the diplomatic layer reproduces the typist's glyphs."
})
F.append({
 "page": 384,
 "where": "Définition 5.1, first line",
 "scan": "Un E-faisceau constructible: 'Un' and 'faisceau constructible' underlined, 'E-' not",
 "tex": L("@underline{Un E-faisceau constructible}"),
 "kind": "underline",
 "confidence": "high",
 "fix": {"old": L("@underline{Un E-faisceau"), "new": L("@underline{Un} E-@underline{faisceau")},
 "note": "The TeX takes the letter E into the underline; the print underlines only the words (the same form was fixed on p. 388)."
})
F.append({
 "page": 384,
 "where": "Définition 5.1, second line",
 "scan": "est dit T-entier si, pour tout point géométrique: 'est dit' and 'entier si' underlined, 'T-' not",
 "tex": L("@underline{est dit T-entier si, pour tout point géométrique}"),
 "kind": "underline",
 "confidence": "high",
 "fix": {"old": L("@underline{est dit T-entier"), "new": L("@underline{est dit} T-@underline{entier")},
 "note": "Only the letter T is taken out of the underline; the restart of the underline after the comma is left to the global pass."
})
F.append({
 "page": 384,
 "where": "Définition 5.1, last line",
 "scan": "est un automorphisme T-entier de G̲_x̄ . : 'est un automorphisme' and 'entier de' underlined, 'T-' not; the G of G_x̄ has its own short underline",
 "tex": L("@underline{est un automorphisme T-entier de} $G_{@bar{x}}$"),
 "kind": "underline",
 "confidence": "high",
 "fix": {"old": L("@underline{est un automorphisme T-entier de} $G_{@bar{x}}$"), "new": L("@underline{est un automorphisme} T-@underline{entier de} $@underline{G}_{@bar{x}}$")},
 "note": "Two underline differences in one edit: the T stands outside the print's underline, and the sheaf letter of the fibre is underlined (checked at 6x: a separate underline under the G, after the underline of 'entier de' stops). The G of 'la fibre G_x̄' at the end of 5.0 is not underlined in the print and stays as it is."
})
F.append({
 "page": 385,
 "where": "Lemme 5.2.1, first line",
 "scan": "Soit G̲ un E-faisceau constructible sur un schéma: 'un' and 'faisceau constructible sur un schéma' underlined, 'E-' not",
 "tex": L("@underline{un E-faisceau constructible sur un schéma}"),
 "kind": "underline",
 "confidence": "high",
 "fix": {"old": L("@underline{un E-faisceau"), "new": L("@underline{un} E-@underline{faisceau")},
 "note": "Same form as Définition 5.1 on p. 384: the print leaves E- out of the underline."
})
with io.open(out, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
    fh.write("\n")
print("written", len(F))
