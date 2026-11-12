import pathlib
p = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\crops_306_310\build_findings.py")
lines = p.read_text(encoding="utf-8").split("\n")
fixed = {
    190: r'''    corrected=r"$j_i^{\text{ème}}$")''',
    256: r'''add(310, "diagram, bottom arrow γ", "γ above the arrow", r'\arrow[r,"\gamma"' + "'] (label below the arrow)",''',
    274: r'''    corrected=r"que $A^{\bullet}(D)$ est un $C$-module")''',
}
for n, new in fixed.items():
    print("was:", repr(lines[n - 1]))
    lines[n - 1] = new
    print("now:", repr(lines[n - 1]))
t = "\n".join(lines)
bad = [c for c in t if ord(c) < 32 and c not in "\n"]
print("control characters left:", [hex(ord(c)) for c in bad])
p.write_text(t, encoding="utf-8", newline="\n")
