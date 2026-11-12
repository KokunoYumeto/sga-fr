import json, os, sys

RUN = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I"
FOLDER = os.path.join(RUN, "b151_155")
OUT = os.path.join(RUN, "findings_151_155.json")

EP_NOTE = ("The marked section of P is e_P: the print has the same capital P here as in 1.3.1.0 "
           "('muni d'une section e_P', p. 144), and the TeX writes e_P on pp. 144-150. Same slip as "
           "G_p for G_P. (expose_VII_body.tex line 923 has one more e_p, in $(e_p,e_Q)$, on a later page.)")
TIMES_NOTE = ("The TeX writes the letter x (set as a math-italic x) for the printed product cross; "
              "elsewhere in the expose it writes \\times (P\\times P, G_{P\\times P} on p. 152), and p. 135 "
              "GxP was fixed the same way.")

F = []

def add(**kw):
    F.append(kw)

# ---------------- page 151 ----------------
add(page=151,
    where="first paragraph: 'u est trivial sur les trois morceaux P\u00d7e_P\u00d7e_P , e_P\u00d7P\u00d7e_P , e_P\u00d7e_P\u00d7P' (first morceau)",
    scan="P\u00d7e_P\u00d7e_P: both subscripts are capital P (cap height, top level with the subscript G of e_G on this page, no descender)",
    tex="$P\\times e_p\\times e_p$",
    kind="symbol", confidence="high",
    fix={"old": "$P\\times e_p\\times e_p$", "new": "$P\\times e_P\\times e_P$"},
    note=EP_NOTE)
add(page=151,
    where="same sentence, second morceau 'e_P\u00d7P\u00d7e_P'",
    scan="e_P\u00d7P\u00d7e_P (capital P in both subscripts)",
    tex="$e_p\\times P\\times e_p$",
    kind="symbol", confidence="high",
    fix={"old": "$e_p\\times P\\times e_p$", "new": "$e_P\\times P\\times e_P$"},
    note="As the previous entry.")
add(page=151,
    where="same sentence, third morceau 'e_P\u00d7e_P\u00d7P'",
    scan="e_P\u00d7e_P\u00d7P (capital P in both subscripts)",
    tex="$e_p\\times e_p\\times P$",
    kind="symbol", confidence="high",
    fix={"old": "$e_p\\times e_p\\times P$", "new": "$e_P\\times e_P\\times P$"},
    note="As the previous entries.")
add(page=151,
    where="Corollaire 1.3.6, second line: 'qui est trivial sur P\u00d7e_G et sur e_P\u00d7G soit trivial'",
    scan="e_P\u00d7G: capital P subscript, same height and level as the subscript G of e_G just before",
    tex="\\underline{et sur} $e_p\\times G$",
    kind="symbol", confidence="high",
    fix={"old": "\\underline{et sur} $e_p\\times G$", "new": "\\underline{et sur} $e_P\\times G$"},
    note="As the previous entries.")
add(page=151,
    where="proof of 1.3.6: 'tel que les restrictions \u00e0 P\u00d7e_G et \u00e0 e_P\u00d7G du morphisme correspondant'",
    scan="e_P\u00d7G (capital P subscript)",
    tex="\u00e0 $e_p\\times G$",
    kind="symbol", confidence="high",
    fix={"old": "\u00e0 $e_p\\times G$", "new": "\u00e0 $e_P\\times G$"},
    note="As the previous entries.")
add(page=151,
    where="proof of 1.3.6, first sentence: 'il faut prouver que l'op\u00e9ration de P sur G d\u00e9finie par l'extension G est triviale'",
    scan="l'extension G (checked at zoom: the same capital G as in 'sur G' just before)",
    tex="l'extension $G$",
    kind="misprint_in_print", confidence="medium",
    fix=None,
    corrected="l'extension $E$",
    note=("G is the kernel; the operation of P on G is the one defined by the extension (the Groupe E) of P by G, "
          "named E in the second assertion and in 'si E est une extension de P par G' a few lines below. "
          "The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring."))

# ---------------- page 153 ----------------
add(page=153,
    where="top of the page, before 'd\u00e9finie par \u03b4(E), o\u00f9'",
    scan="the page's text begins with 'd\u00e9finie par \u03b4(E), o\u00f9' (continuing the sentence of p. 152); 'VII' is only the running head at the top right, beside '- 21 -'",
    tex="VII (a line of its own after the marker line)",
    kind="extra", confidence="high",
    fix={"old": "\nVII\n", "new": "\n"},
    note=("The running head was typed into the body text: it would print 'VII' inside the sentence "
          "'... la nullit\u00e9 de la section \u03b4(E) \u2208 \u0393 R^1 h_*(G_{P\u00d7P}) d\u00e9finie par \u03b4(E), o\u00f9'. "
          "Same on p. 154; expose_VII_body.tex has two more such lines (889 and 904) on later pages."))
add(page=153,
    where="display after 'd\u00e9finie par \u03b4(E), o\u00f9': 'h : P\u00d7P \u27f6 e'",
    scan="P\u00d7P with the serifless product cross",
    tex="h : PxP",
    kind="symbol", confidence="high",
    fix={"old": "h : PxP", "new": "h : P\\times P"},
    note=TIMES_NOTE)
add(page=153,
    where="1.3.8, paragraph after (1.3.8.1): 'pour les puissances cart\u00e9siennes P\u00d7P, P\u00d7P\u00d7P, ...'",
    scan="P\u00d7P, P\u00d7P\u00d7P with product crosses",
    tex="cart\u00e9siennes $PxP$, $PxPxP$",
    kind="symbol", confidence="high",
    fix={"old": "cart\u00e9siennes $PxP$, $PxPxP$", "new": "cart\u00e9siennes $P\\times P$, $P\\times P\\times P$"},
    note="As the previous entry.")
add(page=153,
    where="paragraph 'Si maintenant G est un sch\u00e9ma affine': 'la m\u00eame conclusion s'applique aux produits P\u00d7P, P\u00d7P\u00d7P, et de m\u00eame'",
    scan="P\u00d7P, P\u00d7P\u00d7P with product crosses",
    tex="produits $PxP$, $PxPxP$",
    kind="symbol", confidence="high",
    fix={"old": "produits $PxP$, $PxPxP$", "new": "produits $P\\times P$, $P\\times P\\times P$"},
    note="As the previous entries.")
add(page=153,
    where="last paragraph: 'on voit que tout morphisme de P, P\u00d7P, P\u00d7P\u00d7P ... dans G'",
    scan="P\u00d7P, P\u00d7P\u00d7P with product crosses",
    tex="de $P$, $PxP$, $PxPxP$",
    kind="symbol", confidence="high",
    fix={"old": "de $P$, $PxP$, $PxPxP$", "new": "de $P$, $P\\times P$, $P\\times P\\times P$"},
    note="As the previous entries.")

# ---------------- page 154 ----------------
add(page=154,
    where="top of the page, before 'tout S-morphisme'",
    scan="the page's text begins with 'tout S-morphisme P\u00d7G \u27f6 G' (continuing the sentence of p. 153); 'VII' is only the running head at the top right, beside '- 22 -'",
    tex="VII (a line of its own after the marker line)",
    kind="extra", confidence="high",
    fix={"old": "\nVII\n", "new": "\n"},
    note="Running head typed into the body text, as on p. 153; it would print 'VII' inside the sentence '... de m\u00eame si G est plat, tout S-morphisme ...'.")
add(page=154,
    where="first line: 'tout S-morphisme P\u00d7G \u27f6 G compatible avec les sections marqu\u00e9es'",
    scan="P\u00d7G with the product cross",
    tex="$PxG$",
    kind="symbol", confidence="high",
    fix={"old": "$PxG$", "new": "$P\\times G$"},
    note=TIMES_NOTE)
add(page=154,
    where="1.3.8.2, third line: 'Dans ce cas, les conclusions de 3.5 et de 3.6 sont donc valables pour tout Groupe G affine sur S'",
    scan="de 3.5 et de 3.6",
    tex="de 3.5 et de 3.6",
    kind="misprint_in_print", confidence="medium",
    fix=None,
    corrected="de 1.3.5 et de 1.3.6",
    note=("The conclusions meant are those of 1.3.5 and 1.3.6, named in full just before ('les conditions "
          "d'application de 1.3.5, et \u00e9galement de 1.3.6', top of this page; 'les hypoth\u00e8ses faites dans 1.3.5 "
          "et dans 1.3.6', p. 152); 3.5 and 3.6 would point to section 3 of the expos\u00e9. Wrong reference numbers; "
          "the TeX keeps the printed reading. 'corrected' replaces the 'tex' substring."))

# ---------------- page 155 ----------------
add(page=155,
    where="after (1.4.5): 'qui pour A=Z et i=0,1 co\u00eencident avec (1.4.3) et (1.4.4)'",
    scan="co\u00eencident: a peaked circumflex over the i (checked at 10x zoom), not a diaeresis",
    tex="co\u00efncident",
    kind="misprint_in_print", confidence="high",
    fix={"old": "co\u00efncident", "new": "co\u00eencident"},
    corrected="co\u00efncident",
    note=("Same printed spelling as on pp. 144-145 (circumflex for diaeresis). The TeX silently corrects it; "
          "the fix restores the print. 'corrected' is the current TeX."))

# ---------------- checks ----------------
ok = True
for i, f in enumerate(F):
    keys = list(f.keys())
    fx = f.get("fix")
    if fx is not None:
        path = os.path.join(FOLDER, "page_%03d.tex" % f["page"])
        with open(path, "r", encoding="utf-8", newline="") as h:
            txt = h.read()
        n = txt.count(fx["old"])
        marker_cross = "%%%%%%%%%%" in fx["old"]
        if n != 1 or marker_cross:
            ok = False
            print("BAD", i, f["page"], repr(fx["old"]), n, marker_cross)
        else:
            print("ok ", i, f["page"], repr(fx["old"]))
    else:
        path = os.path.join(FOLDER, "page_%03d.tex" % f["page"])
        with open(path, "r", encoding="utf-8", newline="") as h:
            txt = h.read()
        n = txt.count(f["tex"])
        print("nofix", i, f["page"], repr(f["tex"]), "tex occurs", n)

# order keys as specified
ORDER = ["page", "where", "scan", "tex", "kind", "confidence", "fix", "corrected", "note"]
out = []
for f in F:
    d = {}
    for k in ORDER:
        if k in f:
            d[k] = f[k]
    out.append(d)

if ok:
    with open(OUT, "w", encoding="utf-8", newline="\n") as h:
        json.dump(out, h, ensure_ascii=False, indent=1)
        h.write("\n")
    print("written", OUT, len(out))
else:
    print("NOT WRITTEN")
    sys.exit(1)
