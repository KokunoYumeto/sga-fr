"""One-off: replace the DIAG definition (lines starting at 'DIAG = ') in make_findings.py by a correct one."""
import pathlib

p = pathlib.Path(__file__).resolve().parent / "make_findings.py"
lines = p.read_text(encoding="utf-8").split("\n")
i = next(k for k, l in enumerate(lines) if l.startswith("DIAG = "))
new = [
    'DIAG = (r"\\[\\n\\begin{tikzcd}[column sep=large,row sep=large]\\n"',
    "        + r'\\Lambda \\arrow[r,\"\\widetilde c\"] \\arrow[d,\"\\widetilde c_0\"' + \"'] &\" + r\"\\n\"",
    '        + r"\\Ch(\\Gr\\Lambda)\\\\\\n\\Ch(\\Omega) \\arrow[ur] &\\n\\end{tikzcd}\\n\\]\\n")',
]
lines[i:i + 3] = new
p.write_text("\n".join(lines), encoding="utf-8")
print("\n".join(lines[i:i + 3]))
