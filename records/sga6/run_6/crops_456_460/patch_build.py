"""One-off patch of build_findings.py: take the folio-461 strings from the snapshot page files (main.tex
already has that marker move since 16:05:07) and date the main.tex line numbers. Splices from the bottom up."""
import pathlib
P = pathlib.Path(__file__).resolve().parent / "build_findings.py"
lines = P.read_text(encoding="utf-8").split("\n")

def check(n, start):
    assert lines[n - 1].startswith(start), (n, lines[n - 1][:80])

C_BLOCK = r'''# C: taken from the snapshot (page_461.tex of batch 461-465 begins with 'donc :' and the display)
p461 = (RUN / "b461_465" / "page_461.tex").read_text(encoding="utf-8")
k0 = p461.index(M461 + NL) + len(M461 + NL)
k1 = p461.index(NL + "\\]" + NL, k0) + len(NL + "\\]" + NL)
C_disp = p461[k0:k1]
assert C_disp.startswith("donc :" + NL)
C_old = "et définissent" + NL + M461 + NL + C_disp
C_new = "et définissent" + NL + C_disp + M461 + NL'''.split("\n")

T2_BLOCK = r'''    c_new = txt.count(C_new); i_new = txt.find(C_new)
    info["C_applied"] = (c_new, line_of(txt, i_new) if i_new >= 0 else None, line_of(txt, i_new + len(C_new) - 1) if i_new >= 0 else None)
    t2 = txt.replace(A_old, A_new).replace(B_old, B_new).replace(C_old, C_new).replace(H_old, H_new)'''.split("\n")

DC_BLOCK = r'''dC, cC = sim["diplomatic"]["C_applied"], sim["current"]["C_applied"]
C_APPLIED = sim["diplomatic"]["C"][0] == 0 and sim["current"]["C"][0] == 0 and dC[0] == 1 and cC[0] == 1
print("folio-461 move already in main.tex:", C_APPLIED)'''.split("\n")

CNOTE_BLOCK = r'''    ("ALREADY APPLIED IN MAIN.TEX, NO ACTION. " if C_APPLIED else "") +
    "Page 461 really begins at 'Enfin, on remarque': the folio-461 marker line belongs directly after the '\\]' that closes the i_gr/j_gr display. "
    f"Exact edit: replace '{esc(C_old)}' by '{esc(C_new)}'. " +
    (f"main.tex (both layers, file time 16:05:07) already has the new form (diplomatic lines {dC[1]}-{dC[2]}, current {cC[1]}-{cC[2]}) and no longer the old one, "
     "evidently from the report of batch 461-465; listed because page_460.tex of this batch still ends at 'et définissent'. The moved lines match the print of p. 460."
     if C_APPLIED else
     "(old string once per layer). The moved lines match the print of p. 460. The checker of p. 461 may report the same boundary: apply once."))'''.split("\n")

KEYS_LINE = r'''    for k in (("A", "B", "H") if C_APPLIED else ("A", "B", "C", "H")):'''

# bottom-up splices
check(287, '    for k in ("A", "B", "C", "H"):')
lines[286:287] = [KEYS_LINE]
check(237, '    "Page 461 really begins at')
check(240, '    "The checker of p. 461 may report the same boundary: apply once.")')
lines[236:240] = CNOTE_BLOCK
check(232, '    "(old string once per layer; simulated in memory')
lines[231] = lines[231].replace("(old string once per layer;", "(line numbers as of the 16:05:07 main.tex; old string once per layer;", 1)
for n in range(80, 100):
    if "current {cH[1]}; once per layer)" in lines[n - 1]:
        lines[n - 1] = lines[n - 1].replace("current {cH[1]}; once per layer)", "current {cH[1]} as of the 16:05:07 main.tex; once per layer)", 1)
        break
else:
    raise SystemExit("H note not found")
check(78, '    "(old string once per layer; simulated in memory')
lines[77] = lines[77].replace("(old string once per layer;", "(line numbers as of the 16:05:07 main.tex; old string once per layer;", 1)
check(60, 'dC, cC = sim["diplomatic"]["C"], sim["current"]["C"]')
lines[59:60] = DC_BLOCK
check(48, '    t2 = txt.replace(A_old, A_new)')
lines[47:48] = T2_BLOCK
check(32, "# C: the display after 'donc :'")
check(37, "C_new = C_old.replace(M461 + NL")
lines[31:37] = C_BLOCK
P.write_text("\n".join(lines), encoding="utf-8", newline="\n")
print("patched", len(lines))
