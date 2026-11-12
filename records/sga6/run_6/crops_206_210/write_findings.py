"""Write findings_206_210.json and check that every fix's old string occurs exactly once in its page file."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
B = RUN / "b206_210"
OUT = RUN / "findings_206_210.json"

F = [
    {
        "page": 206,
        "where": "start of page, first word",
        "scan": "p. 206 begins 'quence du lemme suivant :', the end of 'conséquence' divided at the page break (both scans)",
        "tex": "the folio-206 marker stands before the whole word 'conséquence'",
        "kind": "marker",
        "confidence": "medium",
        "fix": None,
        "note": "Page 206 really begins with 'quence'. Split the word at the marker as at folios 18, 36, 46, 54 and 161: "
                "python -I marker_split_word.py 6 206 split consé quence (simulated in memory on both layers with "
                "crops_206_210/sim_split.py: '... La proposition sera donc' / 'consé%' / marker / 'quence du lemme "
                "suivant~:'). The checker of p. 205 may report the same boundary: apply once.",
    },
    {
        "page": 206,
        "where": "Lemme 2.2.1, conclusion: 'contenant s x U'",
        "scan": "'Il existe alors un ouvert U' de S x U contenant s x U, et un S-morphisme': s x U without the hand-drawn "
                "braces that the lemma's hypotheses and the proof give it ({s} x U) (both scans)",
        "tex": r"contenant $s\times U$",
        "kind": "misprint_in_print",
        "confidence": "low",
        "fix": None,
        "corrected": r"contenant $\{s\}\times U$",
        "note": "The TeX keeps the printed reading. The proof concludes 'est un ouvert de S x U contenant {s} x U'. "
                "Low: it may be a deliberate abbreviation (s identified with {s}).",
    },
    {
        "page": 207,
        "where": "Preuve of Corollaire 2.4: 'le foncteur H^o(A,.) est exact'",
        "scan": "H^o(A,.) with a typed full stop on the baseline as the placeholder (both scans)",
        "tex": r"$H^0(A,\cdot)$",
        "kind": "symbol",
        "confidence": "medium",
        "fix": {"old": r"H^0(A,\cdot)", "new": r"H^0(A,.)"},
        "note": r"\cdot raises the typed stop to mid-height; same kind of fix as (P,\cdot) -> (P,.) on p. 89.",
    },
    {
        "page": 208,
        "where": "Preuve of Corollaire 2.6, display H^o(X_s, i_s^{-1}Hom(X,Y)) = Lim Hom(X|S',Y) (S' ouvert)",
        "scan": "a typed 'Lim' with capital L and no arrow, 'S'\u220bs' typed under it (both scans)",
        "tex": r"=\varinjlim_{S'\ni s}\Homop(X|S',Y)",
        "kind": "formula",
        "confidence": "high",
        "fix": {"old": r"\varinjlim_{S'\ni s}", "new": r"\operatorname*{Lim}_{S'\ni s}"},
        "note": r"\varinjlim sets a lower-case lim with an arrow under it, which this display does not have. On p. 210 "
                r"the print has lower-case 'lim' with a hand-drawn arrow, where \varinjlim is right.",
    },
    {
        "page": 209,
        "where": "start of page",
        "scan": "p. 209 begins 'de s tel que f|X|S' : X|S' --> Y|S' soit un isomorphisme.'; p. 208 ends '... Il existe "
                "alors un voisinage S'' (both scans)",
        "tex": r"'de $s$ tel que $f|X|S':X|S'\longrightarrow Y|S'$' ends the last line of page_208.tex (under the "
               r"folio-208 marker); page_209.tex begins 'soit un isomorphisme.'",
        "kind": "marker",
        "confidence": "high",
        "fix": None,
        "note": r"Page 209 really begins with 'de $s$ tel que'. python -I move_marker.py 6 209 'de $s$ tel que $f|X|S' "
                r"--before (single quotes for the shell; the last occurrence before the marker is the one after 'un "
                r"voisinage $S'$'; simulated in memory on both layers with crops_206_210/sim_markers.py: '... Il existe "
                r"alors un voisinage $S'$ ', the marker, 'de $s$ tel que $f|X|S':X|S'\longrightarrow Y|S'$', 'soit un "
                r"isomorphisme.').",
    },
    {
        "page": 209,
        "where": "Preuve of Corollaire 2.8: 'forment un système fondamental de voisinage de Z_s'",
        "scan": "'voisinage' in the singular (both scans)",
        "tex": r"système fondamental de voisinage de $Z_s$",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": r"système fondamental de voisinages de $Z_s$",
        "note": "The TeX keeps the printed reading. Corollaires 2.5 and 2.8 have 'système fondamental de voisinages'.",
    },
    {
        "page": 210,
        "where": "end of page",
        "scan": "p. 210 ends '... d'image dense, et l'on a' (both scans); p. 211 begins '(loc.cit.)', then the display "
                "C^oo(X,E) = lim<- C^r_2(X,E) (main scan of p. 211)",
        "tex": "page_210.tex ends 'et l'on a (loc.cit.)': '(loc.cit.)' stands under the folio-210 marker",
        "kind": "marker",
        "confidence": "high",
        "fix": None,
        "note": "Page 211 really begins with '(loc.cit.)'. python -I move_marker.py 6 211 '(loc.cit.)' --before "
                "(simulated in memory on both layers with crops_206_210/sim_markers.py: '... d'image dense, et l'on a ', "
                "the marker, '(loc.cit.)', then the display). The checker of p. 211 may report the same boundary: "
                "apply once.",
    },
]

bad = 0
for x in F:
    t = (B / f"page_{x['page']:03d}.tex").read_text(encoding="utf-8")
    if x["fix"]:
        n = t.count(x["fix"]["old"])
        print(x["page"], "fix old count", n, repr(x["fix"]["old"]))
        bad += n != 1
        if "%%%%%%%%%%" in x["fix"]["old"]:
            print("  marker inside old!"); bad += 1
    if x["kind"] == "misprint_in_print":
        n = t.count(x["tex"])
        print(x["page"], "misprint tex count", n, repr(x["tex"]))
        bad += n != 1
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
json.loads(OUT.read_text(encoding="utf-8"))
print("written", OUT, len(F), "findings; problems:", bad)
