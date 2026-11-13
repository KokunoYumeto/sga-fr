"""Build findings_491_495.json; check that every fix's old occurs exactly once in its page file
and does not touch a marker line; simulate all fixes per page."""
import json, pathlib, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
B = HERE.parent / "b491_495"
OUT = HERE.parent / "findings_491_495.json"


def nl(s):
    return s.replace("¶", "\n")


def fx(old, new):
    return {"old": nl(old), "new": nl(new)}


def F(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    return d


M492 = "%%%%%%%%%%  scan idx 505  |  folio 492  %%%%%%%%%%"
M494 = "%%%%%%%%%%  scan idx 507  |  folio 494  %%%%%%%%%%"

PARA = "Missing paragraph break (the TeX runs the indented paragraph on after the display)."

findings = [
    # ---------------- page 491 ----------------
    F(491, "letters of sheaves on pp. 491-495",
      "underlined in the print (both scans): p. 491 J, J of J/J² and J', J' of J'/J'² (T_i, T_j display), "
      "F and N of 0 → F → g*(N) → O_Y'(1) → 0, J twice in '0 → J → O_X → O_Y → 0, où J est ici inversible'; "
      "p. 492 J of 'Comme J est inversible', J, J of 'Or T_i = -cl(J/J²)', E of 'et E = (O_Y)^{r+1}'; "
      "p. 493 Ω of Ω¹_{P/Y} in both displays of Proposition 5.2, E of f*(E) (twice) and 'défini par E', "
      "F of F(-1) and 'F = Ker', B four times in the text ('B = ⊕', 'B est une', 'B-Modules' twice), "
      "Ω and B three times each in (5.2.1), E of the four S(E); "
      "p. 494 Ω ten times (Ω¹_{B/O_P} twice, Ω¹_{Z/Y}, Ω¹_{V/Y} three times, Ω¹_{B/Y}, Ω¹_{P/Y} twice in "
      "Remarque 5.2.1 and once in 5.3), B of B(-1), of ⊗B and of the subscripts B/O_P, B/Y, E of the eight "
      "S(E) and of 'défini par E', S(E)⊗E, 'car E est', g*(E), f*(E) twice, F of F(-1); "
      "p. 495 E of 'Comme E = (O_Y)^{r+1}'. Plain in the print: N of '= -N', L, the classes F, L of "
      "g*(T_i) = -(F + L), F of Todd(F̌) and λ_{-1}(F), J of i_*(1) = 1-J, c̃(J), ch(J), c¹(J), i*(J), J̌, c(J); "
      "E of g*(E).ξ^{-1} (5.3), of c̃(E) and of 'on a E = r+1'",
      r"all plain; Exposé VIII (folios 466-497) has no \underline",
      "underline", "high", None,
      r"Convention of the Exposé VIII transcription, as in Exposés VI-VII: not itemized. Places where the "
      r"plain letter merges two printed objects: p. 491 the sheaf F̲ of the exact sequence and the class F of "
      r"g*(T_i) = -(F + L); p. 492 'Comme \(J\) est inversible, on a \(\widetilde c(J)=...' (sheaf J̲, class J); "
      r"p. 495 'Comme \(E=(\mathcal O_Y)^{r+1}\), on a \(E=r+1\)' (sheaf E̲, class E). Three examples in the "
      r"form to use if the diplomatic layer reproduces the underline: p. 491 '0\longrightarrow F\longrightarrow g^*(N)' "
      r"-> '0\longrightarrow \underline{F}\longrightarrow g^*(\underline{N})'; p. 492 'Comme \(J\) est inversible' "
      r"-> 'Comme \(\underline{J}\) est inversible'; p. 495 'Comme \(E=(\mathcal O_Y)^{r+1}\)' -> "
      r"'Comme \(\underline{E}=(\mathcal O_Y)^{r+1}\)'. The underlined O written \mathcal O falls under the "
      r"pending structure-sheaf decision."),
    F(491, "'Compte tenu de 4.4, la relation à démontrer s'écrit donc :'",
      "begins a new, indented paragraph after the Todd display (both scans)",
      r"'\]' followed directly by 'Compte tenu de 4.4' (the paragraph runs on)",
      "other", "high", fx(r"\]¶Compte tenu de 4.4", r"\]¶¶Compte tenu de 4.4"), PARA),
    F(491, "'Posant z = g*(x).λ_{-1}(F), cette relation n'est autre que le théorème'",
      "begins a new, indented paragraph after the display ch(j_*(...)) = j_gr(...) (both scans)",
      r"'\]' followed directly by 'Posant \(z=...' (the paragraph runs on)",
      "other", "high", fx(r"\]¶Posant \(z=", r"\]¶¶Posant \(z="), PARA),
    F(491, "'on tire : i_*(1) = 1-J , d'où' (last lines of the page)",
      "a comma after the display i_*(1) = 1-J, then 'd'où' with a small d (both scans)",
      r"'i_*(1)=1-J.' then 'D'où'",
      "punctuation", "high", fx(r"i_*(1)=1-J.¶\]¶D'où", r"i_*(1)=1-J,¶\]¶d'où"),
      r"The sentence runs on: '..., on tire : i_*(1) = 1-J, d'où ch(i_*(i*(y))) = ch(y).ch(1-J).' (the second "
      r"display opens p. 492). The TeX's full stop and capital D split it. Independent of the folio-492 marker "
      r"move, whose old string starts at the next '\['."),
    F(491, "'On est donc remané au cas où Y est un diviseur'",
      "'remané' (both scans)",
      "remané (printed reading kept)",
      "misprint_in_print", "high", None,
      "Typist's slip; the exposé writes 'on est ramené', 'se ramener' elsewhere.",
      corrected="ramené"),
    # ---------------- page 492 ----------------
    F(492, "start of page (folio-492 marker)",
      "p. 491 ends with 'i_*(1) = 1-J , / d'où' and blank space; p. 492 begins with the display "
      "'ch(i_*(i*(y))) = ch(y).ch(1-J) .', then 'Comme J est inversible, ...' (both scans)",
      r"page_491.tex ends 'D'où\n\[\n \ch(i_*(i^*(y)))=\ch(y)\cdot\ch(1-J).\n\]' above the folio-492 marker; "
      r"page_492.tex begins 'Comme \(J\) est inversible'",
      "marker", "high", None,
      r"Page 492 really begins at the display '\[ \ch(i_*(i^*(y)))=\ch(y)\cdot\ch(1-J). \]'. Exact edit in "
      r"main.tex, both layers (diplomatic lines 12680-12683, current 12686-12689, main.tex as of 16:16; the file is being edited, the old string is unique in each layer): replace "
      r"'\[\n \ch(i_*(i^*(y)))=\ch(y)\cdot\ch(1-J).\n\]\n" + M492 + r"\n' by '" + M492 +
      r"\n\[\n \ch(i_*(i^*(y)))=\ch(y)\cdot\ch(1-J).\n\]\n' (old string once per layer; simulated together "
      r"with the p. 491 'd'où' fix: crops_491_495/sim_markers.py). The sentence runs on ('d'où' + display), "
      r"so no blank line."),
    F(492, "'Comme i_*(1) = 1-J, i_gr(1) est l'image dans Gr¹K˙(X) de 1-J'",
      "begins a new, indented paragraph after the display i_gr(Todd(Ť_i)) = ... (both scans)",
      r"'\]' followed directly by 'Comme \(i_*(1)=1-J\)' (the paragraph runs on)",
      "other", "high", fx(r"\]¶Comme \(i_*(1)=1-J\)", r"\]¶¶Comme \(i_*(1)=1-J\)"), PARA),
    F(492, "'donc c'est -c(J)'",
      "-c(J), no exponent (both scans; crops_491_495/c492_cJ.png, w492_cJ.png)",
      r"\(-c(J)\) (printed reading kept)",
      "misprint_in_print", "medium", None,
      r"i_gr(1) lies in Gr¹K˙(X), where the image of 1-J is -c¹(J); the page's last display needs "
      r"i_gr(1).Todd(-J̌) = 1-exp(c¹(J)) with Todd(-J̌) = (1-exp(c¹(J)))/(-c¹(J)). The exposé writes c(z) for the "
      r"total Chern class (folio 484: \Todd(z)=\Todd(c(z))) and c¹ for the first one, as in the six other "
      r"places of this page. In 'donc c'est \(-c(J)\).'",
      corrected=r"-c^1(J)"),
    F(492, "5.1: 'f : P^r_Y ⟶ Y' and 'On pose P = P^r_Y'",
      "P with a double underline in both places (both scans; crops_491_495/c492_P.png, c492_P2.png); "
      "the P of 'On pose P =' plain",
      r"\mathbb P^r_Y (both places)",
      "font", "high", None,
      r"Convention of the Exposé VIII transcription: the exposé writes this P as \mathbb P throughout (13 places: "
      r"folios 480, 482 (2), 487 (7), 488, 492 (2)), never \mathbf P, whereas Exposés VI-VII write the doubly "
      r"underlined P bold (\mathbf P; \bfP = \mathbf P, main.tex line 10490). One decision for the exposé; if "
      r"bold, the two edits here: 'f:\mathbb P^r_Y' -> 'f:\bfP^r_Y'; 'P=\mathbb P^r_Y' -> 'P=\bfP^r_Y'. The "
      r"other folios for their batches to check against the print."),
    F(492, "'On obtient donc finalement :'",
      "begins a new, indented paragraph after the Todd(-J̌) display (both scans)",
      r"'\]' followed directly by 'On obtient donc finalement' (the paragraph runs on)",
      "other", "high", fx(r"\]¶On obtient donc finalement", r"\]¶¶On obtient donc finalement"), PARA),
    # ---------------- page 493 ----------------
    F(493, "Proposition 5.2 (the statement)",
      "underlined word group by word group (both scans): 'Proposition', 'On a sur', 'la suite exacte', the i "
      "and the e of 'i.e.', 'on a un isomorphisme'; P, the colon and the two displays not underlined (apart "
      "from the sheaf letters)",
      r"\textbf{Proposition 5.2.} and the statement in roman",
      "underline", "high", None,
      "Exposé II pattern (GLOBAL_ISSUES 82): not itemized; the word groups listed for the scripted pass. No "
      "emphasized defined terms and no category L on pp. 491-495."),
    F(493, "the diagram P ←h— Z over Y (arrows f, g)",
      "a full stop after Y (both scans; crops_491_495/c493_diag.png)",
      "no punctuation after Y",
      "punctuation", "high", fx(r"& Y &¶\end{tikzcd}", r"& Y. &¶\end{tikzcd}"),
      "The file's form for punctuation after a diagram's last entry, as '& Y,' in Définition 1.1 (folio 466)."),
    F(493, "'Or cette suite exacte est une suite exacte graduée de B-Modules gradués.'",
      "begins a new, indented paragraph after (5.2.1) (both scans)",
      r"'\end{equation}' followed directly by 'Or cette suite exacte' (the paragraph runs on)",
      "other", "high", fx(r"\end{equation}¶Or cette suite exacte", r"\end{equation}¶¶Or cette suite exacte"), PARA),
    F(493, "S(E) on pp. 493-494 (twelve places)",
      "S with a double underline, E underlined, in all twelve places (both scans): p. 493 the three S(E) of the "
      "diagram and 'graduation de S(E)[T,T^{-1}]'; p. 494 'S(E)-dérivation', the four S(E) of the display of d, "
      "'facteur S(E).dT', 'défini par S(E)', 'S(E)⊗_{O_Y}E'",
      "S(E) with a plain S in all twelve places",
      "font", "high", None,
      r"Convention of the Exposé VIII transcription (these are the exposé's only S(E)): not itemized. The "
      r"volume's form for this doubly underlined S is \Sym (renewed to \mathbf{S} at main.tex line 9131, "
      r"Exposé VI); Exposé VII writes \cS (findings_426_430). Three examples in the file's form: p. 493 "
      r"'S(E) \arrow[rr]' -> '\Sym(E) \arrow[rr]'; p. 494 'une \(S(E)\)-dérivation' -> 'une \(\Sym(E)\)-dérivation'; "
      r"p. 494 'défini par \(S(E)\), donc' -> 'défini par \(\Sym(E)\), donc'."),
    F(493, "the diagram S(E) → ⊕_{n∈Z} S(E)(n) ≃ S(E)[T,T^{-1}]: the bottom algebra",
      "O_X (both scans)",
      r"\mathcal O_X (printed reading kept)",
      "misprint_in_print", "medium", None,
      r"§5 has no X: the base is Y (f : P = P^r_Y → Y, E = (O_Y)^{r+1}, S(E) an O_Y-algebra), and the bottom "
      r"algebra maps to S(E) and to ⊕ S(E)(n). In '& \mathcal O_X \arrow[ul] \arrow[ur] &' (the only X of §5, "
      r"folios 492-497).",
      corrected=r"\mathcal O_Y"),
    # ---------------- page 494 ----------------
    F(494, "start of page (folio-494 marker)",
      "p. 493 ends '... les deux autres algèbres étant supposées réduites'; p. 494 begins 'au degré 0.', then "
      "the indented paragraph 'Le module des différentielles ...' (both scans)",
      r"page_493.tex ends 'supposées réduites au degré \(0\).\n\nLe' above the folio-494 marker; page_494.tex "
      r"begins 'module des différentielles'",
      "marker", "high", None,
      r"Page 494 really begins at 'au degré \(0\).'. Exact edit in main.tex, both layers (diplomatic lines "
      r"12758-12762, current 12764-12768, main.tex as of 16:16; the old string is unique in each layer): replace 'réduites au degré \(0\).\n\nLe\n" + M494 +
      r"\nmodule des différentielles' by 'réduites\n" + M494 + r"\nau degré \(0\).\n\nLe module des "
      r"différentielles' (old string once per layer; simulated: crops_491_495/sim_markers.py). The sentence "
      r"runs on across the page turn, so no blank line before the marker; the blank line before 'Le' stays "
      r"(indented paragraph in the print)."),
    F(494, "'la propriété universelle qui définit Ω¹_{B/O_P} en posant d(aT^n) = ...'",
      "no comma after Ω¹_{B/O_P} (both scans; crops_491_495/c494_definit.png, w494_definit.png)",
      r"'\(\Omega^1_{B/\mathcal O_P}\), en posant'",
      "punctuation", "high",
      fx(r"\(\Omega^1_{B/\mathcal O_P}\), en posant", r"\(\Omega^1_{B/\mathcal O_P}\) en posant"),
      "Comma added by the TeX."),
    F(494, "'En prenant les termes de degré 0 dans la suite exacte (5.2.1), on trouve la suite exacte annoncée.'",
      "begins a new, indented paragraph after '... considéré comme étant de degré 1.' (both scans)",
      "one paragraph with the preceding sentences",
      "other", "high", fx(r"de degré \(1\). En prenant", r"de degré \(1\).¶¶En prenant"),
      "Missing paragraph break."),
    F(494, "Remarque 5.2.1: 'on obtient directement un isomorphisme Ω¹_{P/Y} ⥲ F(-1) d'après la caractérisation'",
      "the isomorphism stands in the line of text, between 'isomorphisme' and 'd'après' (both scans)",
      r"set as a display \[ ... \]",
      "other", "medium",
      fx(r"directement un isomorphisme¶\[¶\Omega^1_{P/Y}\xrightarrow{\sim}F(-1)¶\]¶d'après",
         r"directement un isomorphisme \(\Omega^1_{P/Y}\xrightarrow{\sim}F(-1)\) d'après"),
      "In-line formula of the print set as a display by the TeX."),
    F(494, "5.3: 'T_f = cl(Ω¹_{P/Y}) = g*(E).ξ^{-1} - 1'",
      "g*(E) (both scans; crops_491_495/c494_Tf.png, w494_Tf.png)",
      r"g^*(E)\cdot\xi^{-1}-1 (printed reading kept)",
      "misprint_in_print", "high", None,
      r"By 5.2, Ω¹_{P/Y} ≃ F(-1) with F = Ker(f*(E) → O_P(1)), so cl(Ω¹_{P/Y}) = f*(E).ξ^{-1} - 1 in K˙(P); "
      r"g is the morphism Z → Y. In 'T_f=\cl(\Omega^1_{P/Y})=g^*(E)\cdot\xi^{-1}-1.'",
      corrected=r"f^*(E)"),
    F(494, "end of page_494.tex, before the folio-495 marker (first line of p. 495: 'Comme E = (O_Y)^{r+1}, on a E = r+1')",
      "p. 495 opens with an indented paragraph (both scans)",
      r"'\]' of the c̃(T_f) display followed directly by the folio-495 marker and 'Comme' (the paragraph runs on)",
      "other", "high", fx(r"-\widetilde c(1).¶\]¶", r"-\widetilde c(1).¶\]¶¶"),
      "Missing paragraph break at the page turn; the blank line goes before the marker, as before the folio-491 marker."),
    # ---------------- page 495 ----------------
    F(495, "'D'après la définition de Todd, on a donc :'",
      "begins a new, indented paragraph after the display c̃(Ť_f) = (r,(1+x)^{r+1}) (both scans)",
      r"'\]' followed directly by 'D'après la définition' (the paragraph runs on)",
      "other", "high", fx(r"\]¶D'après la définition", r"\]¶¶D'après la définition"), PARA),
    F(495, "'On voit donc qu'il suffit de montrer le théorème pour les ξ^k'",
      "begins a new, indented paragraph after the f_gr display (both scans)",
      r"'\]' followed directly by 'On voit donc' (the paragraph runs on)",
      "other", "high", fx(r"\]¶On voit donc", r"\]¶¶On voit donc"), PARA),
]

# ---- checks ----
pages = {p: (B / f"page_{p}.tex").read_text(encoding="utf-8") for p in range(491, 496)}
ok = True
for f in findings:
    fix = f["fix"]
    if fix is None:
        continue
    t = pages[f["page"]]
    n = t.count(fix["old"])
    if n != 1:
        ok = False
        print("COUNT", n, f["page"], repr(fix["old"]))
    if "%%%%%%%%%%" in fix["old"] or "%%%%%%%%%%" in fix["new"]:
        ok = False
        print("MARKER in fix", f["page"], repr(fix["old"]))
# simulate all fixes per page, in list order
for p, t in pages.items():
    for f in findings:
        if f["page"] == p and f["fix"] is not None:
            assert t.count(f["fix"]["old"]) == 1, (p, f["fix"]["old"])
            t = t.replace(f["fix"]["old"], f["fix"]["new"], 1)
    open(HERE / f"patched_{p}.tex", "w", encoding="utf-8", newline="\n").write(t)
print("ok" if ok else "PROBLEMS", len(findings))
from collections import Counter
c = Counter((f["page"], f["kind"] == "misprint_in_print") for f in findings)
for p in range(491, 496):
    print(p, c[(p, False)], "/", c[(p, True)])
open(OUT, "w", encoding="utf-8", newline="\n").write(json.dumps(findings, ensure_ascii=False, indent=1) + "\n")
print(OUT)
