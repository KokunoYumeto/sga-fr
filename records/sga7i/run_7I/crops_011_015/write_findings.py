import json
import pathlib

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I")
PAGES = RUN / "b011_015"
OUT = RUN / "findings_011_015.json"

F = [
    # ---------------- page 11 ----------------
    {
        "page": 11,
        "where": "line after (3.1.2): 'Ces formules sont identiques à celles qui, sur C , donnent la cohomologie de D^{*B} x D^k'",
        "scan": "double-struck C",
        "tex": r"$\mathbf{C}$",
        "kind": "font",
        "confidence": "high",
        "fix": {"old": r"\mathbf{C}", "new": r"\mathbb{C}"},
        "note": r"Same kind as the known global double-struck issue of Exposé I, but C is not among the Z, Q, F named for that pass; this is the only \mathbf{C} in expose_I_body.tex.",
    },
    {
        "page": 11,
        "where": "(3.1.2) H^o(U,Lambda); Théorème 3.3 (i) and (ii): psi^o_{t x-bar}, # H_o(K)",
        "scan": "index zero typed as a small raised or lowered letter o: H^o, psi^o, H_o(K) (the digit 0 only on the line, as in 'q ≠ 0' on p. 12)",
        "tex": r"H^{0}(U,\Lambda) ; \psi^{0}_{t\bar{x}} ; H_{0}(K)",
        "kind": "number",
        "confidence": "low",
        "fix": None,
        "note": r"Convention, reported once: the TeX writes 0 for an index-zero o in cohomological degrees (p. 11 H^{0}(U,\Lambda), \psi^{0}_{t\bar{x}}, H_{0}(K); p. 12 H^{0}(\widetilde{U},\Lambda); p. 13 \psi_t^0; also p. 9 \psi^{0}) but keeps the letter o for named objects (C_o on p. 13; S_o, V_o, H_o, k_o on pp. 4-7). The print uses the same small o in both. One rendering should be chosen for the edition; no per-occurrence fix given.",
    },
    {
        "page": 11,
        "where": "a) of the proof of 3.3: 'X_n = X_(x)[(t_j^{1/n})] (pour (n,p) = 1 ; c'est un schéma régulier)'",
        "scan": "X_{(x)} without the bar",
        "tex": r"$X_{n} = X_{(\bar{x})}\left[(t_{j}^{1/n})\right]$",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": {"old": r"X_{n} = X_{(\bar{x})}\left[", "new": r"X_{n} = X_{(x)}\left["},
        "corrected": r"X_{(\bar{x})}",
        "note": "X_n is built over the strict localization X_{(x-bar)} named twice earlier in the same sentence; the print drops the bar here. The spot is clean and the DjVu witness also has no bar, so it is not a scan loss. The TeX silently corrects it; the fix restores the printed reading.",
    },
    {
        "page": 11,
        "where": "a) of the proof of 3.3: 'pour m = x d , l'application \"image réciproque\" de H^q(U_n,Lambda) dans H^q(U_m,Lambda) est la multiplication par d^q'",
        "scan": "m = x d",
        "tex": r"$m = x d$",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": r"m = n d",
        "note": "The pull-back from U_n to U_m is multiplication by d^q (continued on p. 12) for m = nd; the print types x for n. Same in the DjVu witness. The TeX keeps the printed reading.",
    },
    # ---------------- page 12 ----------------
    {
        "page": 12,
        "where": "Corollaire 3.4: 'Soit q >= 0 , et q' la borne inférieure de q et du nombre maximum de diviseurs D_j passant par un même point'",
        "scan": "la borne inférieure de q et du nombre maximum",
        "tex": r"\underline{la borne inférieure de} $q$ \underline{et du nombre maximum de diviseurs}",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": r"q+1",
        "note": "Wrong index (perhaps a slip of the original rather than of the typist). By 3.3 the psi^j_t vanish for j >= c (c = maximum number of D_j through a point) and T^N acts trivially on each, so the spectral sequence gives (T^N - I)^{inf(q+1,c)} = 0 on H^q. With inf(q,c) the statement fails for q = 0 (exponent 0) and for H^1 of a curve with semistable reduction (q = 1, c = 2, N = 1); Théorème 3.5 derives (T^N - I)^2 = 0 on H^1 from 3.4, which needs inf(q+1,c). Same in the DjVu witness. The TeX keeps the printed reading.",
    },
    # ---------------- page 13 ----------------
    {
        "page": 13,
        "where": "Remarque 3.6: 'on trouve encore que l'action de I sur H^1(A_eta,Q_l) ou T_l(A) est quasi-unipotente d'échelon 2'",
        "scan": "A_eta without the bar",
        "tex": r"$H^1(A_\eta,\mathbb{Q}_\ell)$",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": r"H^1(A_{\bar\eta},\mathbb{Q}_\ell)",
        "note": "I acts on the cohomology of the geometric generic fibre, as in Théorème 3.5 (H^1(C_eta-bar,Q_l)) and Remarque 3.7 (X_eta-bar). The spot is clean and the DjVu witness also has no bar. The TeX keeps the printed reading.",
    },
    {
        "page": 13,
        "where": "Remarque 3.7: 'L'action de I sur H^1(X_eta-bar,Q) est en fait quasi-unipotente d'échelon 2'",
        "scan": "double-struck Q without the index l",
        "tex": r"$H^1(X_{\bar\eta},\mathbb{Q})$",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": r"H^1(X_{\bar\eta},\mathbb{Q}_\ell)",
        "note": "l-adic coefficients, as in 3.5 and 3.6 just before; the index l is missing in the print (no trace of it in the PDF scan or the DjVu witness). The TeX keeps the printed reading.",
    },
    {
        "page": 13,
        "where": "4.1 a): 'Sur X_s - X'_s , phi^{-1} = Lambda et les autres phi^i sont nuls'",
        "scan": "straight phi (circle with a vertical stroke), twice",
        "tex": r"$\varphi^{-1} = \Lambda$  et les autres  $\varphi^i$",
        "kind": "symbol",
        "confidence": "medium",
        "fix": {"old": r"$\varphi^{-1} = \Lambda$  et les autres  $\varphi^i$", "new": r"$\phi^{-1} = \Lambda$  et les autres  $\phi^i$"},
        "note": r"The typescript's phi is the straight form, which expose_I_body.tex writes \phi everywhere else (pp. 9, 15, 16) for the same sheaves phi^i; only pp. 13-14 use \varphi (five times: two here, three on p. 14).",
    },
    # ---------------- page 14 ----------------
    {
        "page": 14,
        "where": "b) at the top: 'sur X'_s , les phi^i et psi^i relatifs à X/S ou à X'/S coïncident'",
        "scan": "straight phi",
        "tex": r"les  $\varphi^i$  et",
        "kind": "symbol",
        "confidence": "medium",
        "fix": {"old": r"les  $\varphi^i$  et", "new": r"les  $\phi^i$  et"},
        "note": r"Straight phi of the print, \phi elsewhere in the file; see p. 13.",
    },
    {
        "page": 14,
        "where": "b) at the top: 'coïncident, et phi^{-1} = 0'",
        "scan": "straight phi",
        "tex": r"$\varphi^{-1} = 0$",
        "kind": "symbol",
        "confidence": "medium",
        "fix": {"old": r"$\varphi^{-1} = 0$", "new": r"$\phi^{-1} = 0$"},
        "note": r"Straight phi of the print, \phi elsewhere in the file; see p. 13.",
    },
    {
        "page": 14,
        "where": "4.4: 'que les phi^i pour i petit sont nuls'",
        "scan": "straight phi",
        "tex": r"les  $\varphi^i$  pour",
        "kind": "symbol",
        "confidence": "medium",
        "fix": {"old": r"les  $\varphi^i$  pour", "new": r"les  $\phi^i$  pour"},
        "note": r"Straight phi of the print, \phi elsewhere in the file; see p. 13.",
    },
    {
        "page": 14,
        "where": "Théorème 4.2 (ii): 'Plus précisément, pour x un point de X_s'",
        "scan": "underline ends before the comma",
        "tex": r"\underline{Plus précisément,}",
        "kind": "underline",
        "confidence": "low",
        "fix": {"old": r"\underline{Plus précisément,}", "new": r"\underline{Plus précisément},"},
        "note": "Underline extent only.",
    },
    {
        "page": 14,
        "where": "proof of 4.2 (ii), b) and c): 'H^i(X_{(x)eta-bar'},Lambda) = 0' and 'H^i(X_{(x)eta-bar},Lambda) = H^i(X_{(x)eta-bar'},Lambda)^Q'",
        "scan": "(x) without the bar, three times",
        "tex": r"$H^i(X_{(x)\overline{\eta'}},\Lambda) = 0$ ; $H^i(X_{(x)\bar\eta},\Lambda) = H^i(X_{(x)\overline{\eta'}},\Lambda)^Q$",
        "kind": "misprint_in_print",
        "confidence": "low",
        "fix": None,
        "corrected": r"X_{(\bar{x})\overline{\eta'}} (in b and c) and X_{(\bar{x})\bar\eta} (in c)",
        "note": "Earlier in the same proof psi^i_x-bar = H^i(X_{(x-bar)eta-bar},Lambda) carries the bar, and c) must give that group to prove the theorem; the three omissions in two lines may be the author's shorthand, hence low. Same in the DjVu witness. The TeX keeps the printed reading.",
    },
    {
        "page": 14,
        "where": "4.4: 'on s'appuyera sur la théorie de la dualité locale'",
        "scan": "s'appuyera",
        "tex": r"on s'appuyera sur",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": r"s'appuiera",
        "note": "Spelling slip (verbs in -uyer take i before mute e). Same in the DjVu witness. The TeX keeps the printed reading.",
    },
    # ---------------- page 15 ----------------
    {
        "page": 15,
        "where": "proof of 4.5: 'Pour S le normalisé de S dans eta-bar , soient X-bar_x = X_x x_S S-bar , V-bar = V x_S S-bar'",
        "scan": "first S without the bar",
        "tex": r"Pour  $S$  le normalisé de  $S$  dans",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": r"\bar{S}",
        "note": "The normalization being defined is S-bar, used at once in X-bar_x and V-bar ('S le normalisé de S' is circular). The spot is clean and the DjVu witness also has no bar. The TeX keeps the printed reading.",
    },
    {
        "page": 15,
        "where": "after (1) of the proof of 4.5: 'sous les hypothèses de 4.5, (a) est d'application pour m = infini (SGA 4 XV 2.1)'",
        "scan": "(a)",
        "tex": r"(a) est d'application pour  $m =$ $\infty$",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": r"(1)",
        "note": "Wrong reference: it is statement (1), which has the parameter m, that applies for m = infinity (hypothesis (a) of 4.5 gives the vanishing of the phi^i at the generizations of x). Same in the DjVu witness. The TeX keeps the printed reading.",
    },
    {
        "page": 15,
        "where": "Corollaire 4.6: 'un point de non lissité isolé dans sa fibre, on a phi^i_x = 0'",
        "scan": "underline ends before the comma",
        "tex": r"\underline{un point de non lissité isolé dans sa fibre,}",
        "kind": "underline",
        "confidence": "low",
        "fix": {"old": r"sa fibre,}", "new": r"sa fibre},"},
        "note": "Underline extent only.",
    },
    {
        "page": 15,
        "where": "Corollaire 4.7: 'phi^n_x est un Lambda-module plat.'",
        "scan": "only 'module plat' underlined; 'Lambda-' and the full stop are not",
        "tex": r"\underline{$\Lambda$-module plat.}",
        "kind": "underline",
        "confidence": "medium",
        "fix": {"old": r"\underline{$\Lambda$-module plat.}", "new": r"$\Lambda$-\underline{module plat}."},
        "note": r"As in '$\Lambda$-\underline{algèbres graduées}' on p. 11, the typist does not underline the symbol.",
    },
    {
        "page": 15,
        "where": "last line: 'fournit en effet, pour les phi^i_Lambda , relatifs à Lambda' ,'",
        "scan": "phi^i with subscript Lambda (no prime)",
        "tex": r"pour les  $\phi^i_{\Lambda}$ , relatifs à  $\Lambda'$",
        "kind": "misprint_in_print",
        "confidence": "low",
        "fix": None,
        "corrected": r"\phi^i_{\Lambda'}",
        "note": "The sheaves relative to Lambda' are the phi_{Lambda'} of the formula that follows on p. 16 (phi^{n-i}_{Lambda'} = Tor^Lambda_i(Lambda', phi^n_Lambda)); the prime is missing in the print and in the DjVu witness. Low because the subscript could be read as generic notation. The TeX keeps the printed reading.",
    },
]

# check every fix's old occurs exactly once on its page
ok = True
for f in F:
    if f["fix"] is None:
        continue
    t = (PAGES / ("page_%03d.tex" % f["page"])).read_text(encoding="utf-8")
    n = t.count(f["fix"]["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE", f["page"], n, repr(f["fix"]["old"]))
    if "%%%%%%%%%%" in f["fix"]["old"]:
        ok = False
        print("MARKER IN OLD", f["page"])
# check the tex quotes exist on the page (informational)
for f in F:
    t = (PAGES / ("page_%03d.tex" % f["page"])).read_text(encoding="utf-8")
    for part in f["tex"].split(" ; "):
        if part not in t:
            print("tex quote not verbatim:", f["page"], repr(part))
print("all fixes unique" if ok else "FIX PROBLEMS")
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=2), encoding="utf-8")
from collections import Counter
c = Counter((f["page"], f["kind"] == "misprint_in_print") for f in F)
for p in range(11, 16):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
print(OUT)
