import json, sys

out = sys.argv[1]
F = []
NL = "\n"
Q = "'"


def add(**kw):
    F.append(kw)


# ---------------- page 306
add(page=306,
    where=r"first line after (5.8.4.7): 'la flèche en bas est injective,ce qui résulte du fait'",
    scan=r"injective,ce (no space after the comma)",
    tex=r"injective,ce qui",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"injective, ce qui",
    note=r"Typing slip of the print (missing space after the comma). The TeX keeps the printed reading; the corrected layer already has the space (SGA7II-FR-XVIII-072).")

# ---------------- page 307
add(page=307,
    where=r"(5.8.6.1 bis), top arrow from ~X_S to ~X, label alpha_S",
    scan=r"alpha_S stands ABOVE the leftward arrow",
    tex=r'\arrow[l, "\alpha_S"] (no swap mark: tikz-cd sets the label of a leftward arrow below it)',
    kind="other", confidence="medium",
    fix={"old": r'\arrow[l, "\alpha_S"]', "new": r'\arrow[l, "\alpha_S"' + Q + ']'},
    note=r"Placement only. Compiled: without the swap mark ' the label of a leftward arrow sits below it, with it above, as printed and as the file's own STRUCTURE comment says ('label \alpha_S ABOVE the shaft').")
add(page=307,
    where=r"(5.8.6.1 bis), bottom arrow from S to P^1, label pi",
    scan=r"pi stands ABOVE the leftward arrow",
    tex=r'\arrow[l, "\pi"] (label set below the arrow)',
    kind="other", confidence="medium",
    fix={"old": r'\arrow[l, "\pi"]', "new": r'\arrow[l, "\pi"' + Q + ']'},
    note=r"Placement only, as for alpha_S; the STRUCTURE comment says 'label \pi ABOVE the shaft'.")
add(page=307,
    where=r"(5.8.6.2), top arrow from ~X_V to ~X, label alpha_V",
    scan=r"alpha_V stands ABOVE the leftward arrow",
    tex=r'\arrow[l, "\alpha_V"] (label set below the arrow)',
    kind="other", confidence="medium",
    fix={"old": r'\arrow[l, "\alpha_V"]', "new": r'\arrow[l, "\alpha_V"' + Q + ']'},
    note=r"Placement only, as in (5.8.6.1 bis); the STRUCTURE comment says 'label \alpha_V ABOVE the shaft'.")
add(page=307,
    where=r"(5.8.6.2), diagonal arrow from ~X down-left to X, label f",
    scan=r"f stands ABOVE the diagonal shaft (upper-left side); in (5.8.6.1 bis) the f stands below its shaft",
    tex=r'\arrow[dl, "f"] in (5.8.6.2) (label set below-right of the shaft)',
    kind="other", confidence="medium",
    fix={"old": r'\arrow[dl, "f"] \arrow[dd, "\rho"] & \widetilde{X}_V',
         "new": r'\arrow[dl, "f"' + Q + r'] \arrow[dd, "\rho"] & \widetilde{X}_V'},
    note=r"Placement only. Compiled: without the swap mark the label of a down-left arrow sits below-right of the shaft (right for (5.8.6.1 bis), where the print has f below), with it above-left, as printed in (5.8.6.2).")
add(page=307,
    where=r"(5.8.6.2), bottom arrow from V to P^1, label pi mu",
    scan=r"pi mu stands ABOVE the leftward arrow",
    tex=r'\arrow[l, "{\pi\,\mu}"] (label set below the arrow)',
    kind="other", confidence="medium",
    fix={"old": r'\arrow[l, "{\pi\,\mu}"]', "new": r'\arrow[l, "{\pi\,\mu}"' + Q + ']'},
    note=r"Placement only; the STRUCTURE comment says 'label \pi\,\mu ABOVE the shaft'.")

# ---------------- page 308
add(page=308,
    where=r"last display (specialization), left-hand side",
    scan=r"R^{n-1}ρ_{V_*}Q_ℓ(j))   =   (π μ)* R^{n-1}ρ_*Q_ℓ(j): two closing parentheses after j, one opening",
    tex=r"\mathrm{R}^{n-1}\rho_{\mathrm{V}_*}\mathbb{Q}_\ell(j)) = (\pi\ \mu)^*",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"\mathrm{R}^{n-1}\rho_{\mathrm{V}_*}\mathbb{Q}_\ell(j) = (\pi\ \mu)^*",
    note=r"Unbalanced parenthesis in the print (checked at 2x). The TeX keeps the printed reading (its SOURCE DEFECTS comment 2). The corrected layer removes it (SGA7II-FR-XVIII-074), but that record calls it a transcription repair: it is a misprint of the print (record wording, as global items 52/55).")

# ---------------- page 309
add(page=309,
    where=r"cartesian square at the foot of the page, left vertical arrow V -> U, label pi",
    scan=r"pi stands to the RIGHT of the left vertical arrow (inside the square)",
    tex=r'\arrow[d, "\pi"' + Q + r'] (swap mark: label on the left of the arrow)',
    kind="other", confidence="medium",
    fix={"old": r'\arrow[d, "\pi"' + Q + ']', "new": r'\arrow[d, "\pi"]'},
    note=r"Placement only. Compiled: with the swap mark ' tikz-cd sets the label of a downward arrow on its left; without it on the right, as printed (both pi labels of the square stand to the right of their arrows).")
add(page=309,
    where=r"display after 'Il suffit donc de démontrer l'injectivité de' (Prim^n(X,Q_ℓ(j)) -> H^1(V,μ*π*E^{n-1}ρ_*Q_ℓ(j)))",
    scan=r"no equation number at this display; p. 310 says 'de sorte que (5.8.7.3) se factorise'",
    tex=r"\begin{equation*}" + NL + r"\begin{tikzcd}[column sep=huge]" + NL,
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"\begin{equation*}\tag{5.8.7.3}" + NL + r"\begin{tikzcd}[column sep=huge]" + NL,
    note=r"No display of the exposé is numbered (5.8.7.2) or (5.8.7.3); the map that p. 310 factorises through H^1(U,ν*E^{n-1}ρ_*Q_ℓ(j)) is this one (μ*π* = π_U*ν*). The TeX keeps the printed reading (no number); the corrected layer already adds the tag (SGA7II-FR-XVIII-075).")

# ---------------- page 310
add(page=310,
    where=r"first display, right-hand side: μ*π* E^{n-1}ρ_*Q_ℓ(j) = π_U*ν* E^{n-1}ρ_*Q_ℓ",
    scan=r"the right-hand side ends with ρ_*Q_ℓ, without (j)",
    tex=r"\;=\; \pi_U^*\nu^*\, E^{n-1}\rho_*\mathbb{Q}_\ell" + NL,
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"\;=\; \pi_U^*\nu^*\, E^{n-1}\rho_*\mathbb{Q}_\ell(j)" + NL,
    note=r"Tate twist omitted on the right (the left-hand side and every later occurrence have Q_ℓ(j)). The TeX keeps the printed reading; the corrected layer has the twist (SGA7II-FR-XVIII-077).")
add(page=310,
    where=r"trace map after 'une application'",
    scan=r"tr_{π_U}: H^1( V,π_U^* ) ⟶ H^1(U,F(j)): no sheaf after π_U^* (checked at 2.5x), and the target carries a twist (j)",
    tex=r"H^1(\ V,\pi_U^*\ ) \longrightarrow H^1(U,F(j))",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"H^1(\ V,\pi_U^*F\ ) \longrightarrow H^1(U,F)",
    note=r"The argument F of π_U^* is missing in the print; the (j) of the target does not fit 'l'injectivité de H*(U,F) -> H*(V,π_U^*F)' two lines below (a trace H^1(V,π_U^*F) -> H^1(U,F)). The TeX keeps the printed reading. The corrected layer has this reading (SGA7II-FR-XVIII-078, which also writes tr_{π_U} ∘ π_U^* for the print's tr_π ∘ π*), but that record calls it a transcription repair: the missing F and the (j) are in the print (record wording, as global items 52/55).")

with open(out, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
    fh.write("\n")
print(len(F), "findings written to", out)
