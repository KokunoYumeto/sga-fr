"""Write the conventions pass's decisions into REVIEW_5_OPEN.jsonl (CRLF kept, one JSON object per line)."""
import json

P = 'C:/Users/user/Documents/sga_scan_check_20261105/REVIEW_5_OPEN.jsonl'
raw = open(P, 'rb').read().decode('utf-8')
lines = raw.split('\r\n')
assert lines[-1] == ''
DEC = {
    'Lemme 4.7 proof calls the ring A':
        'decided (12 Nov 2026, conventions pass, Claude Opus 5.5 high): all five corrected to R in the corrected '
        'layer; diplomatic keeps A (GLOBAL_ISSUES 99, HANDFIX_5.jsonl)',
    'The print types Card where':
        'closed (12 Nov 2026, conventions pass): all ten Card of XII section 4 were already \\operatorname{Card}; '
        'no \\card use left; card on pp. 69, 393, 401 is lower-case in the print (GLOBAL_ISSUES 96 d)',
    'Expose XII: the print has a hand-drawn script H':
        'applied (12 Nov 2026, conventions pass): 45 H -> \\mathcal{H} per layer on pp. 408-432 (GLOBAL_ISSUES 97)',
    'Printed p. 435 (scan idx 446) repeats p. 434':
        'decided (12 Nov 2026, conventions pass): recorded as a print defect in GLOBAL_ISSUES 100; no marker or text added',
    'The print types the isomorphism sign as':
        'decided (12 Nov 2026, conventions pass): a typist glyph variant (item 78): \\simeq stands in both layers; '
        'the itemized \\approx of pp. 429 (2) and 432 (1) set back to \\simeq (GLOBAL_ISSUES 96 c)',
}
out = []
done = 0
for ln in lines[:-1]:
    d = json.loads(ln)
    if '\x07pprox' in d.get('what', ''):  # a '\a' of '\approx' read as BEL when the line was written
        d['what'] = d['what'].replace('\x07pprox', '\\approx')
    for key, dec in DEC.items():
        if d.get('what', '').startswith(key):
            d['status'] = dec
            done += 1
    out.append(json.dumps(d, ensure_ascii=False))
assert done == len(DEC), done
open(P, 'wb').write(('\r\n'.join(out) + '\r\n').encode('utf-8'))
print('updated', done)
