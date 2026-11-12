import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
B = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\b226_230")
OUT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\findings_226_230.json")

F = []


def add(**k):
    F.append(k)


add(page=226,
    where="Preuve de (1.1)(fin), definition of 'spécial': '(nous dirons spécial pour abréger)'",
    scan="'spécial' underlined (both scans)",
    tex="(nous dirons spécial pour abréger)",
    kind="underline", confidence="high",
    fix={"old": "(nous dirons spécial pour abréger)", "new": "(nous dirons \\emph{spécial} pour abréger)"},
    note="The defined term is underlined in the print; the TeX leaves it plain.")

add(page=226,
    where="proof label 'Preuve de (1.1)(fin).'",
    scan="'Preuve de' and 'fin' underlined separately; '(1.1)(', ')' and the full stop not underlined (both scans)",
    tex="\\emph{Preuve de (1.1)(fin).}",
    kind="underline", confidence="medium",
    fix={"old": "\\emph{Preuve de (1.1)(fin).}", "new": "\\emph{Preuve de} (1.1)(\\emph{fin})."},
    note="The emphasis runs over the number (1.1) and the parentheses. p. 228 has the print's form '\\emph{Preuve de} (A).'. Proof labels are left to the checkers (as SGA 5 item 75); skip if the block-underline volume decision is extended to labels.")

add(page=226,
    where="diagram (a'), label of the top arrow X' -> Y'",
    scan="i\" (i with a double quote) over the arrow (both scans; crops_226_230/p226_i2.png)",
    tex="X' \\arrow[r,\"i''\"] (printed reading kept)",
    kind="misprint_in_print", confidence="high",
    fix=None,
    corrected="X' \\arrow[r,\"i'\"]",
    note="The TeX keeps the printed reading. The text names this closed immersion i' ('i' une immersion fermée', 'i'_*p'^*(E)', 'du choix de i', p', f''), and the cube on p. 227 labels X' -> Y' as i'; i\" is the arrow of (a'').")

add(page=227,
    where="(A): 'et soit E ∈ ob D(X_2)'",
    scan="'ob' in small letters (both scans); Exposé III types 'ob' throughout from p. 222 (ii) on (OCR of pp. 223-245; both scans of pp. 227-229)",
    tex="\\(E\\in\\Ob D(X_2)\\), with \\Ob = \\operatorname{Ob} (main.tex line 5340, \\renewcommand for Exposé III)",
    kind="word", confidence="high",
    fix={"old": "\\(E\\in\\Ob D(X_2)\\)", "new": "\\(E\\in\\operatorname{ob} D(X_2)\\)"},
    note="Convention of the transcription for Exposé III, reported once: \\Ob prints 'Ob' where the print has 'ob'. Other places on these pages: p. 228 'p^*(E) ∈ ob D(X_1)', 'E ∈ ob D(X)' and 'E ∈ ob D(f)_{n-coh}' (Déf. 1.2), p. 229 'E ∈ ob D(f)_coh'. Better: change line 5340 to \\renewcommand{\\Ob}{\\operatorname{ob}} (then this page edit is unnecessary but harmless); p. 222 (i) and its display print 'Ob' (witness) and would then need \\operatorname{Ob} written out.")

add(page=227,
    where="statements of Exposé III: (A) here; Définition 1.2 (pp. 228-229), Proposition 1.4 and Définition 1.5 (p. 230)",
    scan="the print underlines each statement word group by word group: (A) 'un carré commutatif de schémas', 'où', 'est un morphisme spécial', 'un morphisme lisse', 'et', 'des immersions fermées', 'et soit', 'Alors', 'pour que', 'soit', 'pseudo-cohérent', 'il faut et il suffit que', 'le soit' (both scans)",
    tex="statements in roman ((A) has only \\emph{Soit})",
    kind="underline", confidence="high",
    fix=None,
    note="Exposé III follows the Exposé II pattern of GLOBAL_ISSUES 82 (Théorème 1.1 on p. 222 too, witness): one decision for the exposé, not itemized. No \\emph on defined terms that the print leaves plain on these pages.")

add(page=228,
    where="Preuve de (A), last sentence: 'on conclut finalement que \"i_2*(E) n-pseudo-cohérent\" équivaut à ...'",
    scan="i_{2*}(E) without a prime (both scans; crops_226_230/p228_i2star.png)",
    tex="« \\(i'_{2*}(E)\\) \\(n\\)-pseudo-cohérent » équivaut à « \\(i_{1*}p^*(E)\\) ...",
    kind="symbol", confidence="high",
    fix={"old": "finalement que « \\(i'_{2*}(E)\\)", "new": "finalement que « \\(i_{2*}(E)\\)"},
    note="The TeX adds a prime. The print's conclusion is the assertion (A) itself (i_{2*}(E) against i_{1*}p^*(E)).")

add(page=229,
    where="Définition 1.2 (cont.): '... relativement à f. On dira que f est n-pseudo-cohérent'",
    scan="no paragraph break: 'On' follows 'relativement à f.' on the same line (both scans)",
    tex="a blank line before 'On dira que \\(f\\) est'",
    kind="other", confidence="medium",
    fix={"old": "relativement à \\(f\\).\n\nOn dira que \\(f\\)", "new": "relativement à \\(f\\). On dira que \\(f\\)"},
    note="The TeX splits the definition into two paragraphs.")

add(page=230,
    where="start of page",
    scan="p. 230 begins '(-1)-pseudo-cohérent équivaut à dire que f est localement de présentation finie'; p. 229 ends 'En particulier, dire que f est' (both scans)",
    tex="'\\((-1)\\)-' ends the last line of page_229.tex (under the folio-229 marker); page_230.tex begins 'pseudo-cohérent équivaut'",
    kind="marker", confidence="high",
    fix=None,
    note="Page 230 really begins with '\\((-1)\\)-pseudo-cohérent'. python -I marker_split_word.py 6 230 pull '\\((-1)\\)-' (simulated in memory on both layers with crops_226_230/sim_markers.py: '... dire que \\(f\\) est', the marker, '\\((-1)\\)-pseudo-cohérent équivaut ...'). This also removes the space that the line end now puts between '(-1)-' and 'pseudo-cohérent'.")

add(page=230,
    where="Proposition 1.4: 'et soit [triangle] un triangle distingué de D(X)'",
    scan="a small triangle: E -> F on the line, G above, arrows G -> E and F -> G; no [1] (both scans; crops_226_230/p230_tri.png)",
    tex="\\[ E\\longrightarrow F\\longrightarrow G\\longrightarrow E[1] \\]",
    kind="formula", confidence="high",
    fix={"old": "E\\longrightarrow F\\longrightarrow G\\longrightarrow E[1]",
         "new": "\\begin{tikzcd}\n& G \\arrow[dl] & \\\\\nE \\arrow[rr] && F \\arrow[ul]\n\\end{tikzcd}"},
    note="The TeX writes the triangle as a line and adds E[1]. Same convention in Exposé III on p. 223 (main.tex lines 5381, 5385, witness) and probably pp. 235, 239 (lines 5676, 5755); Exposé I sets these triangles with tikzcd (as in the new text).")

add(page=230,
    where="Preuve of 1.4: 'On a alors un triangle distingué [triangle]'",
    scan="a triangle: f_*(E) -> f_*(F) on the line, f_*(G) above, arrows f_*(G) -> f_*(E) and f_*(F) -> f_*(G); no [1] (both scans)",
    tex="\\[ f_*(E)\\longrightarrow f_*(F)\\longrightarrow f_*(G)\\longrightarrow f_*(E)[1] \\]",
    kind="formula", confidence="high",
    fix={"old": "f_*(E)\\longrightarrow f_*(F)\\longrightarrow f_*(G)\\longrightarrow f_*(E)[1]",
         "new": "\\begin{tikzcd}\n& f_*(G) \\arrow[dl] & \\\\\nf_*(E) \\arrow[rr] && f_*(F) \\arrow[ul]\n\\end{tikzcd}"},
    note="As the triangle of Proposition 1.4. Independent of the comma entry below (either order).")

add(page=230,
    where="Preuve of 1.4, after the triangle",
    scan="a comma to the right of the triangle, on the line of f_*(F) (both scans)",
    tex="no punctuation before 'et l'assertion résulte de (I 2.6)'",
    kind="punctuation", confidence="high",
    fix={"old": "\n\\]\net l'assertion", "new": ",\n\\]\net l'assertion"},
    note="Works before or after the triangle edit above.")

add(page=230,
    where="Définition 1.5, display: 'Tor_i^S(O_X,O_Y) = 0 pour i ≠ 0'",
    scan="Tor underlined (the sheaf Tor) (both scans; crops_226_230/p230_tor.png)",
    tex="\\Tor_i^S(\\mathcal O_X,\\mathcal O_Y)",
    kind="underline", confidence="high",
    fix={"old": "\\Tor_i^S(\\mathcal O_X", "new": "\\underline{\\Tor}_i^S(\\mathcal O_X"},
    note="As underlined Hom: main.tex writes \\underline{\\Tor}_i elsewhere (p. 49).")

add(page=230,
    where="Définition 1.5: 'les Tor_i^S étant les hyper-tor locaux'",
    scan="Tor underlined, with an underline of its own between those of 'les' and 'étant les hyper-tor locaux définis dans' (both scans)",
    tex="les \\(\\Tor_i^S\\) étant",
    kind="underline", confidence="high",
    fix={"old": "les \\(\\Tor_i^S\\) étant", "new": "les \\(\\underline{\\Tor}_i^S\\) étant"},
    note="As the display.")

add(page=230,
    where="Définition 1.5, display: 'Tor_i^S(O_X,O_Y)'",
    scan="O_X underlined, O_Y a plain O without its underline (both scans; crops_226_230/p230_oy.png, w_230_tor.png)",
    tex="\\mathcal O_Y (the form the TeX gives the underlined O)",
    kind="misprint_in_print", confidence="low",
    fix={"old": "\\mathcal O_Y)=0", "new": "O_Y)=0"},
    corrected="\\mathcal O_Y)=0",
    note="The TeX silently corrects the typist's missing underline of the structure sheaf O_Y; the fix restores the printed plain O. Independent of the Tor edit (its old stops before O_Y).")

add(page=230,
    where="end of page",
    scan="p. 230 ends '... définis dans (EGA III 6.5).'; p. 231 begins 'C'est une condition de nature locale' (OCR of p. 231; both scans of p. 230)",
    tex="page_230.tex ends '(EGA III 6.5). C'est une': 'C'est une' stands under the folio-230 marker",
    kind="marker", confidence="high",
    fix=None,
    note="Page 231 really begins with 'C'est une'. python -I move_marker.py 6 231 \"C'est une\" --before (simulated in memory on both layers with crops_226_230/sim_markers.py, after the p. 230 pull: '... (EGA III 6.5). ', the marker, 'C'est une', 'condition de nature locale ...'). The checker of p. 231 may report the same boundary: apply once.")

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")

ok = True
for x in F:
    if x["fix"] is None:
        continue
    t = (B / f"page_{x['page']:03d}.tex").read_text(encoding="utf-8")
    n = t.count(x["fix"]["old"])
    if n != 1:
        ok = False
    print(x["page"], n, repr(x["fix"]["old"][:60]))
print("all unique" if ok else "NOT UNIQUE")
from collections import Counter
c = Counter((x["page"], x["kind"] == "misprint_in_print") for x in F)
for p in range(226, 231):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
