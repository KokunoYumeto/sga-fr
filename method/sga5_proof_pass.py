"""SGA 5, both layers: the proofs that Exposé I sets as \\begin{proof}[Preuve] ... \\end{proof} (an italic "Preuve."
and a closing square) become the print's underlined "Preuve :" with no end mark, i.e. "\\emph{Preuve} : " and no
\\end{proof} (checkers of batches 006-015, 10 Nov 2026). Proofs with another label (Démonstration) are left for the
checkers. Also "dim. q. inj" and "dim. inj", which Exposé I sets with q and inj in math italic, become upright as in the
later exposés (\\dim.\\mathrm{q.inj}, \\dim.\\mathrm{inj}). Every change is logged in FIXLOG_5*.jsonl.
usage: python -I sga5_proof_pass.py [--apply]"""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = pathlib.Path(__file__).parent
APPLY = "--apply" in sys.argv
TOK = re.compile(r"\\begin\{(proof|prooftext)\}\[\s*([^\]]*?)\s*\]|\\end\{(proof|prooftext)\}")


def proof_pass(t):
    stack, edits = [], []                      # edits: (start, end, replacement)
    for m in TOK.finditer(t):
        if m.group(0).startswith("\\begin"):
            stack.append(m)
        elif stack:
            b = stack.pop()
            if b.group(2) != "Preuve" or b.group(1) != m.group(3):
                continue
            # the label: join the first line of the proof to it when it is ordinary text
            after = t[b.end():b.end() + 2]
            rest = t[b.end():].lstrip(" ")
            nxt = rest[1:] if rest.startswith("\n") else rest
            joinable = rest.startswith("\n") and nxt[:1] not in ("\n", "\\") or not rest.startswith("\n")
            bend = b.end() + (len(t[b.end():]) - len(rest)) + (1 if rest.startswith("\n") and joinable else 0)
            edits.append((b.start(), bend, "\\emph{Preuve} : " if joinable else "\\emph{Preuve} :"))
            # the end mark: drop it, with its line when it stands alone
            ls = t.rfind("\n", 0, m.start()) + 1
            le = t.find("\n", m.end())
            le = len(t) if le < 0 else le
            if t[ls:m.start()].strip() == "" and t[m.end():le].strip() == "":
                edits.append((ls, min(le + 1, len(t)), ""))
            else:
                edits.append((m.start(), m.end(), ""))
            del after
    for s, e, r in sorted(edits, reverse=True):
        t = t[:s] + r + t[e:]
    return t, len(edits) // 2


for layer, log in (("diplomatic", "FIXLOG_5.jsonl"), ("current", "FIXLOG_5_CURRENT.jsonl")):
    p = ROOT / "sga5" / layer / "s5.tex"
    t = p.read_text(encoding="utf-8")
    t2, nproof = proof_pass(t)
    n1, n2 = t2.count("\\dim.\\,q.\\,inj"), t2.count("\\dim.\\,inj")
    t2 = t2.replace("\\dim.\\,q.\\,inj", "\\dim.\\mathrm{q.inj}").replace("\\dim.\\,inj", "\\dim.\\mathrm{inj}")
    beg = len(re.findall(r"\\begin\{proof(?:text)?\}", t2))
    end = len(re.findall(r"\\end\{proof(?:text)?\}", t2))
    print(f"{layer}: proofs converted {nproof}, dim.q.inj {n1}, dim.inj {n2}; left: begin{{proof}} {beg}, end{{proof}} {end}")
    if APPLY and t2 != t:
        p.write_text(t2, encoding="utf-8", newline="")
        with open(ROOT / log, "a", encoding="utf-8") as f:
            for kind, old, new, n in (("proof label", "\\begin{proof}[Preuve] ... \\end{proof}", "\\emph{Preuve} : ...", nproof),
                                      ("upright", "\\dim.\\,q.\\,inj", "\\dim.\\mathrm{q.inj}", n1),
                                      ("upright", "\\dim.\\,inj", "\\dim.\\mathrm{inj}", n2)):
                for _ in range(n):
                    f.write(json.dumps({"vol": "5", "file": "s5.tex", "page": None, "old": old, "new": new, "kind": kind,
                                        "source": "global: the print's form (batches 006-015, 10 Nov 2026)"},
                                       ensure_ascii=False) + "\n")
