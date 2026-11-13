import json
from collections import Counter

base = r"C:/Users/user/Documents/sga_scan_check_20261105/run_6"
NL = "\u23ce"  # placeholder for a line break inside raw strings


def s(x):
    return None if x is None else x.replace(NL, "\n")


def F(page, where, scan, tex, kind, conf, old=None, new=None, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": s(tex), "kind": kind,
         "confidence": conf,
         "fix": None if old is None else {"old": s(old), "new": s(new)}}
    if corrected is not None:
        d["corrected"] = s(corrected)
    d["note"] = note
    return d


f = []
# ---------------- page 506 ----------------
f.append(F(506, "proof of Prop. 1.8, 'du complexe Rg_*(F) = g_*(F)'",
           "double-struck R: \u211dg*(F) = g*(F)", r"$Rg_*(F)=g_*(F)$", "font", "high",
           r"$Rg_*(F)", r"$\mathbb Rg_*(F)",
           "Derived functor R double-struck in the print, plain in the TeX (reported singly)."))
f.append(F(506, "last line, 'la classe de Lg^*(F)'",
           "double-struck L: \U0001D543g*(F)", r"\(Lg^*(F)", "font", "high",
           r"\(Lg^*(F)", r"\(\mathbb Lg^*(F)",
           "Derived functor L double-struck in the print, plain in the TeX."))
f.append(F(506, "last line, 'F \u2297^L_{O_X} O_S'",
           "\u2297 with a double-struck \U0001D543 above it and O_X below", r"F\otimes^L_{\mathcal O_X}", "font", "high",
           r"F\otimes^L_{\mathcal O_X}", r"F\otimes^{\mathbb L}_{\mathcal O_X}",
           "The derived tensor's L is double-struck in this exposé (not the plain L handled for Exposés III and IV)."))
f.append(F(506, "last paragraph, 'Pour calculer g^*(g_*(f))'",
           "g*(g*(f)) with a small f (both scans)", r"$g^*(g_*(f))$", "misprint_in_print", "high",
           note="Typing error: the class is F ('de classe F dans K.(S)'; the display on p. 507 computes g^*(g_*(F))). The TeX keeps the printed small f.",
           corrected=r"$g^*(g_*(F))$"))
f.append(F(506, "after 'Cet énoncé est l'analogue, pour le K., de VII 2.7.'",
           "'Soit F un O_S-Module cohérent ...' begins a new indented paragraph",
           r"de VII 2.7. Soit $F$ un ... (one paragraph)", "other", "medium",
           r"de VII 2.7. Soit $F$", r"de VII 2.7.⏎⏎Soit $F$",
           "Missing paragraph break."))
f.append(F(506, "end of the page, before the folio 507 marker",
           "p. 507 opens with an indented new paragraph 'Pour cela, on considère le complexe :'",
           r"page ends '\mathcal O_S\).' with no blank line before the marker, so 'Pour cela' runs on in the same paragraph",
           "other", "medium",
           r"\mathcal O_S\).", r"\mathcal O_S\).⏎",
           "Adds the blank line before the folio 507 marker line (the marker itself is unchanged); pp. 507-509 end the same way."))
f.append(F(506, "throughout pp. 506-510 (26 places); first: 'l'homomorphisme K^\\circ(X) -> K_\\bullet(X)'",
           "K with a raised dot (K\u02d9)", r"K^\circ", "symbol", "high",
           note=("CONVENTION of this exposé, one global pass, not itemized: the print's raised-dot K is written K^\\circ on every page here. "
                 "Examples: p. 506 '$K^\\circ(X)\\to K_\\bullet(X)$', p. 509 '$K^\\circ(P)\\simeq K^\\circ(S)/...$', "
                 "p. 510 '$K_\\bullet(S)\\otimes_{K^\\circ(S)}K^\\circ(X)$'. Same fix as for Exposés IV and VI on 10 Nov: K^\\circ -> K^{\\bullet}.")))
f.append(F(506, "throughout pp. 506-510; first: Prop. 1.8 'E un O_S-Module'",
           "letters that name Modules underlined (E, F, L, L., L_i, F_i, A, A', A'', A_m, A_1); the same letters plain where they name classes in K",
           r"all plain ($E$, $F$, $L$, $L_\bullet$, $A$, $A_m$, ...)", "underline", "high",
           note=("CONVENTION, not itemized, but not a blind script: the print separates the Module (underlined) from its class (plain); the TeX loses this. "
                 "Examples: p. 506 'en notant $E$ la classe de $E$' (second E underlined), p. 508 'où $L$ est la classe dans $K^\\circ(S)$ de $L$' "
                 "(second L underlined), p. 510 'On note donc $L_i$ ... $F_i$ le noyau de $L_i\\to L_{i-1}$' (all underlined). "
                 "Plain in the print: lambda_{-1}(E), lambda_{-1}(L), 'de classe F', 'Alors g_*(F)', g^*(g_*(F)), F.lambda_{-1}(E), 1-L, "
                 "and the E of 'sur S(E)', 'Lambda^k(f^*(E))' (p. 507) and 'complet D(E)' (p. 510).")))
f.append(F(506, "Lemme 1.7 and Prop. 1.8 (also Prop. 2.2 p. 508, Cor. 2.3 p. 509, Prop. 3.1 p. 510)",
           "statement text underlined word group by word group (symbols, numbers, punctuation not underlined)",
           "statements set in roman", "underline", "high",
           note="Same pattern as Exposé II (GLOBAL_ISSUES 82, pending volume decision); not itemized."))

# ---------------- page 507 ----------------
SNOTE = ("The symmetric algebra is printed with a struck S (an S with a vertical bar, the typescript's double-struck S, like its Z, R, L, D), "
         "all six times on this page in both scans; the plain S is the base scheme. \\mathbb S matches the print; "
         "\\Sym (bold S) is the Exposé VI form for a doubly underlined S. Apply the five S(E) edits of this page together.")
f.append(F(507, "first display, first term",
           "\u2227^r(E)\u2297_{O_S} \U0001D54A(E) (struck S)", r"\Lambda^r(E)\otimes_{\mathcal O_S}S(E)", "font", "medium",
           r"\Lambda^r(E)\otimes_{\mathcal O_S}S(E)", r"\Lambda^r(E)\otimes_{\mathcal O_S}\mathbb S(E)", SNOTE))
f.append(F(507, "first display, second term",
           "\u2227^{r-1}(E)\u2297_{O_S} \U0001D54A(E) (struck S)", r"\Lambda^{r-1}(E)\otimes_{\mathcal O_S}S(E)", "font", "medium",
           r"\Lambda^{r-1}(E)\otimes_{\mathcal O_S}S(E)", r"\Lambda^{r-1}(E)\otimes_{\mathcal O_S}\mathbb S(E)",
           "Struck S, see the first display item."))
f.append(F(507, "first display, '-> ... ->'",
           "typed baseline dots '...'", r"\cdots", "symbol", "low",
           r"\cdots", r"\ldots",
           "As GLOBAL_ISSUES 87 (Exposé V, volume decision). The only \\cdots on pp. 506-510; p. 510 writes the same typed dots as \\ldots."))
f.append(F(507, "first display, last two terms",
           "E\u2297_{O_S} \U0001D54A(E) -> \U0001D54A(E) (struck S twice)", r"E\otimes_{\mathcal O_S}S(E)\longrightarrow S(E)", "font", "medium",
           r"E\otimes_{\mathcal O_S}S(E)\longrightarrow S(E)", r"E\otimes_{\mathcal O_S}\mathbb S(E)\longrightarrow \mathbb S(E)",
           "Struck S, see the first display item."))
f.append(F(507, "end of the first display",
           "'-> S(E) -> 0' with no punctuation (both scans)", r"\longrightarrow 0,", "punctuation", "high",
           r"\longrightarrow 0,⏎\]", r"\longrightarrow 0⏎\]",
           "Comma added at the end of the display."))
f.append(F(507, "after the display, 'où S(E) est l'algèbre symétrique de E'",
           "où \U0001D54A(E) (struck S)", r"où $S(E)$", "font", "medium",
           r"où $S(E)$", r"où $\mathbb S(E)$", "Struck S, see the first display item."))
f.append(F(507, "'C'est une résolution de O_S sur S(E) (VI 1.11)'",
           "sur \U0001D54A(E) (struck S)", r"sur $S(E)$", "font", "medium",
           r"sur $S(E)$", r"sur $\mathbb S(E)$", "Struck S, see the first display item."))
f.append(F(507, "'on a donc L. \u2297 F = O_S \u2297^L F'",
           "O_S \u2297 F with a double-struck \U0001D543 above \u2297 and O_X below",
           r"\mathcal O_S\otimes^L_{\mathcal O_X}F", "font", "high",
           r"\otimes^L_{\mathcal O_X}F", r"\otimes^{\mathbb L}_{\mathcal O_X}F",
           "Derived tensor's L double-struck in the print."))
f.append(F(507, "2.1, 'soit encore T ≃ G^r_{m S}'",
           "underlined typed G (superscript r, subscript 'm S')", r"\mathbb G_{m,S}^r", "font", "medium",
           r"\simeq \mathbb G", r"\simeq \underline{G}",
           "The print's G_m is an underlined typed G here and on p. 509 and a plain G on p. 508; the TeX writes \\mathbb G in all three (cf. the underlined O written \\cO)."))
f.append(F(507, "2.1, subscript of G^r_{m S}",
           "'m S': space, no comma (both scans)", r"_{m,S}", "punctuation", "medium",
           r"{m,S}^r", r"{m\,S}^r",
           "Comma added in the subscript; same on pp. 508 and 509."))
f.append(F(507, "exterior powers, pp. 507 and 510 (5 places)",
           "small wedge \u2227 with its index set above it",
           r"\Lambda^r(E), \Lambda^{r-1}(E), \Lambda^k(f^*(E)), \Lambda^i(E), \Lambda^i(F_j)", "symbol", "medium",
           note=("CONVENTION, not itemized: as GLOBAL_ISSUES 88 (Exposé V), the print's exterior power is a small wedge and the TeX writes \\Lambda. "
                 "Examples: p. 507 '\\Lambda^r(E)\\otimes_{\\mathcal O_S}', p. 507 '$\\Lambda^k(f^*(E))$', p. 510 '$\\Lambda^i(F_j)$'. "
                 "One pass with the Exposé V decision (\\Lambda -> \\wedge).")))

# ---------------- page 508 ----------------
f.append(F(508, "'On suppose d'abord r = 1, i.e. T = G_{m S}'",
           "plain typed G (not underlined, not double-struck; both scans)", r"$T=\mathbb G_{m,S}$", "font", "medium",
           r"$T=\mathbb G", r"$T=G",
           "Plain G here; underlined G on pp. 507 and 509."))
f.append(F(508, "subscript of G_{m S}",
           "'m S': space, no comma", r"_{m,S}", "punctuation", "medium",
           r"_{m,S}$", r"_{m\,S}$", "Comma added in the subscript."))
f.append(F(508, "end of the display after 'on a d'après 1.1 la suite exacte :'",
           "'K.(P) -> 0' with no punctuation (both scans)", r"\longrightarrow 0,", "punctuation", "high",
           r"0,⏎\]⏎où $g", r"0⏎\]⏎où $g",
           "Comma added. The later display after 'On a donc la suite exacte :' has its printed comma."))
f.append(F(508, "end of the display after 'd'où l'on tire d'après 1.8 :'",
           "'... = K.(S)/(1-L)K.(S)' with no punctuation (both scans)", r"(1-L)K_\bullet(S),", "punctuation", "high",
           r"(1-L)K_\bullet(S),⏎\]", r"(1-L)K_\bullet(S)⏎\]", "Comma added."))

# ---------------- page 509 ----------------
f.append(F(509, "'de groupe G_{m P_1}'",
           "underlined typed G (subscript 'm P_1'; both scans)", r"$\mathbb G_{m,P_1}$", "font", "medium",
           r"groupe $\mathbb G", r"groupe $\underline{G}",
           "As p. 507."))
f.append(F(509, "subscript of G_{m P_1}",
           "'m P_1': space, no comma", r"_{m,P_1}", "punctuation", "medium",
           r"_{m,P_1}", r"_{m\,P_1}", "Comma added in the subscript."))
f.append(F(509, "end of the display of Cor. 2.3",
           "'K\u02d9(P) ≃ K\u02d9(S)/((η(m) - 1)_{m∈M})' with no punctuation", r"\bigr),", "punctuation", "high",
           r"\bigr),⏎\]", r"\bigr)⏎\]", "Comma added."))

# ---------------- page 510 ----------------
DNOTE = ("The flag scheme is a double-struck D in all five places on this page (both scans); the TeX has a plain D. "
         "The plain D of D_S(M) on pp. 507 and 509 is right. Apply the four D edits of this page together.")
f.append(F(510, "Prop. 3.1, 'et X = D_π(E)'",
           "double-struck \U0001D53B_π(E)", r"$X=D_\pi(E)$", "font", "high",
           r"$X=D_\pi(E)$", r"$X=\mathbb D_\pi(E)$", DNOTE))
f.append(F(510, "'fibré en drapeaux complet D(E)'",
           "double-struck \U0001D53B(E)", r"complet $D(E)$", "font", "high",
           r"complet $D(E)$", r"complet $\mathbb D(E)$", "Double-struck D, see the Prop. 3.1 item."))
f.append(F(510, "display after 'supposons que'",
           "K.(S) \u2297_{K\u02d9(S)} K\u02d9(\U0001D53B(E)) -> K.(\U0001D53B(E))",
           r"K^\circ(D(E))\longrightarrow K_\bullet(D(E))", "font", "high",
           r"K^\circ(D(E))\longrightarrow K_\bullet(D(E))", r"K^\circ(\mathbb D(E))\longrightarrow K_\bullet(\mathbb D(E))",
           "Double-struck D twice, see the Prop. 3.1 item."))
f.append(F(510, "last line, 'Comme K.(S) -> K.(D(E)) se factorise'",
           "K.(\U0001D53B(E))", r"$K_\bullet(S)\to K_\bullet(D(E))$", "font", "high",
           r"\to K_\bullet(D(E))$", r"\to K_\bullet(\mathbb D(E))$",
           "Double-struck D, see the Prop. 3.1 item."))
f.append(F(510, "display after 'D'après 1.3, cela entraîne que l'homomorphisme :'",
           "K.(S) \u2297_{K\u02d9(S)} K\u02d9(S) -> K.(X) (both scans)",
           r"K_\bullet(S)\otimes_{K^\circ(S)}K^\circ(S)\longrightarrow K_\bullet(X)", "misprint_in_print", "high",
           note=("Typing error: the map is that of Prop. 3.1, K.(S) \u2297_{K\u02d9(S)} K\u02d9(X) -> K.(X) (statement display; p. 511 factorises it); "
                 "the second factor K\u02d9(S) should be K\u02d9(X). The TeX keeps the printed K^\\circ(S)."),
           corrected=r"K_\bullet(S)\otimes_{K^\circ(S)}K^\circ(X)\longrightarrow K_\bullet(X)"))

# ---------------- checks ----------------
ok = True
texts = {p: open(f"{base}/b506_510/page_{p}.tex", encoding="utf-8").read() for p in range(506, 511)}
spans = {}
for i, d in enumerate(f):
    if d["fix"] is None:
        continue
    t = texts[d["page"]]
    old = d["fix"]["old"]
    n = t.count(old)
    if n != 1:
        ok = False
        print("NOT UNIQUE", d["page"], n, repr(old))
        continue
    if "%%%%%%%%%%" in old:
        ok = False
        print("MARKER IN OLD", d["page"], repr(old))
    a = t.index(old)
    spans.setdefault(d["page"], []).append((a, a + len(old), i))
for p, lst in spans.items():
    lst.sort()
    for (a1, b1, i1), (a2, b2, i2) in zip(lst, lst[1:]):
        if a2 < b1:
            ok = False
            print("OVERLAP", p, repr(f[i1]["fix"]["old"]), repr(f[i2]["fix"]["old"]))
# apply all fixes of a page in sequence: each old must still occur exactly once
for p in range(506, 511):
    t = texts[p]
    for d in f:
        if d["page"] == p and d["fix"]:
            if t.count(d["fix"]["old"]) != 1:
                ok = False
                print("SEQUENTIAL FAIL", p, repr(d["fix"]["old"]))
            t = t.replace(d["fix"]["old"], d["fix"]["new"], 1)
print("all checks ok" if ok else "PROBLEMS")
out = f"{base}/findings_506_510.json"
with open(out, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(f, fh, ensure_ascii=False, indent=1)
c = Counter((d["page"], d["kind"] == "misprint_in_print") for d in f)
for p in range(506, 511):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
print(len(f), "findings written to", out)
