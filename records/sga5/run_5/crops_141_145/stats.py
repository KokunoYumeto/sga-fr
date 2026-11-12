"""Read-only statistics of Exposé III B in s5.tex (diplomatic layer)."""
import itertools
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
p = r"C:\Users\user\Documents\sga_scan_check_20261105\sga5\diplomatic\s5.tex"
lines = open(p, encoding="utf-8").read().split("\n")
start = next(i for i, l in enumerate(lines) if l.startswith(r"\section*{Exposé III B"))
end = next(i for i, l in enumerate(lines) if l.startswith(r"\section*{Exposé V."))
seg = "\n".join(lines[start:end])
print("III B lines", start + 1, end)
print("emph", len(re.findall(r"\\emph\{", seg)), "underline", len(re.findall(r"\\underline\{", seg)))
print("otimes_S^LL", seg.count(r"\otimes_S^{\LL}"), "otimes^LL", seg.count(r"\otimes^{\LL}"),
      "LL total", len(re.findall(r"\\LL(?![a-zA-Z])", seg)),
      "overset mathrm", seg.count(r"\overset{\mathrm"), "overset mathbf", seg.count(r"\overset{\mathbf"),
      "lten", seg.count(r"\lten"))
print("uRHom", len(re.findall(r"\\uRHom(?![a-zA-Z])", seg)), "RHom", len(re.findall(r"\\RHom(?![a-zA-Z])", seg)),
      "R", len(re.findall(r"\\R(?![a-zA-Z])", seg)))
print("statement", seg.count(r"\begin{statement}"), "prooftext", seg.count(r"\begin{prooftext}"))
print([m.group(0) for m in itertools.islice(re.finditer(r"\\(?:emph|underline)\{[^}]*\}", seg), 60)])
print([m.group(0) for m in re.finditer(r"\\begin\{(?:statement|prooftext)\}(?:\{[^}]*\}|\[[^]]*\])", seg)][:60])
