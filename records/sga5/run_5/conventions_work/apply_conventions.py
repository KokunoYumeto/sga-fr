"""SGA 5 conventions pass (12 Nov 2026): Part 1 (four unrecorded rewordings of the
corrected layer) and Part 2 (volume-wide conventions).

usage:  python -I -X utf8 apply_conventions.py          dry run: counts and up to five examples
        python -I -X utf8 apply_conventions.py --apply  write both layers, append HANDFIX_5.jsonl

Every rule names its layers, its folio range and the exact number of matches expected
in each layer; the run stops if a count differs.  Page markers are compared before and
after (same lines, same order).  Files are read and written as UTF-8 with LF endings.
"""
import datetime
import json
import re
import sys

BS = chr(92)
ROOT = 'C:/Users/user/Documents/sga_scan_check_20261105/'
FILES = {L: ROOT + 'sga5/' + L + '/s5.tex' for L in ('diplomatic', 'current')}
HANDFIX = ROOT + 'HANDFIX_5.jsonl'
BY = 'Claude Opus 5.5 (effort high), conventions'
MARK = re.compile(r'^%{10}  scan idx \d+  \|  folio (\d+)  %{10}$', re.M)
BOTH = ('diplomatic', 'current')
CUR = ('current',)


def b(s):
    """Write TeX with '\\' as a single backslash: b('\\fr') == BS + 'fr'."""
    return s.replace('\\\\', BS)


def folio_span(text, a, z):
    """Character span from the marker of folio a to the marker after folio z."""
    ms = list(MARK.finditer(text))
    start = next(m.start() for m in ms if int(m.group(1)) == a)
    after = [m.start() for m in ms if int(m.group(1)) > z]
    return start, (after[0] if after else len(text))


# ---------------------------------------------------------------- replacements
# (id, item, layers, (folio a, folio z), regex?, old, new, expected {layer: n}, what)
R = []


def rule(rid, item, layers, span, old, new, n, what, regex=False):
    exp = n if isinstance(n, dict) else {L: n for L in layers}
    R.append(dict(id=rid, item=item, layers=layers, span=span, regex=regex,
                  old=old, new=new, n=exp, what=what))


# Part 1. Restore the print's wording in the corrected layer.
rule('P1-184', 'Part 1, p. 184', CUR, (184, 184),
     b("où\n\\\\[\nL_1\\\\lten_{S,A}L_2\n\\\\stackrel{\\\\mathrm{dfn}}{=}p_1^*L_1\\\\lten_Ap_2^*L_2.\n\\\\]\n"
       "Il s'en déduit, comme en (III 1.6), qu'elle est un isomorphisme."),
     b("(où\n\\\\[\nL_1\\\\lten_{S,A}L_2\n\\\\stackrel{\\\\mathrm{dfn}}{=}p_1^*L_1\\\\lten_Ap_2^*L_2\n\\\\]),\n"
       "dont on déduit de (loc. cit.), comme en (III 1.6), qu'elle est un isomorphisme."),
     1, "the print's '(où ... ), dont on déduit de (loc. cit.), comme en (III 1.6), qu'elle est un "
        "isomorphisme' restored for the ref_c4 rewording 'où ... . Il s'en déduit, comme en (III 1.6), ...'")
rule('P1-201a', 'Part 1, p. 201', CUR, (201, 201),
     b("\\\\emph{est la diagonale}, la flèche horizontale supérieure \\\\emph{est le produit tensoriel des flèches}"),
     b("\\\\emph{est la diagonale}, (1) \\\\emph{est produit tensoriel des flèches}"),
     1, "Lemme 6.23.3: the print's label (1) and 'est produit tensoriel' restored for the ref_c4 wording "
        "'la flèche horizontale supérieure est le produit tensoriel'")
rule('P1-201b', 'Part 1, p. 201', CUR, (201, 201),
     b("la flèche verticale \\\\emph{est déduite du produit tensoriel externe"),
     b("(2) \\\\emph{est la flèche déduite du produit tensoriel externe"),
     1, "Lemme 6.23.3: the print's '(2) est la flèche déduite' restored for 'la flèche verticale est déduite'")
rule('P1-201c', 'Part 1, p. 201', CUR, (201, 201),
     b("\\\\emph{et} la flèche horizontale inférieure \\\\emph{est composée de} 6.5.3"),
     b("\\\\emph{et} (3) \\\\emph{est composé de} 6.5.3"),
     1, "Lemme 6.23.3: the print's '(3) est composé de' restored for 'la flèche horizontale inférieure est composée de'")
rule('P1-390', 'Part 1, p. 390', CUR, (390, 390),
     b("K^*(\\\\mathbb Z_\\\\ell[G])\\\\xrightarrow{\\\\ tr\\\\ }"),
     b("K^{\\\\bullet}(\\\\mathbb Z_\\\\ell[G])\\\\xrightarrow{\\\\ tr\\\\ }"),
     1, "the print's K with a raised dot (K^\\bullet, as in the diplomatic layer and Prop. 3.2) restored for K^*; "
        "the corrected 'tr' (misprint record, print 'tv') kept. The reference (3.2) for the printed (3.3.1) is kept "
        "as a misprint correction, now recorded in MISPRINTS_5.json")
rule('P1-289', 'Part 1, p. 289', CUR, (289, 289), b("A^*("), b("A^\\\\bullet("), 7,
     "§2.2.5-2.2.6: the print's A with a raised dot (A^\\bullet, as the diplomatic layer and p. 308) restored "
     "for A^* (seven places); the corrected 'systématiquement' kept")
rule('P1-310', 'Part 1, p. 310 (same notation as p. 289)', CUR, (310, 310),
     b("A^*(S)[T_{i,j_i}]\\\\to A^*(S)[U_k]"), b("A^\\\\bullet(S)[T_{i,j_i}]\\\\to A^\\\\bullet(S)[U_k]"), 1,
     "the print's A^\\bullet restored for A^* twice; the corrected (S) of A^\\bullet(S)[U_k] (misprint record) kept")

# Part 2, Exposé XII.
rule('XII-H', 'XII script H', BOTH, (407, 441),
     r'(?<![A-Za-z\\])H(?=(?:\^\\vee)?_\{(?:n,|m,|U\'))', b("\\\\mathcal{H}"),
     {'diplomatic': None, 'current': None},
     "the print's hand-drawn script H of H_{n,U',X'}, H_{m,U',X'}, H_{U',X'}(\\ell) and their duals: "
     "H -> \\mathcal{H} (as pp. 425 and 433 already had)", regex=True)
rule('XII-4.7a', 'XII Lemme 4.7', CUR, (417, 417), b("A/\\\\fm^r"), b("R/\\\\fm^r"), 2,
     "Lemme 4.7 a): the ring is R (misprint record, print A); corrected layer, all five places")
rule('XII-4.7b', 'XII Lemme 4.7', CUR, (417, 417), b("A/\\\\fm^{r+1}"), b("R/\\\\fm^{r+1}"), 2,
     "Lemme 4.7 b): the ring is R (misprint record, print A); corrected layer, all five places")
rule('XII-4.7c', 'XII Lemme 4.7', CUR, (420, 420), b("des fractions de $A$"), b("des fractions de $R$"), 1,
     "Lemme 4.7, proof: 'le corps K des fractions de R' (misprint record, print A); corrected layer, all five places")
rule('XII-441fr', 'XII Exemple 7.3 underline', BOTH, (441, 441), b("\\\\underline{\\\\fr}_X"), b("\\\\fr_X"), 1,
     "Exemple 7.3: the explicit underline of the first fr_X removed; the local \\fr/\\Fr of p. 441 now underline every fr and Fr")
rule('XII-441Fr', 'XII Exemple 7.3 underline', ('diplomatic',), (441, 441),
     b("\\\\operatorname{\\\\mathbb{F}r}_{Y/S}"), b("\\\\underline{\\\\operatorname{\\\\mathbb{F}r}}_{Y/S}"), 1,
     "Exemple 7.3: the printed underline of Fr_{Y/S} (written out, the diplomatic layer keeps the typed 𝔽)")

# Part 2, Exposés XIV-XV.
rule('XV-442', 'XV fr/Fr', BOTH, (442, 442), b("\\\\underline{\\\\underline{\\\\fr}}_X"), b("\\\\fr_X"), 1,
     "p. 442: explicit double underline of fr_X removed (the local \\fr of Exposé XV now gives it)")
rule('XV-443', 'XV fr/Fr', BOTH, (443, 443), b("Frobenius $\\\\fr_X$ dépend"),
     b("Frobenius $\\\\operatorname{fr}_X$ dépend"), 1,
     "p. 443 'L'endomorphisme de Frobenius fr_X dépend': printed without underline, kept plain")
rule('XV-456', 'XV fr/Fr', BOTH, (456, 456), b("alors $\\\\Fr^*_{F/X}$ est"),
     b("alors $\\\\operatorname{Fr}^*_{F/X}$ est"), 1,
     "p. 456 'alors Fr*_{F/X} est un isomorphisme': printed without underline, kept plain")
rule('XV-460', 'XV fr/Fr', BOTH, (460, 460), b("=(\\\\fr_X\\\\times\\\\id_{X'})\\\\circ"),
     b("=(\\\\operatorname{fr}_X\\\\times\\\\id_{X'})\\\\circ"), 1,
     "p. 460 'fr_{XxX'} = (fr_X x id_{X'}) o (...)': the first fr_X printed without underline, kept plain")
rule('XV-447', 'XV underlined Omega', BOTH, (447, 447), r'\\Omega\^1', b("\\\\underline{\\\\Omega}^1"), 6,
     "p. 447: the print underlines the Omega of the differentials Omega^1 (six places)", regex=True)

# Whole volume: the isomorphism sign (GLOBAL_ISSUES 78: typist glyph variants are not reproduced).
rule('iso-429', 'isomorphism sign', BOTH, (429, 429), b(" \\\\approx "), b(" \\\\simeq "), 2,
     "the typed two-tilde isomorphism sign: \\simeq stands (GLOBAL_ISSUES 78, 96); itemized \\approx set back")
rule('iso-432', 'isomorphism sign', BOTH, (432, 432), b("F_{U',X'}\\\\approx "), b("F_{U',X'}\\\\simeq "), 1,
     "the typed two-tilde isomorphism sign: \\simeq stands (GLOBAL_ISSUES 78, 96); itemized \\approx set back")

# ---------------------------------------------------------------- insertions
# (id, item, anchor kind, anchor, text, what); kinds: 'after_line' (exact line), 'before_marker' (folio)
INS = [
    ('VIII-start', 'Ob VIII', 'after_line', b("\\\\section*{Exposé VIII}"),
     b("% Exposé VIII prints 'Ob' (GLOBAL_ISSUES, 12 Nov; conventions pass)\n\\\\renewcommand{\\\\Ob}{\\\\operatorname{Ob}}"),
     "\\Ob redefined as \\operatorname{Ob} for Exposé VIII (decision of 12 Nov, GLOBAL_ISSUES last bullet)"),
    ('VIII-end', 'Ob VIII', 'before_marker', 372,
     b("% End of Exposé VIII: back to the volume's \\\\Ob\n\\\\renewcommand{\\\\Ob}{\\\\operatorname{ob}}\n"),
     "end of Exposé VIII: \\Ob back to \\operatorname{ob}"),
    ('X-start', 'EP and Ob X', 'after_line', b("\\\\section*{Exposé X}"),
     b("% Exposé X prints EP double-struck and 'Ob' (conventions pass, 12 Nov; GLOBAL_ISSUES 96)\n"
       "\\\\renewcommand{\\\\EP}{\\\\operatorname{\\\\mathbb{EP}}}\n\\\\renewcommand{\\\\Ob}{\\\\operatorname{Ob}}"),
     "\\EP redefined as \\operatorname{\\mathbb{EP}} and \\Ob as \\operatorname{Ob} for Exposé X"),
    ('X-end', 'EP and Ob X', 'before_marker', 407,
     b("% End of Exposé X: back to the volume's \\\\EP and \\\\Ob\n"
       "\\\\renewcommand{\\\\EP}{\\\\operatorname{EP}}\n\\\\renewcommand{\\\\Ob}{\\\\operatorname{ob}}\n"),
     "end of Exposé X: \\EP and \\Ob back to the volume's definitions"),
    ('XII-441', 'XII Exemple 7.3 underline', 'after_marker', 441,
     b("% Exemple 7.3 underlines fr and Fr once (conventions pass, 12 Nov; GLOBAL_ISSUES 98)\n"
       "\\\\renewcommand{\\\\fr}{\\\\underline{\\\\operatorname{fr}}}\\\\renewcommand{\\\\Fr}{\\\\underline{\\\\operatorname{Fr}}}"),
     "\\fr and \\Fr singly underlined for Exemple 7.3 (p. 441, end of Exposé XII)"),
    ('XV-start', 'XV fr/Fr', 'after_line', b("\\\\section*{EXPOSÉ XV}"),
     b("% Exposés XIV-XV underline fr and Fr twice (conventions pass, 12 Nov; GLOBAL_ISSUES 98)\n"
       "\\\\renewcommand{\\\\fr}{\\\\underline{\\\\underline{\\\\operatorname{fr}}}}"
       "\\\\renewcommand{\\\\Fr}{\\\\underline{\\\\underline{\\\\operatorname{Fr}}}}"),
     "\\fr and \\Fr doubly underlined for Exposés XIV-XV"),
    ('XV-end', 'XV fr/Fr', 'before_marker', 481,
     b("% End of Exposés XIV-XV: back to the volume's \\\\fr and \\\\Fr\n"
       "\\\\renewcommand{\\\\fr}{\\\\operatorname{fr}}\\\\renewcommand{\\\\Fr}{\\\\operatorname{Fr}}\n"),
     "end of Exposés XIV-XV: \\fr and \\Fr back to plain \\operatorname"),
]


def markers(text):
    return [m.group(0) for m in MARK.finditer(text)]


def page_of(text, pos):
    f = None
    for m in MARK.finditer(text):
        if m.start() > pos:
            break
        f = int(m.group(1))
    return f


def run(apply):
    texts = {L: open(FILES[L], encoding='utf-8', newline='').read() for L in BOTH}
    for L in BOTH:
        assert '\r' not in texts[L], L + ' has CR'
    before_marks = {L: markers(texts[L]) for L in BOTH}
    log = []
    t = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    ok = True
    for r in R:
        for L in r['layers']:
            s = texts[L]
            a, z = folio_span(s, *r['span'])
            seg = s[a:z]
            if r['regex']:
                hits = list(re.finditer(r['old'], seg))
                n = len(hits)
                new_seg = re.sub(r['old'], lambda m: r['new'], seg)
                ex = [seg[max(0, h.start() - 30):h.end() + 30].replace('\n', ' ') for h in hits[:5]]
            else:
                n = seg.count(r['old'])
                new_seg = seg.replace(r['old'], r['new'])
                ex = [r['old'][:120].replace('\n', ' ') + '  ->  ' + r['new'][:120].replace('\n', ' ')]
            want = r['n'][L]
            flag = '' if (want is None or n == want) else '   <<< EXPECTED %s' % want
            if flag:
                ok = False
            print(f"[{r['id']}] {L} folios {r['span'][0]}-{r['span'][1]}: {n} match(es){flag}")
            for e in ex:
                print('      ', e)
            if apply and n:
                texts[L] = s[:a] + new_seg + s[z:]
                pages = sorted({page_of(s, a + h.start()) for h in re.finditer(
                    r['old'] if r['regex'] else re.escape(r['old']), seg)})
                rec = {'t': t, 'vol': '5'}
                rec.update({'page': pages[0]} if len(pages) == 1 else {'pages': pages})
                rec.update({'file': FILES[L], 'old': r['old'] if not r['regex'] else 'regex ' + r['old'],
                            'new': r['new'], 'count': n, 'what': r['what'],
                            'source': 'CONVENTIONS_5_REPORT.md (' + r['item'] + ')', 'by': BY})
                log.append(rec)
    for iid, item, kind, anchor, text, what in INS:
        for L in BOTH:
            s = texts[L]
            if kind == 'after_line':
                assert s.count('\n' + anchor + '\n') == 1, (iid, L)
                pos = s.index('\n' + anchor + '\n') + len(anchor) + 2
                new = text + '\n'
            elif kind == 'after_marker':
                m = [m for m in MARK.finditer(s) if int(m.group(1)) == anchor]
                assert len(m) == 1, (iid, L)
                pos = m[0].end() + 1
                new = text + '\n'
            else:
                m = [m for m in MARK.finditer(s) if int(m.group(1)) == anchor]
                assert len(m) == 1, (iid, L)
                pos = m[0].start()
                new = text
            print(f'[{iid}] {L}: insert at char {pos} (line {s[:pos].count(chr(10)) + 1}):')
            for ln in new.rstrip('\n').split('\n'):
                print('       +', ln)
            if apply:
                texts[L] = s[:pos] + new + s[pos:]
                log.append({'t': t, 'vol': '5', 'page': page_of(texts[L], pos), 'file': FILES[L],
                            'line': texts[L][:pos].count('\n') + 1, 'inserted': new.rstrip('\n'),
                            'what': what, 'source': 'CONVENTIONS_5_REPORT.md (' + item + ')', 'by': BY})
    if not ok:
        sys.exit('counts differ: nothing written')
    for L in BOTH:
        assert markers(texts[L]) == before_marks[L], 'markers changed in ' + L
    if apply:
        for L in BOTH:
            with open(FILES[L], 'w', encoding='utf-8', newline='\n') as f:
                f.write(texts[L])
        with open(HANDFIX, 'a', encoding='utf-8', newline='\n') as f:
            for rec in log:
                f.write(json.dumps(rec, ensure_ascii=False) + '\n')
        print(f'written; {len(log)} lines appended to HANDFIX_5.jsonl')


if __name__ == '__main__':
    run('--apply' in sys.argv)
