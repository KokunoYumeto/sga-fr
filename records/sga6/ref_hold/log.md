# SGA6 corrected French log

## Scope

This no-overwrite successor owns the corrected French SGA6 edition only. It is not a bilingual reader and it is not the separately required diplomatic French edition.

The starting source is the completed pagewise workpass formerly maintained at `sga6_full_audit_20260703`. It covers the French mathematical body through scan index 702 and includes the terminological and notation indexes through scan index 713. Commercial publisher advertisements at indices 716--719 are outside the mathematical edition. The preserved inherited audit ledger records the direct pagewise source comparison and every earlier reversal.

## Immutable inputs

- Authority: `Théorie des Intersections et Théorème de Riemann-Roch.pdf`, 720 physical pages, 26,833,956 bytes, SHA-256 `73FBBAD41340C12ECCDCFCF6C3A1656953FE3D712AA8E391678458CCD17B4BAA`.
- Inherited corrected source: 1,320,486 bytes, SHA-256 `2B9CFBD3FC833B77F91D9F714A8A864A9CF9BE62097588B34A0F921479922F52`.
- Inherited reader: 373 pages, 2,873,452 bytes, SHA-256 `25D3AD8A45ED9FFCB39520904990A06302D812EBF459A979616D19042105C05D`.
- The exact inherited decision history is preserved as `hist/cert.md`, `hist/errata.md`, and `hist/index.md`.

## Current gate

Before freezing this successor, resolve the eleven explicitly open index reports against the scan at 1100 dpi minimum, escalating narrow ambiguous glyphs to 5000--9000 dpi; rebuild; inspect every affected page; and record every accepted, rejected, or superseded reading. Preserve source-visible typographical defects in the diplomatic edition later, rather than silently conflating diplomatic and corrected surfaces.

## Process correction

- The first PowerShell existence probe used a pipeline directly after a `foreach` block and failed to parse. It made no filesystem change. The retry accumulated rows before piping them and succeeded. This is process history only.
- The first corrected-reader build invocation passed `-output-directory=$build` to the native TeX executable without quoting the complete argument. PowerShell therefore produced a literal workspace-root `$build` scratch directory. The TeX pass itself exited zero and produced 373 pages, but those scratch bytes were non-adjudicative; the exact directory was deleted immediately after its resolved path was checked. Subsequent passes use a fully quoted output-directory argument.
- The first reader-render invocation selected the bundled workspace Python, which lacks PyMuPDF/`fitz`, and failed before creating any image. The retry uses the already-configured Miniconda Python whose PyMuPDF import was verified first.
- One combined validation probe returned process exit 1 solely because its final optional `Get-Command qpdf` lookup found no qpdf executable. All preceding TeX, text, and image-object checks in that probe completed and passed. The link check was then run separately with PyMuPDF and found 93 named internal links with zero broken targets.
- The first public-projection privacy scan passed the literal Windows prefix `C:\Users\` to `Select-String` as a regular expression, which made `\U` an invalid escape. The scan made no change and was rerun with literal/simple matching.

## Index and bibliography adjudication — 2026-08-05

All eleven inherited ambiguity reports were resolved directly against the authority. Whole-page index context was reviewed at 1100 dpi. Small or ambiguous notation was re-rendered as narrow 5000-dpi crops; no 9000-dpi escalation remained necessary. The exact dispositions and evidence bindings are in `decisions.csv`.

Accepted source-backed repairs:

- restore the left-subscript and underlined-object structure in the four derived-category index entries;
- restore `|underlined F|`, `Filt_n`, underlined `Hom_M`, `Proj_0`, and the six complete widehat-G symbols;
- reproduce the visible spacing in the index entry `Loc lib(U)` without rewriting the body-wide compact convention;
- correct bibliography item [17] from the corrupt printed `U. Mausin / MAt. Sborik` to `Yu. I. Manin / Mat. Sbornik`. The edition's own endnote and the primary MathNet bibliographic record independently identify Manin; this correction belongs only to the corrected edition.

Retained readings/conventions:

- `K'` and `Gr'` remain primes. Although the index glyph is dot-like even at 5000 dpi, the earlier 6000-dpi body comparison identifies the prime and the notation is structurally consistent throughout the source.
- `naïf` already renders correctly because its earlier effective macro contains the diaeresis; the later fallback definition is inert.
- there is no wholesale conversion of semantic TeX notation into literal source underlining. Underlines are restored only where the source uses them to distinguish mathematical objects.

The first corrected build also exposed four accent warnings caused by direct diaeresis spellings of `naïf` inside math mode. Three source sites were changed to the already-defined `naif` semantic macro. This preserves the visible French word and mathematical meaning while removing all four warnings; decision `SGA6-BLD-001` records the exact rationale.

The rebuilt bibliography and notation-index pages were reviewed at 600-dpi layout context and in bounded 1100-dpi detail. Every changed entry is legible, remains inside its table cell or paragraph envelope, and agrees with the adjudicated notation. No clipping, collision, or unintended page-count change was found.

## Translation as correction evidence

Translation is treated as a substantive independent correction pass, not as mere downstream formatting. Re-expression in another language repeatedly exposes unbound variables, ill-typed maps, reversed arrows, missing hypotheses, and grammatical ambiguities that can remain visually plausible in transcription. A translation witness never overrides the French authority by itself: every accepted French correction must still be tied to the scan, internal mathematical typing, an independent bibliographic source, or an explicit counterexample. The translation therefore adds an additional quality-assurance channel while the diplomatic French edition preserves every printed reading reversibly.
## 2026-08-05 — retrospective source-layer failure and fail-close

After the first local package had been built, a record-by-record parse of `hist/errata.md` found 39 `[corrected]` records covering 40 atomic source occurrences. The historical narrative does not bind those decisions to deterministic source offsets or context hashes. Direct inspection then showed that `main.tex` is mixed: many printed adverse readings remain, while other recorded corrections have already been applied.

This invalidates the semantic claim “complete corrected French edition” without invalidating the proven build, link, font, raster, visual-surface, or privacy checks. The unpublished candidate was fail-closed before Zenodo publication and preserved as adverse history. No blanket reversal was attempted because it would corrupt entries already in the printed state; no blanket correction was attempted because exact per-occurrence provenance is still being materialized.

Required repair: create an exact occurrence ledger, classify each row against the current source, and build separate diplomatic and corrected successors with one-match/context-hash assertions and independent replay. `HOLD.md` supersedes the earlier corrected-edition PASS claim.
