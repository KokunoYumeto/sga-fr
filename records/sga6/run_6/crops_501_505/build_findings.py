"""Build findings_501_505.json; check that every fix's old occurs exactly once in its page file, never crosses a
marker line, and that the fixes of a page apply one after the other (no edit destroys another's old)."""
import json, pathlib, sys
sys.stdout.reconfigure(encoding='utf-8')
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
B = RUN / "b501_505"
OUT = RUN / "findings_501_505.json"
NL = "\\n"   # a written line break inside notes
M502 = "%%%%%%%%%%  scan idx 515  |  folio 502  %%%%%%%%%%"
M505 = "%%%%%%%%%%  scan idx 518  |  folio 505  %%%%%%%%%%"

F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def fx(old, new):
    return {"old": old, "new": new}


# ---------------------------------------------------------------- page 501
add(501, "'Enfin, on note encore ξ_i les images des ξ_i dans K˙(X_S') et K˙(X_U), et on note :'",
    "a comma after K˙(X_U): the witness has a clean comma with nothing above it; the main scan has the comma with a "
    "faint speck above and to its left, far smaller and lighter than the upper dot of the page's semicolons ('; on a :') "
    "(crops_501_505/m501_KXU_zoom.png, w501_KXU_zoom2.png, m501_semicolon_ref.png)",
    r"$K^\circ(X_U)$; et on note :",
    "punctuation", "high",
    fx("$; et on note :", "$, et on note :"),
    "The semicolon reads the speck as the dot of a semicolon. The old string avoids K^\\circ, so the entry applies "
    "before or after the K˙ script (entry below).")

add(501, "diagram (1.2.1), end of the lower row 'K.(X_U) → 0'",
    "no punctuation after the 0 (both scans)",
    r"K_\bullet(X_U) \arrow[r] & 0,",
    "punctuation", "high",
    fx("& 0,", "& 0"),
    "The TeX adds a comma at the end of the display.")

add(501, "'Soit (x'_i)_{i∈I} ∈ K.(S')^{(I)} ; on a :'",
    "begins a new, indented paragraph after '... que les deux carrés sont commutatifs.' (both scans)",
    "runs on in the paragraph 'Les deux lignes horizontales ...'",
    "other", "high",
    fx("sont commutatifs. Soit", "sont commutatifs.\n\nSoit"),
    "Missing paragraph break.")

add(501, "K˙ on pp. 501-504 (11 places: 2 on p. 501, 4 on p. 503, 5 on p. 504)",
    "K with a raised filled dot in every place (both scans; crops_501_505/m501_Kdot_zoom.png, m503_Kdot_zoom.png, "
    "w501_KXU.png)",
    r"K^\circ (a raised circle) in all 11 places",
    "symbol", "high", None,
    "Convention of the Exposé IX TeX: K^\\circ for the print's K˙ throughout the exposé (88 in Exposé IX in each "
    "layer, no K^\\bullet there), as in Exposé VII (findings_416_420: one script K^\\circ -> K^{\\bullet}, both layers) "
    "and Exposé VI §1 before the 10 Nov pass: not itemized. Three examples: p. 501 'dans $K^\\circ(X_{S'})$' -> "
    "'dans $K^{\\bullet}(X_{S'})$'; p. 503 'K_\\bullet(S)\\otimes_{K^\\circ(S)}K^\\circ(X)' -> "
    "'K_\\bullet(S)\\otimes_{K^{\\bullet}(S)}K^{\\bullet}(X)'; p. 504 '$1\\in K^\\circ(X)$' -> "
    "'$1\\in K^{\\bullet}(X)$'. No old string in this file contains K^\\circ.")

# ---------------------------------------------------------------- page 502
add(502, "start of page (folio-502 marker)",
    "p. 501 ends '... vraie d'après IV 3.1.1, car i est propre et f plat.'; p. 502 begins, indented, "
    "'Soit (x_i)_{i∈I} ∈ K.(S)^{(I)} ; on a :' (both scans; b501_505/page_501_s4.png, page_502_s1.png; "
    "crops_501_505/wit_501_half.png, wit_502_half.png)",
    "page_501.tex ends 'car $i$ est' above the folio-502 marker; page_502.tex begins 'propre et $f$ plat. Soit "
    "$(x_i)_{i\\in I}$...' in one paragraph",
    "marker", "high", None,
    "Page 502 really begins at 'Soit $(x_i)_{i\\in I}\\in K_\\bullet(S)^{(I)}$~; on a :', and the print starts a new "
    "paragraph there. Exact edit in main.tex, both layers (at the time of checking diplomatic line 12976, current "
    "12982; the file was being edited): replace 'car $i$ est" + NL + M502 + NL + "propre et $f$ plat. Soit "
    "$(x_i)_{i\\in I}' by 'car $i$ est" + NL + "propre et $f$ plat." + NL + NL + M502 + NL + "Soit $(x_i)_{i\\in I}' "
    "(old string once per layer; simulated in memory: crops_501_505/sim_markers.py). The blank line is the print's "
    "paragraph break.")

add(502, "second display, end: '... = Σ_i ξ_i.f*_U ∘ j*(x_i)'",
    "no punctuation after j*(x_i) (both scans; crops_501_505/m502_disp2_end.png, w502_disp2_end.png)",
    r"f_U^*\circ j^*(x_i),",
    "punctuation", "high",
    fx("j^*(x_i),", "j^*(x_i)"),
    "The TeX adds a comma at the end of the display.")

add(502, "diagram K.(S_red)^{(I)} → K.(S)^{(I)} over K.(X_{S_red}) → K.(X)",
    "a comma to the right of the lower row, after K.(X) (both scans)",
    "no punctuation after the diagram",
    "punctuation", "high",
    fx(r"\arrow[r] & K_\bullet(X)", r"\arrow[r] & K_\bullet(X),"),
    "Missing comma; placed in the last cell, as the TeX sets the end of diagram (1.2.1).")

add(502, "'Soit y ∈ K.(X). Par hypothèse, K.(X_s) est engendré ...'",
    "begins a new, indented paragraph after '... alors O_{S,s} = K.' (both scans)",
    "runs on in the paragraph 'On se place donc ...'",
    "other", "high",
    fx("=K$. Soit $y", "=K$.\n\nSoit $y"),
    "Missing paragraph break.")

# ---------------------------------------------------------------- page 503
add(503, "display 'X_s = X×_S Spec(K) = lim← X×_S Spec(A_f)'",
    "no punctuation at the end of the display (both scans)",
    r"\varprojlim_f X\times_S\Spec(A_f),",
    "punctuation", "high",
    fx(r"X\times_S\Spec(A_f),", r"X\times_S\Spec(A_f)"),
    "The TeX adds a comma at the end of the display.")

add(503, "statements of pp. 503-505: Corollaire 1.3 (p. 503), Corollaire 1.4 (p. 504), Proposition 1.6 (p. 505)",
    "underlined word group by word group (both scans): Cor. 1.3 'Soit', 'un morphisme plat de schémas noethériens', "
    "'On suppose que pour tout point', 'de', 'l'homomorphisme', 'est surjectif', 'Alors l'homomorphisme déduit de', "
    "'est surjectif'; Cor. 1.4 'Soit', 'un morphisme plat de schémas noethériens', 'On suppose que pour tout point s "
    "de', 'l'homomorphisme canonique', 'est un isomorphisme', 'Alors l'homomorphisme', 'est surjectif', 'Si de plus', "
    "'possède une section', 'de tor-dimension finie', 'alors', 'est un isomorphisme'; Prop. 1.6 'Soient', 'un schéma "
    "noethérien', 'E', 'un', 'O_S-Module localement libre de type fini', 'le fibré vectoriel associé à E', 'et', "
    "'le morphisme structural de', 'Alors', 'est un isomorphisme'; formulas, the other letters and the punctuation "
    "plain; the labels underline only the word (Remarque 1.5 likewise)",
    "the statements in roman (Exposé IX has one \\underline in all and no \\emph)",
    "underline", "high", None,
    "Exposé IX follows the Exposé II pattern of GLOBAL_ISSUES 82 (pending volume decision), as Exposé VII does "
    "(findings_416_420): not itemized. The TeX adds no emphasis on defined terms on pp. 501-505, and these pages have "
    "no category letter.")

# ---------------------------------------------------------------- page 505
add(505, "start of page (folio-505 marker)",
    "p. 504 ends '... (ou encore lisse en ces points si on suppose f'; p. 505 begins 'de présentation finie).' "
    "(both scans; b501_505/page_504_s4.png, page_505_s1.png; crops_501_505/wit_504_half.png, wit_505_half.png)",
    "page_504.tex ends 'si on suppose $f$ de' above the folio-505 marker; page_505.tex begins 'présentation finie).'",
    "marker", "high", None,
    "Page 505 really begins at 'de présentation finie).'. Exact edit in main.tex, both layers (at the time of "
    "checking diplomatic line 13054, current 13060): replace 'si on suppose $f$ de" + NL + M505 + NL +
    "présentation finie).' by 'si on suppose $f$" + NL + M505 + NL + "de présentation finie).' (old string once per "
    "layer; simulated in memory: crops_501_505/sim_markers.py). The sentence runs on, so no blank line.")

add(505, "the Module E: Proposition 1.6 'E un O_S-Module', 'associé à E'; proof, 'Dans ce cas, E est somme directe'",
    "E underlined in all three places (both scans); the underlined O of O_S and O_{X_s,g(s)} (and O_{S,s} on p. 502) "
    "is the structure sheaf",
    "plain $E$",
    "underline", "high", None,
    "Convention of the Exposé IX TeX (underlined letters written plain), as reported for Exposés VI and VII "
    "(findings_401_405, findings_441_445): not itemized; places listed for the closing pass. The form to use if the "
    "diplomatic layer reproduces the underline: '$E$ un $\\mathcal O_S$-Module' -> '$\\underline{E}$ un "
    "$\\mathcal O_S$-Module'; 'associé à $E$' -> 'associé à $\\underline{E}$'; 'Dans ce cas, $E$ est' -> "
    "'Dans ce cas, $\\underline{E}$ est'. The underlined O written \\mathcal O falls under the pending volume "
    "decision.")

# ---------------------------------------------------------------- checks
ok = True
pages = {}
for d in F:
    pages.setdefault(d["page"], []).append(d)
for p, lst in sorted(pages.items()):
    t = (B / f"page_{p}.tex").read_text(encoding="utf-8")
    assert "\r" not in t
    cur = t
    for d in lst:
        f = d["fix"]
        if not f:
            continue
        old, new = f["old"], f["new"]
        n = t.count(old)
        if n != 1:
            ok = False
            print("NOT UNIQUE", p, n, repr(old))
        if "%%%%%%%%%%" in old or "%%%%%%%%%%" in new:
            ok = False
            print("MARKER IN FIX", p, repr(old))
        if cur.count(old) != 1:
            ok = False
            print("SEQUENTIAL FAIL", p, repr(old))
        cur = cur.replace(old, new, 1)
    print(p, "fixes:", sum(1 for d in lst if d["fix"]), "entries:", len(lst))
for d in F:
    if d["kind"] == "misprint_in_print" and "corrected" not in d:
        ok = False
        print("misprint without corrected", d["where"])
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("written", OUT, len(F), "entries; checks", "OK" if ok else "FAILED")
# round trip
json.loads(OUT.read_text(encoding="utf-8"))
