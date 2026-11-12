import json
import pathlib

B = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I\b176_180")
OUT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I\findings_176_180.json")

KEEP = "The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring."
PP = ("Same P_p-for-E_p slip of the typescript as in 1.1.2.1-1.1.3 (pp. 136-138), (1.1.5.10) on p. 142 and "
      "p. 144 (GLOBAL_ISSUES item 29). ")

F = [
    dict(page=176,
         where="2.10, second sentence: 'Nous les signalons par acquit de conscience, car nous n'autons pas à les utiliser.'",
         scan="n'autons",
         tex="n'autons",
         kind="misprint_in_print", confidence="high", fix=None,
         corrected="n'aurons",
         note="Typing error (t for r). " + KEEP),
    dict(page=177,
         where="2.10.1 continued, first line: 'muni de structures d'entension centrale de Q_P par G_P'",
         scan="d'entension",
         tex="d'entension",
         kind="misprint_in_print", confidence="high", fix=None,
         corrected="d'extension",
         note="Typing error (n for x). " + KEEP),
    dict(page=177,
         where="2.10.1: 'et compatibles entre elles i.e. rendent commuatifs les diagrammes (2.1.1)'",
         scan="commuatifs",
         tex="commuatifs",
         kind="misprint_in_print", confidence="high", fix=None,
         corrected="commutatifs",
         note="Typing error: the t between u and a is missing. " + KEEP),
    dict(page=177,
         where="2.10.1: 'La plupart des développements qui précèdent sont valables mutatis mutandis pour cette notion plus général.'",
         scan="plus général. (the full stop follows the l directly; no final e)",
         tex="cette notion plus général.",
         kind="misprint_in_print", confidence="high", fix=None,
         corrected="cette notion plus générale.",
         note="Agreement slip: 'notion' is feminine (the next sentence prints 'plus générale que celle de 2.1'). " + KEEP),
    dict(page=177,
         where="2.10.2, second paragraph: 'G étant le groupe multiplicatif sur G_m (comparer 2.9.2)'",
         scan="le groupe multiplicatif sur G_m (underlined G, subscript m)",
         tex="groupe multiplicatif sur $\\underline{G}_m$",
         kind="misprint_in_print", confidence="low", fix=None,
         corrected="groupe multiplicatif $\\underline{G}_m$",
         note="'sur' followed by the group itself does not parse; the base is the schéma S named just before "
              "(cf. 2.9.5: 'G=G_{mS} le schéma en groupes multiplicatif sur S'). Probably a stray 'sur'; "
              "'le groupe multiplicatif G_m sur S' is also possible, so low. " + KEEP),
    dict(page=177,
         where="2.10.3, first line: 'La notion de biextension 2.1 peut-être considérée comme une variante'",
         scan="peut-être (with a hyphen)",
         tex="peut-être considérée",
         kind="misprint_in_print", confidence="high", fix=None,
         corrected="peut être considérée",
         note="The verb pouvoir + être ('can be'), not the adverb peut-être ('perhaps'). " + KEEP),
    dict(page=178,
         where="display after 'par la donnée d'isomorphismes': mu_{a,p} : ^a(P_p) ~-> P_{ap}  (p in P(S), a in A(S))",
         scan="^a(P_p) and P_{ap}: capital P with subscripts p and ap",
         tex="{}^a(P_p) \\overset{\\sim}{\\longrightarrow} P_{ap}",
         kind="misprint_in_print", confidence="high", fix=None,
         corrected="{}^a(E_p) \\overset{\\sim}{\\longrightarrow} E_{ap}",
         note="The isomorphisms mu_{a,p} of the A-linear variant of 1.1.6 relate the torseurs of the family named "
              "earlier in the same paragraph ('une famille de torseurs E_p sous les G_p ... E_p étant assujetti à varier de "
              "façon A-linéaire'): the image of E_p by the extension of scalars a, and E_{ap}. " + PP
              + "Correct together with the next entry. " + KEEP),
    dict(page=178,
         where="last line: 'où le premier membre désigne l'image du G_S-torseur P_p par l'extension'",
         scan="P_p (capital P, subscript small p)",
         tex="torseur $P_p$",
         kind="misprint_in_print", confidence="high", fix=None,
         corrected="torseur $E_p$",
         note="The G_S-torseur is the fibre E_p (see the previous entry). " + PP + KEEP),
    dict(page=179,
         where="3.1, after (3.1.1): 'Nous allons définir une catégorie cofibré Psi = Psi_{L.} sur C'",
         scan="cofibré (no final e)",
         tex="cofibré $\\underline{\\Psi}",
         kind="misprint_in_print", confidence="high", fix=None,
         corrected="cofibrée $\\underline{\\Psi}",
         note="Agreement slip: 'catégorie' is feminine (the heading of 3.1 and the same sentence print "
              "'catégorie cofibrée', 'catégories cofibrées'). " + KEEP),
    dict(page=180,
         where="display after 'résultant de l'isomorphisme de transitivité': d_1^*(d_o^*(E)) ~ (d_o d_1)^*(E)",
         scan="E in both members",
         tex="d^*_1(d^*_o(E)) \\;\\simeq\\; (d_o d_1)^*(E)",
         kind="misprint_in_print", confidence="low", fix=None,
         corrected="d^*_1(d^*_o(X)) \\;\\simeq\\; (d_o d_1)^*(X)",
         note="The isomorphism is applied to the extension X of (3.1.2): the same sentence prints d_1^*(d_o^*(X)); "
              "E (the letter of sections 1-2) is not defined in 3.1. Low: the transitivity isomorphism holds "
              "for any extension and E may be meant generically. " + KEEP),
    dict(page=180,
         where="footnote (*): 'Une façon plus simple de décrire psi_{L.}(A) (signalée par DELIGNE)'",
         scan="a small psi (with descender), not underlined; the main text writes the cofibred category as an "
              "underlined capital Psi (heading of 3.1, 'Psi = Psi_{L.}' and 'Les objets de Psi_{L.}' on p. 179)",
         tex="$\\psi_{L.}$",
         kind="misprint_in_print", confidence="low", fix=None,
         corrected="$\\underline{\\Psi}_{L.}$",
         note="The footnote describes the fibre over A of the cofibred category Psi_{L.} (pairs (X, alpha) with X an "
              "extension of L_o by A), which the text writes \\underline{\\Psi}_{L.} (A) (e.g. 3.1.7). Low: the "
              "footnote may use a looser notation. " + KEEP),
]

pages = {}
for p in sorted({f["page"] for f in F}):
    pages[p] = (B / f"page_{p:03d}.tex").read_text(encoding="utf-8")

ok = True
for f in F:
    t = pages[f["page"]]
    n = t.count(f["tex"])
    if n != 1:
        ok = False
        print("TEX NOT UNIQUE", f["page"], n, repr(f["tex"]))
    if f["fix"] is not None:
        m = t.count(f["fix"]["old"])
        if m != 1:
            ok = False
            print("OLD NOT UNIQUE", f["page"], m, repr(f["fix"]["old"]))
    if "MARKER" in f["tex"] or "%%%%" in f["tex"]:
        ok = False
        print("touches marker", f)

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
print("written", OUT, len(F), "ok" if ok else "PROBLEMS")
from collections import Counter
c = Counter((f["page"], f["kind"] == "misprint_in_print") for f in F)
for p in (176, 177, 178, 179, 180):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
