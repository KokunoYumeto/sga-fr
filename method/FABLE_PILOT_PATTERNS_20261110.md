# SGA scan check: patterns across the records (10 November 2026)

Read in full: METHODOLOGY.md, GLOBAL_ISSUES_SGA.md (75 items), NOTE_5/6/7I/7II, the EXTRA notes in sga_api_batch.py,
FIXLOG_7I (708 lines), FIXLOG_7II (717), FIXLOG_5 (62), the pilot findings of SGA 5 and SGA 6 (pp. 1-5),
api_batches.jsonl. Counts marked **[T]** come from pattern counts over the diplomatic TeX files (comment lines
excluded), **[R]** from the records, **[S]** from a scan strip I looked at, **[G]** is a guess. Fix-log line numbers are
written #n. No file was changed.

## 1. 170 pages of SGA 7 were checked only over the API and are not on the re-check list [R]

METHODOLOGY §5 names the API pages to check again as 7 I pp. 251-270, 401-530 and 7 II pp. 266-285, 396-430; all of
those have a `_recheck.json`. api_batches.jsonl and items 56, 58, 61 show three more API batches whose pages have no
re-check file and no crops folder (only `_raw.txt` / `_coordinator.md`, the API form):

- **7 I pp. 276-310 and 316-350** (14 batches; Exposé VIII end, Exposé IX start);
- **7 II pp. 291-320 and 326-395** (20 batches; Exposés XVIII end to XXI).

The re-checks done so far added 41 fixes on 148 pages of 7 I (the API pass had found 66 there) and 95 on 55 pages of
7 II (API: 206). At those rates the unre-checked pages hold roughly 20 (7 I) and 60 (7 II) further fixes [G].
METHODOLOGY also says "32 API batches" for 7 I; the ledger has 44 for 7 I and 31 for 7 II.

## 2. SGA 5 and SGA 6 are transcriptions of the Exposé XXII kind, and their notes are written for the other kind

Exposé XXII of 7 II took 370 of the volume's 717 logged fixes in 38 pages: 9.7 per page,
against 0.5-1.7 for every other exposé of 7 I and 7 II [R]. Its TeX has a different fingerprint, and s5.tex and
SGA 6 main.tex share it [T] (occurrences per 10 kB):

| | `\operatorname` | `\mathbb F` unbraced | `% STRUCTURE` | `\underline{` | `\emph{` | displays as `\[` |
|---|---|---|---|---|---|---|
| 7 I, 7 II except XXII | 0-1.9 | 0 | 0-2.6 | 17-91 | 0-0.2 | 0-5 |
| 7 II Exposé XXII | 16.9 | 43.9 | 0 | 35.6 | 0 | 4.1 |
| SGA 5 | 3.7 | 8.7 | 0 | 3.5 | 1.7 | 21.8 |
| SGA 6 | 5.3 | 5.7 | 0 | 2.1 | 5.2 | 11.9 |

The first kind copies the page and leaves things out (punctuation after diagrams, Fraktur as `\mathcal`). The second
kind rewrites the page in modern LaTeX and **adds** things. What XXII's log shows for it, with the size of the same
feature in SGA 5 / SGA 6 [T]:

- commas and full stops added at the end of displays and of `cases` rows (most of XXII's 77 punctuation fixes):
  1,136 of 2,194 display ends carry punctuation in SGA 5, 1,302 of 2,042 in SGA 6;
- an index added to a bare sum, product or intersection sign (#392, 413, 414, 459, 482, 554, 591, 594, 670, 681-683):
  `\sum_` 135 / 272;
- `\pmod` for a printed "mod" without parentheses (item 66): 11 / 16;
- `\longmapsto` for a printed plain arrow (#347, 349), abbreviations written out (#402), words dropped or added
  (#426-494 passim), `\text{si }` rows: `\mapsto` 72 / 79;
- en dash in joint names (item 74): 22 / 98; guillemets for typewriter quotes: 40 / 252 (the SGA 6 pilot found both);
- statement text whose underline is missing (89 underline fixes in XXII).

NOTE_5 and NOTE_6 name none of these. They also lack the "report each" list of NOTE_7I/7II (punctuation after
diagrams, Fraktur as `\mathcal`: SGA 6 has 2,046 `\mathcal` and 67 `\mathfrak`). All of this needs the scan, page by
page; none is safe to script. The pilots gave 35 findings on SGA 6 pp. 1-5 and 13 on SGA 5 pp. 1-5 [R].
For the volumes not yet checked: run the fingerprint per file first; it predicts which error families and what
density to expect, and item 38 (7 II p. 204) shows that one file can hold a patch of the other kind.

## 3. The checkers do not see the macro definitions, and SGA 5/6 hide glyphs behind macros [T, R]

page_NNN.tex starts at the marker; the preamble is not in the prompt. FIXLOG_5 #8 changed `\R\,\underline{\Hom}` to
`\mathbb{R}\,\underline{\Hom}` with the note "the TeX writes the derived-functor R as roman \R everywhere", but
s5.tex defines `\newcommand{\R}{\mathbb{R}}`: the fix changes nothing in the output, and the same checker saw a plain
R in the print on p. 2 and left `\R` there. `\R` occurs 705 times in SGA 5 (127 pages). Other definitions a checker
cannot guess: `\D`, `\E`, `\H` upright; `\LL` = `\mathbf L`; in SGA 6 `\cF` = `\mathscr F`, `\eps` = `\varepsilon`,
`\K` = plain K, `\Gr`. Also `enumerate` with generated labels (98 lists in SGA 5, 136 in SGA 6): the printed label
of an item cannot be compared or reproduced (7 II had `(1)` for `(i)`, #12, #51).
To do: put the macro table into NOTE_5/NOTE_6 (or expand the macros in page_NNN.tex), and decide each font macro
once against the print.

The derived-functor letters need one decision per volume before more batches run: SGA 5 has `\R` (double-struck) 705
times but `\mathbf L` 269 times; SGA 6 has `\mathbf R` 35, plain `R` before `f_*`, `\Gamma`, `\Hom` 120, `\R` 7, and
`\mathbf L` 158. NOTE_5/6 say "double-struck Z, Q, F, C, A sometimes as `\mathbf`: do not report". That rule came from
7 I Exposé I; in SGA 5/6 there is no `\mathbf` Z, Q or F at all, the bold letters are L, R, P, f, n, so the rule
makes checkers skip 270 and 254 bold letters of another kind.

## 4. SGA 5 and SGA 6 are patchworks; a convention seen on five pages does not hold for the volume [T]

Inline mathematics switches between `$...$` and `\(...\)` in blocks (SGA 5: `\(` on pp. 226-300 only; SGA 6: `$` on
pp. 1-70 and 176-210, `\(` on pp. 71-140, 246-385 and 561-630, mixed elsewhere), and the other features move with
it: in SGA 5 `\underline` is on pp. 1-75 (278 of 294), `\mathbf` mostly on pp. 76-125 (225 of 272), and `\emph` is
nearly absent on pp. 151-275 (1 occurrence); in SGA 6 `\emph` falls from 40-100 per 35 pages to 3-11 on pp. 281-560. Guess: on those stretches the print's underlined emphasis was not
transcribed, and "underline missing" will be their main finding; decide beforehand whether each one is reported.
The exposés also had different typists, so label and punctuation habits are per exposé.
Concrete case: the `\emph{Preuve.}` → `\emph{Preuve} :` pass was decided on pp. 1-5 (Exposé I) and applied to the
whole file: the new form stands in 55 places, 41 of them in Exposé VII (pp. 283-347) [T]; NOTE_5 tells checkers not to report the form. The first checker of
Exposé VII should verify it. The same holds for "label underlined with its number": the SGA 5 print underlines
"Proposition 1.3." with the number [S, p. 4], while 7 II XXII underlines only the word (item 72).

## 5. Error families, and what a script may do

| Family (evidence) | Script? | SGA 5 / 6, later volumes |
|---|---|---|
| **Punctuation after a diagram left out** (7 I about 40 fixes, 7 II about 45). The transcriber's own STRUCTURE comment says so ("not included in the tikzcd", "omitted", "cannot be carried", "non représenté"). | Listing only: grep those phrases in comments, check each on the scan. In 7 I/7 II 8 hits remain: six are stale comments on diagrams already fixed (7 I VII p. 212, VIII p. 245; 7 II X p. 6, XIII p. 99, XIV p. 144 twice), one is the p. 397 case of §6.4, one is unrelated. | Not in SGA 5/6 (no such comments). Any volume with `% STRUCTURE`: grep first. |
| **Final `, . ; :` inside `\underline{}`** (item 12; 217 left in 7 I, 233 in 7 II). | Safe: `\underline{X[,.;:]}` → `\underline{X}[,.;:]`. Not inside mathematics; leave `...`. Every logged fix goes this way. | 2 / 0. |
| **Underline starting with the hyphen after a math letter** (items 17, 51; 14 + 22 left). | Not blind: four fixes made at the scan *write* this form (7 I #602; 7 II #261, #329, #330). Check the 36 places. | 0. |
| **Parenthesis or quotation mark inside the underline** (about 28 logged fixes, all move it out; left: opening 8 + 15, closing 9 + 10, quotes 6 + 3). | Listing, then check: `\underline{(`, `)}`, `\underline{"`, `` \underline{`` ``. Likely all to move. | 0. |
| **Math letters underlined with the words** (7 I IX, 7 II XXII, more than 100 fixes; left 39 + 22, of which 7 I VII 24). | Page by page (the typist sometimes underlines through). List: `\underline{[^{}$]*\$`. | 0. |
| **Look-alike glyphs, both directions in one exposé**: O / 0 / o (7 II XIV #86-89 against #125-129, #137, #139; 7 I IX pp. 357-358, 16 fixes; p. 505), Ψ / ψ (XV, 8), φ / ϕ (7 I Exp. I to `\phi`, 7 II XV to `\varphi`), ∧ / Λ, p / P (7 I VII-VIII, 23), Fraktur as `\mathcal` or `\mathbb` (7 I VI about 20, 7 II XIII-XIV about 30), b for ♭ (IX, 5), Fraktur J for I (XXI, 4), x for χ (XXII). | Never. A script can list, per exposé, the pages of the rarer variant of each pair. | Certain. SGA 6: `\epsilon` 66 / `\varepsilon` 30; degree dot `\bullet` 1,324 and `^\circ` 408 (SGA 5: 335 and 99). Items 15 and 70 are still open; decide the degree dot per volume now. |
| **A modern symbol for the printed one**: `\cong` for ≃ (#26, 137, 138), `\bigsqcup` for ∐ (#18, 150), `\xrightarrow{\sim}` for ≃ (7 I #633-638), ∼ for ≈ over an arrow (7 II #138, 141, 142), `\check{x}` for x^∨ (7 I #56, 7 II #36), ↔ for ⇔ (#139-141), label on the wrong side of a tikzcd arrow (7 I 10, nine of them in VI; 7 II about 18). | Listing by command name; fix at the scan. | SGA 5 / 6: `\xrightarrow{\sim}` 223 / 111, `\simeq` 142 / 141, `\cong` 0 / 3 (pp. 535, 537, 546). |
| **`\mathbf` for double-struck** (item 1). | Safe only as `\mathbf{[ZQF]}` in 7 I Exposé I (39 of the 40 left). Must not touch: 7 I IX p. 424 `\mathbf{C}` (written by a checker, #674), 7 II `\mathbf{x}` p. 182, `\mathbf R_B` p. 426, `\mathbf{P}` in XVII, and every `\mathbf` of SGA 5/6. | See §3. |
| **Misprints silently corrected**: accents, doubled letters, joined words, and parentheses balanced (7 II #33, 46, 47, 190, 275, 290, 295, 309, 318, 365, 469, 530). The TeX reads correctly, so a tired check passes over them. | Prose: word diff of the scan's OCR against the TeX (§7). Formulas: none. | Certain; SGA 6 pilot: 13 misprints on 5 pages, 3 of them silently corrected. |
| **Line-end hyphen kept in a word, running head typed as text, CONT tags, letter x for ×, `f*` for `f^*`**. | Exhausted: 0 hits left in 7 I/7 II, 0 in SGA 5/6 by pattern (one legitimate "co-niveau"). | Not expected in SGA 5/6. |

## 6. Inconsistencies in the records

1. **coîncident.** NOTE_7I/7II: "the TeX's ï stands" (item 33, p. 160 fix held). Yet the diplomatic layer has î in 7 I
   pp. 144, 145, 155 and 7 II pp. 2, 29, beside 13 + 9 ï [T]; four of the five were put there by logged misprint
   fixes (7 I #204 p. 145, #224 p. 155; 7 II #2, #23). The corrected layer has ï throughout.
2. **Plain letter where a double-struck one is meant: three treatments.** Font fix, both layers: 7 II #192, #195
   (A^{n+1}_S), #224, #226 (P^r). Misprint, diplomatic layer only: 7 I #682, #683 (Q_S, Q_ℓ), 7 II #212 (E), #667,
   #668, #674 (Q_p). Held: 7 II pp. 362, 384, 389 (item 61). Item 63 still lists pp. 416 and 418 as held; the
   re-check applied them.
3. **The typist's capital Lambda for ∧.** "Symbol" on 7 II p. 160 (#147) and p. 223 (#229); "misprint" on pp. 276-277
   (#631-633, corrected layer keeps `\wedge`); unchanged on p. 272 (item 71); the 7 II note says "report each with a fix".
4. **Punctuation on a line of its own after a diagram.** Item 49 treats it as a defect in 7 I (none left). In 7 II
   two fixes created it (#291 p. 345, #331 p. 397); six such lines stand in both layers (XIV 1, XX 2, XXI 3) [T].
5. **Dashes.** Joint names go from `--` to a hyphen (7 II #422, #640, #712; item 74), but #510 writes
   `CHEVALLEY--WARNING` in the same exposé. Number ranges keep `--` on 7 II p. 438 (#605, #608), while 7 I
   p. 526 changes a hyphen to `--` (#667) and 135 prices to `,--`. One rule is needed before SGA 6 (98 names, 22 ranges).
6. **`\pmod`.** Item 66: replace throughout XXII. Nine remain (pp. 410, 433, 434); #381, #383, #385 edited three of
   them and kept `\pmod` [T].
7. **First check and re-check read the same mark two ways**: 7 I p. 435 (#626 full stop, then #681 "misprint: comma"),
   p. 500 (#656, #695), 7 II p. 409 (#375, #659). The corrected layer keeps the first reading in each case.
8. **Passes decided but not run** [T]: base ring `\wedge` in 7 I VI (141 left, item 8); italic operator names in 7 I
   (about 66: I 14, VI 16, VII 11, VIII 22); italic ef/et/an/ab in IX (117); underlines through an inner comma
   (107 + 122, item 48); three labels underlined with their number (7 II XVII p. 217, XXII pp. 428, 430).

## 7. Other observations

- **A word diff of the scan's OCR against the TeX finds silent corrections cheaply.** ocr_5 and ocr_6 exist already
  (they placed the markers). On SGA 6 pp. 1-5 a diff of words of four letters or more gave 9 near-miss pairs; one is
  "haut | baut", the print's misprint that the TeX had corrected (found by the pilot checker at medium confidence);
  the others are line-end hyphens and OCR noise ("velable": the print has "valable" [S]). Given to the checker as
  "look here" hints, this is an independent witness for prose. ocr_5 is in another encoding (é read as S) and needs
  normalizing first.
- **Global items carry several topics under one number** (17, 26, 27, 34, 59, 61, 63), and decisions sit in three
  places (the item, the NOTE, EXTRA). The inconsistencies of §6 all come from a rule that reached one of them
  only. A table "convention, scope (exposé), rule for each layer, state of the pass" would hold it in one place.
- **A large share of the logged fixes are one convention applied place by place, not separate errors** [R]: in 7 II,
  162 underline and 135 punctuation fixes out of 717. For SGA 5/6 the degree dot,
  the derived-functor letters, the quotes, the dashes, missing emphasis and display punctuation are each several
  hundred to two thousand places; deciding them before the batches run decides the size of the job.
