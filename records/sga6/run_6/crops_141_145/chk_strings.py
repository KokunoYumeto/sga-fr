import tokenize
BS = chr(92)
with open('make_findings.py', 'rb') as f:
    for tok in tokenize.tokenize(f.readline):
        if tok.type == tokenize.STRING:
            s = tok.string
            i = 0
            while s[i] not in "'\"":
                i += 1
            prefix = s[:i].lower()
            if 'r' not in prefix and BS in s:
                print(tok.start[0], ascii(s[:100]))
