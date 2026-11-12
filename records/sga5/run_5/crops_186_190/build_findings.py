"""Build findings_186_190.json. Checks, applying the fixes of each page in list order:
- every fix's old occurs exactly once in the live page span of the diplomatic s5.tex (what process_sga.py uses),
- and, where the text is in the batch snapshot page_NNN.tex, exactly once there too;
- the count in the corrected layer is printed for information (replay of non-misprint fixes).
usage: python -I -B build_findings.py [--write]"""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
RUN = W / "run_5"
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")

F = []


def add(page, where, scan, tex, kind, confidence, old=None, new=None, note="", corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, confidence=confidence,
             fix=None if old is None else dict(old=old, new=new))
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


QUOTES = ("Guillemets for the print's straight typewriter quotes; the accepted forms are ``...'' and \"...\" (as "
          "pp. 110, 183, 184); the file writes ``...'' elsewhere in Exposé III B.")
PLAIN_HOM = "Global Hom, plain in the print (the TeX's \\uHom underlines it)."
HEAD = "Number with a full stop in the print, as 6.2.-6.4. (pp. 183, 185)."

# ================================================================ page 186
add(186, "display (6.4.3), top of the page (under the p. 186 marker since the coordinator moved it at 20:36; not in "
         "the batch snapshot page_186.tex)",
    "H^o(X,c_*c^!(D_AL_1 ⊗^L_{S,A} L_2) ⥲ Hom_A(c*_1L_1,c^!_2L_2) .  — two parentheses opened, one closed after L_2",
    r"H^0(X,c_*c^!(D_AL_1\lten_{S,A}L_2))",
    "misprint_in_print", "high",
    r"c_*c^!(D_AL_1\lten_{S,A}L_2))", r"c_*c^!(D_AL_1\lten_{S,A}L_2)",
    "The print lacks the closing parenthesis of H^o(X, ...); the TeX silently adds it.",
    corrected=r"c_*c^!(D_AL_1\lten_{S,A}L_2))")
add(186, "display (6.4.3), right-hand side",
    "Hom_A(c*_1L_1,c^!_2L_2) — Hom not underlined (H^o of the RHom: the global Hom)",
    r"\uHom_A(c_1^*L_1,c_2^!L_2).",
    "underline", "high",
    "\\uHom_A(c_1^*L_1,c_2^!L_2).\n\\tag{6.4.3}", "\\Hom_A(c_1^*L_1,c_2^!L_2).\n\\tag{6.4.3}",
    PLAIN_HOM)
add(186, "'Les éléments de Hom_A(c*_1L_1,c^!_2L_2) s'appelleront'",
    "Hom_A not underlined", r"$\uHom_A(c_1^*L_1,c_2^!L_2)$",
    "underline", "high",
    r"Les éléments de $\uHom_A(c_1^*L_1,c_2^!L_2)$", r"Les éléments de $\Hom_A(c_1^*L_1,c_2^!L_2)$",
    PLAIN_HOM + " These are the elements of the right side of 6.4.3.")
add(186, "'s'appelleront correspondances cohomologiques de L_1 à L_2 à support dans c'",
    "underlined: 'correspondances cohomologiques de', 'à' (between L_1 and L_2), 'à support dans'; not L_1, L_2, c",
    "no underline", "underline", "high",
    r"s'appelleront correspondances cohomologiques de $L_1$ à $L_2$ à support dans",
    r"s'appelleront \emph{correspondances cohomologiques de} $L_1$ \emph{à} $L_2$ \emph{à support dans}",
    "Defined term, underlined in the print; \\emph is this exposé's command for the underline (as 'la \\emph{pente}' "
    "on p. 154).")
add(186, "'c (la terminologie diffère ... de (loc. cit.), les deux ... dans la pratique).'",
    "c (la terminologie diffère légèrement de celle de (loc. cit.), les deux terminologies coïncident pour c propre, "
    "ce qui est le cas dans la pratique).",
    "$c$. La terminologie ... de (loc. cit.); les deux ... dans la pratique.",
    "punctuation", "high",
    ". La terminologie diffère légèrement de celle de (loc. cit.); les deux terminologies coïncident pour $c$ propre, "
    "ce qui est le cas dans la pratique.",
    " (la terminologie diffère légèrement de celle de (loc. cit.), les deux terminologies coïncident pour $c$ propre, "
    "ce qui est le cas dans la pratique).",
    "The TeX turns the print's parenthesis into a sentence and its comma into a semicolon; one edit, so that the two "
    "parentheses stay together.")
add(186, "'des flèches \"image directe\" analogues'",
    "straight typewriter double quotes: \"image directe\"", "« image directe »",
    "punctuation", "high", "« image directe »", "``image directe''", QUOTES)
add(186, "'(III 3.7.6) (pour L_i ∈ ob D_ctf(_AX_i)) .'",
    "(III 3.7.6) (pour L_i ∈ ob D_ctf(_AX_i))  .", r"(III 3.7.6), pour $L_i\in\Ob D_{\mathrm{ctf}}({}_AX_i)$.",
    "punctuation", "high",
    r"(III 3.7.6), pour $L_i\in\Ob D_{\mathrm{ctf}}({}_AX_i)$.",
    r"(III 3.7.6) (pour $L_i\in\Ob D_{\mathrm{ctf}}({}_AX_i)$).",
    "The print has no comma and puts 'pour L_i ...' in parentheses.")
add(186, "number of no. 6.5", "'6.5.' with a full stop", r"\subsection*{6.5}",
    "punctuation", "high", r"\subsection*{6.5}", r"\subsection*{6.5.}", HEAD)
add(186, "6.5, 'p_1 , p_2 : X^2 ⇉ X les projections canoniques'",
    "a double arrow ⇉ (two parallel arrows)", r"$p_1,p_2:X^2\to X$",
    "symbol", "high", r"$p_1,p_2:X^2\to X$", r"$p_1,p_2:X^2\rightrightarrows X$",
    "\\rightrightarrows (amssymb) is already used in s5.tex.")
add(186, "'On définit un homomorphisme \"trace locale\"'",
    "\"trace locale\" in straight quotes, the words underlined (not the quotes)", "« trace locale »",
    "underline", "high", "« trace locale »", r"``\emph{trace locale}''",
    "Defined term, underlined in the print; the same edit replaces the guillemets by the print's straight quotes.")
add(186, "display (6.5.6), printed at the top of p. 187 (still under the p. 186 marker, see the marker finding of p. 187)",
    "D_AL ⊗^L_A L ⟶ KA_{X,L♮}  — no punctuation after the display", r"KA_{X,L_{\natural}}.",
    "punctuation", "high",
    "KA_{X,L_{\\natural}}.\n\\tag{6.5.6}", "KA_{X,L_{\\natural}}\n\\tag{6.5.6}",
    "Full stop added by the TeX. Filed under page 186, where the display sits until the p. 187 marker is moved: "
    "apply before that move (or look it up on page 187 after it).")

# ================================================================ page 187
add(187, "top of the page",
    "p. 187 begins 'et la flèche d'évaluation 5.3.5' and the display (6.5.6); p. 186 ends with (6.5.5) "
    "'δ*(D_AL ⊗_{S,A} L) = D_AL ⊗_A L ,'",
    "'et la flèche d'évaluation 5.3.5', '\\begin{equation}', the (6.5.6) formula and its \\tag are the last four "
    "lines of page_186.tex; the folio-187 marker stands before the '\\end{equation}' of 6.5.6",
    "marker", "high", None, None,
    "Page 187 really begins at 'et la flèche d'évaluation 5.3.5'. Exact fix: python -I move_marker.py 5 187 "
    "\"et la flèche d'évaluation 5.3.5\" --before (simulated in memory on both layers: the marker then stands "
    "between the \\end{equation} of 6.5.5 and 'et la flèche').")
add(187, "'grâce à 6.3.2 K_X ⊗^L A = KA_X )'",
    "K_X ⊗ A with an L above the tensor sign", r"$K_X\otimes A=KA_X$",
    "formula", "high", r"$K_X\otimes A=KA_X$", r"$K_X\lten A=KA_X$",
    "The print's derived tensor (plain L above ⊗), as in the rest of the line.")
add(187, "display (6.5.9)", "Tr_A : Hom_A(c*_1L,c^!_2L) ⟶ H^o(X^c,KA_{X^c,L♮}) — Hom not underlined",
    r"\Tr_A:\uHom_A(c_1^*L,c_2^!L)",
    "underline", "high", r"\Tr_A:\uHom_A(c_1^*L,c_2^!L)", r"\Tr_A:\Hom_A(c_1^*L,c_2^!L)",
    PLAIN_HOM + " H^o of 6.5.8.")
add(187, "'1 désignant la correspondance diagonale (plus précisément, ...'",
    "diagonale (plus précisément, la flèche ...", "diagonale. Plus précisément, la flèche",
    "punctuation", "high", "diagonale. Plus précisément, la flèche", "diagonale (plus précisément, la flèche",
    "Opening parenthesis of the print; it closes after 'Hom(L,L)' (next-but-one finding): apply the two together.")
add(187, "'définie par (III 4.2.4') (avec X_1 = X_2 , L_1 = L_2 , d = δ ) et la correspondance'",
    "(III 4.2.4') (avec X_1 = X_2 , L_1 = L_2 , d = δ ) et la",
    r"(III 4.2.4') avec $X_1=X_2$, $L_1=L_2$, $d=\delta$, et la",
    "punctuation", "high",
    r"(III 4.2.4') avec $X_1=X_2$, $L_1=L_2$, $d=\delta$, et la",
    r"(III 4.2.4') (avec $X_1=X_2$, $L_1=L_2$, $d=\delta$) et la",
    "The print puts 'avec ...' in parentheses, without a comma before 'et'.")
add(187, "'et la correspondance diagonale 1 ∈ Hom(L,L) ).'",
    "1 ∈ Hom(L,L) ).  — the closing parenthesis of '(plus précisément'", r"$1\in\Hom(L,L)$.",
    "punctuation", "high", r"$1\in\Hom(L,L)$.", r"$1\in\Hom(L,L)$).",
    "Closing parenthesis of the print; apply together with the edit 'diagonale (plus précisément'.")
add(187, "number of no. 6.6", "'6.6.' with a full stop", r"\subsection*{6.6}",
    "punctuation", "high", r"\subsection*{6.6}", r"\subsection*{6.6.}", HEAD)

# ================================================================ page 188
add(188, "top of the page",
    "p. 188 begins with the display 'RHom_A(p*_1L_1,p*_1KA_{X_1}) ⊗^L_A p*_2L_2 ⊗^L_Λ ...'; p. 187 ends "
    "'On identifie le premier membre à'",
    "page_188.tex begins with 'membre à', the end of the last line of p. 187",
    "marker", "high", None, None,
    "Page 188 really begins at the '\\[' after 'membre à'. Exact fix: python -I move_marker.py 5 188 '\\[' "
    "(the first '\\[' after the marker; simulated in memory on both layers: the marker then stands between "
    "'membre à' and '\\[').")
add(188, "'par le produit tensoriel de flèches d'évaluation 5.3.6'",
    "tensoriel de flèches d'évaluation", "tensoriel des flèches d'évaluation",
    "word", "high", "tensoriel des flèches", "tensoriel de flèches", "")
add(188, "'... par 6.5.2 et (III 1.7.6). Si c : C ⟶ X'",
    "one paragraph: 'Si c : C ⟶ X ,' follows '(III 1.7.6).' in the same line",
    "a blank line (new paragraph) before 'Si $c:C\\to X$'",
    "other", "high", "(III 1.7.6).\n\nSi $c:C", "(III 1.7.6). Si $c:C", "Paragraph break added by the TeX.")
add(188, "'d'où un \"cup-produit\"'",
    "\"cup-produit\" in straight double quotes", "d'où un cup-produit",
    "punctuation", "high", "d'où un cup-produit", "d'où un ``cup-produit''",
    "Quotes of the print left out (the file writes ``cup-produit'' in III B 1.1).")
add(188, "display (6.6.3)",
    "< , >_A : Hom_A(c*_1L_1,c^!_2L_2) ⊗ Hom_A(d*_2L_2,d^!_1L_1) ⟶ H^o(E,KA_{E,L♮}) — Hom not underlined",
    r"\uHom_A(c_1^*L_1,c_2^!L_2)\otimes \uHom_A(d_2^*L_2,d_1^!L_1)",
    "underline", "high",
    "\\uHom_A(c_1^*L_1,c_2^!L_2)\\otimes\n\\uHom_A(d_2^*L_2,d_1^!L_1)",
    "\\Hom_A(c_1^*L_1,c_2^!L_2)\\otimes\n\\Hom_A(d_2^*L_2,d_1^!L_1)",
    PLAIN_HOM + " Both factors.")
add(188, "'pour u ∈ Hom_A(c*_1L_1,c^!_2L_2), v ∈ Hom_A(d*_2L_2,d^!_1L_1)'",
    "Hom_A not underlined (both)", r"u\in\uHom_A(c_1^*L_1,c_2^!L_2),\qquad v\in\uHom_A(d_2^*L_2,d_1^!L_1),",
    "underline", "high",
    "u\\in\\uHom_A(c_1^*L_1,c_2^!L_2),\\qquad\nv\\in\\uHom_A(d_2^*L_2,d_1^!L_1),",
    "u\\in\\Hom_A(c_1^*L_1,c_2^!L_2),\\qquad\nv\\in\\Hom_A(d_2^*L_2,d_1^!L_1),", PLAIN_HOM)
add(188, "'La formule de Lefschetz (III 4.4) se généralise'",
    "a new, indented paragraph after (6.6.4)",
    "no blank line after the (6.6.4) equation: the TeX continues the paragraph",
    "other", "high", "\\end{equation}\nLa formule de Lefschetz", "\\end{equation}\n\nLa formule de Lefschetz",
    "Paragraph break of the print left out.")
add(188, "display (6.6.5)", "< f_*u,f_*v >_A = g_*< u,v >_A  — no punctuation after the display",
    r"g_*\langle u,v\rangle_A.",
    "punctuation", "high", r"g_*\langle u,v\rangle_A.", r"g_*\langle u,v\rangle_A",
    "Full stop added by the TeX.")
add(188, "number of no. 6.7, printed at the top of p. 189 (still under the p. 188 marker, see the marker finding of p. 189)",
    "'6.7.' with a full stop", r"\subsection*{6.7}",
    "punctuation", "high", r"\subsection*{6.7}", r"\subsection*{6.7.}",
    HEAD + " Filed under page 188, where the heading sits until the p. 189 marker is moved.")

# ================================================================ page 189
add(189, "top of the page",
    "p. 189 begins with the heading '6.7. Soient X et c comme en 6.5'; p. 188 ends '... par tensorisation avec "
    "A ⊗^L_{A^e} A) .'",
    "'\\subsection*{6.7}' is the last line of page_188.tex; the folio-189 marker follows it",
    "marker", "high", None, None,
    "Page 189 really begins at '\\subsection*{6.7}'. Exact fix: python -I move_marker.py 5 189 '\\subsection*{6.7' "
    "--before (anchor without the closing brace, so that it also finds the heading after the full-stop fix filed "
    "under page 188; simulated in memory on both layers).")
add(189, "'du comportement de la flèche \"produit tensoriel\"'",
    "straight typewriter double quotes", "« produit tensoriel »",
    "punctuation", "high", "« produit tensoriel »", "``produit tensoriel''", QUOTES)
add(189, "'et de la flèche \"d'évaluation\"'",
    "straight typewriter double quotes", "« d'évaluation »",
    "punctuation", "high", "« d'évaluation »", "``d'évaluation''", QUOTES)
add(189, "'A ⊗^L_{A^e} A ⟶ B ⊗^L_{B^e} B ; il en résulte que'",
    "B ⊗^L_{B^e} B   ; il en résulte que  (semicolon, small i)", "B\\lten_{B^e}B. \\] Il en résulte que",
    "punctuation", "high", "B\\lten_{B^e}B.\n\\]\nIl en résulte", "B\\lten_{B^e}B;\n\\]\nil en résulte",
    "One sentence in the print.")
add(189, "'pour u ∈ Hom_A(c*_1L,c^!_2L) , on a'", "Hom_A not underlined", r"$u\in\uHom_A(c_1^*L,c_2^!L)$",
    "underline", "high", r"$u\in\uHom_A(c_1^*L,c_2^!L)$, on a", r"$u\in\Hom_A(c_1^*L,c_2^!L)$, on a", PLAIN_HOM)
add(189, "'Tr_{B/A} : B♮ ⟶ A♮ , on notera encore'", "a comma after A♮",
    r"$\Tr_{B/A}:B_{\natural}\to A_{\natural}$;",
    "punctuation", "high", r"A_{\natural}$; on notera encore", r"A_{\natural}$, on notera encore", "")
add(189, "display (6.7.3)", "Tr_{B/A} : KB_{X,♮} ⟶ KA_{X,♮}   ,  — a comma after the display",
    r"\Tr_{B/A}:KB_{X,\natural}\longrightarrow KA_{X,\natural}  (no punctuation)",
    "punctuation", "high", "KA_{X,\\natural}\n\\tag{6.7.3}", "KA_{X,\\natural},\n\\tag{6.7.3}",
    "Comma of the print left out.")

# ================================================================ page 190
add(190, "top of the page",
    "p. 190 begins with the diagram (6.7.4); p. 189 ends 'Il découle de 5.10.6 et 5.10.9 que, pour L ∈ ob "
    "D_ctf(_BX), on a un carré commutatif'",
    "'\\begin{equation}' and '\\begin{tikzcd}[column sep=huge,row sep=' are the last two lines of page_189.tex; the "
    "folio-190 marker splits the tikzcd option 'row sep=large' into 'row sep=' / marker / 'large]'",
    "marker", "high", None, None,
    "Page 190 really begins at the '\\begin{equation}' that opens (6.7.4). Exact fix: python -I move_marker.py 5 "
    "190 '\\begin{equation}' --before (simulated in memory on both layers), then join the option split by the old "
    "marker: on page 190, 'row sep=\\nlarge]' -> 'row sep=large]' (both layers).")
add(190, "'Par suite, pour u ∈ Hom_B(c*_1L,c^!_2L) , on a'", "Hom_B not underlined", r"$u\in\uHom_B(c_1^*L,c_2^!L)$",
    "underline", "high", r"pour $u\in\uHom_B(c_1^*L,c_2^!L)$", r"pour $u\in\Hom_B(c_1^*L,c_2^!L)$", PLAIN_HOM)
add(190, "number of no. 6.8", "'6.8.' with a full stop", r"\subsection*{6.8}",
    "punctuation", "high", r"\subsection*{6.8}", r"\subsection*{6.8.}", HEAD)
add(190, "display (6.8.1), left side", "Hom_A(c*_1L,c^!_2L) ⊗ Hom_B(d*_1M,d^!_2M) — Hom not underlined (as Hom_R)",
    r"\uHom_A(c_1^*L,c_2^!L)\otimes \uHom_B(d_1^*M,d_2^!M)",
    "underline", "high",
    r"\uHom_A(c_1^*L,c_2^!L)\otimes \uHom_B(d_1^*M,d_2^!M)",
    r"\Hom_A(c_1^*L,c_2^!L)\otimes \Hom_B(d_1^*M,d_2^!M)",
    PLAIN_HOM + " The TeX already has the plain \\Hom_R on the right side.")
add(190, "'de la commutativité des carrés 5.12.1, 5.12.3, que, pour'", "a comma after 5.12.3",
    "5.12.3 que, pour", "punctuation", "high", "5.12.3 que, pour", "5.12.3, que, pour", "")
add(190, "'u ∈ Hom_A(c*_1L,c^!_2L) , c ∈ Hom_B(d*_1M,d^!_2M)'", "Hom_A, Hom_B not underlined",
    r"u\in\uHom_A(c_1^*L,c_2^!L),\qquad c\in\uHom_B(d_1^*M,d_2^!M),",
    "underline", "high",
    r"u\in\uHom_A(c_1^*L,c_2^!L),\qquad c\in\uHom_B(d_1^*M,d_2^!M),",
    r"u\in\Hom_A(c_1^*L,c_2^!L),\qquad c\in\Hom_B(d_1^*M,d_2^!M),",
    PLAIN_HOM + " The letter c stays (misprint of the print, next finding). The corrected layer reads v here, so the replay there needs the old with v.")
add(190, "'c ∈ Hom_B(d*_1M,d^!_2M)'",
    "c ∈ Hom_B(d*_1M,d^!_2M) — the letter c, for the v of 6.8.2", r"c\in\uHom_B(d_1^*M,d_2^!M)",
    "misprint_in_print", "high", None, None,
    "The TeX keeps the printed c. The element is v (Tr_R(u ⊗ v) in 6.8.2); c is the correspondence on X.",
    corrected=r"v\in\Hom_B(d_1^*M,d_2^!M)")
add(190, "'on a, dans H^o(Z^c,KR_{Z^c,L♮}) ,' (before 6.8.2)",
    "H^o(Z^c,KR_{Z^c,L♮}) — superscript c twice (clear), for the Z^e of 'Z^e = X^c ×_S Y^d'",
    r"$H^0(Z^c,KR_{Z^c,L_{\natural}})$",
    "misprint_in_print", "high", None, None,
    "The TeX keeps the printed Z^c. The fixed-point scheme of e is Z^e = X^c ×_S Y^d (printed two lines above); "
    "Z^c is not defined.",
    corrected=r"$H^0(Z^e,KR_{Z^e,L_{\natural}})$")
add(190, "display (6.8.3), target", "H^o(Z^c;KR_{Z^c,L♮}) — a semicolon after Z^c (clear)",
    r"H^0(Z^c,KR_{Z^c,L_{\natural}})",
    "misprint_in_print", "high", "\\longrightarrow\nH^0(Z^c,KR", "\\longrightarrow\nH^0(Z^c;KR",
    "Typed semicolon for the comma; the TeX silently corrects it.",
    corrected="\\longrightarrow\nH^0(Z^c,KR")
add(190, "display (6.8.3), target", "H^o(Z^c;KR_{Z^c,L♮}) — superscript c twice, for Z^e",
    r"H^0(Z^c,KR_{Z^c,L_{\natural}})",
    "misprint_in_print", "high", None, None,
    "The TeX keeps the printed Z^c (as before 6.8.2).",
    corrected=r"H^0(Z^e,KR_{Z^e,L_{\natural}})")
add(190, "'provenant de l'isomorphisme KA_{X^c,L♮} ⊗^L_S KB_{Y^d,L♮} ⟶ K(A ⊗ B)_{Z^d,L♮}'",
    "K(A ⊗ B)_{Z^d,L♮} — superscript d (clear), for Z^e", r"K(A\otimes B)_{Z^d,L_{\natural}}",
    "misprint_in_print", "high", None, None,
    "The TeX keeps the printed Z^d; the target lives on Z^e = X^c ×_S Y^d.",
    corrected=r"K(A\otimes B)_{Z^e,L_{\natural}}")
add(190, "'(donné par (III 1.7.6) et la flèche (4) de 5.9.1).'",
    "(donné par (III 1.7.6) et la flèche (4) de 5.9.1).", "donné par (III 1.7.6) et la flèche (4) de 5.9.1.",
    "punctuation", "high",
    "donné par (III 1.7.6) et la flèche (4) de 5.9.1.", "(donné par (III 1.7.6) et la flèche (4) de 5.9.1).",
    "Parentheses of the print left out.")
add(190, "number of no. 6.9", "'6.9.' with a full stop", r"\subsection*{6.9}",
    "punctuation", "high", r"\subsection*{6.9}", r"\subsection*{6.9.}", HEAD)
add(190, "6.9, 'Si X est un G-S-schéma (i.e. un S-schéma muni d'une action de G par S-automorphismes (*)), et A'",
    "G-S-schéma (i.e. un S-schéma muni ... S-automorphismes (*)), et A",
    "$G$-$S$-schéma, c'est-à-dire un $S$-schéma muni ... $S$-automorphismes\\footnote{...}, et",
    "word", "high",
    "$G$-$S$-schéma, c'est-à-dire un $S$-schéma muni d'une action de $G$ par $S$-automorphismes\\footnote{On "
    "convient de faire opérer $G$ à droite sur les espaces.}, et",
    "$G$-$S$-schéma (i.e.~un $S$-schéma muni d'une action de $G$ par $S$-automorphismes\\footnote{On convient de "
    "faire opérer $G$ à droite sur les espaces.}), et",
    "The TeX writes out the print's 'i.e.' and drops its parentheses; one edit for the pair of parentheses (the "
    "footnote text is unchanged; 'i.e.~' as the file writes it, cf. p. 182).")
add(190, "6.9, 'et A une Λ-algèbre (**) nous noterons'", "no comma after the footnote mark (**)",
    "\\footnote{...}, nous noterons", "punctuation", "high",
    "commutatives.}, nous noterons", "commutatives.} nous noterons", "Comma added by the TeX.")
add(190, "6.9, '... à gauche sur X (pour les notions de ..., etc.) sur X (pour la topologie étale), nous renvoyons le "
         "lecteur à (X 1)), et nous'",
    "à gauche sur X (pour les notions de G-faisceau d'ensembles, d'anneaux, de modules, etc.) sur X (pour la "
    "topologie étale), nous renvoyons le lecteur à (X 1)), et nous",
    "à gauche sur $X$. Pour les notions de ... etc. sur $X$ pour la topologie étale, nous renvoyons le lecteur à "
    "(X 1). Nous",
    "word", "high",
    "à gauche sur $X$. Pour les notions de $G$-faisceau d'ensembles, d'anneaux, de modules, etc. sur $X$ pour la "
    "topologie étale, nous renvoyons le lecteur à (X 1). Nous",
    "à gauche sur $X$ (pour les notions de $G$-faisceau d'ensembles, d'anneaux, de modules, etc. sur $X$ (pour la "
    "topologie étale), nous renvoyons le lecteur à (X 1)), et nous",
    "The TeX dissolves the print's parentheses into sentences and writes 'Nous' for the print's 'et nous' (p. 191 "
    "goes on 'désignerons'). The new text gives the print's wording without its extra ')' after 'etc.', which the "
    "next finding (a misprint) puts back: apply this edit first.")
add(190, "6.9, 'de modules, etc.) sur X (pour la topologie étale)'",
    "etc.) — the print closes one parenthesis too many in '(pour les notions ..., etc.) sur X (pour la topologie "
    "étale), nous renvoyons le lecteur à (X 1)),'",
    "the TeX has no parentheses here (silent restructuring, previous finding)",
    "misprint_in_print", "medium",
    "modules, etc. sur $X$ (pour", "modules, etc.) sur $X$ (pour",
    "Old taken from the text after the previous edit. The print opens three parentheses and closes four; the likely "
    "reading drops the ')' after 'etc.', so that '(pour les notions ... à (X 1))' is one parenthesis, closed by the "
    "second ')' after X 1.",
    corrected="modules, etc. sur $X$ (pour")


# ================================================================ checks
def spans(path):
    t = path.read_text(encoding="utf-8")
    ms = list(MARK.finditer(t))
    out = {}
    for i, m in enumerate(ms):
        end = ms[i + 1].start() if i + 1 < len(ms) else len(t)
        out[int(m.group(2))] = t[m.start():end]
    return out


live = spans(W / "sga5" / "diplomatic" / "s5.tex")
curr = spans(W / "sga5" / "current" / "s5.tex")
snap = {p: (RUN / "b186_190" / f"page_{p}.tex").read_text(encoding="utf-8") for p in range(186, 191)}
bad = 0
for i, x in enumerate(F):
    fx = x["fix"]
    if not fx:
        continue
    p, old, new = x["page"], fx["old"], fx["new"]
    if MARK.search(old) or MARK.search(new):
        bad += 1
        print("MARKER IN FIX", i)
    n = live[p].count(old)
    s = snap[p].count(old)
    c = curr[p].count(old)
    flag = "" if n == 1 and s in (0, 1) else "  <-- BAD"
    if flag:
        bad += 1
    info = "" if c == 1 or x["kind"] == "misprint_in_print" else f"  (current layer: {c})"
    print(f"{i:2d} p{p} live={n} snap={s}{flag}{info}  {old[:60]!r}")
    if n == 1:
        live[p] = live[p].replace(old, new, 1)
    if s == 1:
        snap[p] = snap[p].replace(old, new, 1)
    if c == 1 and x["kind"] != "misprint_in_print":
        curr[p] = curr[p].replace(old, new, 1)
print("findings", len(F), "bad", bad)
cnt = {}
for x in F:
    k = "mis" if x["kind"] == "misprint_in_print" else "norm"
    cnt.setdefault(x["page"], {"norm": 0, "mis": 0})[k] += 1
print(cnt)
if bad == 0 and "--write" in sys.argv:
    out = RUN / "findings_186_190.json"
    out.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
    print("written", out)
