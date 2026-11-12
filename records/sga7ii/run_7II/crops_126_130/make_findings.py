import json
import os

RUN = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II"
FOLDER = os.path.join(RUN, "b126_130")
OUT = os.path.join(RUN, "findings_126_130.json")

FRAK_SCAN_128 = "typed Fraktur letters (checked at 3-4x): Fraktur X and Fraktur D, the same element as the Fraktur letters of Exposé XIII"
FRAK_NOTE = "Fraktur letters of 1.4 typed as \\mathcal; \\mathfrak (amsfonts) as in the diplomatic TeX of Exposés XVIII and XXI."

F = []

def add(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "confidence": confidence, "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)

# ---------------- page 126 ----------------
add(126, "1.3.4, heading 'Préliminaire:'",
    "Préliminaire underlined; the underline stops before the colon (checked at 3x)",
    "\\underline{Préliminaire:}",
    "underline", "high",
    {"old": "\\underline{Préliminaire:}", "new": "\\underline{Préliminaire}:"},
    "Colon counterpart of the globally handled comma/full stop inside \\underline; drop this if the global rule covers colons.")

# ---------------- page 127 ----------------
add(127, "last paragraph of 1.3.5, 'et quitte à retrécir D davantage'",
    "retrécir: no accent on the first e (checked at 3x)",
    "\\underline{et quitte à retrécir}",
    "misprint_in_print", "high", None,
    "Spelling error of the print; the TeX keeps the printed reading. Same spelling at the end of 1.3.6.",
    corrected="\\underline{et quitte à rétrécir}")

add(127, "end of 1.3.6, '(quitte à retrécir D )'",
    "retrécir: no accent on the first e (checked at 3x)",
    "(quitte à retrécir $D$ )",
    "misprint_in_print", "high", None,
    "Spelling error of the print; the TeX keeps the printed reading.",
    corrected="(quitte à rétrécir $D$ )")

# ---------------- page 128 ----------------
add(128, "1.4.1, first display '(revêtements universel de D* ) ⟶ (espaces topologiques)'",
    "revêtements universel (no final s on universel; checked at 2x)",
    "(\\mbox{revêtements universel de } D^*\\ )",
    "misprint_in_print", "high", None,
    "Agreement error of the print; the second display of 1.4.1 prints 'revêtements universels'. The TeX keeps the printed reading.",
    corrected="(\\mbox{revêtements universels de } D^*\\ )")

add(128, "1.4.1, 'Un espace topologique 𝔛* sur 𝔇* est un foncteur'",
    "𝔛* sur 𝔇*: " + FRAK_SCAN_128,
    "$\\mathcal{X}^*$ sur $\\mathcal{D}^*$ est un foncteur",
    "font", "high",
    {"old": "$\\mathcal{X}^*$ sur $\\mathcal{D}^*$ est un foncteur",
     "new": "$\\mathfrak{X}^*$ sur $\\mathfrak{D}^*$ est un foncteur"},
    FRAK_NOTE)

add(128, "1.4.1, 'on le note 𝔛*_t . Un faisceau sur 𝔛* est un foncteur'",
    "𝔛*_t and 𝔛*: Fraktur X",
    "$\\mathcal{X}^*_t$ . \\underline{Un faisceau} sur $\\mathcal{X}^*$",
    "font", "high",
    {"old": "$\\mathcal{X}^*_t$ . \\underline{Un faisceau} sur $\\mathcal{X}^*$",
     "new": "$\\mathfrak{X}^*_t$ . \\underline{Un faisceau} sur $\\mathfrak{X}^*$"},
    FRAK_NOTE)

add(128, "1.4.1, 'A 𝔛* , on associe l'espace topologique β* 𝔛* = ...'",
    "both 𝔛*: Fraktur X",
    "A $\\mathcal{X}^*$ , on associe l'espace topologique $\\beta^* \\mathcal{X}^* =",
    "font", "high",
    {"old": "A $\\mathcal{X}^*$ , on associe l'espace topologique $\\beta^* \\mathcal{X}^* =",
     "new": "A $\\mathfrak{X}^*$ , on associe l'espace topologique $\\beta^* \\mathfrak{X}^* ="},
    FRAK_NOTE)

add(128, "1.4.1, 'Tout faisceau F sur 𝔛* définit'",
    "𝔛*: Fraktur X",
    "sur $\\mathcal{X}^*$ définit",
    "font", "high",
    {"old": "sur $\\mathcal{X}^*$ définit", "new": "sur $\\mathfrak{X}^*$ définit"},
    FRAK_NOTE)

add(128, "1.4.1, 'un faisceau β*F sur β* 𝔛* , d'où'",
    "β* 𝔛*: Fraktur X",
    "sur $\\beta^* \\mathcal{X}^*$ , d'où",
    "font", "high",
    {"old": "sur $\\beta^* \\mathcal{X}^*$ , d'où", "new": "sur $\\beta^* \\mathfrak{X}^*$ , d'où"},
    FRAK_NOTE)

add(128, "1.4.1, diagram, top row β* 𝔛* → 𝔛*",
    "both top nodes carry Fraktur X",
    "\\beta^* \\mathcal{X}^* \\arrow[r] \\arrow[d] & \\mathcal{X}^* \\arrow[d]",
    "font", "high",
    {"old": "\\beta^* \\mathcal{X}^* \\arrow[r] \\arrow[d] & \\mathcal{X}^* \\arrow[d]",
     "new": "\\beta^* \\mathfrak{X}^* \\arrow[r] \\arrow[d] & \\mathfrak{X}^* \\arrow[d]"},
    FRAK_NOTE + " The STRUCTURE comment below the diagram still says 'script'.")

add(128, "1.4.1, diagram, bottom-right node 𝔇*",
    "𝔇*: Fraktur D",
    "\\arrow[r, \"\\beta\"] & \\mathcal{D}^*",
    "font", "high",
    {"old": "\\arrow[r, \"\\beta\"] & \\mathcal{D}^*",
     "new": "\\arrow[r, \"\\beta\"] & \\mathfrak{D}^*"},
    FRAK_NOTE)

add(128, "1.4.1, after the diagram",
    "a typed full stop to the right of 𝔇* on the bottom row",
    "\\end{tikzcd} (no full stop; the STRUCTURE comment records it)",
    "punctuation", "high",
    {"old": "\\end{tikzcd}", "new": "\\end{tikzcd}\\quad ."},
    "Known case of punctuation after a diagram; written as in the earlier fixes. Does not overlap the Fraktur fix of the node 𝔇*.")

add(128, "1.4.2, 'Un espace topologique 𝔛 sur 𝔇 consiste en'",
    "𝔛, 𝔇: Fraktur X and D",
    "$\\mathcal{X}$ sur $\\mathcal{D}$ consiste en",
    "font", "high",
    {"old": "$\\mathcal{X}$ sur $\\mathcal{D}$ consiste en",
     "new": "$\\mathfrak{X}$ sur $\\mathfrak{D}$ consiste en"},
    FRAK_NOTE)

add(128, "1.4.2 (a), 'un espace topologique 𝔛* sur 𝔇* ;'",
    "𝔛*, 𝔇*: Fraktur X and D",
    "$\\mathcal{X}^*$ sur $\\mathcal{D}^*$ ;",
    "font", "high",
    {"old": "$\\mathcal{X}^*$ sur $\\mathcal{D}^*$ ;",
     "new": "$\\mathfrak{X}^*$ sur $\\mathfrak{D}^*$ ;"},
    FRAK_NOTE)

add(128, "1.4.2, 'Un faisceau sur 𝔛 consiste en un faisceau'",
    "𝔛: Fraktur X",
    "sur $\\mathcal{X}$ consiste en un faisceau",
    "font", "high",
    {"old": "sur $\\mathcal{X}$ consiste en un faisceau",
     "new": "sur $\\mathfrak{X}$ consiste en un faisceau"},
    FRAK_NOTE)

add(128, "1.4.2, 'un faisceau sur 𝔛* , donné par F_η'",
    "𝔛*: Fraktur X",
    "sur $\\mathcal{X}^*$ , donné par",
    "font", "high",
    {"old": "sur $\\mathcal{X}^*$ , donné par", "new": "sur $\\mathfrak{X}^*$ , donné par"},
    FRAK_NOTE)

# ---------------- page 129 ----------------
add(129, "first diagram, top row X_o ↪ 𝔛 ↩ 𝔛*",
    "𝔛 and 𝔛*: Fraktur X",
    "hook] \\arrow[d] & \\mathcal{X} \\arrow[d] & \\mathcal{X}^*",
    "font", "high",
    {"old": "hook] \\arrow[d] & \\mathcal{X} \\arrow[d] & \\mathcal{X}^*",
     "new": "hook] \\arrow[d] & \\mathfrak{X} \\arrow[d] & \\mathfrak{X}^*"},
    FRAK_NOTE + " Apply before the next finding (missing arrowhead), whose 'old' is taken from the text after this edit.")

add(129, "first diagram, middle vertical 𝔛 — 𝔇",
    "a plain vertical rule from 𝔛 down to 𝔇 with no arrowhead (checked at 2x; the rule ends clean; the outer verticals X_o → {O} and 𝔛* → 𝔇* have heads)",
    "\\mathcal{X} \\arrow[d] & (arrowhead drawn)",
    "misprint_in_print", "high",
    {"old": "\\mathfrak{X} \\arrow[d] & \\mathfrak{X}^*",
     "new": "\\mathfrak{X} \\arrow[d, dash] & \\mathfrak{X}^*"},
    "The structural morphism 𝔛 → 𝔇 (it has its head in the second diagram of the page). The TeX silently supplies the arrowhead; the edit restores the printed plain rule. 'old' is taken from the text after the preceding Fraktur edit of this row, which must be applied first.",
    corrected="\\arrow[d]")

add(129, "first diagram, bottom row {O} ↪ 𝔇 ↩ 𝔇*",
    "𝔇 and 𝔇*: Fraktur D",
    "& \\mathcal{D} & \\mathcal{D}^*",
    "font", "high",
    {"old": "& \\mathcal{D} & \\mathcal{D}^*", "new": "& \\mathfrak{D} & \\mathfrak{D}^*"},
    FRAK_NOTE)

add(129, "after the first diagram",
    "a typed full stop to the right of 𝔇* on the bottom row",
    "\\end{tikzcd} (no full stop; the STRUCTURE comment records it)",
    "punctuation", "high",
    {"old": "\\arrow[l, hook]\n\\end{tikzcd}", "new": "\\arrow[l, hook]\n\\end{tikzcd}\\quad ."},
    "Known case of punctuation after a diagram; written as in the earlier fixes. Does not overlap the Fraktur fix of the bottom row.")

add(129, "'un morphisme de topos Ψ : 𝔛 → X_o × 𝔇'",
    "𝔛, 𝔇: Fraktur X and D",
    "$\\Psi : \\mathcal{X} \\to X_o \\times \\mathcal{D}$",
    "font", "high",
    {"old": "$\\Psi : \\mathcal{X} \\to X_o \\times \\mathcal{D}$",
     "new": "$\\Psi : \\mathfrak{X} \\to X_o \\times \\mathfrak{D}$"},
    FRAK_NOTE)

add(129, "'Ce morphisme induit Ψ_η : 𝔛* ⟶ X_o × 𝔇*'",
    "𝔛*, 𝔇*: Fraktur X and D",
    "\\Psi_\\eta : \\mathcal{X}^* \\longrightarrow X_o \\times \\mathcal{D}^*",
    "font", "high",
    {"old": "\\Psi_\\eta : \\mathcal{X}^* \\longrightarrow X_o \\times \\mathcal{D}^*",
     "new": "\\Psi_\\eta : \\mathfrak{X}^* \\longrightarrow X_o \\times \\mathfrak{D}^*"},
    FRAK_NOTE)

add(129, "1.4.3, 'A un espace topologique 𝔛 sur 𝔇 , on associe'",
    "𝔛, 𝔇: Fraktur X and D",
    "$\\mathcal{X}$ sur $\\mathcal{D}$ , on associe",
    "font", "high",
    {"old": "$\\mathcal{X}$ sur $\\mathcal{D}$ , on associe",
     "new": "$\\mathfrak{X}$ sur $\\mathfrak{D}$ , on associe"},
    FRAK_NOTE)

add(129, "1.4.3, 'X = β* 𝔛 sur D'",
    "𝔛: Fraktur X",
    "$X = \\beta^* \\mathcal{X}$",
    "font", "high",
    {"old": "$X = \\beta^* \\mathcal{X}$", "new": "$X = \\beta^* \\mathfrak{X}$"},
    FRAK_NOTE)

add(129, "1.4.3, 'On adjoint à X* = β* 𝔛* la fibre'",
    "𝔛*: Fraktur X",
    "$X^* = \\beta^* \\mathcal{X}^*$",
    "font", "high",
    {"old": "$X^* = \\beta^* \\mathcal{X}^*$", "new": "$X^* = \\beta^* \\mathfrak{X}^*$"},
    FRAK_NOTE)

add(129, "1.4.3, 'en prenant pour système fondamental de voisinage de x_o'",
    "voisinage (singular; checked at 2x)",
    "système fondamental de voisinage de",
    "misprint_in_print", "medium", None,
    "Agreement slip of the print (a fundamental system of neighbourhoods); the TeX keeps the printed reading.",
    corrected="système fondamental de voisinages de")

add(129, "1.4.3, 'Pour F un faisceau sur 𝔛* , on a'",
    "𝔛*: Fraktur X",
    "un faisceau sur $\\mathcal{X}^*$ , on a",
    "font", "high",
    {"old": "un faisceau sur $\\mathcal{X}^*$ , on a", "new": "un faisceau sur $\\mathfrak{X}^*$ , on a"},
    FRAK_NOTE)

add(129, "1.4.3, second diagram, top-right node 𝔛",
    "𝔛: Fraktur X",
    "& \\mathcal{X} \\arrow[d] \\\\",
    "font", "high",
    {"old": "& \\mathcal{X} \\arrow[d] \\\\", "new": "& \\mathfrak{X} \\arrow[d] \\\\"},
    FRAK_NOTE)

add(129, "1.4.3, second diagram, bottom-right node 𝔇",
    "𝔇: Fraktur D",
    "D \\arrow[r, \"\\beta\"] & \\mathcal{D}",
    "font", "high",
    {"old": "D \\arrow[r, \"\\beta\"] & \\mathcal{D}", "new": "D \\arrow[r, \"\\beta\"] & \\mathfrak{D}"},
    FRAK_NOTE)

add(129, "'tel que, pour tout faisceau F sur 𝔛 , on ait'",
    "𝔛: Fraktur X",
    "sur $\\mathcal{X}$ , on ait",
    "font", "high",
    {"old": "sur $\\mathcal{X}$ , on ait", "new": "sur $\\mathfrak{X}$ , on ait"},
    FRAK_NOTE)

# ---------------- page 130 ----------------
FRAK_NOTE_BB = "Fraktur letters typed here as \\mathbb (blackboard bold); \\mathfrak as on pp. 128-129."

add(130, "first line, 'entre foncteurs de D^+(𝔛) dans D^+(X_o × 𝔇)'",
    "𝔛 and 𝔇: Fraktur X and D (the 𝔇 typed heavily, same shape; checked at 3x)",
    "$D^+(\\mathbb{X})$ \\underline{dans} $D^+(X_o \\times \\mathbb{D})$",
    "font", "high",
    {"old": "$D^+(\\mathbb{X})$ \\underline{dans} $D^+(X_o \\times \\mathbb{D})$",
     "new": "$D^+(\\mathfrak{X})$ \\underline{dans} $D^+(X_o \\times \\mathfrak{D})$"},
    FRAK_NOTE_BB)

add(130, "1.4.6, 'pour K ∈ Ob D^+(𝔛*)'",
    "𝔛*: Fraktur X",
    "D^+(\\mathbb{X}^*)",
    "font", "high",
    {"old": "D^+(\\mathbb{X}^*)", "new": "D^+(\\mathfrak{X}^*)"},
    FRAK_NOTE_BB)

add(130, "'Pour K sur 𝔛 , avec sp : sp* K_o ⟶ K_η'",
    "𝔛: Fraktur X",
    "Pour $K$ sur $\\mathbb{X}$",
    "font", "high",
    {"old": "Pour $K$ sur $\\mathbb{X}$", "new": "Pour $K$ sur $\\mathfrak{X}$"},
    FRAK_NOTE_BB)

# ---------------- verification ----------------
texts = {}
for p in (126, 127, 128, 129, 130):
    with open(os.path.join(FOLDER, "page_%03d.tex" % p), encoding="utf-8", newline="") as fh:
        texts[p] = fh.read()
    assert "\r" not in texts[p], p

ok = True
applied = dict(texts)
for d in F:
    fx = d["fix"]
    if fx is None:
        continue
    p = d["page"]
    n_orig = texts[p].count(fx["old"])
    n_seq = applied[p].count(fx["old"])
    if "%%%%%%%%%%" in fx["old"]:
        print("MARKER IN OLD", d["where"]); ok = False
    if n_seq != 1:
        print("NOT UNIQUE (sequential)", p, n_orig, n_seq, repr(fx["old"])); ok = False
    elif n_orig != 1:
        print("needs the preceding edit:", p, repr(fx["old"]))
    applied[p] = applied[p].replace(fx["old"], fx["new"], 1)

# overlap check of olds in the original texts (except the declared sequential one)
for p in texts:
    spans = []
    for d in F:
        if d["page"] != p or d["fix"] is None:
            continue
        o = d["fix"]["old"]
        i = texts[p].find(o)
        if i >= 0:
            spans.append((i, i + len(o), o))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            print("OVERLAP on", p, repr(a[2]), repr(b[2]))

for p in texts:
    left = applied[p].count("\\mathcal{X}") + applied[p].count("\\mathcal{D}") + applied[p].count("\\mathbb{X}") + applied[p].count("\\mathbb{D}")
    # count only outside comment lines
    body = "\n".join(l for l in applied[p].split("\n") if not l.lstrip().startswith("%"))
    left_body = sum(body.count(s) for s in ("\\mathcal{X}", "\\mathcal{D}", "\\mathbb{X}", "\\mathbb{D}"))
    print(p, "remaining script/bb X,D in body after all fixes:", left_body)

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
    fh.write("\n")

from collections import Counter
c = Counter((d["page"], d["kind"] == "misprint_in_print") for d in F)
for p in (126, 127, 128, 129, 130):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
print("OK" if ok else "PROBLEMS")
