"""Build findings_051_055.json (SGA 5 pp. 51-55) and check every fix: its old occurs exactly once in the snapshot
page_NNN.tex and in the live page span of both layers (the corrected layer only for fixes that are replayed there),
and no old or new touches a marker line. usage: python -I build_findings.py [--write]"""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, r"C:\Users\user\Documents\sga_scan_check_20261105")
from sga_config import MARK, pages  # noqa: E402

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
NL = "\n"
ISO = "≃: a hand-drawn tilde over a straight bar, no arrowhead at either end"
TITLE = "title typed plain, not underlined"
TITLE_NOTE = ("The bibliography underlines none of its seven titles; the TeX sets all seven in \\emph (the file's "
              "command for the print's underline); each is listed, as on SGA 6 p. 19.")


def F(page, where, scan, tex, kind, conf, old=None, new=None, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
         "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


items = [
    # ---------------- p. 51 ----------------
    F(51, "'Cela étant, les H^i_x(A_X) sont déterminés par la suite exacte'",
      "H^i_x(A_X): plain typed H, no underline (clean paper under the H, beside the subscript x)",
      "les $\\uH_x^i(A_X)$ sont (\\uH = \\underline{\\mathrm H})", "underline", "high",
      "les $\\uH_x^i(A_X)$ sont", "les $\\H_x^i(A_X)$ sont",
      "The print underlines none of the six local-cohomology H_x of this page; the TeX writes all six as \\uH. "
      "Each is listed (as pp. 18-20). The underlined H of 'H^i(E)' on p. 55 is right as \\uH."),
    F(51, "(5.1.2), second term 'H^0_x(A_X)'", "plain H, no underline", "0\\longrightarrow \\uH_x^0(A_X)",
      "underline", "high", "0\\longrightarrow \\uH_x^0(A_X)", "0\\longrightarrow \\H_x^0(A_X)"),
    F(51, "(5.1.2), fifth term 'H^1_x(A_X)'", "plain H, no underline", "\\longrightarrow \\uH_x^1(A_X)\\longrightarrow0",
      "underline", "high", "\\longrightarrow \\uH_x^1(A_X)\\longrightarrow0", "\\longrightarrow \\H_x^1(A_X)\\longrightarrow0"),
    F(51, "(5.1.3), left side 'H^i_x(A_X)'", "plain H, no underline", "(5.1.3)\\qquad \\uH_x^i(A_X)",
      "underline", "high", "(5.1.3)\\qquad \\uH_x^i(A_X)", "(5.1.3)\\qquad \\H_x^i(A_X)"),
    F(51, "(5.1.3), the sign 'H^i_x(A_X) ≃ H^{i-1}(U,A_U)'", ISO, "\\xrightarrow{\\sim}\\H^{i-1}(U,A_U)",
      "symbol", "high", "\\xrightarrow{\\sim}\\H^{i-1}(U,A_U)", "\\simeq \\H^{i-1}(U,A_U)",
      "As on pp. 26-35. Nine such signs on pp. 51-53, each listed; the one sign drawn with an arrowhead, in (5.1.8) "
      "on p. 52, is right as \\xrightarrow{\\sim}."),
    F(51, "'Or on a trivialement ... donc H^0_x(A_X) = H^1_x(A_X) = 0.', first H", "plain H, no underline",
      "donc $\\uH_x^0(A_X)", "underline", "high", "donc $\\uH_x^0(A_X)", "donc $\\H_x^0(A_X)"),
    F(51, "same line, second H 'H^1_x(A_X) = 0'", "plain H, no underline", "=\\uH_x^1(A_X)=0$",
      "underline", "high", "=\\uH_x^1(A_X)=0$", "=\\H_x^1(A_X)=0$"),
    F(51, "'on a la suite spectrale de Hochschild - Serre'",
      "Hochschild - Serre: the typewriter hyphen, with a space on each side", "Hochschild--Serre (en dash)",
      "punctuation", "high", "Hochschild--Serre", "Hochschild - Serre",
      "En dash added by the transcription (NOTE_5: report each). The corrected layer may keep the en dash of modern "
      "usage (as global issue 74 for SGA 7 II)."),
    F(51, "(5.1.4) 'H^p(G,M) ≃ H^p(H,M^P) .'", ISO, "\\H^p(G,M)\\xrightarrow{\\sim}\\H^p(H,M^P)", "symbol", "high",
      "\\H^p(G,M)\\xrightarrow{\\sim}\\H^p(H,M^P)", "\\H^p(G,M)\\simeq \\H^p(H,M^P)"),
    F(51, "(5.1.5) 'H^p(G,M) ≃ H^p(Ẑ(1),M^P) .'", ISO, "\\xrightarrow{\\sim}\\H^p(\\widehat{\\Z}(1),M^P)", "symbol",
      "high", "\\xrightarrow{\\sim}\\H^p(\\widehat{\\Z}(1),M^P)", "\\simeq \\H^p(\\widehat{\\Z}(1),M^P)"),
    F(51, "(5.1.6), ends of its first two lines",
      "'H^i(Ẑ,N) = 0 pour i ⩾ 2 ;' and 'H^0(Ẑ,N) = N^Ẑ ;': semicolons (the third line ends with a full stop)",
      "commas: 'i\\geqslant2,' and 'N^{\\widehat{\\Z}},'", "punctuation", "high",
      "i\\geqslant2," + NL + "\\qquad" + NL + "\\H^0(\\widehat{\\Z},N)=N^{\\widehat{\\Z}},",
      "i\\geqslant2;" + NL + "\\qquad" + NL + "\\H^0(\\widehat{\\Z},N)=N^{\\widehat{\\Z}};",
      "Both marks in one edit."),
    F(51, "printed at the top of p. 52, in page_051.tex as the files stand: 'et H^1(U,A_U) ≃ A.'", ISO,
      "\\H^1(U,A_U)\\xrightarrow{\\sim}A.", "symbol", "high",
      "\\H^1(U,A_U)\\xrightarrow{\\sim}A.", "\\H^1(U,A_U)\\simeq A.",
      "Filed under p. 51 because the line stands in page_051.tex: apply before the marker move of p. 52 (the old "
      "stays unique on p. 52 after the move)."),
    # ---------------- p. 52 ----------------
    F(52, "top of the page",
      "p. 52 begins 'De (5.1.3), (5.1.5), et (5.1.6) on déduit aussitôt que'; p. 51 ends with the third line of "
      "(5.1.6), 'H^1(Ẑ,N) = N_Ẑ .'",
      "the folio-52 marker stands after 'Ce dernier' (s5.tex line 1489 at 16:57); 'De (5.1.3) ...', the two "
      "displays and 'Ce dernier' (lines 1480-1488) end page_051.tex", "marker", "high", None, None,
      "Page 52 really begins at 'De (5.1.3)' (s5.tex line 1480 at 16:57). Exact fix: python -I move_marker.py 5 52 "
      "'De (5.1.3)' --before (simulated in memory on both layers: the marker then stands between the \\] of (5.1.6) "
      "and 'De (5.1.3)'; 'Ce dernier' and 'isomorphisme' then follow each other on two lines of one paragraph). "
      "Text not moved; it agrees with the print except the ≃ filed under p. 51."),
    F(52, "(5.1.7) 'H^1(U,μ_n) ≃ A .'", ISO, "\\H^1(U,\\mu_n)\\xrightarrow{\\sim}A.", "symbol", "high",
      "\\H^1(U,\\mu_n)\\xrightarrow{\\sim}A.", "\\H^1(U,\\mu_n)\\simeq A."),
    F(52, "number of the display (5.1.8)",
      "(5.1.8.): a full stop after the 8 inside the parentheses (clear at 5x); no other formula number of pp. 51-53 "
      "has one, and p. 53 cites '(5.1.8)' and '(5.1.8)''",
      "(5.1.8)\\qquad", "misprint_in_print", "high",
      "(5.1.8)\\qquad \\H^i(U,M)", "(5.1.8.)\\qquad \\H^i(U,M)",
      "The TeX silently drops the stray full stop; the fix restores the printed number (diplomatic layer only). "
      "If the trailing stop counts as the typist's own form (the TeX keeps '(3.4.1.)' on p. 2), apply it to both "
      "layers instead.", corrected="(5.1.8)"),
    F(52, "(5.1.8), right-hand side '(μn)_x^{⊗-1}'",
      "the typed n stands on the line after the hand-drawn μ (its foot on the baseline of the U before it), not "
      "lowered like the n of μ_n in (5.1.7) (about 19 px lower there)",
      "(\\mu_n)_x^{\\otimes -1}", "misprint_in_print", "medium",
      "(\\mu_n)_x^{\\otimes -1}", "(\\mu n)_x^{\\otimes -1}",
      "The typist did not lower the subscript n; the TeX silently corrects; the fix restores the print (diplomatic "
      "layer only). The subscript after the parenthesis is a small x (16 px high, as the n; the capital X of A_X on "
      "this page is 23 px): the diplomatic _x is right. The corrected layer has (\\mu_n)_X with the comment 'FIX "
      "#53 ... source prints (mu_n)_X', which the scan contradicts.", corrected="(\\mu_n)_x^{\\otimes -1}"),
    F(52, "end of the paragraph before Lemme 5.1.9: '... Nous utiliserons le lemme élémentaire suivant :'",
      "a colon after 'suivant' (space before it)", "suivant. (full stop)", "punctuation", "high",
      "le lemme élémentaire suivant.", "le lemme élémentaire suivant :"),
    F(52, "Lemme 5.1.9 (i), 'D(M^G) ≃ (DM)_G .'", ISO, "D(M^G)\\xrightarrow{\\sim}(DM)_G.", "symbol", "high",
      "D(M^G)\\xrightarrow{\\sim}(DM)_G.", "D(M^G)\\simeq (DM)_G."),
    # ---------------- p. 53 ----------------
    F(53, "proof of 5.1.9 (i), 'D(M^G) ≃ lim Coker(DM -> DM) ...', first sign", ISO,
      "D(M^G)\\xrightarrow{\\sim}\\varinjlim", "symbol", "high",
      "D(M^G)\\xrightarrow{\\sim}\\varinjlim", "D(M^G)\\simeq \\varinjlim"),
    F(53, "same display, second sign '... DM) ≃ (DM)_G ,'", ISO, "DM)\\xrightarrow{\\sim}(DM)_G,", "symbol", "high",
      "DM)\\xrightarrow{\\sim}(DM)_G,", "DM)\\simeq (DM)_G,"),
    F(53, "'Prouvons (ii), Soit M' le A-module défini par la suite exacte'",
      "a comma after (ii) (tail below the line, checked at 2.5x), then the capital S of 'Soit'",
      "Prouvons (ii). Soit", "misprint_in_print", "high", "Prouvons (ii). Soit", "Prouvons (ii), Soit",
      "The TeX silently corrects to a full stop; the fix restores the printed comma (diplomatic layer only).",
      corrected="Prouvons (ii). Soit"),
    F(53, "(5.1.8)', '... -> H^1(Ẑ,A) ≃ A .'", ISO, "(\\widehat{\\Z},A)\\xrightarrow{\\sim}A.", "symbol", "high",
      "(\\widehat{\\Z},A)\\xrightarrow{\\sim}A.", "(\\widehat{\\Z},A)\\simeq A."),
    F(53, "heading of the bibliography (printed at the top of p. 54; in page_053.tex as the files stand)",
      "BIBLIOGRAPHIE: capitals (underlined)", "\\section*{Bibliographie}", "word", "medium",
      "\\section*{Bibliographie}", "\\section*{BIBLIOGRAPHIE}",
      "Capitals as printed (as 'A.~GROTHENDIECK', 'L.~ILLUSIE' on p. 1); the underline is the accepted \\section* "
      "setting. Filed under p. 53: apply before the marker move of p. 54 (its anchor '\\section*{B' matches either "
      "spelling)."),
    # ---------------- p. 54 ----------------
    F(54, "top of the page",
      "p. 54 begins with the heading BIBLIOGRAPHIE; p. 53 ends 'Cela achève la démonstration de (5.1).'",
      "\\section*{Bibliographie}, \\begin{description}[...] and '\\item[{[2]}]' (s5.tex lines 1540-1543 at 16:57) "
      "end page_053.tex; the folio-54 marker (line 1544) follows them, so page_054.tex begins 'Hironaka, H.'",
      "marker", "high", None, None,
      "Page 54 really begins at the heading (s5.tex line 1540 at 16:57). Exact fix: python -I move_marker.py 5 54 "
      "'\\section*{B' --before (the short anchor also matches after the BIBLIOGRAPHIE fix; simulated in memory on "
      "both layers: the marker then stands after 'de (5.1).' and its blank line; '\\item[{[2]}]' and 'Hironaka' "
      "then follow each other on two lines of one item). Text not moved."),
    F(54, "[2], title", TITLE,
      "\\emph{Resolution of singularities of an algebraic variety over a field of characteristic zero}",
      "underline", "high",
      "\\emph{Resolution of singularities of an algebraic variety over a field of characteristic zero}",
      "Resolution of singularities of an algebraic variety over a field of characteristic zero", TITLE_NOTE),
    F(54, "[2], 'Ann. of Math, vol. 79 (1964), p. 109.'",
      "'Math,': no full stop after Math (clear at 2x); [1] prints 'Ann. of Math., vol 63'",
      "Ann. of Math., vol. 79", "misprint_in_print", "high", "Math., vol. 79", "Math, vol. 79",
      "The TeX silently supplies the full stop; the fix restores the print (diplomatic layer only).",
      corrected="Math., vol. 79"),
    F(54, "[1], first title", TITLE,
      "\\emph{Local uniformization on algebraic surfaces over ground fields of characteristic $p\\ne0$}",
      "underline", "high",
      "\\emph{Local uniformization on algebraic surfaces over ground fields of characteristic $p\\ne0$}",
      "Local uniformization on algebraic surfaces over ground fields of characteristic $p\\ne0$",
      TITLE_NOTE + " 'fields' is a typed correction (the s struck in before 'of'): the TeX's 'fields of' is right."),
    F(54, "[1], 'Ann. of Math., vol 63 (1956)'",
      "'vol 63': no full stop after vol (clear at 2.5x); [2] prints 'vol. 79'", "vol. 63", "misprint_in_print",
      "high", "vol. 63", "vol 63",
      "The TeX silently supplies the full stop; the fix restores the print (diplomatic layer only).",
      corrected="vol. 63"),
    F(54, "[1], page range 'p.491-526'", "typewriter hyphen", "p.~491--526 (en dash)", "punctuation", "high",
      "491--526", "491-526", "En dash added by the transcription (NOTE_5: report each). As with the joint-name "
      "dash (global issue 74), the corrected layer may keep the en dash."),
    F(54, "[1], second title", TITLE, "\\emph{Resolution of singularities of arithmetical surfaces}",
      "underline", "high", "\\emph{Resolution of singularities of arithmetical surfaces}",
      "Resolution of singularities of arithmetical surfaces", TITLE_NOTE),
    F(54, "[H], title", TITLE, "\\emph{Residues and duality}", "underline", "high",
      "\\emph{Residues and duality}", "Residues and duality", TITLE_NOTE),
    F(54, "[H], 'Lecture Notes n° 20 / Springer (1966).'", "no comma between '20' (line end) and 'Springer'",
      "n\\textsuperscript{o}~20, Springer", "punctuation", "high",
      "n\\textsuperscript{o}~20, Springer", "n\\textsuperscript{o}~20 Springer", "The TeX adds a comma."),
    F(54, "[SGAA], title", TITLE, "\\emph{Cohomologie étale des schémas}", "underline", "high",
      "\\emph{Cohomologie étale des schémas}", "Cohomologie étale des schémas", TITLE_NOTE),
    F(54, "[SGAA], '1963-64.'", "typewriter hyphen", "1963--64 (en dash)", "punctuation", "high",
      "1963--64", "1963-64", "En dash added by the transcription (NOTE_5: report each). As with the joint-name "
      "dash (global issue 74), the corrected layer may keep the en dash."),
    F(54, "[CL], 'Serre, J-P.'", "J-P. : no full stop after J (checked at 4x); the same in [CG]", "Serre, J.-P.",
      "punctuation", "high", "[{[CL]}] Serre, J.-P.", "[{[CL]}] Serre, J-P.",
      "The TeX adds a full stop to the initials."),
    F(54, "[CL], title", TITLE, "\\emph{Corps locaux}", "underline", "high",
      "\\emph{Corps locaux}", "Corps locaux", TITLE_NOTE),
    F(54, "[CG], 'Serre, J-P.'", "J-P. : no full stop after J", "Serre, J.-P.", "punctuation", "high",
      "[{[CG]}] Serre, J.-P.", "[{[CG]}] Serre, J-P.", "As [CL]."),
    F(54, "[CG], title", TITLE, "\\emph{Cohomologie galoisienne}", "underline", "high",
      "\\emph{Cohomologie galoisienne}", "Cohomologie galoisienne", TITLE_NOTE),
    F(54, "[CG], 'Lecture Notes n° 5 / Springer (1964).'", "no comma between '5' (line end) and 'Springer'",
      "n\\textsuperscript{o}~5, Springer", "punctuation", "high",
      "n\\textsuperscript{o}~5, Springer", "n\\textsuperscript{o}~5 Springer", "The TeX adds a comma."),
    F(54, "heading of the appendix (printed at the top of p. 55; in page_054.tex as the files stand)",
      "APPENDICE: capitals (centred, not underlined)", "\\section*{Appendice}", "word", "medium",
      "\\section*{Appendice}", "\\section*{APPENDICE}",
      "Filed under p. 54: apply before the marker move of p. 55 (its anchor '\\section*{A' matches either spelling)."),
    F(54, "byline of the appendix (printed on p. 55; in page_054.tex as the files stand)",
      "par L. ILLUSIE: surname in capitals", "par L.~Illusie", "word", "high",
      "par L.~Illusie", "par L.~ILLUSIE",
      "As 'L.~ILLUSIE' on p. 1. Filed under p. 54: apply before the marker move of p. 55. The short rule centred "
      "under the byline and the '-:-:-:-' that closes p. 54 are ornaments, not transcribed anywhere in the volumes: "
      "not listed."),
    # ---------------- p. 55 ----------------
    F(55, "top of the page",
      "p. 55 begins with the heading APPENDICE and 'par L. ILLUSIE'; p. 54 ends with [CG] 'Springer (1964).' and "
      "an ornament",
      "\\section*{Appendice}, \\begin{center} and 'par L.~Illusie' (s5.tex lines 1553-1555 at 16:57) end "
      "page_054.tex; the folio-55 marker (line 1556) stands inside the center environment, before \\end{center}",
      "marker", "high", None, None,
      "Page 55 really begins at the heading (s5.tex line 1553 at 16:57). Exact fix: python -I move_marker.py 5 55 "
      "'\\section*{A' --before (also matches after the APPENDICE fix; simulated in memory on both layers: the marker "
      "then stands after \\end{description} and its blank line, and the center environment is whole on p. 55). "
      "Text not moved."),
    F(55, "paragraph number '1.1.'",
      "'1.1. Soit X un préschéma': the number in the ordinary type of the line, not underlined, not bold",
      "\\textbf{1.1.}", "font", "medium", "\\textbf{1.1.} Soit", "1.1. Soit",
      "Not an underlined title, so not covered by the accepted \\textbf (as '1) Cas particulier :' on p. 18). The "
      "next number, '\\textbf{1.2.}' at the top of p. 56, has the same form."),
    F(55, "'La notion de A_X-Module (à gauche) constructible se définit comme dans (SGAA IX 2.3)'",
      "'constructible' underlined (the term being defined)", "(à gauche) constructible se (no emphasis)",
      "underline", "high", "(à gauche) constructible se", "(à gauche) \\emph{constructible} se",
      "\\emph is the file's command for the print's underline in Exposé I and the appendix (\\emph{constructible}, "
      "\\emph{bidualisant}, \\emph{Preuve})."),
]


def page_text(n):
    return (RUN / "b051_055" / f"page_{n:03d}.tex").read_text(encoding="utf-8")


ok = True
spans = {layer: pages("5", layer) for layer in ("diplomatic", "current")}
for i, x in enumerate(items, 1):
    fx = x["fix"]
    if not fx:
        continue
    old, new = fx["old"], fx["new"]
    if MARK.search(old) or MARK.search(new):
        print(i, "TOUCHES A MARKER");
        ok = False
    c = page_text(x["page"]).count(old)
    live = []
    for layer in ("diplomatic", "current"):
        f, s, e = spans[layer][x["page"]][0]
        live.append(f.read_text(encoding="utf-8")[s:e].count(old))
    flag = "" if c == 1 and live[0] == 1 else "  <-- CHECK"
    if x["kind"] != "misprint_in_print" and live[1] != 1:
        flag += "  (current layer: %d)" % live[1]
    if flag.strip():
        ok = False
    print(f"{i:2d} p{x['page']} {x['kind']:18s} snapshot {c} live-dipl {live[0]} live-curr {live[1]}{flag}")
print("all fixes unique:", ok)
if "--write" in sys.argv:
    out = RUN / "findings_051_055.json"
    out.write_text(json.dumps(items, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("written", out, len(items))
