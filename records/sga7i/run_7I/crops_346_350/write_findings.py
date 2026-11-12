import json, sys, pathlib

run = pathlib.Path(r"C:/Users/user/Documents/sga_scan_check_20261105/run_7I")
out = run / "findings_346_350_recheck.json"
NOTE_TAIL = " The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring."

findings = [
    {
        "page": 346,
        "where": "Lemme 3.1.3, hypotheses (second line of the statement)",
        "scan": "s \u2208 S, t \u2208 T une g\u00e9n\u00e9risation de s",
        "tex": "$t \in T$",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "$t \in S$",
        "note": "No T is defined: t is a generization of s \u2208 S, and the lemma compares the fibres K_s and K_t of K over S." + NOTE_TAIL,
    },
    {
        "page": 347,
        "where": "Remarque 3.1.4, last sentence",
        "scan": "On conclut, gr\u00e2ce \u00e0 SGA XVII 4.6.1 (vi), que dans c), ...",
        "tex": "gr\u00e2ce \u00e0 SGA XVII 4.6.1",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "gr\u00e2ce \u00e0 SGA 3 XVII 4.6.1",
        "note": "The volume number 3 is omitted (checked at zoom: one space between SGA and XVII). The remark cites SGA 3 throughout, including SGA 3 XVII 7.2.1 three lines earlier." + NOTE_TAIL,
    },
    {
        "page": 347,
        "where": "Remarque 3.1.4, last sentence",
        "scan": "si K_t est unipotent (SGA 3 VII 1.1, il en est de m\u00eame de K_s.",
        "tex": "(SGA 3 VII 1.1, il en est",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "(SGA 3 XVII 1.1), il en est",
        "note": "The parenthesis is never closed (certain). 'VII' is very probably 'XVII': SGA 3 has no plain Expos\u00e9 VII (only VII_A and VII_B, on infinitesimal theory), while unipotent algebraic groups are defined in SGA 3 Exp. XVII \u00a71 'D\u00e9finition des groupes alg\u00e9briques unipotents', D\u00e9finition 1.1 ([online text of SGA 3 Exp. XVII](https://www.williamstein.org/sga/SGA3/Expo17.pdf)), the expos\u00e9 the remark cites twice. If only the certain part is wanted: '(SGA 3 VII 1.1), il en est'." + NOTE_TAIL,
    },
    {
        "page": 349,
        "where": "3.4.0, last sentence",
        "scan": "la notion se ram\u00e8ne m\u00eame au cas S o\u00f9 S est un trait strictement local",
        "tex": "au cas $S$ o\u00f9 $S$ est",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "au cas o\u00f9 $S$ est",
        "note": "Doubled S." + NOTE_TAIL,
    },
    {
        "page": 350,
        "where": "Proposition 3.5 (ii), display",
        "scan": "V \u2282 V^\u22a5 .  (the \u22a5 written by hand after the second V)",
        "tex": "V \subset V^{\perp}",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "V^{\perp} \subset V",
        "note": "The printed inclusion is reversed. By the diagram (2.5.4) on folio 341, rank V/W = 2\u03b1 and rank V^\u22a5/W = 2\u03bb, so V \u2282 V^\u22a5 means \u03b1 = 0, not semi-stability: with good reduction V = U and V^\u22a5 = 0, and the printed (ii) fails. The proof on this page ends 'V^\u22a5 \u2282 U^I=V, ce qui est (ii)', and (ii) \u27fa (iii) through W = V\u2229V^\u22a5 holds only for V^\u22a5 \u2282 V. A slip of the original (the author's, or of the hand-inserted \u22a5 signs), not a typewriter error; it goes with the misprinted (2.5.5) on folio 341. Apply together with the next entry and with the (2.5.5) correction." + NOTE_TAIL,
    },
    {
        "page": 350,
        "where": "proof of 3.5, sentence after the display \u03bb = 0",
        "scan": "ce qui en vertu de (2.5.5) \u00e9quivaut \u00e0 V = V\u2229V^\u22a5 i.e. \u00e0 (ii)",
        "tex": "\u00e9quivaut \u00e0 $V = V \cap V^{\perp}$",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "\u00e9quivaut \u00e0 $V^{\perp} = V \cap V^{\perp}$",
        "note": "\u03bb = 0 means rank V^\u22a5/W = 0 by (2.5.4), i.e. V^\u22a5 = V\u2229V^\u22a5 = W, which is the corrected (ii). The printed reading follows (2.5.5) on folio 341 as printed, 'rang V/V \u2229 V^\u22a5 = rang V/W = 2\u03bb', which contradicts (2.5.4) and the sentence before it ('V/W soit de rang 2\u03b1'); there it should read 'rang V^\u22a5/V \u2229 V^\u22a5 = rang V^\u22a5/W = 2\u03bb'. Apply together with the previous entry and with that (2.5.5) correction." + NOTE_TAIL,
    },
    {
        "page": 350,
        "where": "proof of 3.5, sentence on (iv)",
        "scan": "D'ailleurs (iv) signifie aussi que I op\u00e8re trivialement sur U^I = V, ce qui par dualit\u00e9 signifie qu'il op\u00e8re trivialement sur V^\u22a5",
        "tex": "trivialement sur $U^{I} = V$",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "trivialement sur $U/U^{I} = U/V$",
        "note": "I acts trivially on U^I by definition, so the printed clause says nothing. (iv) amounts to I acting trivially on U/U^I = U/V (take U' = U^I; conversely U' \u2282 U^I), and U/V is dual to V^\u22a5 under the polarization form, as the sentence goes on to use. The exact intended wording is inferred." + NOTE_TAIL,
    },
]

# every 'tex' must occur exactly once in its page file; every fix 'old' likewise
ok = True
for f in findings:
    p = run / "b346_350" / f"page_{f['page']}.tex"
    text = p.read_text(encoding="utf-8")
    n = text.count(f["tex"])
    if n != 1:
        ok = False
        print("tex count", n, f["page"], repr(f["tex"]))
    if f["fix"] is not None:
        m = text.count(f["fix"]["old"])
        if m != 1:
            ok = False
            print("old count", m, f["page"], repr(f["fix"]["old"]))
print("all unique" if ok else "PROBLEM")
out.write_text(json.dumps(findings, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
json.loads(out.read_text(encoding="utf-8"))
print("written", out, len(findings))
