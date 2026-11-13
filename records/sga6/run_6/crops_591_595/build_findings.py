"""Build findings_591_595.json and check that every fix's old string occurs exactly once in its page file."""
import json, pathlib, sys
from collections import Counter
sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
B = RUN / "b591_595"
OUT = RUN / "findings_591_595.json"
MK591 = "%%%%%%%%%%  scan idx 604  |  folio 591  %%%%%%%%%%"
MK592 = "%%%%%%%%%%  scan idx 605  |  folio 592  %%%%%%%%%%"


def F(old, new):
    return {"old": old, "new": new}


E = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    e = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if kind == "misprint_in_print":
        e["corrected"] = corrected
    e["note"] = note
    E.append(e)


# ---------------- page 591 ----------------
add(591, "start of page (folio-591 marker)",
    "p. 591 begins 'tères pour que F(k) → F(K) soit injectif (resp. surjectif).', the second half of 'critères' "
    "divided at the page break; p. 590 ends '... nous cherchons des cri-' (both scans; OCR of p. 590)",
    "the whole word 'critères' ends the last line above the folio-591 marker ('... nous cherchons des critères'); "
    "page_591.tex begins 'pour que'",
    "marker", "high", None,
    "Page 591 really begins with 'tères'. Already applied in the live main.tex (both layers, 16:36): '... nous "
    "cherchons des cri%' / marker / 'tères pour que', the split-word form of folios 18, 36, 46 and 262; "
    "page_591.tex was extracted before that edit. No action; do not split the word again.")

add(591, "first line: 'tères pour que F(k) → F(K) soit injectif (resp. surjectif).'",
    "the map F(k) → F(K) stands in the running text, on one line with 'pour que' and 'soit injectif (resp. "
    "surjectif).' (both scans)",
    "a display \\[ F(k)\\longrightarrow F(K) \\] between 'pour que' and 'soit injectif'",
    "other", "high",
    F("pour que\n\\[\n  F(k)\\longrightarrow F(K)\n\\]\nsoit injectif",
      "pour que \\(F(k)\\longrightarrow F(K)\\) soit injectif"),
    "The TeX makes an inline formula a display.")

add(591, "7.18.2, 'Alors l'application F(k) → K(K) est injective.'",
    "K(K) (both scans; crops_591_595/wit_591_half.png)",
    "\\(F(k)\\to K(K)\\) (printed reading kept)",
    "misprint_in_print", "high", None,
    "Typing slip: the statement concerns F(k) → F(K) (7.18.1; 7.18.3 (ii)). The diplomatic TeX keeps the printed "
    "reading; the current layer reads F(K).",
    corrected="\\(F(k)\\to F(K)\\)")

add(591, "7.18.3, display 'N_{k'/k} : F(k') → F(k)'",
    "no punctuation after F(k) (both scans)",
    "N_{k'/k}:F(k')\\longrightarrow F(k),",
    "punctuation", "high",
    F("F(k')\\longrightarrow F(k),\n\\]", "F(k')\\longrightarrow F(k)\n\\]"),
    "Comma added at the end of the display.")

# ---------------- page 592 ----------------
add(592, "start of page (folio-592 marker)",
    "p. 592 begins '(i) Pour toute extension K de k'; p. 591 ends 'Sous ces conditions, on a :' (both scans)",
    "the \\item that prints '(i)' is the last line above the folio-592 marker (after "
    "'\\begin{enumerate}[label=(\\roman*)]'); page_592.tex begins with the item's text",
    "marker", "medium", None,
    "Page 592 really begins at '(i)'. Exact fix in main.tex (both layers): replace '\\item\\n" + MK592 + "\\n' by '"
    + MK592 + "\\n\\item\\n' (once in each layer; the \\begin{enumerate} line stays on p. 591, as at folio 281). "
    "Equivalent: python -I move_marker.py 6 592 '\\item' --before (simulated in memory on both layers with "
    "crops_591_595/sim_markers.py). Independent of the 'Pour' entries below.")

add(592, "item (i), first word",
    "(i) Pour toute extension K de k, ... (capital P; both scans)",
    "pour toute extension \\(K\\) de \\(k\\), le noyau",
    "word", "high",
    F("pour toute extension \\(K\\) de \\(k\\), le noyau", "Pour toute extension \\(K\\) de \\(k\\), le noyau"),
    "Capital P in the print.")

add(592, "item (i), end: 'est un groupe de torsion.'",
    "full stop after 'torsion', on the baseline without the comma's tail (both scans; crops_591_595/"
    "m592_torsion_z.png, w592_torsion.png; the OCR's comma is a misreading)",
    "groupe de torsion,",
    "punctuation", "high",
    F("groupe de torsion,", "groupe de torsion."),
    "The TeX has a comma.")

add(592, "item (ii), first word",
    "(ii) Pour toute extension pure K de k, ... (capital P; both scans)",
    "\\item pour toute extension pure",
    "word", "high",
    F("\\item pour toute extension pure", "\\item Pour toute extension pure"),
    "Capital P in the print.")

add(592, "7.18.4, 'Si on suppose de plus k infini, où qu'on peut définir des homomorphismes norme comme dans 7.18.3'",
    "où with a grave accent (both scans; crops_591_595/m592_ou.png, wit_592_half.png)",
    "où qu'on (printed reading kept)",
    "misprint_in_print", "medium", None,
    "The sentence joins two alternative hypotheses (k infinite, as in 7.18.2 b), or norms as in 7.18.3 (ii)): "
    "'ou' (or). Both layers of main.tex read 'où'.",
    corrected="ou qu'on")

# ---------------- page 593 ----------------
add(593, "first sentence, '(grâce à (IV 2.12). En vertu de'",
    "one closing parenthesis only: '(grâce à (IV 2.12).' (both scans; crops_591_595/m593_IV212b.png)",
    "(grâce à (IV 2.12). (printed reading kept)",
    "misprint_in_print", "high", None,
    "Unbalanced parenthesis of the print. The diplomatic TeX keeps it; the current layer reads '(IV 2.12)).'",
    corrected="(grâce à (IV 2.12)).")

add(593, "'donc il définit un homomorphisme image directe p = N_{k'/k} : K.(X⊗_k k') → K.(X). On vérifie "
    "immédiatement'",
    "the formula stands in the running text, followed on the same line by '. On vérifie immé-' (both scans; "
    "crops_591_595/m593_pN.png)",
    "a display \\[ p=N_{k'/k}:K_\\bullet(X\\otimes_k k')\\longrightarrow K_\\bullet(X). \\]",
    "other", "high",
    F("image directe\n\\[\n  p=N_{k'/k}:K_\\bullet(X\\otimes_k k')\\longrightarrow K_\\bullet(X).\n\\]\nOn vérifie",
      "image directe \\(p=N_{k'/k}:K_\\bullet(X\\otimes_k k')\\longrightarrow K_\\bullet(X)\\). On vérifie"),
    "The TeX makes an inline formula a display.")

add(593, "'s'identifie à l'application K.(X) → K.(X x_k U), qui est surjective pour X noethérien'",
    "the formula stands in the running text: 'l'application K.(X) → K.(Xx_kU), qui est surjective pour X "
    "noethérien,' is one line (both scans)",
    "a display \\[ K_\\bullet(X)\\longrightarrow K_\\bullet(X\\times_k U), \\]",
    "other", "high",
    F("l'application\n\\[\n  K_\\bullet(X)\\longrightarrow K_\\bullet(X\\times_k U),\n\\]\nqui est surjective",
      "l'application \\(K_\\bullet(X)\\longrightarrow K_\\bullet(X\\times_k U)\\), qui est surjective"),
    "The TeX makes an inline formula a display. The typed x for the product (\\times) is handled globally.")

add(593, "'Ces résultats restent valable si on suppose seulement X noethérien'",
    "valable (both scans; crops_591_595/m593_valable.png)",
    "valable (printed reading kept)",
    "misprint_in_print", "high", None,
    "Agreement slip (résultats is plural). The diplomatic TeX keeps the printed reading; the current layer reads "
    "'valables'.",
    corrected="valables")

add(593, "'(de sorte que X_K est encore de type fini. De plus,'",
    "no closing parenthesis after 'fini' (both scans; crops_591_595/m593_sorte.png)",
    "de type fini. De plus (printed reading kept)",
    "misprint_in_print", "high", None,
    "The parenthesis opened at '(de sorte que' is not closed in the print. The diplomatic TeX keeps the printed "
    "reading; the current layer reads 'fini). De plus'.",
    corrected="de type fini). De plus")

# ---------------- page 594 ----------------
add(594, "heading of the bibliography",
    "BIBLIOGRAPHIE: typed capitals, underlined (both scans)",
    "\\subsection*{Bibliographie}",
    "word", "medium",
    F("\\subsection*{Bibliographie}", "\\subsection*{BIBLIOGRAPHIE}"),
    "Capitals against the TeX's small letters; the missing underline of a \\subsection* title is accepted. Same form "
    "as the bibliography headings of Exposés II-IX in main.tex (\\subsection*{BIBLIOGRAPHIE}).")

TIT = ("The typescript neither underlines nor italicizes the titles of this bibliography; same fix as the "
       "bibliographies of pp. 19, 159, 273, 296, 364 and 415.")
add(594, "bibliography [1] Dickson, title",
    "'Linear groups' typed plain, not underlined (both scans; crops_591_595/wit_594_half.png)",
    "\\emph{Linear groups}", "font", "high",
    F("\\emph{Linear groups}", "Linear groups"), TIT)
add(594, "bibliography [3] Kleiman, title",
    "'Towards a numerical theory of ampleness' typed plain, not underlined (both scans)",
    "\\emph{Towards a numerical theory of ampleness}", "font", "high",
    F("\\emph{Towards a numerical theory of ampleness}", "Towards a numerical theory of ampleness"), "As [1].")
add(594, "bibliography [3] Kleiman, 'pp. 293-344.'",
    "293-344: typed hyphen (both scans)",
    "293--344", "punctuation", "high",
    F("293--344", "293-344"),
    "En dash added by the transcription, as the bibliography ranges fixed on pp. 220-221 and 497.")
add(594, "bibliography [4] Murre, title",
    "'On contravariant functors from the category of préschemes over a field into the category of abelian groups' "
    "typed plain, not underlined (both scans)",
    "\\emph{On contravariant functors ... abelian groups}", "font", "high",
    F("\\emph{On contravariant functors from the category of préschemes over a field into the category of abelian "
      "groups}",
      "On contravariant functors from the category of préschemes over a field into the category of abelian groups"),
    "As [1].")
add(594, "bibliography [6] Abhyankar, title",
    "'Resolution of singularities of arithmetical surfaces' typed plain, not underlined (both scans)",
    "\\emph{Resolution of singularities of arithmetical surfaces}", "font", "high",
    F("\\emph{Resolution of singularities of arithmetical surfaces}",
      "Resolution of singularities of arithmetical surfaces"),
    "As [1]. 'Harper - Row' (Harper--Row in the TeX) is a joint name: handled globally.")

# ---------------- page 595 ----------------
add(595, "exposé heading and title",
    "'EXPOSE XII' in typed capitals with a single underline and no full stop, on its own line at the left; then the "
    "centred title 'UN THEOREME DE REPRESENTABILITE RELATIVE SUR' / 'LE FONCTEUR DE PICARD' in typed capitals, two "
    "lines, each with a double underline (both scans; crops_591_595/m595_head.png, wit_595_half.png)",
    "\\section*{Exposé XII. Un théorème de représentabilité relative sur le foncteur de Picard}: number and title "
    "run together with a full stop, the title in small letters, no underline",
    "word", "medium",
    F("\\section*{Exposé XII. Un théorème de représentabilité relative sur le foncteur de Picard}",
      r"\section*{\underline{EXPOSÉ XII}\\[3pt] \underline{\underline{UN THÉORÈME DE REPRÉSENTABILITÉ RELATIVE SUR}}"
      r"\\[3pt] \underline{\underline{LE FONCTEUR DE PICARD}}}"),
    "Same form as the applied headings of Exposés III, IV, VIII, IX and X (main.tex: \\section*{\\underline{EXPOSÉ "
    "X}\\\\[3pt] \\underline{\\underline{...}}}), the two title lines split as in the Exposé VI heading (\\underline "
    "cannot break a line). É and È keep the TeX's accents (rule for typed capitals: the print has EXPOSE, THEOREME, "
    "REPRESENTABILITE). Independent of the author-line entry.")

add(595, "author line of the heading",
    "'par M. Raynaud (rédigé par S. Kleiman)' in mixed case, the whole line underlined (both scans; "
    "crops_591_595/m595_head.png)",
    "par M. Raynaud (rédigé par S. Kleiman) (no underline)",
    "underline", "medium",
    F("par M. Raynaud (rédigé par S. Kleiman)", "\\underline{par M. Raynaud (rédigé par S. Kleiman)}"),
    "As the applied author lines (\\underline{par O. Jussila}, p. 519; \\underline{par P. BERTHELOT}).")

add(595, "Avertissement, '(p. C 07-C 11)'",
    "C 07-C 11: typed hyphen (both scans; crops_591_595/m595_C07.png)",
    "C 07--C 11", "punctuation", "high",
    F("C 07--C 11", "C 07-C 11"),
    "En dash added by the transcription.")

add(595, "Avertissement, 'de ses \"Fondements de la Géométrie Algébrique\" (cité FGA)'",
    "the title between straight double quotes, not underlined (both scans; crops_591_595/m595_C07.png)",
    "\\emph{Fondements de la Géométrie Algébrique} (italics, no quotes)",
    "punctuation", "high",
    F("\\emph{Fondements de la Géométrie Algébrique}", "«~Fondements de la Géométrie Algébrique~»"),
    "The TeX drops the print's quotes and sets the title in italics. «~...~» is the file's form for the print's "
    "straight quotes (handled globally; e.g. «~polynômes de Hilbert~», p. 596).")

add(595, "Avertissement, 'forgé par I. Castelnuovo et aiguisé et utilisé par T. Matsusaka'",
    "I. Castelnuovo: a typed capital I with its full stop (both scans; crops_591_595/m595_Castel.png)",
    "I. Castelnuovo (printed reading kept)",
    "misprint_in_print", "low", None,
    "Wrong initial: the geometer is Guido Castelnuovo. Possibly a misread initial of the manuscript rather than a "
    "typing slip; both layers of main.tex read 'I.'.",
    corrected="G. Castelnuovo")

# ---------------- checks ----------------
bad = 0
for e in E:
    fx = e["fix"]
    if fx is None:
        continue
    t = (B / f"page_{e['page']}.tex").read_text(encoding="utf-8")
    n = t.count(fx["old"])
    if n != 1 or "%%%%%%%%%%  scan idx" in fx["old"]:
        bad += 1
        print("BAD", e["page"], n, repr(fx["old"][:60]))
OUT.write_text(json.dumps(E, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
c = Counter((e["page"], e["kind"] == "misprint_in_print") for e in E)
for p in range(591, 596):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
print("entries", len(E), "bad", bad)
