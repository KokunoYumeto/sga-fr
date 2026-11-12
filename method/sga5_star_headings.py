"""SGA 5, both layers: unstarred \\section{...}, \\subsection{...}, \\subsubsection{...} print LaTeX's own number before
the print's ("1.1 2. Unicité ..."); make them starred, as the rest of the volume (checker of batch 031-035, 10 Nov
2026). Logged in FIXLOG_5*.jsonl.
usage: python -I sga5_star_headings.py"""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).parent
PAT = re.compile(r"\\((?:sub)*section)\{")
for layer, log in (("diplomatic", "FIXLOG_5.jsonl"), ("current", "FIXLOG_5_CURRENT.jsonl")):
    p = ROOT / "sga5" / layer / "s5.tex"
    t = p.read_text(encoding="utf-8")
    hits = PAT.findall(t)
    p.write_text(PAT.sub(lambda m: "\\" + m.group(1) + "*{", t), encoding="utf-8", newline="")
    with open(ROOT / log, "a", encoding="utf-8") as f:
        for h in hits:
            f.write(json.dumps({"vol": "5", "file": "s5.tex", "page": None, "old": "\\" + h + "{", "new": "\\" + h + "*{",
                                "kind": "heading",
                                "source": "global: unnumbered headings, the print gives its own numbers (findings_031_035.json)"},
                               ensure_ascii=False) + "\n")
    print(layer, len(hits), "headings starred")
