# SGA 5: hand replay of the last 33 fixes on the corrected layer

12 Nov 2026, Claude Opus 5.5 (effort high).

These are the 33 set-aside items: the 32 items of `REPLAY_MANUAL_5.json` that had no `resolved` key, and the one item of `MANUAL_5_findings_231_235.json`. Each was checked against its full finding in `run_5/findings_<A>_<B>.json`, against `MISPRINTS_5.json`, and against the passage in both layers between the folio's marker and the next one.

- Edits: `run_5/hand_replay_work/apply_hand_replay.py`. Each old string occurs exactly once in its page region. The file keeps LF line endings and UTF-8, the markers are unchanged, and the diplomatic layer is unchanged (byte-compared).
- Log: 24 lines appended to `HANDFIX_5.jsonl`, with t = 2026-11-12T16:29:09Z and by = "Claude Opus 5.5 (effort high), hand replay".
- Outcomes: `resolved` keys written by `run_5/hand_replay_work/resolve_items.py`. The files keep their structure: indent 1, UTF-8, CRLF line endings.
- Helper: `run_5/hand_replay_work/show_item.py` (item, finding, misprint records, both layers).

## Items

| # | Page | Kind | Outcome | Reason |
|---|---|---|---|---|
| R0 | 59 | punctuation | already | Current reads `\dim.\mathrm{top}_{\bar{x}}(K)$ la borne`, with no comma. |
| R1 | 105 | formula | already | Current reads `c_*c^!(…)` with no prime. |
| R2 | 105 | formula | apply | The prime was already gone. Restored the derived L: `d_*d^!(P\overset{\mathrm{L}}{\otimes} Q)`. |
| R3 | 85 | formula | apply | Current already has L, not 1. Only the form changed, `P\otimes^LL` to `P\overset{\mathrm{L}}{\otimes}L`, as the note asks. |
| R4 | 110 | font | apply | `\R` changed to plain R in `\Hom(Rf_{2*}A,Rf_{1*}A)`. The corrected index 2 is kept. |
| R5 | 128 | number | already | Current reads `6.8.3`. |
| R6 | 147 | symbol | apply | Current had v without its underline. Now `\underline{v}`. |
| R7 | 171 | underline | apply | `\uHom_A` changed to `\Hom_A`. The current layer's subscript A is kept. |
| R8 | 158 | formula | already | Current reads `q>1`. |
| R9 | 184 | punctuation | **open** | The corrected layer (from ref_c4) recasts the sentence, which leaves the printed comma no place (details below). |
| R10 | 190 | underline | apply | `\Hom_A`, `\Hom_B` with no underline. The corrected v (for the printed c) is kept. |
| R11 | 201 | underline | apply (adapted) | The corrected layer writes "la flèche horizontale supérieure" for "(1)". `\emph` on "où", "est la diagonale" and "est le produit tensoriel des flèches". |
| R12 | 201 | underline | apply (adapted) | "la flèche verticale \emph{est déduite … selon la diagonale}". |
| R13 | 201 | underline | apply (adapted) | "\emph{et} la flèche horizontale inférieure \emph{est composée de} 6.5.3 (\emph{définie car}". |
| R14 | 284 | font | apply | `\R_!^{2r}q` changed to `\mathrm{R}_!^{2r}q`. The corrected subscript ! is kept. |
| R15 | 289 | underline | apply | Statement underline in Cor. 2.2.6 set as `\emph`. The current layer's `A^*` is kept. |
| R16 | 308 | symbol | apply | `A^*` changed to `A^{\bullet}` twice. The corrected index p_i is kept. |
| R17 | 309 | word | apply | Current already reads "de l'anneau". Now `\emph{l'idéal de l'anneau de polynômes}`. |
| R18 | 309 | word | apply | `$j_i^{\text{ème}}$ \emph{fonction symétrique élémentaire des éléments}`. The corrected singular and j_i are kept. |
| R20 | 331 | formula | apply | (8.5.4) now reads `g^*[g_*(\cdot)]c_{d-1}(\check F)`: the print's brackets at the corrected place. |
| R21 | 323 | punctuation | apply (adapted) | Cor. 7.4 carries the accepted correction SGA-SRC-000366 (projective, ample, hyperplane section). The comma after n is gone, and `\emph` is set. |
| R22 | 323 | underline | apply (adapted) | `\emph{une section hyperplane lisse de} $X$, \emph{définie par une section d'un}`. |
| R23 | 323 | word | apply (adapted) | `-\emph{Module ample} $L$. \emph{Notant}`: the typescript's capital M. The corrected "ample" is kept. |
| R24 | 365 | font | apply | The first display had `\mathbf L\Phi`. Now `\underline{\underline{L}}^{-}\Phi`, as in the three places below it. |
| R25 | 367 | underline | apply | The proof label "Démonstration de la proposition 8.1." is now plain. The corrected 8.1 is kept. |
| R26 | 390 | symbol | already | Current reads `$Y'=p^{-1}(Y)$`. |
| R27 | 390 | punctuation | apply | "(3.2) l'homomorphisme trace:". The current layer's reference (3.2) is kept; the print has 3.3.1. |
| R31 | 427 | formula | already | Current reads `\nu_y(f)=1`. |
| R32 | 396 | underline | apply | Statement underline in Thm 7.1 set as `\emph`. The corrected reference 6.1 is kept. |
| R33 | 434 | formula | already | Current reads `\alpha_{x'}(f'/G_{x'}, v, f', G_{x'}, \varphi_{x'})`. |
| R34 | 402 | punctuation | apply | `$W$),` changed to `$W$)`. The corrected W (the print has S) is kept. |
| R35 | 466 | font | apply | Plain R for `\R`, three times. The current layer's corrected exponent form is kept. |
| M | 231 | extra | already | p. 230 reads `\emph{Preuve} :` and p. 231 has no `\end{prooftext}`. The paired fix is complete (6 `\begin{prooftext}` and 6 `\end{prooftext}`). |

(R = index in `REPLAY_MANUAL_5.json`; M = the item of `MANUAL_5_findings_231_235.json`.)

## Counts

| Outcome | Items |
|---|---|
| applied | 24 (of which 6 adapted to a reworded corrected text) |
| already | 8 |
| not applicable | 0 |
| open | 1 |
| total | 33 |

No item was a misprint that the corrected layer rightly corrects. The fixes that touch misprinted passages (R4, R7, R10, R16, R17, R18, R25, R32, R34) were applied around the corrected reading, which is kept.

## Open item

- **R9, p. 184, comma after "\])".** The print reads "(où … ), dont on déduit de (loc. cit.), comme en (III 1.6), qu'elle est un isomorphisme". The corrected layer, inherited from ref_c4, reads "où \[…\]. Il s'en déduit, comme en (III 1.6), qu'elle est un isomorphisme". It has no parenthesis, so the comma has no place, and it drops "de (loc. cit.)". No misprint record or Codex reconciliation entry covers this rewording. Restoring the printed sentence is an editorial decision.

## Other differences seen while checking (not changed)

- p. 289: the current layer writes `A^*` throughout §2.2.5–2.2.6, where the print and the diplomatic layer have `A^\bullet`. R16 now gives p. 308 `A^{\bullet}`.
- p. 390: the current layer cites "(3.2)" where the print has "(3.3.1)". This comes from ref_c4, and no record covers it.
- p. 201: the current layer replaces the labels (1), (2), (3) of Lemme 6.23.3 with "la flèche horizontale supérieure / verticale / horizontale inférieure". This comes from ref_c4.

## Compile check

The folder has no whole-volume compile script; `run_5/crops_*/compile_check.py` covers single batches only. The volume's other compile records use pdflatex, and `\pdftrailerid` in the preamble is pdfTeX-only. The check therefore ran `pdflatex -interaction=nonstopmode s5.tex` on a temporary copy of `sga5/current/s5.tex`, which is the master file. It ran once before the edits and once after:

| | Exit | `!` errors | Pages | Overfull boxes |
|---|---|---|---|---|
| before | 0 | 0 | 306 | 13 |
| after | 0 | 0 | 306 | 13 |
