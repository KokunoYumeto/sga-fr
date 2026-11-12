# SGA 5: the volume-wide conventions, and four unrecorded rewordings

12 Nov 2026, Claude Opus 5.5 (effort high).

- Edits: `run_5/conventions_work/apply_conventions.py`. Each rule names its layers, its folio range and the exact number of matches expected per layer; the dry run printed every count with up to five examples before anything was written. The script keeps UTF-8 and LF, and it checks that the page markers are the same lines in the same order before and after.
- Log: 44 lines appended to `HANDFIX_5.jsonl` (43 from the script, one for the p. 390 record), by = "Claude Opus 5.5 (effort high), conventions".
- Records: one misprint added to `MISPRINTS_5.json` (p. 390, format kept: indent 1, CRLF); five items of `REVIEW_5_OPEN.jsonl` given a status; GLOBAL_ISSUES items 96-100.
- Scans checked for this pass: pp. 184, 201, 390, 392, 401, 410, 426 (crop), 432, 441, 443, 447, 448 (crop), 456, 457, 458, 460, 461, 470 (crops), and p. 69.

## Part 1. The four rewordings of the corrected layer

| Page | What the corrected layer had (from ref_c4) | Done |
|---|---|---|
| 184 | « où \[…\]. Il s'en déduit, comme en (III 1.6), … » | Restored the print: « (où \[…\]), dont on déduit de (loc. cit.), comme en (III 1.6), qu'elle est un isomorphisme ». The display has no full stop, as in the print. The recorded misprints of the page are unchanged: the stray full stop after « 5.4.2 » stays corrected. The printed `X_{2B}` stays as it is in this layer. |
| 201 | « la flèche horizontale supérieure / verticale / horizontale inférieure » | Restored the print's labels and words: « (1) est produit tensoriel des flèches », « (2) est la flèche déduite … », « (3) est composé de 6.5.3 ». The recorded misprint « (cf. (SGA » stays corrected. |
| 390 | « (3.2) » where the print has « (3.3.1) » | **Not restored; recorded as a misprint instead.** The proof needs the injectivity of the trace homomorphism K°(Z_ℓ[G]) → F(G,Z_ℓ). That is Proposition 3.2 (p. 377). (3.3.1) is the formula for the induced character (p. 378). So the print's reference is wrong, and ref_c4's (3.2) corrects it. The gap was the missing record, which is now added to `MISPRINTS_5.json`. On the same page, `K^*` was a notation change and is now `K^{\bullet}`, as the print has it; the recorded correction « tr » (the print has « tv ») is kept. |
| 289 | `A^*` in §2.2.5–2.2.6 | `A^\bullet` restored in all seven places. The same change was needed twice on p. 310 (`A^\bullet(S)[T_{i,j_i}] → A^\bullet(S)[U_k]`), where the recorded correction (S) is kept. No `A^*` is left in Exposé VII. |

The p. 323 correction SGA-SRC-000366 is unchanged. After the pass, the two layers of pp. 184, 201, 289, 310 and 390 differ only by recorded misprints.

## Part 2. The conventions

### Exposé X
- **EP, double-struck in the print:** applied. This is decided by the rule for the print's double-struck letters (GLOBAL item 1; NOTE_5). A local `\renewcommand{\EP}{\operatorname{\mathbb{EP}}}` is set at the head of Exposé X and ended at its end, in both layers. It covers 26 uses. The `\EP` of p. 111 (Exposé III) is untouched.
- **`\Ob` printed « ob »:** applied. This follows the decision of 12 Nov for Exposé VIII (the last bullet of GLOBAL_ISSUES). A local `\renewcommand{\Ob}{\operatorname{Ob}}` is set for Exposé X (16 `\Ob` in the diplomatic layer, 17 in the corrected one) and ended at its end, in both layers. That decision had not been carried out for Exposé VIII either, so the same local definition is set there (19 `\Ob`).
- **Plain R on pp. 391–400:** nothing left to do. The batches had itemized every place. The two `\RG` that remain (pp. 391, 392) are the print's double-struck R, checked on the scan of p. 392.

### Exposé XII
- **Script ℋ:** applied. This was not decided before and is now GLOBAL item 97. H becomes `\mathcal{H}` in H_{n,U',X'}, H_{m,U',X'}, H_{U',X'}(ℓ) and their duals: 45 places per layer, on pp. 408–432. The volume writes hand-drawn script letters as `\mathcal`, and pp. 425 and 433 already did so. The scans of pp. 410, 426 and 432 were checked. The H of the Galois group on p. 440 is unchanged.
- **Card in §4:** nothing left to do. All ten places were itemized and applied before this pass. No use of `\card` is left in the volume, so no redefinition was needed. The lower-case « card » on pp. 69, 393 (three times) and 401 is lower-case in the print (scans of pp. 69 and 401; the checker of p. 393).
- **Lemme 4.7, A for R:** all five corrected in the corrected layer (pp. 417, 420); the diplomatic layer keeps A. A is defined nowhere in §4. Proposition 4.6 and the rest of the proof use R, and the misprint records give R. This is GLOBAL item 99.
- **Exemple 7.3 (p. 441):** the print underlines every fr and Fr once. The checker of pp. 441–445 had filed this as a convention entry and left it open. From the folio-441 marker on, `\fr` and `\Fr` are singly underlined, in both layers. The one explicit `\underline{\fr}_X` was removed, and in the diplomatic layer the written-out `\operatorname{\mathbb{F}r}_{Y/S}` was underlined.

### Exposés XIV–XV
- **fr and Fr, double underline:** applied. This was not decided before and is now GLOBAL item 98. Double-underlined letters are written `\underline{\underline{…}}`, as the volume already writes the L of pp. 37 and 365. From the head of Exposé XV to the end of p. 480, `\fr` and `\Fr` are redefined in both layers, about 295 uses. The explicit double underline of p. 442 was removed. Three places stay plain as `\operatorname`: the two the brief named (p. 456 « alors Fr*_{F/X} », p. 460 « (fr_X × id_{X'}) ») and a third on p. 443 (« L'endomorphisme de Frobenius fr_X dépend »). The checker had noted the third, and I confirmed it on the scan. The scans of pp. 457, 458, 460 and 461 confirm the double underline elsewhere.
- **Checked whether the remaining pages need the batches' fixes:**
  - The § headings: all three are in capitals.
  - The R of R^i_!: none is left in `\R` form.
  - Underlined statements: every statement of the exposé has `\emph`; the Remarque of p. 474 is not underlined.
  - « (resp. …) »: the one « respectivement » left (p. 459, « définis respectivement par ») was not reported by its checker and was left.
  - Squiggly arrows: no `\mapsto` or `\longmapsto` is left in the exposé.
- **Underlined Ω on p. 447:** this had **not** been itemized, although the brief said it had. The scan shows all six Ω^1 of the differentials underlined. They are now `\underline{\Omega}^1` in both layers.
- **Left open (GLOBAL item 98):** the R of RΓ in Exposé XV. The print double-underlines it on most pages (pp. 457, 458, 460, 461) but prints a plain R in some places (p. 461 « RΓ défini », already `\mathrm{R}`; p. 460, the lower node). The TeX's `\RGamma` gives ℝ in the diplomatic layer and a plain R in the corrected one, in 32 places on pp. 457–474. The scans do not settle a single rule without a page-by-page look.

### Whole volume
- **≈ for the isomorphism sign:** decided by GLOBAL item 78, so `\simeq` stands. The typescript types ≈ with two tildes on some pages (p. 432) and draws ≃ on others (p. 448). The reading is the same, so it is a typist's glyph variant, which the layers do not reproduce. Earlier batches had itemized three `\approx` (p. 429 twice, p. 432), and these are set back to `\simeq` in both layers. Left as they are: `\xrightarrow{\approx}` on p. 9 (three arrows) and `\approxeq` on p. 357.
- **p. 435:** nothing added to the text. It is recorded as a defect of the print in GLOBAL item 100.

## New GLOBAL_ISSUES items

- **96.** Decisions already taken and now applied: `\Ob` in Exposés VIII and X, EP in Exposé X, ≈ under item 78, Card in XII §4, and the R of Exposé X.
- **97.** Exposé XII: the script ℋ is written `\mathcal{H}`.
- **98.** fr and Fr: a double underline in XIV–XV and a single one in XII 7.3, with the three plain exceptions; the underlined Ω on p. 447. Open: the R of RΓ in Exposé XV, and the typed 𝔽 in Fr_{Y/S} on p. 441 that the diplomatic layer reproduces against item 78.
- **99.** Lemme 4.7: A becomes R in the corrected layer, all five places.
- **100.** p. 435 is a second printing of p. 434, a defect of the print.

## Compile

`pdflatex -interaction=nonstopmode` was run on temporary copies of `sga5/<layer>/s5.tex` in the session scratchpad (`run_5/conventions_work/compile_layers.py`):

| | Exit | `!` errors | Pages | Overfull hbox |
|---|---|---|---|---|
| diplomatic, before | 0 | 0 | 306 | 14 |
| diplomatic, after | 0 | 0 | 307 | 14 |
| current, before | 0 | 0 | 306 | 13 |
| current, after | 0 | 0 | 307 | 13 |

The extra page comes from the double underlines of Exposé XV, which deepen its lines. I checked the PDF pages of Corollaire 7.12 (double-struck EP, « Ob »), Exemple 7.3 (single underline) and Proposition 2 of XV (double underline, with « alors Fr*_{F/X} » plain).
