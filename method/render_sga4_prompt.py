"""Render the subagent checker prompt for one SGA 4 spot-check batch: the equivalent of render_sga_prompt.py for the
SGA 4 batches prepared by prep_sga4.py. The template is CHECKER_PROMPT_SGA.txt, filled with the title of SGA 4 and
NOTE_4.txt. Five passages of the template describe the diplomatic layer and the page-marker lines of SGA 5-7; they
are replaced by their SGA 4 counterparts (the TeX is a modern edition, not a diplomatic one, and its pages are cut at
whole lines with a comment line on top). Each replaced passage must occur exactly once in the template, so a changed
template stops the script instead of producing a mixed prompt. A batch paragraph names the tome, exposé, scan and
source file; the batch with a second witness (Exposé XVII) also names its witness strips.

usage: python -I render_sga4_prompt.py FIRST LAST     prints the prompt of batch run_4/bFFF_LLL
       python -I render_sga4_prompt.py --all          writes run_4/prompt_FFF_LLL.txt for every batch, prints paths
"""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(__file__).resolve().parent
R = W / "run_4"
TITLE = "SGA 4, Théorie des topos et cohomologie étale des schémas"
spec = json.loads((R / "BATCHES.json").read_text(encoding="utf-8"))
man = json.loads((R / "PREP_MANIFEST.json").read_text(encoding="utf-8"))
root = pathlib.Path(spec["corpus_root"])

REPLACE = [
    ("The transcription is a DIPLOMATIC edition: it must reproduce the print, including the print's own misprints. "
     "{NOTE}",
     "{NOTE}"),
    ('- page_NNN.tex: the LaTeX for that page. It starts at the page\'s marker line "%%%%%%%%%%  scan idx ... | '
     'folio N" (the first line names the source file) and ends where the next page begins.',
     r"- page_NNN.tex: the LaTeX for that page, cut from the edition's source file at whole lines. Its first line is "
     r"a comment that names the source file and the line range, and says when the first or the last line is shared "
     r"with the neighbouring page; the page on the far side of such a line begins at the word just before that "
     r"line's \pageoriginale."),
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
# apply to SGA 4, whose emphasis is typography (NOTE_4); it is cut between these two anchors.
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
    """The witness bullet (if any) and the batch paragraph, inserted after the template's file bullets."""
    vol = spec["volumes"][b["tome"]]
    pages = rec["pages"]
    pdf = [p["scan_pdf_page"] for p in pages]
    lines = [pages[0]["lines"][0], pages[-1]["lines"][1]]
    src = root / b["tex"]
    cfg = src.parent.parent / "fichiers-configuration-latex"
    bullet = ""
    if all("witness_pdf_page" in p for p in pages):
        w = pages[0]
        bullet = (f"\n- page_NNN_w1.png ... page_NNN_w4.png: the same page in a second scan, Springer's lossless "
                  f"300-dpi scan of Exposés XVII-XVIII ({pathlib.Path(w['witness'])}, PDF page = printed page - "
                  f"{w['folio'] - w['witness_pdf_page']}). The main scan of this tome stores the text as a JBIG2 mask, "
                  f"whose symbol coding can put a look-alike in place of a character: where a letter, digit, index "
                  f"or prime matters and the main strip is faint, broken or doubtful, read the witness strip before "
                  f"deciding; do not read the witness strips otherwise.")
        scans = ""
    elif b["tome"] == "3":
        scans = (" This tome's scan stores the text as a JBIG2 mask, whose symbol coding can put a look-alike in "
                 "place of a character, and there is no second scan of these pages: where a stroke is faint, broken "
                 "or doubtful, say so and do not guess.")
    else:
        scans = " These pages have one scan only: where a stroke is faint or broken, say so and do not guess."
    para = (f"\n\nThese pages: SGA 4 Tome {b['tome']} (LNM {vol['lnm']}), Exposé {b['expose']}, printed pages "
            f"{b['first']}-{b['last']} (typescript pages {pages[0]['typescript']} to {pages[-1]['typescript']}); main "
            f"scan {pathlib.Path(vol['scan'])} (300 dpi), PDF pages {pdf[0]}-{pdf[-1]}; TeX from {src}, lines "
            f"{lines[0]}-{lines[1]} (read only: labels, \\bibitem entries and the neighbouring pages can be looked up "
            f"there); the edition's macros are defined in macros.tex and numerotation.tex in {cfg}.{scans}")
    return bullet + para


def render(first, last):
    b = next(x for x in spec["batches"] if x["first"] == first and x["last"] == last)
    name = f"b{first:03d}_{last:03d}"
    rec = next(x for x in man["batches"] if x["batch"] == name)
    folder = R / name
    out = R / f"findings_{first:03d}_{last:03d}.json"
    assert folder.is_dir(), "batch not prepared: %s" % folder
    missing = [n for n in range(first, last + 1) if not (folder / f"page_{n:03d}.tex").exists()]
    note = (W / "NOTE_4.txt").read_text(encoding="utf-8").strip()
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
