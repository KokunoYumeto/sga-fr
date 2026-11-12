import pathlib

p = pathlib.Path(__file__).resolve().parent / "build_findings.py"
s = p.read_text(encoding="utf-8")
old = r"""Then join '\\begin{prooftext}[' and 'Preuve]' on one line ('\\begin{prooftext}[Preuve]'): the line break left by the marker insertion puts a space at the start of the label. Text not moved."""
new = r"""Then, on p. 242, replace '\\begin{prooftext}[' + newline + 'Preuve]' by '\\begin{prooftext}[Preuve]': the line break left by the marker insertion puts a space before 'Preuve' (seen in a test compile). Text not moved."""
assert s.count(old) == 1, s.count(old)
p.write_text(s.replace(old, new), encoding="utf-8")
print("ok")
