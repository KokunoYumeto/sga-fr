"""One-off patch of build_findings.py: stamp the main.tex line numbers with the file's modification time
(main.tex is being edited while this batch runs), instead of a fixed time."""
import pathlib
P = pathlib.Path(__file__).resolve().parent / "build_findings.py"
s = P.read_text(encoding="utf-8")

anchor = 'layers = {L: (SGA6 / L / "main.tex").read_text(encoding="utf-8") for L in ("diplomatic", "current")}'
assert s.count(anchor) == 1
s = s.replace(anchor, anchor + "\n" +
              "import datetime\n"
              "STAMP = max(datetime.datetime.fromtimestamp((SGA6 / L / \"main.tex\").stat().st_mtime) for L in (\"diplomatic\", \"current\")).strftime(\"%H:%M:%S\")\n"
              "print(\"main.tex time:\", STAMP)", 1)

old_plain = '    "(line numbers as of the 16:05:07 main.tex; old string once per layer;'
assert s.count(old_plain) == 2, s.count(old_plain)
s = s.replace(old_plain, '    f"(line numbers as of the {STAMP} main.tex; old string once per layer;')

old_h = "current {cH[1]} as of the 16:05:07 main.tex; once per layer)"
assert s.count(old_h) == 1
s = s.replace(old_h, "current {cH[1]}, as of the {STAMP} main.tex; once per layer)")

old_c = "(f\"main.tex (both layers, file time 16:05:07) already has the new form"
assert s.count(old_c) == 1
s = s.replace(old_c, "(f\"main.tex (both layers, as of {STAMP}) already has the new form")

assert "16:05:07" not in s
P.write_text(s, encoding="utf-8", newline="\n")
print("patched")
