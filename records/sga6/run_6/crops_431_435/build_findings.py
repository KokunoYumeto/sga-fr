"""Build findings_431_435.json; check that every fix's old occurs exactly once in its page file, and that the
fixes of a page apply one after the other (no edit destroys another's old)."""
import json, pathlib, sys
sys.stdout.reconfigure(encoding='utf-8')
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
B = RUN / "b431_435"
OUT = RUN / "findings_431_435.json"
NL = "\n"
M431 = "%%%%%%%%%%  scan idx 444  |  folio 431  %%%%%%%%%%"
M432 = "%%%%%%%%%%  scan idx 445  |  folio 432  %%%%%%%%%%"

F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def fx(old, new):
    return {"old": old, "new": new}


def tor(page, where, old, new, note="Sheaf Tor underlined in the print (the module Tor^A of these pages is plain, as in the TeX); \\underline{\\Tor} is the file's form (main.tex lines 1126-1162, 5562-5564)."):
    add(page, where, "Tor underlined, the sheaf Tor of O_X-Modules (both scans)", "\\Tor plain", "underline", "high",
        fx(old, new), note)


# ---------------------------------------------------------------- page 431
add(431, "start of page (folio-431 marker)",
    "p. 430 ends '... alternée (i.e. telle que pour tout'; p. 431 begins 'x ∈ P., on ait x² = 0), alors il en est de même pour ⊕ Tor_i^A(B,C).' (both scans; crops_431_435/w431_top.png, b426_430/page_430_s4.png)",
    "page_430.tex ends 'pour tout \\(x\\in P_\\bullet\\), on ait \\(x^2=0\\)),' above the folio-431 marker; page_431.tex begins 'alors il en est de même'",
    "marker", "high", None,
    "Page 431 really begins at '\\(x\\in P_\\bullet\\), on ait \\(x^2=0\\)),'. Exact edit in main.tex, both layers (diplomatic lines 10773-10775, current 10779-10781): replace 'pour tout \\(x\\in P_\\bullet\\), on ait \\(x^2=0\\)),\\n" + M431 + "\\nalors il en est de même' by 'pour tout\\n" + M431 + "\\n\\(x\\in P_\\bullet\\), on ait \\(x^2=0\\)), alors il en est de même' (old string once per layer; simulated in memory: crops_431_435/sim_markers.py). The sentence runs on, so no blank line.")

add(431, "statements of pp. 431-435: Lemme 2.4 (p. 431), Proposition 2.5 (pp. 431-432), Proposition 2.7 (p. 435)",
    "underlined word group by word group (both scans): Lemme 2.4 'Soient', 'deux', 'schémas', 'et', 'M', 'un', '-Module plat', 'Alors', 'pour tout', 'on a un isomorphisme canonique'; Prop. 2.5 'Soient', 'un schéma', 'et', 'deux sous-schémas fermés de', 'On suppose que pour tout', 'il existe un voisinage ouvert', p. 432 'de', 'et une suite de sections', 'de', 'telles que le complexe de Koszul associé à', 'soit une résolution de', 'le complexe de Koszul associé à', 'une résolution de', 'et le complexe de Koszul associé à', 'une résolution de', 'conditions satisfaites en particulier dans le cas noethérien si la suite', 'est régulière et si', 'Soient', 'les idéaux de', 'On a alors les isomorphismes suivants', 'où on note', 'l'immersion de', 'dans', 'et', 'l'immersion de', 'dans', 'En particulier', 'pour toute immersion fermée régulière', 'on a'; Prop. 2.7 'Soient', 'un schéma ayant un faisceau ample', 'une immersion fermée régulière', 'le faisceau conormal de', 'dans', 'Alors', 'pour tout', 'on a la relation', 'où', 'est la classe de', 'dans', 'et'; formulas, letters and punctuation plain; the labels underline only the word",
    "the statements in roman (no \\underline, no \\emph)", "underline", "high", None,
    "Exposé VII follows the Exposé II pattern of GLOBAL_ISSUES 82 (pending volume decision), as findings_416_420 reports for pp. 416-420: not itemized. No emphasized defined terms and no category letter on pp. 431-435.")

add(431, "letters of sheaves and complexes on pp. 431-435",
    "underlined in the print (both scans): M of Lemme 2.4 and its display (3), 'M est défini' (p. 431); I, J ('Soient I, J', I∩J/I.J), N_{Y/X}, N_{Z/X}, N_{T/X} of ii) and ii'), E, E' and the K of K.(u), K.(v) (p. 432); every K.(u), K.(v) and E of ∧^pE, ∧^iE (p. 433); I, J, N_{Y/X}, N_{Z/X}, N_{T/X}, K, the 0 opening the exact sequence 0 → I∩J/I.J → ... (p. 434); N_{T/X}, N_{Y/X}, N_{Z/X}, L˙ (3), N of Proposition 2.7 (p. 435). Plain in the print: X, Y, Z, T, U, x, f_i, g_j, h_k, u, v, A, A', A'', B, C, P., the A'-module M (p. 431), the K.. of the spectral sequence (p. 433), the class N and the N of λ_{-1}(N) (p. 435)",
    "all plain", "underline", "high", None,
    "Convention of the Exposé VII transcription (findings_416_420, after Exposé VI): not itemized. Two places where the plain letter merges two printed letters: p. 431 '\\(M\\) est défini par un \\(A'\\)-module plat \\(M\\)' (sheaf M̲, module M); p. 435 'où \\(N\\) est la classe de \\(N\\)' (class N, sheaf N̲). Three examples in the form to use if the diplomatic layer reproduces the underline: p. 431 '; \\(M\\) est défini' -> '; \\(\\underline{M}\\) est défini'; p. 432 'Soient \\(I,J\\) les idéaux' -> 'Soient \\(\\underline{I},\\underline{J}\\) les idéaux'; p. 435 'est la classe de \\(N\\) dans' -> 'est la classe de \\(\\underline{N}\\) dans'. The underlined O written \\cO falls under the pending volume decision.")

tor(431, "2.3: 'et définissent sur ⊕_{i≥0} Tor_i^{O_X}(O_{X'},O_{X''}) une structure'",
    "\\bigoplus_{i\\ge0}\\Tor_i^{\\cO_X}", "\\bigoplus_{i\\ge0}\\underline{\\Tor}_i^{\\cO_X}",
    "Sheaf Tor underlined in the print; the module Tor_i^A(B,C) of the same paragraph is plain, as in the TeX. \\underline{\\Tor} is the file's form (main.tex lines 1126-1162, 5562-5564; findings_046_050, findings_226_230). Exposé VII writes all its 54 sheaf Tor plain.")

add(431, "Lemme 2.4, the display",
    "no equation number: the display 'Tor_i^{O_X}(M,O_X'') ≃ M ⊗_{O_X'} Tor_i^{O_X}(O_X',O_X'') .' stands alone, its left margin empty (both scans; crops_431_435/w431_mid.png)",
    "\\begin{equation}\\tag{2.4.1}", "extra", "high", fx("\\begin{equation}\\tag{2.4.1}", "\\begin{equation}\\notag"),
    "The number is the TeX's addition; Exposé VII never cites (2.4.1). \\notag as in the applied p. 403 entry (findings_401_405). Independent of the two Tor entries of the display.")

tor(431, "Lemme 2.4, display, left member Tor_i^{O_X}(M,O_X'')", "\\Tor_i^{\\cO_X}(M,", "\\underline{\\Tor}_i^{\\cO_X}(M,", "As in 2.3.")
tor(431, "Lemme 2.4, display, right member M ⊗_{O_X'} Tor_i^{O_X}(O_X',O_X'')", "M\\otimes_{\\cO_{X'}}\\Tor_i^{\\cO_X}",
    "M\\otimes_{\\cO_{X'}}\\underline{\\Tor}_i^{\\cO_X}", "As in 2.3.")

add(431, "'Il suffit de définir un isomorphisme fonctoriel dans le cas affine'",
    "begins a new, indented paragraph after the display of Lemme 2.4 (both scans)",
    "'\\end{equation}' followed directly by 'Il suffit' (the paragraph runs on)", "other", "high",
    fx("\\end{equation}" + NL + "Il suffit", "\\end{equation}" + NL + NL + "Il suffit"), "Missing paragraph break.")

add(431, "'Soient alors X = Spec(A), X' = Spec(A'), X'' = Spec(A'') ; M est défini'",
    "begins a new, indented paragraph after '... dans le cas général.' (both scans)",
    "'... dans le cas général. Soient alors' in one paragraph", "other", "high",
    fx("dans le cas général. Soient alors", "dans le cas général." + NL + NL + "Soient alors"), "Missing paragraph break.")

add(431, "'M est défini par un A'-module plat M, Soit P. une résolution projective'",
    "'plat M, Soit': a comma after the (overstruck) M before the capital S (both scans; crops_431_435/c431_Msoit.png, w431_Msoit.png)",
    "plat \\(M\\). Soit (silently corrected)", "misprint_in_print", "medium",
    fx("plat \\(M\\). Soit", "plat \\(M\\), Soit"),
    "Typist's comma for the full stop that the capital 'Soit' requires. The current layer also reads '\\(M\\). Soit' (the corrected edition keeps it).",
    corrected="plat \\(M\\). Soit")

add(431, "'Par ailleurs, l'isomomorphisme canonique : M ⊗_{A'}(A'⊗_A P.) ≃ M ⊗_A P.'",
    "'l'isomomorphisme' (both scans; crops_431_435/c431_isomom.png, w431_isomom.png)",
    "l'isomorphisme (silently corrected)", "misprint_in_print", "high",
    fx("Par ailleurs, l'isomorphisme", "Par ailleurs, l'isomomorphisme"),
    "Doubled syllable of the typist. The current layer also reads 'l'isomorphisme'.",
    corrected="Par ailleurs, l'isomorphisme")

# ---------------------------------------------------------------- page 432
add(432, "start of page (folio-432 marker)",
    "p. 431 ends 'il existe un voisinage ouvert'; p. 432 begins 'U de x, et une suite de sections f_1,...' (both scans; crops_431_435/w432_top.png)",
    "page_431.tex ends 'il existe un voisinage ouvert \\(U\\) de \\(x\\), et une' above the folio-432 marker; page_432.tex begins 'suite de sections'",
    "marker", "high", None,
    "Page 432 really begins at '\\(U\\) de \\(x\\), et une'. Exact edit in main.tex, both layers (diplomatic lines 10789-10791, current 10795-10797): replace 'il existe un voisinage ouvert \\(U\\) de \\(x\\), et une\\n" + M432 + "\\nsuite de sections' by 'il existe un voisinage ouvert\\n" + M432 + "\\n\\(U\\) de \\(x\\), et une suite de sections' (old string once per layer; simulated: crops_431_435/sim_markers.py). The statement runs on, so no blank line.")

add(432, "Proposition 2.5: 'si la suite f_1,...,f_p,g_1,...g_r,h_1,...,h_s est régulière'",
    "'g_1,...g_r': no comma between the dots and g_r (both scans; crops_431_435/c432_suite.png, w432_top.png); the four other lists of the page have it",
    "g_1,\\ldots,g_r (silently corrected)", "misprint_in_print", "high",
    fx("\\ldots,g_r,h_1,\\ldots,h_s\\) est", "\\ldots g_r,h_1,\\ldots,h_s\\) est"),
    "Dropped comma of the typist. The current layer also reads 'g_1,\\ldots,g_r'.",
    corrected="g_1,\\ldots,g_r")

tor(432, "Proposition 2.5 i), left member Tor_i^{O_X}(O_Y,O_Z)", "\\Tor_i^{\\cO_X}(\\cO_Y,\\cO_Z)\\xrightarrow",
    "\\underline{\\Tor}_i^{\\cO_X}(\\cO_Y,\\cO_Z)\\xrightarrow", "As on p. 431.")
tor(432, "Proposition 2.5 i), right member ∧^i Tor_1^{O_X}(O_Y,O_Z)", "\\bigwedge^i\\Tor_1^{\\cO_X}(\\cO_Y,\\cO_Z);",
    "\\bigwedge^i\\underline{\\Tor}_1^{\\cO_X}(\\cO_Y,\\cO_Z);", "As on p. 431.")
tor(432, "Proposition 2.5 ii), Tor_1^{O_X}(O_Y,O_Z) ≃ I∩J/I.J", "\\Tor_1^{\\cO_X}(\\cO_Y,\\cO_Z)\\simeq",
    "\\underline{\\Tor}_1^{\\cO_X}(\\cO_Y,\\cO_Z)\\simeq", "As on p. 431.")
tor(432, "Proposition 2.5 i'), left member Tor_i^{O_X}(O_Y,O_Y)", "\\Tor_i^{\\cO_X}(\\cO_Y,\\cO_Y)\\xrightarrow",
    "\\underline{\\Tor}_i^{\\cO_X}(\\cO_Y,\\cO_Y)\\xrightarrow", "As on p. 431.")
tor(432, "Proposition 2.5 i'), right member ∧^i Tor_1^{O_X}(O_Y,O_Y)", "\\bigwedge^i\\Tor_1^{\\cO_X}(\\cO_Y,\\cO_Y);",
    "\\bigwedge^i\\underline{\\Tor}_1^{\\cO_X}(\\cO_Y,\\cO_Y);", "As on p. 431.")
tor(432, "Proposition 2.5 ii'), Tor_1^{O_X}(O_Y,O_Y) ≃ N_{Y/X}", "\\Tor_1^{\\cO_X}(\\cO_Y,\\cO_Y)\\simeq",
    "\\underline{\\Tor}_1^{\\cO_X}(\\cO_Y,\\cO_Y)\\simeq", "As on p. 431.")

add(432, "proof of Proposition 2.5, first words",
    "the indented paragraph 'i) On a vu en 2.3 que ⊕ Tor_i^{O_X}(O_Y,O_Z) pouvait être muni ...' follows ii') directly; no label (both scans; crops_431_435/w432_bot.png)",
    "\\emph{Démonstration.} i) On a vu", "extra", "high", fx("\\emph{Démonstration.} i) On a vu", "i) On a vu"),
    "The transcription's proof label, as on pp. 416, 418, 420 (findings_416_420; main.tex line 10813).")

tor(432, "proof i): 'On a vu en 2.3 que ⊕_{i≥0} Tor_i^{O_X}(O_Y,O_Z) pouvait être muni'",
    "\\bigoplus_{i\\ge0}\\Tor_i^{\\cO_X}(\\cO_Y,\\cO_Z)\\) pouvait", "\\bigoplus_{i\\ge0}\\underline{\\Tor}_i^{\\cO_X}(\\cO_Y,\\cO_Z)\\) pouvait",
    "As on p. 431; independent of the label entry above.")
tor(432, "(2.5.1), left member ∧ Tor_1^{O_X}(O_Y,O_Z)", "\\bigwedge \\Tor_1^{\\cO_X}", "\\bigwedge \\underline{\\Tor}_1^{\\cO_X}", "As on p. 431.")
tor(432, "(2.5.1), right member ⊕_{i≥0} Tor_i^{O_X}(O_Y,O_Z)", "\\bigoplus_{i\\ge0}\\Tor_i^{\\cO_X}(\\cO_Y,\\cO_Z),",
    "\\bigoplus_{i\\ge0}\\underline{\\Tor}_i^{\\cO_X}(\\cO_Y,\\cO_Z),", "As on p. 431.")

# ---------------------------------------------------------------- page 433
tor(433, "'de type fini, les Tor_i^{O_X}(O_Y,O_Z) sont les faisceaux d'homologie'", "fini, les \\(\\Tor_i^{\\cO_X}",
    "fini, les \\(\\underline{\\Tor}_i^{\\cO_X}", "As on p. 431.")

add(433, "'On considère la suite spectrale telle que 'E²_{pq} = H^I_p(H^{II}_q(K..))'",
    "'K..': two dots side by side, no comma (both scans; crops_431_435/c433_Kdd.png, w433_top.png)",
    "K_{\\bullet,\\bullet}", "punctuation", "medium", fx("K_{\\bullet,\\bullet}", "K_{\\bullet\\bullet}"),
    "The comma between the two indices is the TeX's addition.")

add(433, "'car les immersions Z → X, et T → Z → X sont régulières'",
    "a comma after 'Z → X' (both scans; crops_431_435/c433_ZXet.png, w433_mid.png)",
    "\\(Z\\to X\\) et \\(T\\to Z\\to X\\)", "punctuation", "high", fx("\\(Z\\to X\\) et", "\\(Z\\to X\\), et"), "")

tor(433, "'Par conséquent la suite spectrale dégénère, et les Tor_i^{O_X}(O_Y,O_Z) sont'", "dégénère, et les \\(\\Tor_i^{\\cO_X}",
    "dégénère, et les \\(\\underline{\\Tor}_i^{\\cO_X}", "As on p. 431.")
tor(433, "(2.5.2), left member Tor_i^{O_X}(O_Y,O_Z)", "\\tag{2.5.2}" + NL + "\\Tor_i", "\\tag{2.5.2}" + NL + "\\underline{\\Tor}_i", "As on p. 431.")

add(433, "(2.5.2), second arrow: 'O_T⊗_{O_X} ∧^iE → ∧^i(O_T)^p'",
    "a plain arrow without tilde; the first arrow of the display carries its tilde (both scans; crops_431_435/c433_arrow2.png, w433_mid.png)",
    "\\xrightarrow{\\sim} (both arrows)", "symbol", "high",
    fx("\\xrightarrow{\\sim}" + NL + "\\bigwedge^i(\\cO_T)^p", "\\longrightarrow" + NL + "\\bigwedge^i(\\cO_T)^p"), "")

add(433, "'En particulier, on trouve pour i = 1 :'",
    "begins a new, indented paragraph after (2.5.2) (both scans)",
    "'\\end{equation}' followed directly by 'En particulier' (the paragraph runs on)", "other", "high",
    fx("\\end{equation}" + NL + "En particulier", "\\end{equation}" + NL + NL + "En particulier"),
    "Missing paragraph break. 'd'où pour tout i :' below continues at the left margin, as in the TeX.")

tor(433, "display for i = 1: Tor_1^{O_X}(O_Y,O_Z) ≃ (O_T)^n", "\\Tor_1^{\\cO_X}", "\\underline{\\Tor}_1^{\\cO_X}",
    "As on p. 431; the old stops before the misprinted exponent of the next entry.")

add(433, "display for i = 1: 'Tor_1^{O_X}(O_Y,O_Z) ≃ (O_T)^n ,'",
    "exponent n (both scans; crops_431_435/w433_bot.png)",
    "(\\cO_T)^n (printed reading kept)", "misprint_in_print", "high", None,
    "E = (O_X)^p, and (2.5.2) for i = 1 gives ∧^1(O_T)^p; the proof has no n. The current layer already reads (\\cO_T)^p.",
    corrected="(\\cO_T)^p")

tor(433, "(2.5.3), left member Tor_i^{O_X}(O_Y,O_Z)", "\\tag{2.5.3}" + NL + "\\Tor_i", "\\tag{2.5.3}" + NL + "\\underline{\\Tor}_i", "As on p. 431.")
tor(433, "(2.5.3), right member ∧^i Tor_i^{O_X}(O_Y,O_Z)", "\\bigwedge^i\\Tor", "\\bigwedge^i\\underline{\\Tor}",
    "As on p. 431; the old stops before the misprinted index of the next entry.")

add(433, "(2.5.3), right member: '∧^i Tor_i^{O_X}(O_Y,O_Z)'",
    "the Tor under ∧^i has the index i (both scans; crops_431_435/c433_253.png, w433_bot.png)",
    "\\bigwedge^i\\Tor_i^{\\cO_X}(\\cO_Y,\\cO_Z) (printed reading kept)", "misprint_in_print", "high", None,
    "(2.5.3) follows from (2.5.2) and the case i = 1: Tor_i ≃ ∧^i Tor_1, as in 2.5 i). 'corrected' is given with the underline of the entry above. The current layer already reads \\bigwedge^i\\Tor_1.",
    corrected="\\bigwedge^i\\underline{\\Tor}_1^{\\cO_X}(\\cO_Y,\\cO_Z)")

# ---------------------------------------------------------------- page 434
add(434, "'Or il résulte de 2.2 que l'isomorphisme :'",
    "a colon after 'l'isomorphisme' (both scans; crops_431_435/w434_top.png)",
    "que l'isomorphisme (no colon)", "punctuation", "high",
    fx("que l'isomorphisme" + NL + "\\[", "que l'isomorphisme:" + NL + "\\["), "")

add(434, "first display: '∧(O_T)^n ≃ ⊕_{i≥0} Tor_i^{O_X}(O_Y,O_Z)'",
    "exponent n (both scans; crops_431_435/w434_top.png)",
    "\\bigwedge(\\cO_T)^n (printed reading kept)", "misprint_in_print", "high", None,
    "The isomorphism is 'défini par les isomorphismes (2.5.2)', whose terms are ∧^i(O_T)^p; the same n as on p. 433. The current layer still reads (\\cO_T)^n here, although it corrects p. 433: the corrected edition needs (\\cO_T)^p.",
    corrected="\\bigwedge(\\cO_T)^p")

tor(434, "first display, right member ⊕_{i≥0} Tor_i^{O_X}(O_Y,O_Z)",
    "\\Tor_i^{\\cO_X}(\\cO_Y,\\cO_Z)" + NL + "\\]" + NL + "défini par les isomorphismes (2.5.2)",
    "\\underline{\\Tor}_i^{\\cO_X}(\\cO_Y,\\cO_Z)" + NL + "\\]" + NL + "défini par les isomorphismes (2.5.2)", "As on p. 431.")

add(434, "'il en est donc de même pour l'isomorphisme :'",
    "a colon after 'l'isomorphisme' (both scans; crops_431_435/w434_top.png)",
    "pour l'isomorphisme (no colon)", "punctuation", "high",
    fx("pour l'isomorphisme" + NL + "\\[", "pour l'isomorphisme:" + NL + "\\["), "")

tor(434, "second display, left member ∧ Tor_i^{O_X}(O_Y,O_Z)", "\\bigwedge\\Tor", "\\bigwedge\\underline{\\Tor}",
    "As on p. 431; the old stops before the misprinted index of the next entry.")

add(434, "second display, left member: '∧ Tor_i^{O_X}(O_Y,O_Z)'",
    "index i under the ∧ (both scans; crops_431_435/c434_disp2.png, w434_top.png)",
    "\\bigwedge\\Tor_i^{\\cO_X}(\\cO_Y,\\cO_Z) (printed reading kept)", "misprint_in_print", "high", None,
    "The exterior algebra of Tor_1, as in (2.5.1) and (2.5.3). 'corrected' is given with the underline of the entry above. The current layer already reads \\bigwedge\\Tor_1.",
    corrected="\\bigwedge\\underline{\\Tor}_1^{\\cO_X}(\\cO_Y,\\cO_Z)")

tor(434, "second display, right member ⊕_{i≥0} Tor_i^{O_X}(O_Y,O_Z)",
    "\\Tor_i^{\\cO_X}(\\cO_Y,\\cO_Z)" + NL + "\\]" + NL + "défini par les isomorphismes (2.5.3)",
    "\\underline{\\Tor}_i^{\\cO_X}(\\cO_Y,\\cO_Z)" + NL + "\\]" + NL + "défini par les isomorphismes (2.5.3)", "As on p. 431.")

add(434, "'et la suite exacte des Tor qui en résulte :'",
    "Tor underlined (both scans; crops_431_435/w434_top.png)", "des Tor qui (plain text)", "underline", "high",
    fx("des Tor qui", "des \\(\\underline{\\Tor}\\) qui"),
    "The sheaf Tor in running text, as '«~$\\underline{\\Tor}$ simultanés' (findings_046_050).")

tor(434, "exact sequence '0 → Tor_1^{O_X}(O_Y,O_Z) → I⊗_{O_X}O_Z → O_Z .'", "0\\longrightarrow\\Tor_1",
    "0\\longrightarrow\\underline{\\Tor}_1", "As on p. 431.")
tor(434, "'Il en résulte que Tor_1^{O_X}(O_Y,O_Z) est le noyau de l'homomorphisme :'", "que \\(\\Tor_1",
    "que \\(\\underline{\\Tor}_1", "As on p. 431.")

# ---------------------------------------------------------------- page 435
tor(435, "'comme Tor_1^{O_X}(O_Y,O_Z) est de rang p d'après la démonstration du i)'", "comme \\(\\Tor_1",
    "comme \\(\\underline{\\Tor}_1", "As on p. 431.")

add(435, "K˙ on p. 435 (2.6 and Proposition 2.7): 'les K˙ formés', 'i_* : K˙(Y) → K˙(X)', 'x ∈ K˙(Y)', 'dans K˙(Y)'",
    "K with a raised dot, five places (both scans; crops_431_435/w435_bot.png)",
    "K^\\circ (five places)", "symbol", "high", None,
    "The Exposé VII convention reported in findings_416_420 (K^\\circ for the print's K˙, 173 in folios 416-465; one script K^\\circ -> K^{\\bullet} for VII, both layers): not itemized. Three examples: 'que les \\(K^\\circ\\) formés' -> 'que les \\(K^{\\bullet}\\) formés'; '\\(i_*:K^\\circ(Y)\\longrightarrow K^\\circ(X)\\)' -> '\\(i_*:K^{\\bullet}(Y)\\longrightarrow K^{\\bullet}(X)\\)'; 'pour tout \\(x\\in K^\\circ(Y)\\)' -> 'pour tout \\(x\\in K^{\\bullet}(Y)\\)'.")

add(435, "2.6: 'la classe du complexe R̳i_*(L˙) = i_*(L˙)'",
    "R with a double underline, the double-struck R of the derived functor (both scans; crops_431_435/c435_Ri.png, w435_bot.png)",
    "\\(Ri_*(L^\\bullet)", "font", "high", fx("\\(Ri_*(L^\\bullet)", "\\(\\mathbb Ri_*(L^\\bullet)"),
    "Double-struck R written plain (reported singly as asked); \\mathbb R as in the applied fixes of pp. 167-217. Page 436 has the same: \\mathrm L i^*(Ri_*(M)) and Ri_*(M) for the print's double-underlined L and R.")

add(435, "Proposition 2.7, the display",
    "no equation number: 'i*(i_*(x)) = x.λ_{-1}(N) ,' stands alone, its left margin empty (both scans; crops_431_435/c435_disp.png, w435_bot.png)",
    "\\begin{equation}\\tag{2.7.1}", "extra", "high", fx("\\begin{equation}\\tag{2.7.1}", "\\begin{equation}\\notag"),
    "The number is the TeX's addition; Exposé VII never cites (2.7.1) (main.tex has it only as this tag in folios 416-465).")

add(435, "end of page: the proof label of Proposition 2.7",
    "p. 435 ends with 'où N est la classe de N dans K˙(Y), et λ_{-1}(N) = Σ (-1)^i λ^i(N).'; p. 436 begins with the indented paragraph 'Comme les deux membres de la relation à démontrer sont additifs ...'; no label on either page (both scans; crops_431_435/w436_top.png)",
    "\\emph{Démonstration.} (last line of page_435.tex)", "extra", "high", fx("\\emph{Démonstration.}", ""),
    "The transcription's proof label (main.tex line 10893), as on p. 432. Leaves a blank line before the folio-436 marker, so 'Comme les deux membres' stays a new paragraph, as printed.")

# ---------------------------------------------------------------- checks
ok = True
pages = {}
for p in range(431, 436):
    pages[p] = (B / f"page_{p}.tex").read_text(encoding="utf-8")
work = dict(pages)
for i, f in enumerate(F):
    if f["fix"] is None:
        continue
    t = pages[f["page"]]
    old = f["fix"]["old"]
    n = t.count(old)
    if n != 1:
        ok = False
        print("NOT UNIQUE", i, f["page"], n, repr(old))
    if "%%%%%%%%%%" in old or "%%%%%%%%%%" in f["fix"]["new"]:
        ok = False
        print("MARKER IN FIX", i)
    w = work[f["page"]]
    m = w.count(old)
    if m != 1:
        ok = False
        print("BROKEN BY EARLIER FIX", i, f["page"], m, repr(old))
    else:
        work[f["page"]] = w.replace(old, f["fix"]["new"], 1)
print("checks ok" if ok else "CHECKS FAILED")
counts = {}
for f in F:
    k = "misprint" if f["kind"] == "misprint_in_print" else "normal"
    counts.setdefault(f["page"], {"normal": 0, "misprint": 0})[k] += 1
print(counts, len(F))
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
print("written", OUT)
# write the patched pages to the crops folder for a look (not the real files)
for p, t in work.items():
    (pathlib.Path(__file__).resolve().parent / f"patched_{p}.tex").write_text(t, encoding="utf-8")
