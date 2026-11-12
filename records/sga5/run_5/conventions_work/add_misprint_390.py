"""Add the misprint record of p. 390 '(3.3.1)' for '(3.2)' to MISPRINTS_5.json (conventions pass, 12 Nov 2026).
The file's format is kept: a JSON list, indent 1, CRLF line endings; the script first checks that
re-serializing the unchanged list reproduces the file byte for byte."""
import json

P = 'C:/Users/user/Documents/sga_scan_check_20261105/MISPRINTS_5.json'
raw = open(P, 'rb').read()
d = json.loads(raw.decode('utf-8'))
for ea in (False, True):
    again = json.dumps(d, ensure_ascii=ea, indent=1).replace('\n', '\r\n').encode('utf-8')
    if again == raw or again + b'\r\n' == raw:
        break
else:
    raise SystemExit('format not reproduced; nothing written')
tail = b'\r\n' if again + b'\r\n' == raw else b''
assert not any(x.get('page') == 390 and '3.3.1' in x.get('print', '') for x in d), 'already recorded'
d.append({
    "vol": "5",
    "page": 390,
    "where": "proof of Proposition 5.1, 'D'autre part (3.3.1) l'homomorphisme trace : K°(Z_ℓ[G]) --tv--> F(G,Z_ℓ) est un monomorphisme'",
    "print": "(3.3.1), clearly typed",
    "correct": "D'autre part (3.2) l'homomorphisme trace:",
    "tex_did": "the diplomatic layer keeps the printed (3.3.1); the corrected layer (from ref_c4) reads (3.2)",
    "note": "Wrong reference: the trace homomorphism K°(Z_ℓ[G]) -> F(G,Z_ℓ) is a monomorphism by Proposition 3.2 (p. 377); (3.3.1) is the formula of the induced character (p. 378), which the proof does not use here. The corrected layer's (3.2), inherited from ref_c4 without a record, is this correction. Recorded in the conventions pass of 12 Nov 2026 (HAND_REPLAY_5_REPORT.md, 'Other differences'; CONVENTIONS_5_REPORT.md).",
    "source": "CONVENTIONS_5_REPORT.md"
})
out = json.dumps(d, ensure_ascii=ea, indent=1).replace('\n', '\r\n').encode('utf-8') + tail
open(P, 'wb').write(out)
print('records:', len(d), 'ensure_ascii:', ea, 'trailing newline:', bool(tail))
