"""Volumes of the SGA 5, 6, 7 I and 7 II scan check: work copies, scans, page markers.

Page markers are comment lines of the SGA 7 transcriptions,
    %%%%%%%%%%  scan idx N  |  folio F  %%%%%%%%%%
where F is the printed page and N the 0-based page index of the volume's scan (SGA 5 and 6 get the same markers).
The text from a marker to the next one is printed page F. Text before a file's first marker continues the page before
it. Front matter in roman numerals is checked separately (no markers).
"""
import pathlib
import re

W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
OS = pathlib.Path(r"C:\Users\user\Documents\Papors\OS")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")

VOLS = {
    "7I": dict(
        dir="sga7i",
        files=["general_introduction_body.tex", "expose_I_body.tex", "expose_II_body.tex", "expose_VI_body.tex",
               "expose_VII_body.tex", "expose_VIII_body.tex", "expose_IX_body.tex"],
        master="SGA7I_Fresh_Source_Transcription_Complete_Working.tex",
        scan=OS / "Groupes de monodromie en géométrie algébrique (Grothendieck, A. (Alexandre)).pdf",
        dpi=360, idx_of=lambda folio: folio + 11,
        witness=OS / "SGA 7-1.tif.djvu", witness_page=lambda folio: folio + 10,
        title="SGA 7 I, Groupes de monodromie en géométrie algébrique I (LNM 288, 1972)",
        note="Exposé VI is printed in English; the other exposés in French."),
    "7II": dict(
        dir="sga7ii",
        files=["expose_X_body.tex", "expose_XI_body.tex", "expose_XII_body.tex", "expose_XIII_body.tex",
               "expose_XIV_body.tex", "expose_XV_body.tex", "expose_XVI_body.tex", "expose_XVII_body.tex",
               "expose_XVIII_body.tex", "expose_XIX_body.tex", "expose_XX_body.tex", "expose_XXI_body.tex",
               "expose_XXII_body.tex"],
        master="SGA7II_French_Source_Transcription_Working_X-XXI_Partial_20260731.tex",
        scan=OS / "Number12.pdf", dpi=300, idx_of=lambda folio: folio + 7,
        witness=OS / "SGA 7-2.tif.djvu", witness_page=lambda folio: folio + 10,
        title="SGA 7 II, Groupes de monodromie en géométrie algébrique II (LNM 340, 1973)", note=""),
    "5": dict(
        dir="sga5", files=["s5.tex"], master="s5.tex",
        scan=OS / "SGA5.pdf", dpi=300, idx_of=lambda folio: folio + 11,
        witness=None, witness_page=None,
        title="SGA 5, Cohomologie l-adique et fonctions L (LNM 589, 1977)", note=""),
    "6": dict(
        dir="sga6", files=["main.tex"], master="main.tex",
        scan=OS / "Théorie des Intersections et Théorème de Riemann-Roch.pdf", dpi=360,
        idx_of=lambda folio: folio + 13,
        witness=OS / "SGA 6.tif.djvu", witness_page=lambda folio: folio + 11,
        title="SGA 6, Théorie des intersections et théorème de Riemann-Roch (LNM 225, 1971)", note=""),
}


def files(vol, edition="diplomatic"):
    v = VOLS[vol]
    return [W / v["dir"] / edition / f for f in v["files"]]


def pages(vol, edition="diplomatic"):
    """folio -> list of (file, start, end) spans; the opening text of a file before its first marker is attached to
    the page before that marker."""
    out = {}
    for f in files(vol, edition):
        t = f.read_text(encoding="utf-8")
        ms = list(MARK.finditer(t))
        if not ms:
            continue
        if t[:ms[0].start()].strip():
            out.setdefault(int(ms[0].group(2)) - 1, []).append((f, 0, ms[0].start()))
        for i, m in enumerate(ms):
            end = ms[i + 1].start() if i + 1 < len(ms) else len(t)
            out.setdefault(int(m.group(2)), []).append((f, m.start(), end))
    return out
