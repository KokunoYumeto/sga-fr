import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = r'C:/Users/user/Documents/sga_scan_check_20261105/run_7I/b061_065/page_%03d.tex'
OUT = r'C:/Users/user/Documents/sga_scan_check_20261105/run_7I/findings_061_065.json'

SQ = "'"

F = []

# ---------------- page 61 ----------------
F.append({
    "page": 61,
    "where": "Representability, 'representable by an object X_0 = (R_0 \u21c9 R_1) in (R_0 \u2a3f R_0, C) i.e. if there exists R_0-map'",
    "scan": "(R_0     R_0, C) : a blank gap between the two R_0, no \u2a3f (no trace of a stroke in a crop); the four other (R_0 \u2a3f R_0, C) on the page carry the hand-written \u2a3f",
    "tex": r"(R_0 \qquad R_0,\ \underline{C})",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": r"(R_0 \amalg R_0,\ \underline{C})",
    "note": "The hand-written coproduct sign was never inserted; X_0 is an object of (R_0 \u2a3f R_0, C), the source category of Hom_{\u03be^#} and of the bijection in the next line. The TeX keeps the printed blank (\\qquad). 'corrected' replaces the 'tex' substring."
})
F.append({
    "page": 61,
    "where": "Same line, 'X_0 = (R_0 \u21c9 R_1)' with s_1 above and s_2 below",
    "scan": "two plain typed rules with s_1 above and s_2 below, no arrowheads at either end (checked in a crop)",
    "tex": r"\overset{s_1}{\underset{s_2}{\rightrightarrows}}",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": {"old": r"\rightrightarrows", "new": r"=\!="},
    "corrected": r"\overset{s_1}{\underset{s_2}{\rightrightarrows}}",
    "note": "The heads of the two arrows s_1, s_2 : R_0 \u2192 R_1 were not added (the same line also lacks its hand-written \u2a3f); the same object (R_0 \u21c9 R_1) has typed arrowheads on pp. 62 and 63. The TeX silently supplies the heads; the fix restores the printed plain double rule. 'corrected' (the TeX's present reading) replaces the 'tex' substring."
})

# ---------------- page 62 ----------------
F.append({
    "page": 62,
    "where": "Display defining (\u03be,\u03c6) on arrows, '... \u27fc the composit map \u03be(f) \u2192 \u03be(hf) \u2192 \u03be(f') .'",
    "scan": "the composit map",
    "tex": r"\text{the composit map}",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": r"\text{the composite map}",
    "note": "Spelling slip. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring."
})
F.append({
    "page": 62,
    "where": "'We note that, for each object S in C , the functor (\u03be,\u03c6)(S) : h_(R_0,R_1,...)(S) \u2192 F(S) is fully-faithful'",
    "scan": "(\u03be,\u03c6)(S)    h_(R_0,R_1,...)(S) \u2192 F(S) : no colon after (\u03be,\u03c6)(S) (checked in a crop)",
    "tex": r"$(\xi,\varphi)(S)$",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": None,
    "corrected": r"$(\xi,\varphi)(S) :$",
    "note": "The colon between the functor and its source and target is missing (the next sentence has '(\u03be,\u03c6) : h_(R_0,R_1,...) \u2192 F'). The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring."
})
F.append({
    "page": 62,
    "where": "'Consequently the functor (\u03be,\u03c6) : h_(R_0,R_1,...) \u2192 F is an C-equivalence if and only if \u03be is a quasi-initial object'",
    "scan": "is an C-equivalence",
    "tex": r"is an $\underline{C}$-equivalence",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": None,
    "corrected": r"is a $\underline{C}$-equivalence",
    "note": "Article slip; the same statement on p. 63 reads 'a C-equivalence'. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring."
})

# ---------------- page 63 ----------------
F.append({
    "page": 63,
    "where": "Proof of 2.11, '\u21d4 given u \u2208 h_{R_1}(S) and a lifting f' or s_1(u) to S' , there exists a lifting u' of u to S''",
    "scan": "a lifting f' or s_1(u) to S' ('or', clear in a crop)",
    "tex": r"or  $s_1(u)$",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": r"of  $s_1(u)$",
    "note": "Typing error for 'of': f' is a lifting of s_1(u) to S' (the lifting u' then satisfies s_1(u') = f'). The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring."
})

# ---------------- page 64 ----------------
F.append({
    "page": 64,
    "where": "Diamond diagram of the proof of 2.12(a), arrow (S_1 \u00d7_S S_2, f_1 \u00d7 s_2(v)) \u2192 (S_1,f_1)",
    "scan": "label \u03c0_1 typed above-left of the shaft, outside the diamond (as (\u03c0_2,v^{-1}) lies above-right of its shaft)",
    "tex": '\\arrow[dl, "\\pi_1"]',
    "kind": "other",
    "confidence": "low",
    "fix": {"old": '\\arrow[dl, "\\pi_1"]', "new": '\\arrow[dl, "\\pi_1"' + SQ + ']'},
    "note": "For a down-left arrow tikz-cd sets an unswapped label below-right of the shaft (inside the diamond); the swap mark ' puts it above-left, as printed. The other three labels of the diagram already sit on their printed sides."
})

# ---------------- page 65 ----------------
F.append({
    "page": 65,
    "where": "End of the fibre-product computation, 'Hom((T, g), (S_1, f_1)) \u00d7_{Hom((T,g), (S,f))} Hom((T, g), (S_2, f_2)) .'",
    "scan": "Hom((T, g), (S_1, f_1) \u00d7 ... : a single closing parenthesis after f_1 (checked in a crop)",
    "tex": r"\mathrm{Hom}((T,\ g),\ (S_1,\ f_1)",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": r"\mathrm{Hom}((T,\ g),\ (S_1,\ f_1))",
    "note": "The first Hom( is never closed (the second factor Hom((T, g), (S_2, f_2)) is). The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring."
})
F.append({
    "page": 65,
    "where": "Proof of 2.12(b), 'since h_{R_0}(k[\u03b5]) \u2192 [h_(R_0,R_1,...)(k[\u03b5])] is bijective'",
    "scan": "[h_(R_0,R_1,...,)(k[\u03b5])] : a comma after the three dots (checked in a crop)",
    "tex": r"(R_0,R_1,\ldots,)",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": r"(R_0,R_1,\ldots)",
    "note": "Stray comma before the closing parenthesis. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring."
})
F.append({
    "page": 65,
    "where": "Proof of 2.12(c), 'the functor Isom(\u03be,\u03be) from C_\u039b/T \u2297_\u039b T to (sets)'",
    "scan": "C_\u039b/T \u2297_\u039bT : no underline under the C (the h's of the same paragraph are underlined)",
    "tex": r"$C_\Lambda/T \otimes_\Lambda T$",
    "kind": "misprint_in_print",
    "confidence": "low",
    "fix": None,
    "corrected": r"$\underline{C}_\Lambda/T \otimes_\Lambda T$",
    "note": "Category letter without its underline (the C of C_\u039b is underlined everywhere else on these pages). Low: an omitted underline, not a wrong character. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring."
})
F.append({
    "page": 65,
    "where": "Proof of 2.12(c), 'is represented by R_1 \u2297_{R_0 \u2297\u0302_\u039b R_0} (T \u2297_\u039b T)'",
    "scan": "(T \u2297_\u039b T) : a faint \u2297 with no hat above it (contrast crop); the hat is typed only over the \u2297 of the subscript R_0 \u2297\u0302_\u039b R_0",
    "tex": r"(T \hat{\otimes}_\Lambda T)",
    "kind": "symbol",
    "confidence": "medium",
    "fix": {"old": r"(T \hat{\otimes}_\Lambda T)", "new": r"(T \otimes_\Lambda T)"},
    "note": "The same sentence twice prints T \u2297_\u039b T without a hat (C_\u039b/T \u2297_\u039b T, T \u21c9 T \u2297_\u039b T); the TeX adds a hat that the print does not have."
})
F.append({
    "page": 65,
    "where": "Proof of 2.12(c), 'By a passage to limit, one get that Isom(\u03be_0, \u03be_0) is pro-represented by some S_1'",
    "scan": "one get that",
    "tex": "one get that",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": "one gets that",
    "note": "Verb agreement slip. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring."
})
F.append({
    "page": 65,
    "where": "Proposition 2.14, '... which induces C_\u039b-equivalence h_(\u03b1_0,\u03b1_1) : ...'",
    "scan": "C_\u039b-equi- | valence : the word is divided at the line end",
    "tex": r"\underline{-equi-} \underline{valence}",
    "kind": "other",
    "confidence": "medium",
    "fix": {"old": r"\underline{-equi-} \underline{valence}", "new": r"\underline{-equivalence}"},
    "note": "The TeX keeps the print's line-end hyphen, so the word is set mid-line as 'equi- valence'; the file joins the other divided words of these pages (disconnected, p. 63; minimally, p. 65)."
})

# ---------------- checks ----------------
ok = True
for f in F:
    txt = open(BASE % f['page'], encoding='utf-8').read()
    n_tex = txt.count(f['tex'])
    if n_tex < 1:
        print('TEX NOT FOUND', f['page'], repr(f['tex'])); ok = False
    if f['fix'] is not None:
        old = f['fix']['old']
        n = txt.count(old)
        if n != 1:
            print('FIX OLD COUNT', n, f['page'], repr(old)); ok = False
        marker = [l for l in txt.split('\n') if l.startswith('%%%%%%%%%%')]
        if any(old in m for m in marker):
            print('OLD IN MARKER', f['page'], repr(old)); ok = False
    if f['kind'] == 'misprint_in_print':
        if 'corrected' not in f:
            print('NO CORRECTED', f['page']); ok = False
    else:
        if 'corrected' in f:
            print('CORRECTED ON NON-MISPRINT', f['page']); ok = False

with open(OUT, 'w', encoding='utf-8', newline='\n') as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
print('written', len(F), 'ok' if ok else 'PROBLEMS')
from collections import Counter
c = Counter((f['page'], f['kind'] == 'misprint_in_print') for f in F)
for p in range(61, 66):
    print(p, 'normal', c[(p, False)], 'misprint', c[(p, True)])
