import json, pathlib

RUN = pathlib.Path(r"C:/Users/user/Documents/sga_scan_check_20261105/run_6")
BATCH = RUN / "b596_600"
OUT = RUN / "findings_596_600.json"
NL = "<NL>"


def s(x):
    return None if x is None else x.replace(NL, "\n")


F = []


def add(page, where, scan, tex, kind, conf, old, new, note, corrected=None, fix_null=False):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf}
    d["fix"] = None if fix_null else {"old": s(old), "new": s(new)}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


PIC = "Pic underlined in the print (both scans); \\Pic is \\operatorname{Pic}, plain. Exposé XII's TeX has no underline markup; the file writes \\underline{\\Pic} in Exposé XIII."

# ---------------- page 596 ----------------
add(596, "Théorème 1.1, display (first Pic)", "f^* : Pic_{Y/S} | V -> ..., 'Pic' underlined",
    r"f^*:\Pic_{Y/S}|_V", "underline", "high",
    r"f^*:\Pic", r"f^*:\underline{\Pic}", PIC)
add(596, "Théorème 1.1, display", "Pic_{Y/S} | V, V on the line",
    r"\Pic_{Y/S}|_V", "formula", "high",
    r"_{Y/S}|_V", r"_{Y/S}|V", "Restriction: the print writes |V with V on the line.")
add(596, "Théorème 1.1, display (second Pic)", "-> Pic_{X/S} | V, 'Pic' underlined",
    r"\longrightarrow \Pic_{X/S}|_V", "underline", "high",
    r"\longrightarrow \Pic", r"\longrightarrow \underline{\Pic}", PIC)
add(596, "Théorème 1.1, display", "Pic_{X/S} | V, V on the line",
    r"\Pic_{X/S}|_V (end of the display line)", "formula", "high",
    r"_{X/S}|_V" + NL, r"_{X/S}|V" + NL, "Restriction: the print writes |V with V on the line.")
add(596, "Corollaire 1.2, 'le foncteur de Picard Pic_{X/S} | V'", "Pic_{X/S} | V, V on the line (Pic plain here)",
    r"\(\Pic_{X/S}|_V\)", "formula", "high",
    r"_{X/S}|_V\)", r"_{X/S}|V\)", "Restriction: V on the line. This Pic is not underlined in the print (both scans), so no underline fix here.")
add(596, "'est représenté par un S-schéma en groupes Pic_{X/S}'", "Pic_{X/S} with 'Pic' underlined",
    r"en groupes \(\Pic_{X/S}\)", "underline", "high",
    r"en groupes \(\Pic", r"en groupes \(\underline{\Pic}", PIC)
add(596, "'de présentation finie. La considération des'", "new indented paragraph at 'La considération des'",
    "the TeX runs 'La considération' on in the same paragraph", "other", "high",
    "présentation finie. La considération", "présentation finie." + NL + NL + "La considération",
    "Paragraph break of the print (both scans).")
add(596, "'permet ici de décomposer Pic_{X/S}'", "'Pic' underlined",
    r"décomposer \(\Pic_{X/S}\)", "underline", "high",
    r"décomposer \(\Pic", r"décomposer \(\underline{\Pic}", PIC)
add(596, "'en somme d'ouverts Pic^q_{X/S}'", "'Pic' underlined",
    r"d'ouverts \(\Pic^q_{X/S}\)", "underline", "high",
    r"d'ouverts \(\Pic^q", r"d'ouverts \(\underline{\Pic}^q", PIC)
add(596, "'que les Pic^q_{X/S} sont de type fini'", "'Pic' underlined",
    r"que les \(\Pic^q_{X/S}\)", "underline", "high",
    r"que les \(\Pic^q", r"que les \(\underline{\Pic}^q", PIC)
add(596, "last line before Lemme 1.3", "'en uti-' / 'sant le': the print reads 'utisant' (both scans)",
    "en utilisant le", "misprint_in_print", "high",
    "en utilisant le", "en utisant le",
    "Typing error of the print (syllable 'li' left out at the line break); the TeX silently corrects it. Diplomatic reading restored.",
    corrected="utilisant")
add(596, "statements of Exposé XII: Théorème 1.1, Corollaire 1.2, Lemme 1.3 (also Lemme 1.4 p. 597, Corollaires 1.5-1.6 p. 598, assertions I, II p. 599, II' p. 600)",
    "the statements are underlined word group by word group ('Soient' 'un schéma noethérien' 'et' 'deux' ...)",
    "set in roman: the TeX of Exposé XII has no \\underline at all", "underline", "high",
    None, None,
    "Convention of the transcription, reported once, not itemized: the same pattern as Exposé II (GLOBAL_ISSUES 82). Examples: Théorème 1.1 (p. 596), Lemme 1.4 (p. 597), Corollaire 1.6 (p. 598).",
    fix_null=True)

# ---------------- page 597 ----------------
add(597, "first line (end of Lemme 1.3): 'plat S' -> V tels que'", "no comma after V (both scans)",
    r"\(S'\to V\), tels", "punctuation", "high",
    r"\(S'\to V\), tels", r"\(S'\to V\) tels", "Comma added by the TeX.")
add(597, "proof of 1.3: 'toute composante irréductible de X_{S_i}'",
    "X_{S_i}: the index of S is a small i (dot, no flag; the 1 of S_1, V_1, h(S_1 - S_2) on the same lines has a flag), clear in the witness",
    r"\(X_{S_1}\)", "misprint_in_print", "high",
    r"\(X_{S_1}\)", r"\(X_{S_i}\)",
    "Wrong index in the print; the TeX silently writes 1. The sentence chooses the open S_2 ('il existe un ouvert non vide S_2 de S_1 tel que ...') and V = V_1 - h(S_1 - S_2) uses it, so the correct reading is S_2 (the TeX's and the corrected layer's S_1 is not it; medium confidence for the correction). Apply together with the 'sur S_i' entry below.",
    corrected=r"X_{S_2}")
add(597, "proof of 1.3: 'X_{S_i}, muni de la structure réduite induite'", "muni (both scans)",
    "muni", "misprint_in_print", "medium",
    None, None,
    "Agreement error of the print ('toute composante ... munie', as on p. 597 l. 1 and p. 599); the TeX keeps the printed reading; the corrected layer already has 'munie'.",
    corrected="munie", fix_null=True)
add(597, "proof of 1.3: 'soit intègre sur S_i (EGA IV 9.7.7)'", "S_i with a small i (as in X_{S_i}), clear in the witness",
    r"sur \(S_1\) (EGA", "misprint_in_print", "high",
    r"sur \(S_1\) (EGA", r"sur \(S_i\) (EGA",
    "Same misprint as X_{S_i} just before (both or neither); correct reading S_2.",
    corrected=r"S_2")
add(597, "proof of 1.3: 'Prenons v = v_1 - h(S_1 - S_2)'",
    "small v twice (x-height; the capital V of '(V)' and 'IV' on the same line is taller), both scans",
    r"\(V=V_1-h(S_1-S_2)\)", "misprint_in_print", "high",
    r"\(V=V_1-h", r"\(v=v_1-h",
    "Typing error of the print (V and V_1 are the open sets of the proof); the TeX silently capitalizes. Diplomatic reading restored.",
    corrected=r"V=V_1")
add(597, "'Alors Pic_{Z/S'} = prod_i Pic_{Z_i/S'}'", "both 'Pic' underlined",
    r"\Pic_{Z/S'}=\prod_i\Pic_{Z_i/S'}", "underline", "high",
    r"\Pic_{Z/S'}=\prod_i\Pic_{Z_i/S'}", r"\underline{\Pic}_{Z/S'}=\prod_i\underline{\Pic}_{Z_i/S'}", PIC)
add(597, "'de type fini. Enfin, 1.1 dit que'", "new indented paragraph at 'Enfin, 1.1 dit que'",
    "the TeX runs 'Enfin' on in the same paragraph", "other", "high",
    "de type fini. Enfin, 1.1", "de type fini." + NL + NL + "Enfin, 1.1",
    "Paragraph break of the print (both scans).")
add(597, "'le morphisme f^* : Pic_{X'/S'} -> Pic_{Z'/S'}'", "both 'Pic' underlined",
    r"f^*:\Pic_{X'/S'}\longrightarrow \Pic_{Z'/S'}", "underline", "high",
    r"f^*:\Pic_{X'/S'}\longrightarrow \Pic", r"f^*:\underline{\Pic}_{X'/S'}\longrightarrow \underline{\Pic}", PIC)
add(597, "'f^* : Pic_{X'/S'} -> Pic_{Z'/S'}'", "Pic_{Z'/S'} with a prime on Z (both scans)",
    r"\Pic_{Z'/S'}", "misprint_in_print", "high",
    None, None,
    "Z is the scheme just defined (f: Z = coprod Z_i -> X'); Z' is not defined. The TeX keeps the printed reading; the corrected layer has \\Pic_{Z/S'}.",
    corrected=r"\Pic_{Z/S'}", fix_null=True)
add(597, "'est réprésentable par un morphisme quasi-affine'", "'réprésentable', acute accent on the first e as well (both scans)",
    "représentable par un morphisme", "misprint_in_print", "high",
    "représentable par un morphisme", "réprésentable par un morphisme",
    "Typing error of the print (as on p. 394); the TeX silently corrects it. Diplomatic reading restored.",
    corrected="représentable")
add(597, "'Pic_{X/S}|V l'est aussi'", "Pic_{X/S}|V, V on the line (Pic plain)",
    r"\(\Pic_{X/S}|_V\) l'est", "formula", "high",
    r"|_V\) l'est", r"|V\) l'est", "Restriction: V on the line.")

# ---------------- page 598 ----------------
add(598, "'D'ailleurs on sait (SGA 3 1.4.2)'", "(SGA 3 1.4.2): the digit 1 with its flag, then a full stop (both scans)",
    "(SGA 3 I 4.2)", "number", "high",
    "(SGA 3 I 4.2)", "(SGA 3 1.4.2)",
    "The TeX reads the 1 as the exposé numeral I and drops the stop. The print gives no exposé (the result is SGA 3 VI_B 1.4.2, the exposé of the reference on p. 597; not recorded as a misprint). The corrected layer has the same 'I 4.2'.")
add(598, "Corollaire 1.5 a), 'Alors Pic_{X/k} est représentable'", "'Pic' underlined",
    r"Alors \(\Pic_{X/k}\)", "underline", "high",
    r"Alors \(\Pic_{X/k}\)", r"Alors \(\underline{\Pic}_{X/k}\)", PIC)
add(598, "Corollaire 1.5 b), 'f^* : Pic_{Y/k} -> Pic_{X/k}'", "both 'Pic' underlined",
    r"f^*:\Pic_{Y/k}\longrightarrow \Pic_{X/k}", "underline", "high",
    r"f^*:\Pic_{Y/k}\longrightarrow \Pic_{X/k}", r"f^*:\underline{\Pic}_{Y/k}\longrightarrow \underline{\Pic}_{X/k}", PIC)
add(598, "Corollaire 1.6 a), 'f^* : Pic_{Y/S} -> Pic_{X/S} est quasi-fini'", "both 'Pic' underlined",
    r"\Pic_{Y/S}\to\Pic_{X/S}\) est quasi-fini", "underline", "high",
    r"\Pic_{Y/S}\to\Pic_{X/S}\) est quasi-fini", r"\underline{\Pic}_{Y/S}\to\underline{\Pic}_{X/S}\) est quasi-fini", PIC)
add(598, "Corollaire 1.6 b), 'Si Pic_{Y/S} est essentiellement propre'", "'Pic' underlined",
    r"Si \(\Pic_{Y/S}\)", "underline", "high",
    r"Si \(\Pic_{Y/S}\)", r"Si \(\underline{\Pic}_{Y/S}\)", PIC)
add(598, "Corollaire 1.6 b), 'au critère voluatif de propreté'", "voluatif (both scans)",
    "voluatif", "misprint_in_print", "high",
    None, None,
    "Typing error of the print; the TeX keeps the printed reading; the corrected layer has 'valuatif'.",
    corrected="valuatif", fix_null=True)
add(598, "Corollaire 1.6 b), 'f^* : Pic_{Y/S} -> Pic_{X/S} est fini'", "both 'Pic' underlined",
    r"\Pic_{Y/S}\to\Pic_{X/S}\) est fini", "underline", "high",
    r"\Pic_{Y/S}\to\Pic_{X/S}\) est fini", r"\underline{\Pic}_{Y/S}\to\underline{\Pic}_{X/S}\) est fini", PIC)
add(598, "after Corollaire 1.6: 'En effet dans a)'", "new indented paragraph",
    r"'En effet' follows \end{enumerate} without a blank line (set unindented, as a continuation)", "other", "medium",
    r"\end{enumerate}" + NL + "En effet", r"\end{enumerate}" + NL + NL + "En effet",
    "Paragraph indentation of the print (both scans).")

# ---------------- page 599 ----------------
add(599, "2.1, first diagram: left vertical arrow X_réd -> X", "label i to the right of the arrow (both scans)",
    '\\arrow[d,"i"\']', "formula", "high",
    '\\arrow[d,"i"\']', '\\arrow[d,"i"]', "The ' sets the label on the left.")
add(599, "2.1, first diagram: lower arrow X -> Y", "label f above the arrow (both scans)",
    '\\arrow[r,"f"\']', "formula", "high",
    '\\arrow[r,"f"\']', '\\arrow[r,"f"]', "The ' sets the label below.")
add(599, "2.1, end of the first diagram", "comma after the diagram (right of Y)",
    "no punctuation", "punctuation", "high",
    "& Y" + NL + r"\end{tikzcd}", "& Y & ," + NL + r"\end{tikzcd}", "Cell form as in earlier fixes (p. 98).")
add(599, "2.1, second diagram, top row", "Pic_{X_réd/S} <- Pic_{Y_réd/S}, both 'Pic' underlined",
    r"\Pic_{X_{\red}/S} & \Pic_{Y_{\red}/S}", "underline", "high",
    r"\Pic_{X_{\red}/S} & \Pic_{Y_{\red}/S}", r"\underline{\Pic}_{X_{\red}/S} & \underline{\Pic}_{Y_{\red}/S}", PIC)
add(599, "2.1, second diagram, bottom row", "Pic_{X/S} <- Pic_{Y/S}, both 'Pic' underlined",
    r"\Pic_{X/S} \arrow[u] & \Pic_{Y/S}", "underline", "high",
    r"\Pic_{X/S} \arrow[u] & \Pic_{Y/S}", r"\underline{\Pic}_{X/S} \arrow[u] & \underline{\Pic}_{Y/S}", PIC)
add(599, "2.1, end of the second diagram", "comma after the diagram (right of Pic_{Y/S})",
    "no punctuation", "punctuation", "high",
    r"\arrow[l] \arrow[u]" + NL + r"\end{tikzcd}", r"\arrow[l] \arrow[u] & ," + NL + r"\end{tikzcd}", "Cell form as in earlier fixes (p. 98).")

# ---------------- page 600 ----------------
add(600, "2.2, end of the first diagram (Y <- coprod_j Y_j over X <- coprod_j Sigma_j)", "comma after the diagram",
    "no punctuation", "punctuation", "high",
    r"\Sigma_j \arrow[l] \arrow[u]" + NL + r"\end{tikzcd}", r"\Sigma_j \arrow[l] \arrow[u] & ," + NL + r"\end{tikzcd}",
    "Cell form as in earlier fixes (p. 98).")
add(600, "2.2, between the two diagrams", "no word between the diagrams ('les deux diagrammes [first] , [second] .'), both scans",
    "et", "extra", "high",
    r"\]" + NL + "et" + NL + r"\[" + NL + r"\begin{tikzcd}", r"\]" + NL + r"\[" + NL + r"\begin{tikzcd}",
    "Word added by the TeX.")
add(600, "2.2, second diagram: Pic_{Y/S} (top left)", "'Pic' underlined",
    r"\Pic_{Y/S} \arrow[r,...]", "underline", "high",
    r"\Pic_{Y/S} \arrow", r"\underline{\Pic}_{Y/S} \arrow", PIC)
add(600, "2.2, second diagram, top right", "Pic_{coprod_j Y_j/S} = prod_j Pic_{Y_j/S}, both 'Pic' underlined",
    r"\Pic_{\coprod_jY_j/S}=\prod_j\Pic_{Y_j/S}", "underline", "high",
    r"\Pic_{\coprod_jY_j/S}=\prod_j\Pic_{Y_j/S}", r"\underline{\Pic}_{\coprod_jY_j/S}=\prod_j\underline{\Pic}_{Y_j/S}", PIC)
add(600, "2.2, second diagram: Pic_{X/S} (bottom left)", "'Pic' underlined",
    r"\Pic_{X/S}", "underline", "high",
    r"\Pic_{X/S}", r"\underline{\Pic}_{X/S}", PIC)
add(600, "2.2, second diagram: lower arrow with circled 3", "circled 3 above the arrow (both scans)",
    '\\arrow[r,"\\sgacircled{3}"\']', "formula", "high",
    '\\arrow[r,"\\sgacircled{3}"\']', '\\arrow[r,"\\sgacircled{3}"]', "The ' sets the label below.")
add(600, "2.2, second diagram, bottom right", "Pic_{coprod_j Sigma_j/S} = prod_j Pic_{Sigma_j/S}, both 'Pic' underlined",
    r"\Pic_{\coprod_j\Sigma_j/S}=\prod_j\Pic_{\Sigma_j/S}", "underline", "high",
    r"\Pic_{\coprod_j\Sigma_j/S}=\prod_j\Pic_{\Sigma_j/S}", r"\underline{\Pic}_{\coprod_j\Sigma_j/S}=\prod_j\underline{\Pic}_{\Sigma_j/S}", PIC)
add(600, "first of 'les deux suites': X_o -> coprod X_i -> Y", "coprod without an index (X_i carries the i), both scans",
    r"\coprod_i X_i", "extra", "high",
    r"\hookrightarrow \coprod_i X_i", r"\hookrightarrow \coprod X_i", "Index added by the TeX.")
add(600, "between 'les deux suites'", "no word between the two displays ('[first] , [second] .'), both scans",
    "et", "extra", "high",
    "Y," + NL + r"\]" + NL + "et" + NL + r"\[", "Y," + NL + r"\]" + NL + r"\[",
    "Word added by the TeX.")
add(600, "second suite: Pic_{coprod X'_i/S}", "coprod without an index in the subscript (both scans)",
    r"\Pic_{\coprod_iX'_i/S}", "extra", "high",
    r"\Pic_{\coprod_iX'_i/S}", r"\Pic_{\coprod X'_i/S}", "Index added by the TeX. The three Pic of this display are plain in the print, as in the TeX.")
add(600, "second suite: Pic_{coprod X'_i/S}", "a short tick at the top right of X, read as a prime (faint in both scans)",
    r"X'_i", "misprint_in_print", "low",
    None, None,
    "If it is a prime it is a misprint: the suite is X_o -> coprod X_i -> Y. The TeX keeps the mark as a prime; the corrected layer has \\Pic_{\\coprod_iX_i/S}. Applies after the index fix just above.",
    corrected=r"\Pic_{\coprod X_i/S}", fix_null=True)
add(600, "'Si l'on sait donc que les Pic_{X_i/S}'", "'Pic' underlined (the following 'Pic_{coprod X_i/S}' is plain)",
    r"les \(\Pic_{X_i/S}\)", "underline", "high",
    r"les \(\Pic_{X_i/S}\)", r"les \(\underline{\Pic}_{X_i/S}\)", PIC)
add(600, "'donc aussi Pic_{coprod X_i/S}'", "coprod without an index (both scans)",
    r"\Pic_{\coprod_iX_i/S}", "extra", "high",
    r"\Pic_{\coprod_iX_i/S}", r"\Pic_{\coprod X_i/S}", "Index added by the TeX.")
add(600, "end of page / start of p. 601",
    "p. 600 ends '... on peut supposer que X_i ∩ X_j = Ø si et seulement si'; p. 601 begins '(X_i)_η ∩ (X_j)_η = Ø. Soient Y_k = ...'",
    r"'\((X_i)_\eta\cap(X_j)_\eta=\varnothing\).' ends page_600.tex, under the folio-600 marker", "marker", "high",
    None, None,
    "Page 601 really begins with '\\((X_i)_\\eta\\cap(X_j)_\\eta=\\varnothing\\).'. Move the folio-601 marker up before it, splitting the line after 'si et seulement si': python -I move_marker.py 6 601 '\\((X_i)_\\eta\\cap(X_j)_\\eta=\\varnothing\\)' --before (simulated in memory on both layers: anchor found once in each; gives '... si et seulement si' / marker / '\\((X_i)_\\eta\\cap(X_j)_\\eta=\\varnothing\\).' / 'Soient ...', the paragraph unbroken).",
    fix_null=True)

# ---------------- checks ----------------
bad = 0
for d in F:
    fx = d["fix"]
    if fx is None:
        continue
    t = (BATCH / ("page_%03d.tex" % d["page"])).read_text(encoding="utf-8")
    n = t.count(fx["old"])
    if n != 1:
        bad += 1
        print("NOT UNIQUE", d["page"], n, repr(fx["old"]))
    if "%%%%%%%%%%" in fx["old"] or "%%%%%%%%%%" in fx["new"]:
        bad += 1
        print("MARKER TOUCHED", d["page"], repr(fx["old"]))
# overlap check per page: no two olds may share characters
for p in (596, 597, 598, 599, 600):
    t = (BATCH / ("page_%03d.tex" % p)).read_text(encoding="utf-8")
    spans = []
    for d in F:
        if d["page"] == p and d["fix"]:
            k = t.find(d["fix"]["old"])
            spans.append((k, k + len(d["fix"]["old"]), d["fix"]["old"][:30]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            bad += 1
            print("OVERLAP", p, a, b)
counts = {}
for d in F:
    c = counts.setdefault(d["page"], [0, 0])
    c[1 if d["kind"] == "misprint_in_print" else 0] += 1
print("counts", counts, "total", len(F), "problems", bad)
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("written", OUT)
