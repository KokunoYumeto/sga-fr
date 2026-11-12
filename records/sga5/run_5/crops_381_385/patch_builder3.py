"""Third one-off patch of build_findings.py: paragraph-break findings, inserted in reading order."""
import pathlib

p = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\crops_381_385\build_findings.py")
s = p.read_text(encoding="utf-8")
INS = [
    (r'''mp(381, "'qui associe à chaque A[G]-module X de module sur A''',
     r'''add(381, "'Un complexe X° de A[G]-modules étant donné, ...' after the display A[G] = Λ[G] ⊗_Λ A .",
    "a new, indented paragraph (as 'Soit A un algèbre' above it)", "runs on after the display (no blank line)",
    "other", "high", "\\]" + NL + "Un complexe", "\\]" + NL + NL + "Un complexe",
    "Paragraph break; drop it if paragraphing is left to a global pass.")

'''),
    (r'''mp(383, "display 'K' ⊃ K , [K':K] == n'"''',
     r'''add(383, "'Soit' before the display K' ⊃ K", "'Soit' stands flush left on the line after '... rationnelles.' "
    "(new paragraphs of this typescript are indented)", "a blank line before 'Soit' (new paragraph)", "other", "low",
    "rationnelles." + NL + NL + "Soit", "rationnelles." + NL + "Soit",
    "The print continues the paragraph of 4.2 on a new line; low because a flush-left line before a display may be "
    "the typist's layout only. Drop it if paragraphing is left to a global pass.")

'''),
    (r'''mp(384, "'Les résultats de Artin-Serre-Swan'"''',
     r'''add(384, "'Les résultats de Artin-Serre-Swan ...' after (4.2.2)", "a new, indented paragraph",
    "runs on after the display (no blank line)", "other", "high", "\\]" + NL + "Les ", "\\]" + NL + NL + "Les ",
    "Paragraph break; drop it if paragraphing is left to a global pass.")

'''),
    (r'''add(384, "'Le caractère σ'_{y'} de Sw'_{y'} est donné par la formule :'"''',
     r'''add(384, "'Le caractère σ'_{y'} de Sw'_{y'} ...' after (4.2.3)", "a new, indented paragraph",
    "runs on after the display (no blank line)", "other", "high", "\\]" + NL + "Le caractère",
    "\\]" + NL + NL + "Le caractère", "Paragraph break; drop it if paragraphing is left to a global pass.")

'''),
    (r'''add(385, "'On a donc :'"''',
     r'''add(385, "'On a donc :' after '... qui sera désigné part Art_{y'} .'", "'On a donc :' stands flush left on the "
    "next line (not indented)", "a blank line before 'On a donc' (new paragraph)", "other", "low",
    "$Art_{y'}$." + NL + NL, "$Art_{y'}$." + NL,
    "As 'Soit' on p. 383: the print does not indent it. Drop it if paragraphing is left to a global pass.")

'''),
    (r'''mp(385, "'Les caractères ... sont notés σ_{y'} , σ'_y , a_y .'"''',
     r'''add(385, "'Les caractères des représentations précédentes ...' after (4.2.8)", "a new, indented paragraph",
    "runs on after the display (no blank line)", "other", "high", "\\]" + NL + "Les caractères",
    "\\]" + NL + NL + "Les caractères", "Paragraph break; drop it if paragraphing is left to a global pass.")

'''),
]
for anchor, block in INS:
    n = s.count(anchor)
    assert n == 1, (n, anchor)
    s = s.replace(anchor, block + anchor)
p.write_text(s, encoding="utf-8", newline="")
print("inserted", len(INS))
