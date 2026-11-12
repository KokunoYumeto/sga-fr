import json
import os
import sys

FOLDER = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I\b191_195"
OUTFILE = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I\findings_191_195.json"

findings = [
    # ---------------- page 191 ----------------
    dict(page=191,
         where="Remarque 3.3.6.3, 'Il convient de le rendre auticommutatif en y remplaçant u^1 par -u^1'",
         scan="auticommutatif",
         tex="auticommutatif",
         kind="misprint_in_print", confidence="high",
         fix=None, corrected="anticommutatif",
         note="Typing error of the print (u for n), two lines after 'et non anticommutatif'. The TeX keeps the printed reading."),
    # ---------------- page 192 ----------------
    dict(page=192,
         where="first line, 'les deux homomorphismes cobords qui y sont envisagés différent par le signe'",
         scan="différent (acute accent on the second e), underlined",
         tex="\\underline{différent par le signe.}",
         kind="misprint_in_print", confidence="medium",
         fix=None, corrected="diffèrent",
         note="Accent error: the verb différer, third person plural ('diffèrent'), is meant; the print has the adjective spelling. The TeX keeps the printed reading."),
    dict(page=192,
         where="3.3.7, 'en réconstituant notamment la catégorie des morphismes cocartésiens'",
         scan="réconstituant",
         tex="réconstituant",
         kind="misprint_in_print", confidence="high",
         fix=None, corrected="reconstituant",
         note="Spurious acute accent (reconstituer). The TeX keeps the printed reading."),
    dict(page=192,
         where="3.3.7, 'est en correspondance biunivoque canonique avec l'ensemble des isomorphismes Hom_{D(C)}(L'. ,L.)'",
         scan="l'ensemble des isomorphismes Hom_{D(C)}(L'. ,L.)",
         tex="l'ensemble des isomorphismes $\\mathrm{Hom}_{D(\\underline{C})}(L'. ,L.)$",
         kind="misprint_in_print", confidence="low",
         fix=None, corrected="homomorphismes",
         note="Probable slip of the print: every morphism f : L'. -> L. gives a cocartesian functor f^* (3.4.3), so the isomorphism classes of cocartesian functors correspond to all of Hom_{D(C)}(L'.,L.), not to its isomorphisms. The TeX keeps the printed reading; correct only after checking the intended wording."),
    dict(page=192,
         where="last line, 'Si (X,alpha) est un objet de Psi_L . on désigne par f*(X,alpha) l'objet'",
         scan="underlined Psi with subscript L, then a space, a full stop on the line, and 'on' without a comma",
         tex="$\\underline{\\Psi}_L$ . on désigne",
         kind="misprint_in_print", confidence="low",
         fix=None, corrected="$\\underline{\\Psi}_{L.}$, on désigne",
         note="The dot of L. is typed on the line after a space and the comma before 'on' is missing. The TeX keeps the printed reading."),
    # ---------------- page 193 ----------------
    dict(page=193,
         where="formula (3.4.5)",
         scan="f^i : Ext^i(L.,-)   [empty space, no arrow]   Ext^i(L'.,-) ,  i in Z .",
         tex="f^i : \\mathrm{Ext}^i(L.,-) \\longrightarrow \\mathrm{Ext}^i(L'.,-)",
         kind="misprint_in_print", confidence="high",
         fix={"old": "(L.,-) \\longrightarrow \\mathrm{Ext}", "new": "(L.,-) \\qquad \\mathrm{Ext}"},
         corrected="\\longrightarrow",
         note="The space left for the hand-drawn arrow is empty: no trace of ink between the two Ext terms, while every other hand-drawn arrow on the page is dark and complete. The TeX silently supplies the arrow."),
    dict(page=193,
         where="diagram (3.4.6), after Ext^i(L'.,A)",
         scan="full stop to the right of Ext^i(L'.,A)",
         tex="no full stop (the STRUCTURE comment records it; the tikzcd omits it)",
         kind="punctuation", confidence="high",
         fix={"old": "\\mathrm{Ext}^i(L'.,A)\n\\end{tikzcd}", "new": "\\mathrm{Ext}^i(L'.,A) & .\n\\end{tikzcd}"},
         note="Punctuation printed after a diagram and left out by the TeX; added as a last cell, as the TeX does for (3.4.2) on page 192."),
    # ---------------- page 194 ----------------
    dict(page=194,
         where="first sentence, 'est essentiellement triviale, et laissé au lecteur'",
         scan="laissé",
         tex="laissé",
         kind="misprint_in_print", confidence="medium",
         fix=None, corrected="laissée",
         note="Agreement error (la vérification ... laissée). The TeX keeps the printed reading."),
    dict(page=194,
         where="proof of 3.4.7, '(resp. f^o est un isomorphisme et f un monomorphisme, resp. f^o et f^1 sont des isomorphismes)'",
         scan="et f un monomorphisme (f without superscript)",
         tex="et $f$ un monomorphisme",
         kind="misprint_in_print", confidence="high",
         fix=None, corrected="$f^1$",
         note="Missing superscript 1: full faithfulness means f^o an isomorphism and f^1 a monomorphism (f^i being the maps (3.4.4), i=0,1). The TeX keeps the printed reading."),
    dict(page=194,
         where="unnumbered diagram after 'd'où des foncteurs du type (3.4.3)', after the last node Psi_{L.}",
         scan="full stop to the right of Psi_{L.}",
         tex="no full stop (the STRUCTURE comment records it; the tikzcd omits it)",
         kind="punctuation", confidence="high",
         fix={"old": "\\underline{\\Psi}_{L.}\n\\end{tikzcd}", "new": "\\underline{\\Psi}_{L.} & .\n\\end{tikzcd}"},
         note="Punctuation printed after a diagram and left out by the TeX."),
    dict(page=194,
         where="same diagram, middle node Psi_{L'.}",
         scan="Psi_{L'.} without underline (the outer nodes Psi_{L''.} and Psi_{L.} are underlined)",
         tex="\\Psi_{L'.}",
         kind="misprint_in_print", confidence="medium",
         fix=None, corrected="\\underline{\\Psi}_{L'.}",
         note="The typist omitted the underline of the cofibred category Psi_{L'.} (underlined in (3.4.3) and everywhere else). The TeX keeps the printed reading."),
    # ---------------- page 195 ----------------
    dict(page=195,
         where="'i.e. un isomorphisme f*(X') ~ 0_{L.,A'}, 0_{L.,A} désignant l'objet nul de Psi_{L.}(A)'",
         scan="0_{L.,A'} (prime after A), followed by a comma on the line",
         tex="0_{L.,A'}",
         kind="misprint_in_print", confidence="medium",
         fix=None, corrected="0_{L.,A}",
         note="Spurious prime: the trivialisation is an isomorphism with the null object 0_{L.,A} of Psi_{L.}(A), A being the object of C under X', as the same sentence says. The TeX keeps the printed reading."),
    dict(page=195,
         where="'satisfaisant j alpha' = d'_o et alpha'd'_1 = 0'",
         scan="j alpha' = d'_o (j without prime)",
         tex="$j\\alpha' = d'_o$",
         kind="misprint_in_print", confidence="medium",
         fix=None, corrected="j'\\alpha' = d'_o",
         note="The projection of the extension is j' : X' -> L'_o (displayed extension in the same sentence; braced relation j'alpha' = d'_o). The TeX keeps the printed reading."),
    dict(page=195,
         where="'satisfaisant jt = f_o et td_o = alpha'f_1'",
         scan="jt = f_o (j without prime; only a speck above the t)",
         tex="$jt = f_o$",
         kind="misprint_in_print", confidence="medium",
         fix=None, corrected="j't = f_o",
         note="As above; braced relation j't = f_o. The TeX keeps the printed reading."),
    dict(page=195,
         where="'revient à la donnée d'une exten-/sion 0 -> A -> X' -> L'_o -> 0'",
         scan="line-end 'exton-': the fourth letter is a closed round o, with faint stubs of a bar inside it",
         tex="extension",
         kind="misprint_in_print", confidence="low",
         fix={"old": "d'une extension", "new": "d'une extonsion"},
         corrected="extension",
         note="The e's of 'donnée' and 'une' on the same line are open at the lower right; this letter is closed. If the faint stubs are an e struck over the o (typist's correction), the TeX is right and this finding should be dropped; otherwise the TeX silently corrects 'extonsion'."),
    dict(page=195,
         where="diagram, arrow j' between X' and L'_o",
         scan="straight arrow with a head at both ends (one at L'_o, one at X', separate from the head of alpha' at X'), label j'",
         tex="X' \\arrow[dl, \"j'\"'] (single head at L'_o)",
         kind="misprint_in_print", confidence="medium",
         fix={"old": "X' \\arrow[dl, \"j'\"']", "new": "X' \\arrow[dl, leftrightarrow, \"j'\"']"},
         corrected="X' \\arrow[dl, \"j'\"']",
         note="j' : X' -> L'_o, so the head at X' is a drawing slip. The TeX silently gives the single arrow although its STRUCTURE comment says 'Reproduced as leftrightarrow'."),
    dict(page=195,
         where="'et A étant l'objet de C sous X''",
         scan="C not underlined",
         tex="$C$",
         kind="misprint_in_print", confidence="low",
         fix=None, corrected="\\underline{C}",
         note="The category C is underlined everywhere else on these pages; the typist omitted the underline here. The TeX keeps the printed reading."),
    dict(page=195,
         where="'de L'_o par un objet A de C, plus un morphisme'",
         scan="C not underlined",
         tex="$C$",
         kind="misprint_in_print", confidence="low",
         fix=None, corrected="\\underline{C}",
         note="As above. The TeX keeps the printed reading."),
]

# ---- validation: every fix 'old' occurs exactly once in its page file; no marker line touched ----
ok = True
for f in findings:
    path = os.path.join(FOLDER, "page_%03d.tex" % f["page"])
    with open(path, "rb") as fh:
        raw = fh.read()
    if b"\r" in raw:
        print("WARNING: CR found in", path)
    text = raw.decode("utf-8")
    if f["kind"] != "misprint_in_print" and "corrected" in f:
        print("ERROR: corrected on non-misprint", f["page"], f["where"])
        ok = False
    fx = f["fix"]
    if fx is None:
        continue
    n = text.count(fx["old"])
    if n != 1:
        print("ERROR: old occurs %d times on page %d: %r" % (n, f["page"], fx["old"]))
        ok = False
    if "%%%%%%%%%%" in fx["old"] or "%%%%%%%%%%" in fx["new"]:
        print("ERROR: marker line in fix", f["page"])
        ok = False

# also confirm the quoted TeX readings of fix-null misprints exist on their pages
checks = {
    191: ["auticommutatif"],
    192: ["\\underline{différent par le signe.}", "réconstituant", "l'ensemble des isomorphismes $\\mathrm{Hom}_{D(\\underline{C})}(L'. ,L.)$", "$\\underline{\\Psi}_L$ . on désigne"],
    194: ["laissé au lecteur", "et $f$ un monomorphisme", "\\Psi_{L'.} \\arrow"],
    195: ["0_{L.,A'}", "$j\\alpha' = d'_o$", "$jt = f_o$", "l'objet de $C$ sous", "objet $A$ de $C$, plus"],
}
for p, subs in checks.items():
    with open(os.path.join(FOLDER, "page_%03d.tex" % p), encoding="utf-8") as fh:
        text = fh.read()
    for s in subs:
        if s not in text:
            print("ERROR: expected TeX reading not found on page", p, repr(s))
            ok = False

if not ok:
    sys.exit(1)

with open(OUTFILE, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(findings, fh, ensure_ascii=False, indent=1)
print("wrote", OUTFILE, len(findings), "findings")
from collections import Counter
c = Counter((f["page"], f["kind"] == "misprint_in_print") for f in findings)
for p in sorted(set(f["page"] for f in findings) | {191, 192, 193, 194, 195}):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
