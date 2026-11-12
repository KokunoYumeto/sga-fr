"""Render the subagent checker prompt for one SGA 4 1/2 spot-check batch: the 4 1/2 variant of render_sga4_prompt.py,
for the batches prepared by prep_sga45.py. The template is CHECKER_PROMPT_SGA.txt, filled with the title of SGA 4 1/2
and NOTE_45.txt. The passages of the template that describe the diplomatic layer and the page-marker lines of
SGA 5-7 are replaced by their SGA 4 1/2 counterparts (the TeX is a modern LaTeX rendition, not a diplomatic one; it
has no page markers, and its pages are cut at whole lines with a comment line on top). Each replaced passage must
occur exactly once in the template, so a changed template stops the script instead of producing a mixed prompt.
A batch paragraph names the part, the scan pages and the source file.

usage: python -I render_sga45_prompt.py FIRST LAST     prints the prompt of batch run_45/bFFF_LLL
       python -I render_sga45_prompt.py --all          writes run_45/prompt_FFF_LLL.txt for every batch, prints paths
"""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(__file__).resolve().parent
R = W / "run_45"
TITLE = "SGA 4½, Cohomologie étale"
spec = json.loads((R / "BATCHES.json").read_text(encoding="utf-8"))
man = json.loads((R / "PREP_MANIFEST.json").read_text(encoding="utf-8"))
root = pathlib.Path(spec["corpus_root"])

REPLACE = [
    ("The transcription is a DIPLOMATIC edition: it must reproduce the print, including the print's own misprints. "
     "{NOTE}",
     "{NOTE}"),
    ('- page_NNN.tex: the LaTeX for that page. It starts at the page\'s marker line "%%%%%%%%%%  scan idx ... | '
     'folio N" (the first line names the source file) and ends where the next page begins.',
     "- page_NNN.tex: the LaTeX for that page, cut from the edition's source file at whole lines (the edition has no "
     "page markers). Its first line is a comment that names the source file and the line range, and says when the "
     "first or the last line is shared with the neighbouring page and through which words the earlier page runs on "
     "that line."),
    ("For every finding give an exact edit for the diplomatic TeX: ",
     "For every finding give an exact edit for the TeX: "),
    ('(for a misprint the TeX already keeps: "fix": null; for a silent correction: change back to the printed '
     'reading)',
     '(for a misprint of the print: "fix": null, whether the TeX keeps it or corrects it)'),
    ('Keep "old" short but unique on the page, never across a marker line, and never change a marker line. A misprint '
     'fix changes only the misprinted characters: the corrected edition skips misprint fixes, so never put a layout or '
     'other change into the same edit; where they overlap, list the other fix first and take the misprint fix\'s '
     '"old" from the text after it.',
     'Keep "old" short but unique on the page, and never take it from the first (comment) line.'),
    ("If the page's text begins or ends at a different place than the marker suggests (text of this page sits under "
     "the neighbouring page's marker, or the reverse), report it once with kind \"marker\" and say where the page "
     "really begins; do not move text yourself.",
     "If page_NNN.tex lacks text that the page prints because the cut is wrong (the text is in the neighbouring "
     "page's file), or holds text of a neighbouring page beyond what its first line says, report it once with kind "
     "\"marker\" and say where the page really begins or ends; do not move text yourself."),
]
# The emphasis clause of the comparison list (the TeX's underline command for the typescript's underlining) does not
# apply here, where emphasis is typography (NOTE_45); it is cut between these two anchors.
EMPH_FROM, EMPH_TO = "punctuation that matters, ", "accents, footnotes"


def template():
    t = (W / "CHECKER_PROMPT_SGA.txt").read_text(encoding="utf-8")
    for old, new in REPLACE:
        assert t.count(old) == 1, "template passage not found exactly once: " + old[:60]
        t = t.replace(old, new)
    i = t.index(EMPH_FROM) + len(EMPH_FROM)
    j = t.index(EMPH_TO, i)
    assert t[i:j].startswith("underlined emphasis (") and t[i:j].endswith("), "), t[i:j]
    return t[:i] + t[j:]


def batch_text(b, rec):
    """The batch paragraph, inserted after the template's file bullets."""
    pages = rec["pages"]
    pdf = [p["scan_pdf_page"] for p in pages]
    lines = [pages[0]["lines"][0], pages[-1]["lines"][1]]
    src = root / b["tex"]
    dup = (" (the scan holds the Rapport twice, PDF pages 81-114 and 115-148, as identical images; these are the "
           "first copy's pages)") if b["part"] == "Rapport" else ""
    return (f"\n\nThese pages: SGA 4½ (LNM 569), {b['title']}, printed pages {b['first']}-{b['last']} (running heads "
            f"{pages[0]['running_head']} to {pages[-1]['running_head']}); scan {pathlib.Path(spec['scan']['path'])} "
            f"(300 dpi), PDF pages {pdf[0]}-{pdf[-1]}{dup}; TeX from {src}, lines {lines[0]}-{lines[1]} (read only: "
            f"labels, \\cite keys and the neighbouring pages can be looked up there); the edition's macros are "
            f"defined in sga-style.sty and its bibliography in sga-sources.bib, in {src.parent}. These pages have "
            f"one scan only: where a stroke is faint or broken, say so and do not guess.")


def render(first, last):
    b = next(x for x in spec["batches"] if x["first"] == first and x["last"] == last)
    name = f"b{first:03d}_{last:03d}"
    rec = next(x for x in man["batches"] if x["batch"] == name)
    folder = R / name
    out = R / f"findings_{first:03d}_{last:03d}.json"
    assert folder.is_dir(), "batch not prepared: %s" % folder
    missing = [n for n in range(first, last + 1) if not (folder / f"page_{n:03d}.tex").exists()]
    note = (W / "NOTE_45.txt").read_text(encoding="utf-8").strip()
    t = template()
    t = (t.replace("{TITLE}", TITLE).replace("{NOTE}", note).replace("{FOLDER}", str(folder))
         .replace("{PAGES}", ", ".join(map(str, range(first, last + 1)))).replace("{OUTFILE}", str(out)))
    assert "{" + "NOTE}" not in t and "{" + "OUTFILE}" not in t
    anchor = "\n\nCompare word by word"
    assert t.count(anchor) == 1
    t = t.replace(anchor, batch_text(b, rec) + anchor)
    if missing:
        t += "\n(No TeX was prepared for page(s) %s: say so in the final message.)\n" % ", ".join(map(str, missing))
    return t


if __name__ == "__main__":
    if sys.argv[1:] == ["--all"]:
        for b in spec["batches"]:
            p = R / f"prompt_{b['first']:03d}_{b['last']:03d}.txt"
            p.write_text(render(b["first"], b["last"]), encoding="utf-8", newline="\n")
            print(p)
    else:
        sys.stdout.write(render(int(sys.argv[1]), int(sys.argv[2])))
