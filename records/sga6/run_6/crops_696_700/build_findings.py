"""Build findings_696_700.json (SGA 6 scan check, pages 696-700)."""
import json
import pathlib

OUT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\findings_696_700.json")
C = "crops_696_700/"
F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, confidence=conf, fix=fix)
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def fx(old, new):
    return {"old": old, "new": new}


# ---------------- printed page 696 ----------------
add(696, "entry 'D(_A S)_coh , D (_A S)_n-coh  I  2.15', "
         "first item",
    r"'D(_A S̲' followed directly by the index 'coh': no closing parenthesis after the underlined S; the second item "
    r"has it, 'D (_A S̲)_n-coh' (both scans; " + C + "p696_Dcoh.png, w696_Dcoh.png)",
    r"\Dcat({}_{A}\underline S)_{\coh}, (parenthesis supplied)",
    "misprint_in_print", "high",
    fx(r"\Dcat({}_{A}\underline S)_{\coh},", r"\Dcat({}_{A}\underline S_{\coh},"),
    "Typing error of the print (the closing parenthesis is left out). The TeX silently corrects it; the fix restores "
    "the printed reading.",
    corrected=r"\Dcat({}_{A}\underline S)_{\coh},")

add(696, "entry 'C^P_num(X)  XIII  5.2'",
    r"capital P as the upper index, C^P_num(X): flat top and foot bar of a capital, not the round bowl and short "
    r"descender of this page's small p in 'App.' (both scans; " + C + "cmp_P_p.png, p696_Cpnum.png, w696_Cp.png)",
    r"C^p_{\num}(X)",
    "misprint_in_print", "medium",
    fx(r"C^p_{\num}(X)", r"C^P_{\num}(X)"),
    r"Exposé XIII 5.2 writes C^p_{\rm num}(X) (cycles of codimension p); the index typed a capital P. The TeX "
    r"silently corrects it.",
    corrected=r"C^p_{\num}(X)")

# ---------------- printed page 697 ----------------
add(697, "entry 'f^* (entre les K^•)  IV  2.7'",
    r"K with a raised dot, K^• (witness clear; " + C + "w697_Kdot.png)",
    r"\(K'\)",
    "symbol", "high",
    fx(r"\(K'\)) & IV & 2.7", r"\(K^{\bullet}\)) & IV & 2.7"),
    r"As decided for Exposé IV on 10 Nov: the print's raised dot is K^{\bullet}, not a prime. The index writes a "
    r"prime for the raised dot of K and Gr in 13 places (pp. 697-698), each listed here.")

add(697, "entry 'f_* (entre les K^•)  IV  2.12'",
    r"K with a raised dot, K^• (both scans)",
    r"\(K'\)",
    "symbol", "high",
    fx(r"\(K'\)) & IV & 2.12", r"\(K^{\bullet}\)) & IV & 2.12"),
    r"Raised dot written as a prime (see the 2.7 entry).")

add(698, "printed p. 697 (text now under the folio-698 marker), entry 'F'_{>n} , F'_{≤n}  I  2.12'",
    r"both truncations are lower indices: F' with '>n' below the line, like F'_{≤n} (both scans; " + C +
    "p697_Fn.png, w697_Fn.png)",
    r"F^{\prime >n} ('>n' raised beside the prime)",
    "formula", "high",
    fx(r"F^{\prime >n}", r"F'_{>n}"),
    r"Exposé I writes F'_{>n} (resp. F'_{\leq n}).")

add(698, "printed p. 697 (text now under the folio-698 marker), entry 'Gr^•(X) , Gr.(X)  X  3.1'",
    r"Gr with a raised dot, Gr^• (both scans; " + C + "p697_Grdot.png)",
    r"\operatorname{Gr}'(X)",
    "symbol", "high",
    fx(r"\operatorname{Gr}'(X)", r"\operatorname{Gr}^{\bullet}(X)"),
    r"The print's raised dot in Gr is \bullet (volume decision); the index's TeX has a prime.")

add(698, "printed p. 697 (text now under the folio-698 marker), entry 'Gr^•_alg , Gr^alg_•  X App.  7.11'",
    r"Gr with a raised dot and index alg, Gr^•_alg (both scans)",
    r"\operatorname{Gr}'_{\alg}",
    "symbol", "high",
    fx(r"\operatorname{Gr}'_{\alg}", r"\operatorname{Gr}^{\bullet}_{\alg}"),
    r"Raised dot written as a prime.")

# ---------------- printed page 698 ----------------
add(698, "start and end of page",
    r"p. 698 (the notation index's p. '3') begins 'Gr^•_num , Gr^num_•  X App.  7.9.4' and ends 'Mod(U)  II  2.0' "
    r"(both scans)",
    r"page_698.tex begins with the last 11 entries of p. 697 ('projectif) & VI & 5.2\\' to "
    r"'\(\operatorname{Gr}'_{\alg},\ ...\) & X App. & 7.11\\'); p. 698 runs from '\(\operatorname{Gr}'_{\num},...' "
    r"to '\(\Mod(U)\) & II & 2.0\\'; the rest of the file ('\(\parfamp_f(E),...' to '\end{document}') is printed on "
    r"pp. 699 and 700, which have no markers.",
    "marker", "high", None,
    r"Page 698 really begins with the Gr_num entry. After this batch's text fixes (which turn its Gr' into "
    r"Gr^{\bullet}): python -I move_marker.py 6 698 '\(\operatorname{Gr}^{\bullet}_{\num}' (before the fixes the "
    r"anchor is '\(\operatorname{Gr}'_{\num}'; simulated on a copy). The marker now splits the entry "
    r"'\(f_*\) (cas du fibré projectif)'; the line break that remains prints as a space. For the missing markers of "
    r"pp. 699 and 700 see the page-699 and page-700 items.")

add(698, "entry 'Gr^•_num , Gr^num_•  X App.  7.9.4'",
    r"Gr with a raised dot and index num, Gr^•_num (both scans)",
    r"\operatorname{Gr}'_{\num}",
    "symbol", "high",
    fx(r"\operatorname{Gr}'_{\num}", r"\operatorname{Gr}^{\bullet}_{\num}"),
    r"Raised dot written as a prime. The folio-698 marker move uses this line as its anchor.")

add(698, "entry 'K^•_alg , K.^alg  X App.  7.11'",
    r"K with a raised dot and index alg (both scans)",
    r"K'_{\alg}",
    "symbol", "high",
    fx(r"K'_{\alg}", r"K^{\bullet}_{\alg}"),
    r"Raised dot written as a prime.")

add(698, "entry 'K^•(_A X) , K.(_A X)  IV  2.2'",
    r"K^•(_A X) , K.(_A X): K with a raised dot, and A as a lower index standing before X (left index) "
    r"(both scans)",
    r"\(K'(A_X),\ K_{\cdot}(A_X)\): a prime, and A with the index X",
    "formula", "high",
    fx(r"\(K'(A_X),\ K_{\cdot}(A_X)\)", r"\(K^{\bullet}({}_{A}X),\ K_{\cdot}({}_{A}X)\)"),
    r"Exposé IV 2.2 writes K^{\bullet}({}_A X) and K_\bullet({}_A X); the left index is written as in this "
    r"index's \Dcat({}_{A}X).")

add(698, "entry 'K^•(_A X)_naïf , K.(_A X)_naïf  IV  2.2'",
    r"K with a raised dot, A as a left lower index before X (both scans)",
    r"\(K'(A_X)_{\naif},\ K_{\cdot}(A_X)_{\naif}\)",
    "formula", "high",
    fx(r"\(K'(A_X)_{\naif},\ K_{\cdot}(A_X)_{\naif}\)",
       r"\(K^{\bullet}({}_{A}X)_{\naif},\ K_{\cdot}({}_{A}X)_{\naif}\)"),
    r"As the entry above (IV 2.2: K^{\bullet}({}_A X)_{\naif}, K_\bullet({}_A X)_{\naif}).")

add(698, "entry 'K^•(f) , K.(f)  IV  3.3.1'",
    r"K with a raised dot (both scans)",
    r"K'(f)",
    "symbol", "high",
    fx(r"K'(f)", r"K^{\bullet}(f)"),
    r"Raised dot written as a prime.")

add(698, "entry 'K^•_num , K.^num  X App.  7.9.4'",
    r"K with a raised dot and index num (both scans)",
    r"K'_{\num}",
    "symbol", "high",
    fx(r"K'_{\num}", r"K^{\bullet}_{\num}"),
    r"Raised dot written as a prime.")

add(698, "entry 'K^•(X) , K.(X)  IV  2.2'",
    r"K with a raised dot (both scans)",
    r"\(K'(X),",
    "symbol", "high",
    fx(r"\(K'(X),", r"\(K^{\bullet}(X),"),
    r"Raised dot written as a prime.")

add(698, "entry 'K^•(X)_naïf , K.(X)_naïf  IV  2.2'",
    r"K with a raised dot (both scans)",
    r"K'(X)_{\naif}",
    "symbol", "high",
    fx(r"K'(X)_{\naif}", r"K^{\bullet}(X)_{\naif}"),
    r"Raised dot written as a prime.")

add(698, "entry 'K^•(X/Y) , K.(X/Y)  IV  3.3.1'",
    r"K with a raised dot (both scans)",
    r"K'(X/Y)",
    "symbol", "high",
    fx(r"K'(X/Y)", r"K^{\bullet}(X/Y)"),
    r"Raised dot written as a prime.")

# ---------------- printed page 699 (text in page_698.tex) ----------------
add(698, "printed p. 699 (no marker; text now under the folio-698 marker), entry "
         "'par.amp_f(E) , par.amp_Y(E)  III  4.1'",
    r"'par.amp' twice, without f (both scans; " + C + "p699_paramp.png, w_699.png)",
    r"\parfamp_f(E),\ \parfamp_Y(E), which prints parf.amp: the index's helper "
    r"\providecommand{\parfamp}{\operatorname{par.amp}} has no effect, because Exposé III's "
    r"\providecommand{\parfamp}{\operatorname{parf.amp}} comes first",
    "misprint_in_print", "high",
    fx(r"\parfamp_f(E),\ \parfamp_Y(E)", r"\operatorname{par.amp}_f(E),\ \operatorname{par.amp}_Y(E)"),
    r"Exposé III 4.1 (folio 250) prints parf.amp; the index's par.amp is a typing error, and the TeX's output "
    r"silently corrects it. The fix restores the printed reading on this line only.",
    corrected=r"\parfamp_f(E),\ \parfamp_Y(E)")

add(698, "printed p. 699 (text now under the folio-698 marker), entry 'Parf(_A S) , Parf(C,C_o) , Parf(S)  I  4.9'",
    r"Parf(_A S̲): A as a lower index standing before the underlined S (both scans; " + C + "p699_Parf_all.png)",
    r"\Parf(A_S): A with the index S",
    "formula", "high",
    fx(r"\Parf(A_S)", r"\Parf({}_{A}\underline S)"),
    r"Written like this index's \Dcat({}_{A}\underline S). The third item, printed Parf(S̲), is \Parf(S) in the TeX: "
    r"pending site-S decision, not itemized; the underlined C, C_o likewise (category letter).")

add(698, "printed p. 699 (text now under the folio-698 marker), entry 'Proj_o  VI  2.3.2'",
    r"Proj underlined, index o (both scans)",
    r"\(\Projz\), which prints a plain Proj_0 here: Exposé VII's \renewcommand{\Projz}{\operatorname{Proj}_0} is "
    r"in force at the index",
    "underline", "high",
    fx(r"\(\Projz\)", r"\(\underline{\operatorname{Proj}}_0\)"),
    r"The form Exposé VI gives \Projz (\underline{\operatorname{Proj}}_0, 10 Nov).")

add(698, "printed p. 699 (text now under the folio-698 marker), entry 'r O_{UxV}  II App. II  1.1'",
    r"a raised r before the underlined O, with U x V as the O's index: ^r O̲_{UxV}; there is no 0 (both scans; " + C +
    "p699_rO.png)",
    r"r^0_{\mathcal O_{U\times V}}: an added upper 0, and the O made an index of r",
    "formula", "high",
    fx(r"r^0_{\mathcal O_{U\times V}}", r"{}^r\mathcal O_{U\times V}"),
    r"II App. II 1.1 writes {}^r\cO_{U\times V} (the sheaf of rings of class C^r). The underlined O stays "
    r"\mathcal O (pending decision on the underlined O).")

add(698, "printed p. 699 (text now under the folio-698 marker), entry 'ρ_t  V  3,4'",
    r"'3,4' with a comma where every other number has a full stop (both scans; " + C + "p699_34.png, w699_34.png)",
    r"3.4",
    "misprint_in_print", "medium",
    fx(r"\(\rho_t\) & V & 3.4", r"\(\rho_t\) & V & 3,4"),
    r"Typing error (comma for the stop); the TeX silently corrects it.",
    corrected=r"\(\rho_t\) & V & 3.4")

add(698, "printed p. 699 (text now under the folio-698 marker), entry 'ψ_k(x)  V  7.1'",
    r"psi with k as a lower index (both scans; " + C + "w699_psi.png)",
    r"\psi_k(x) (as printed)",
    "misprint_in_print", "medium", None,
    r"Exposé V §7 (Appendice, les opérations ψ^k d'Adams) writes \psi^k(x) with an upper index; the TeX keeps the "
    r"printed reading.",
    corrected=r"\psi^k(x)")

# ---------------- printed page 700 (text in page_698.tex) ----------------
add(698, "printed p. 700 (no marker; text now under the folio-698 marker), entry 'x ._N y  V  5.5'",
    r"x, a typed product dot with N below it, then y: x ·_N y (witness clear, " + C + "w700_xNy.png; the main scan "
    r"is blurred there, p700_xNy.png)",
    r"\(x_N\): the dot and the y are lost",
    "formula", "high",
    fx(r"\(x_N\)", r"\(x\cdot_N y\)"),
    r"The multiplication of V (5.5.1), x\cdot_N y=x\cdot y\cdot\lambda_{-1}(N), written as the TeX writes it there.")

add(699, "start and end of page (no folio-699 marker in the TeX)",
    r"p. 699 (the notation index's p. '4') runs from 'par.amp_f(E) , par.amp_Y(E)  III  4.1' to '∇  V  3.5' "
    r"(main scan rendered into " + C + "page_699_s1-s4.png; witness " + C + "w_699.png)",
    r"no marker; the page's text stands in page_698.tex, from '\(\parfamp_f(E),\ \parfamp_Y(E)\) & III & 4.1\\' "
    r"to '\(\nabla\) & V & 3.5\\'",
    "marker", "high", None,
    r"Insert the line '%%%%%%%%%%  scan idx 712  |  folio 699  %%%%%%%%%%' on its own line right after the line "
    r"'\(\Mod(U)\) & II & 2.0\\' (both editions), after this batch's text fixes (those for p. 699 are given under "
    r"page 698).")

add(700, "start and end of page (no folio-700 marker in the TeX)",
    r"p. 700 (the notation index's p. '5') holds '1 + A[[t]]^+  V  1.1' to 'Z(x)  X  1.1.2'; the rest of the page "
    r"is blank (main scan rendered into " + C + "page_700_s1-s4.png; witness " + C + "w_700.png)",
    r"no marker; the text stands at the end of page_698.tex, from '\(1+A[[t]]^+\) & V & 1.1\\' to the end of the "
    r"table and \end{document}",
    "marker", "high", None,
    r"Insert the line '%%%%%%%%%%  scan idx 713  |  folio 700  %%%%%%%%%%' on its own line right after the line "
    r"'\(\nabla\) & V & 3.5\\' (both editions), after this batch's text fixes (those for p. 700 are given under "
    r"page 698).")

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("wrote", OUT, len(F), "findings")
