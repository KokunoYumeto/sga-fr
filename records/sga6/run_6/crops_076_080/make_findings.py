"""Build findings_076_080.json and check that every fix's 'old' occurs exactly once in its page file."""
import json
import pathlib

RUN = pathlib.Path(__file__).resolve().parent.parent
B = RUN / "b076_080"
OUT = RUN / "findings_076_080.json"

F = []


def add(**kw):
    F.append(kw)


# ---------------- page 76 ----------------
add(page=76, where="'chaque fois que p-1 > dim.Y'",
    scan="p-1 > dim.Y: a full stop after dim (both scans)",
    tex="\\(p-1>\\dim Y\\)",
    kind="punctuation", confidence="medium",
    fix={"old": "\\(p-1>\\dim Y\\)", "new": "\\(p-1>\\dim.Y\\)"},
    note="The abbreviation's full stop is printed (as 'supp.F' on p. 15); the TeX's \\dim drops it. "
         "Same three more times on this page (next two entries).")
add(page=76, where="'i.e. chaque fois que dim.Y < (dim.X - 1)/2'",
    scan="dim.Y < (dim.X - 1)/2: a full stop after both dim (both scans)",
    tex="\\(\\dim Y<\\frac{\\dim X-1}{2}\\)",
    kind="punctuation", confidence="medium",
    fix={"old": "\\(\\dim Y<\\frac{\\dim X-1}{2}\\)", "new": "\\(\\dim.Y<\\frac{\\dim.X-1}{2}\\)"},
    note="As the entry before.")
add(page=76, where="'par exemple r > dim.X +1)'",
    scan="r > dim.X +1: a full stop after dim (both scans)",
    tex="\\(r>\\dim X+1\\)",
    kind="punctuation", confidence="medium",
    fix={"old": "\\(r>\\dim X+1\\)", "new": "\\(r>\\dim.X+1\\)"},
    note="As the entries before.")
add(page=76, where="N.B. after 'C.Q.F.D.' ('On s'est servi du fait que ...')",
    scan="N.B. typed plain, not underlined (both scans)",
    tex="\\textbf{N.B.}",
    kind="font", confidence="medium",
    fix={"old": "\\textbf{N.B.}", "new": "N.B."},
    note="Not the accepted case of a label the typescript underlines; most N.B. of main.tex are plain "
         "(lines 871, 1162, 1261, 1384).")
add(page=76, where="N.B., 'comme dans R.R.R. 2.16'",
    scan="R.R.R. 2.16: a full stop after each R (both scans)",
    tex="\\(\\RRR\\) 2.16; \\RRR renders RRR: main.tex line 29 \\newcommand{\\RRR}{\\mathrm{RRR}} wins, "
        "the \\providecommand{\\RRR}{\\mathrm{R.R.R.}} of line 1517 has no effect",
    kind="punctuation", confidence="high",
    fix={"old": "comme dans \\(\\RRR\\) 2.16", "new": "comme dans \\(\\mathrm{R.R.R.}\\) 2.16"},
    note="The TeX's own macro prints RRR where the page prints R.R.R. (\\RR of the same page gives R.R. "
         "correctly). Alternative: make line 1517's R.R.R. effective for the appendix; then this entry is not "
         "needed and the next one becomes 'de \\(\\RRR\\).' -> 'de \\(\\RRR\\)'.")
add(page=76, where="N.B., 'le th. 2.14 de R.R.R.'",
    scan="de R.R.R. (one final full stop, which also ends the sentence; both scans)",
    tex="de \\(\\RRR\\). (renders 'de RRR.')",
    kind="punctuation", confidence="high",
    fix={"old": "de \\(\\RRR\\).", "new": "de \\(\\mathrm{R.R.R.}\\)"},
    note="As the entry before.")
add(page=76, where="'utilisant (6), (9), R.R. pour (Y',X', y λ_{-1}(F)) et la formule'",
    scan="y λ_{-1}(F): no check over this F (both scans); the check is clear over F in 'R.R. est vrai pour "
         "(Y',X', y λ_{-1}(F̌))' above and in (13)",
    tex="\\((Y',X',y\\lambda_{-1}(F))\\) (printed reading kept)",
    kind="misprint_in_print", confidence="medium",
    fix=None,
    corrected="\\((Y',X',y\\lambda_{-1}(\\check F))\\)",
    note="The R.R. used here is the one just obtained from the corollary of lemme 2, for "
         "(Y',X', y λ_{-1}(F̌)); with (13) it gives (12). The hand-drawn check was left out. "
         "The TeX keeps the printed reading.")
add(page=76, where="Extrait d'une lettre, 'soit une variété obtenu par éclatement'",
    scan="une variété obtenu (both scans)",
    tex="une variété obtenu (printed reading kept)",
    kind="misprint_in_print", confidence="medium",
    fix=None,
    corrected="une variété obtenue",
    note="Agreement slip of the print (variété is feminine). The TeX keeps the printed reading.")

# ---------------- page 78 ----------------
add(page=78, where="exposé heading",
    scan="the title page prints no exposé number: only the two-line title and 'par L. ILLUSIE' (both scans); "
         "the running head 'I' begins on p. 79",
    tex="\\section*{Exposé I. Généralités sur les conditions de finitude dans les catégories dérivées}",
    kind="extra", confidence="medium",
    fix={"old": "\\section*{Exposé I. ", "new": "\\section*{"},
    note="Editorial heading words, like the 'Appendice à l'Exposé 0 : RRR' heading removed at p. 20 and the "
         "SGA 5 'SGA 5 --- ' prefixes (global item 75). The headings of Exposés I to XIV in main.tex all have "
         "this 'Exposé N. Title' form (e.g. lines 3766, 5357, 6571): one decision for the volume. Independent "
         "of the next entry.")
add(page=78, where="exposé title",
    scan="GÉNÉRALITÉS SUR LES CONDITIONS DE FINITUDE DANS LES / CATÉGORIES DÉRIVÉES: capitals with their "
         "accents, two centred lines, each with a double underline (both scans)",
    tex="Généralités sur les conditions de finitude dans les catégories dérivées (small letters, no underline)",
    kind="word", confidence="medium",
    fix={"old": "Généralités sur les conditions de finitude dans les catégories dérivées}",
         "new": "\\underline{\\underline{GÉNÉRALITÉS SUR LES CONDITIONS DE FINITUDE DANS LES}}\\\\[3pt] "
                "\\underline{\\underline{CATÉGORIES DÉRIVÉES}}}"},
    note="Same form as the titles of p. 1 and p. 20 (applied). \\underline cannot break a line, hence the break "
         "at the print's line end. If exposé titles set in \\section* are accepted without underline, keep the "
         "capitals only.")
add(page=78, where="author line",
    scan="par L. ILLUSIE: the name in capitals, the whole line underlined (both scans)",
    tex="par L. Illusie",
    kind="word", confidence="medium",
    fix={"old": "par L. Illusie", "new": "\\underline{par L. ILLUSIE}"},
    note="As 'par A. GROTHENDIECK' on p. 20 (applied).")

# ---------------- page 79 ----------------
add(page=79, where="display 'L_n → L_{n-1} → ... → L_o → F → 0 ,'",
    scan="three typed full stops on the baseline, below the level of the arrows (both scans; "
         "crops_076_080/p79_seq.png)",
    tex="\\cdots",
    kind="symbol", confidence="medium",
    fix={"old": "L_{n-1}\\longrightarrow \\cdots \\longrightarrow L_0",
         "new": "L_{n-1}\\longrightarrow \\ldots \\longrightarrow L_0"},
    note="\\cdots sets the dots at mid-height (same kind of fix as p. 49). Same on p. 80.")
add(page=79, where="'le troisième l'est aussi. On généralise aisément'",
    scan="'On généralise ...' follows 'troisième l'est aussi.' on the same line (both scans): the print runs on",
    tex="blank line (new paragraph) before 'On généralise'",
    kind="other", confidence="high",
    fix={"old": "l'est aussi.\n\nOn généralise", "new": "l'est aussi. On généralise"},
    note="Added paragraph break; the typescript indents its new paragraphs (p. 79 'Si O_X est un faisceau').")
add(page=79, where="'en tant que Module. La notion de complexe pseudo-cohérent'",
    scan="'La' stands at the end of the line 'que F est pseudo-cohérent ... en tant que Module. La' "
         "(both scans): the print runs on",
    tex="blank line (new paragraph) before 'La notion de complexe pseudo-cohérent'",
    kind="other", confidence="high",
    fix={"old": "en tant que Module.\n\nLa notion", "new": "en tant que Module. La notion"},
    note="Added paragraph break, as the entry before.")

# ---------------- page 80 ----------------
add(page=80, where="display '0 → L_n → ... → L_o → F → 0 ,'",
    scan="three typed full stops on the baseline, below the level of the arrows (both scans; "
         "crops_076_080/p80_seq.png)",
    tex="\\cdots",
    kind="symbol", confidence="medium",
    fix={"old": "L_n\\longrightarrow \\cdots \\longrightarrow L_0",
         "new": "L_n\\longrightarrow \\ldots \\longrightarrow L_0"},
    note="As p. 79.")
add(page=80, where="'On a évidemment D(X)_parf ⊂ D(X)_coh , mais l'inclusion est stricte'",
    scan="the inclusion stands in the running text: 'tensoriel dérivés. On a évidemment D(X)_parf ⊂ D(X)_coh , "
         "mais l'inclusion est' is one line (both scans)",
    tex="a display \\[ \\Db(X)_{\\mathrm{parf}}\\subset\\Db(X)_{\\mathrm{coh}}, \\]",
    kind="other", confidence="medium",
    fix={"old": "On a évidemment\n\\[\n  \\Db(X)_{\\mathrm{parf}}\\subset\\Db(X)_{\\mathrm{coh}},\n\\]\nmais",
         "new": "On a évidemment \\(\\Db(X)_{\\mathrm{parf}}\\subset\\Db(X)_{\\mathrm{coh}}\\), mais"},
    note="The TeX makes an inline formula a display (same kind of fix as p. 21).")
add(page=80, where="triangle diagram R, L, F",
    scan="a comma to the right of F (both scans)",
    tex="tikzcd without punctuation",
    kind="punctuation", confidence="high",
    fix={"old": "F \\arrow[ul]", "new": "F \\arrow[ul] ,"},
    note="Punctuation printed after a diagram, set in the last cell as on p. 59. The arrows R → L, L → F, "
         "F → R agree with the print.")

order = ["page", "where", "scan", "tex", "kind", "confidence", "fix", "corrected", "note"]
out = [{k: f[k] for k in order if k in f} for f in F]

ok = True
for f in out:
    if f["fix"] is None:
        continue
    t = (B / f"page_{f['page']:03d}.tex").read_text(encoding="utf-8")
    n = t.count(f["fix"]["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE", f["page"], n, repr(f["fix"]["old"]))
    if "%%%%%%%%%%" in f["fix"]["old"] or "%%%%%%%%%%" in f["fix"]["new"]:
        ok = False
        print("MARKER TOUCHED", f["page"], f["where"])
OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
counts = {}
for f in out:
    c = counts.setdefault(f["page"], [0, 0])
    c[1 if f["kind"] == "misprint_in_print" else 0] += 1
print("all unique" if ok else "PROBLEMS", counts, OUT)
