"""Build findings_691_695.json and check that every fix's "old" occurs exactly once in its page file."""
import json
import pathlib

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
B = RUN / "b691_695"
OUT = RUN / "findings_691_695.json"

F = []


def add(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": confidence,
         "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- p. 691 ----------------
add(691,
    "algébriquement équivalent à zéro (dans K·) - X App. 7.11",
    "K with a raised round dot, not the tall wedge-shaped typewriter apostrophe of d'amplitude on the same page "
    "(both scans; crops_691_695/c691_K2.png, wit_691_K.png, c691_apos.png)",
    r"(dans \(K'\))",
    "symbol", "high",
    {"old": r"\(K'\)", "new": r"\(K^{\bullet}\)"},
    r"The print's K with a raised dot, written K^{\bullet} in Exposés IV and VI (10 Nov). The index transcription "
    r"writes the raised dot as a prime (also \operatorname{Gr}' on p. 692).")

add(691,
    "d'amplitude C_o-parfaite contenue dans [a, b] complexe) - I 4.7 (first of the two 4.7 entries)",
    "the continuation line reads 'complexe)' with no opening parenthesis (both scans; crops_691_695/c691_47.png, "
    "wit_691_small.png)",
    r"contenue dans \([a,b]\) (complexe) & I & 4.7",
    "misprint_in_print", "high",
    {"old": r"\([a,b]\) (complexe) & I & 4.7", "new": r"\([a,b]\) complexe) & I & 4.7"},
    "Typing error of the print: '(' left out before 'complexe)'. The TeX silently supplies it; the fix restores the "
    "printed reading.",
    corrected=r"\([a,b]\) (complexe) & I & 4.7")

add(691,
    "d'amplitude C_o parfaite contenue dans [a,b] complexe) - I 4.8",
    "the continuation line reads 'complexe)' with no opening parenthesis (both scans; crops_691_695/c691_48.png, "
    "wit_691_small.png)",
    r"contenue dans \([a,b]\) (complexe) & I & 4.8",
    "misprint_in_print", "high",
    {"old": r"\([a,b]\) (complexe) & I & 4.8", "new": r"\([a,b]\) complexe) & I & 4.8"},
    "Same typing error as in the 4.7 entry two lines above. The TeX silently supplies the '('; the fix restores the "
    "printed reading. Independent of the next finding (same entry, different string).",
    corrected=r"\([a,b]\) (complexe) & I & 4.8")

add(691,
    "d'amplitude C_o parfaite contenue dans [a,b] (complexe) - I 4.8",
    "'d'amplitude C_o parfaite contenue dans [a,b]', with the underlined C and index o and no hyphen (both scans)",
    r"d'amplitude \(\mathcal C_0\) parfaite contenue dans \([a,b]\) (complexe) & I & 4.8",
    "misprint_in_print", "medium",
    None,
    r"The TeX keeps the printed reading. Exemple I 4.8 defines 'd'amplitude parfaite contenue dans [a,b] (resp. "
    r"d'amplitude parfaite finie, resp. parfait)' (amplitude C_0-parfaite for C_0 the facteurs directs de Modules "
    r"libres de type fini); C_0-parfaite is I 4.7, the two entries above, and the index's other 4.8 entries are "
    r"'d'amplitude parfaite finie' and 'parfait (complexe)' (p. 694). The typist repeated the C_o of the 4.7 lines. "
    r"In the corrected edition replace 'd'amplitude \(\mathcal C_0\) parfaite contenue' (once on the page) by the "
    r"corrected reading.",
    corrected=r"d'amplitude parfaite contenue")

add(691,
    "d'amplitude plate finie relativement a f (complexe) - III 3.1",
    "'relativement a f': a without the grave accent (both scans; crops_691_695/c691_a.png); the other entries of "
    "the page have 'à f'",
    r"relativement a \(f\)",
    "misprint_in_print", "high",
    None,
    r"The TeX keeps the printed reading; 'relativement a \(f\)' occurs once on the page.",
    corrected=r"relativement à \(f\)")

# ---------------- p. 692 ----------------
add(692,
    "équivalence numérique (dans Gr·(X) et Gr.(X)) - X 4.5",
    "the first Gr has a raised round dot, the second a full stop on the line (both scans; "
    "crops_691_695/c692_Gr.png, wit_692_Gr.png)",
    r"\(\operatorname{Gr}'(X)\)",
    "symbol", "high",
    {"old": r"\(\operatorname{Gr}'(X)\)", "new": r"\(\operatorname{Gr}^{\bullet}(X)\)"},
    r"The print's raised typed dot in Gr is written \bullet in this volume (the file's \Gro is "
    r"\operatorname{Gr}^{\bullet}); there is no prime in the print. \operatorname{Gr}_{\cdot}(X) for Gr.(X) is right.")

add(692,
    "tau-équivalence - XIII 4.4 (the line after 'τ- équivalence X 2.4.1')",
    "a ditto mark '' under 'équivalence' stands for the term; only 'XIII' and '4.4' are typed in the columns (both "
    "scans; crops_691_695/c692_tau.png, wit_692_small.png)",
    r"\(\tau\)-équivalence & XIII & 4.4",
    "other", "high",
    {"old": r"\(\tau\)-équivalence & XIII & 4.4", "new": r"\qquad'' & XIII & 4.4"},
    "The TeX writes out the term the print gives as a ditto mark (two more ditto marks on p. 693; no ditto mark is "
    "transcribed anywhere in the TeX).")

# ---------------- p. 693 ----------------
add(693,
    "homomorphisme de spécialisation - X App. 7.16 (the line after the X App. 7.3 entry)",
    "two ditto marks, one under 'homomorphisme' and one under 'spécialisation' ('de' has none); 'X App.' and "
    "'7.16' typed in the columns (both scans; crops_691_695/c693_ditto.png, wit_693_small.png)",
    r"homomorphisme de spécialisation & X App. & 7.16",
    "other", "high",
    {"old": r"homomorphisme de spécialisation & X App. & 7.16", "new": r"\qquad''\hspace{8em}'' & X App. & 7.16"},
    "The TeX writes out the words the print gives as ditto marks (as on p. 692).")

# ---------------- p. 694 ----------------
add(694,
    "n-pseudo-cohérent relativement a f (complexe) - III 1.2",
    "'relativement a f': a without the grave accent (both scans; crops_691_695/c694_a.png); the next entry has "
    "'relativement à f'",
    r"relativement a \(f\)",
    "misprint_in_print", "high",
    None,
    r"The TeX keeps the printed reading; 'relativement a \(f\)' occurs once on the page.",
    corrected=r"relativement à \(f\)")

# ---------------- p. 695 ----------------
add(695,
    "end of page (folio-696 and folio-697 markers)",
    "p. 695 (index page '5') prints five entries and nothing else: 'de tor-dimension finie I 5.2', "
    "'tor-indépendance III 1.5', 'trace I 8.1', 'de C_o -type fini I 1.2', 'variété mixte de classe C^r "
    "II App. II 1.1'. P. 696 begins with the heading 'Index des notations' and ends 'd^n_{X/S}(E) II App.II 1.2.2'; "
    "p. 697 (notation index page '2') begins 'D^-(Qcoh(S))_coh , D(Qcoh(S))_parf II 2.2.1' (both scans; "
    "crops_691_695/wit_695_top.png; b696_700/page_696_s1.png, page_696_s4.png, page_697_s1.png)",
    r"page_695.tex stops after 'tor-indépendance & III & 1.5\\'. 'trace & I & 8.1\\' and 'de \(\mathcal C_0\)-type' "
    r"stand under the folio-696 marker; the folio-697 marker splits 'de \(\mathcal C_0\)-type' / 'fini & I & 1.2\\', "
    r"and 'variété mixte de classe \(C^r\) & II App. II & 1.1\\', the end of the table and the whole first page of "
    r"the Index des notations stand under it",
    "marker", "high",
    None,
    r"Page 695 begins at its marker (right) and really ends after 'variété mixte de classe \(C^r\) & II App. II & "
    r"1.1\\' with \bottomrule, \end{longtable}, \endgroup, \newpage. Page 696 really begins at "
    r"'\section*{Index des notations}', page 697 at '\(\Dcat^{-}(\Qcoh(S))_{\coh},\ \Dcat(\Qcoh(S))_{\parf}\) & II "
    r"& 2.2.1\\'. Exact fix, both layers, the two moves together and in this order: "
    r"python -I move_marker.py 6 697 '\(\Dcat^{-}(\Qcoh(S))_{\coh}' , then "
    r"python -I move_marker.py 6 696 '\section*{Index des notations}' . Each anchor occurs once in each layer; "
    r"simulated in memory on both layers (crops_691_695/sim_markers.py): the markers stay in increasing order and "
    r"'de \(\mathcal C_0\)-type' / 'fini & I & 1.2\\' become one entry over a line break. The text under the "
    r"misplaced markers matches the print. The checker of pp. 696-697 will meet the same misplacement from the "
    r"other side; apply it once.")

add(695,
    "de tor-dimension finie - I 5.2",
    "'de tor-dimension finie' on one line, no space after the hyphen (both scans)",
    r"'de tor-' and 'dimension finie & I & 5.2\\' on two lines: the end of line after the hyphen typesets as a "
    r"space ('tor- dimension')",
    "other", "low",
    {"old": "de tor-\ndimension finie", "new": "de tor-dimension finie"},
    "A space inside the compound in the typeset entry; probably left by an earlier marker split. Independent of the "
    "marker finding (the folio-695 marker stays where it is).")

# ---------------- checks ----------------
for d in F:
    if d["fix"] is None:
        continue
    t = (B / f"page_{d['page']:03d}.tex").read_text(encoding="utf-8")
    old = d["fix"]["old"]
    n = t.count(old)
    assert n == 1, (d["page"], old, n)
    assert "%%%%%%%%%%" not in old and "%%%%%%%%%%" not in d["fix"]["new"], old
    i = t.find(old)
    assert t.find("\n", 0, i) >= 0 or True
    print("ok", d["page"], repr(old))

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
back = json.loads(OUT.read_text(encoding="utf-8"))
from collections import Counter
c = Counter((d["page"], d["kind"] == "misprint_in_print") for d in back)
for p in (691, 692, 693, 694, 695):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
print(len(back), "findings written to", OUT)
