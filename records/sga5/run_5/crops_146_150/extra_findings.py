# underlined statement texts (executed inside build_findings.py, which defines add, J and F)
UL_NOTE = ("Exposé III B has no underline markup at all; \\emph is this file's command for the print's underline "
           "in statements (Exposé III: \\emph{Sous les hypothèses de} 4.4, ...). Numbers, formulas and the "
           "punctuation between the underlined pieces are not underlined in the print.")

add(146, "statement of Lemme 2.2",
    "underlined: 'Pour prouver' | 'on peut se borner à considérer les deux cas suivants'; not underlined: "
    "'1.2,' and the final ' :'",
    "Pour prouver 1.2, on peut se borner à considérer les deux cas suivants:  (no underline)",
    "underline", "high",
    ("Pour prouver 1.2, on peut se borner à considérer les deux cas suivants:",
     r"\emph{Pour prouver} 1.2, \emph{on peut se borner à considérer les deux cas suivants}:"),
    UL_NOTE)

add(147, "statement of Lemme 2.3",
    "underlined: 'Sous les hypothèses de' | 'supposons' | 'Alors on' + 'a' (across the line break); not "
    "underlined: '1.1,', the formulas, the full stops",
    "Sous les hypothèses de 1.1, supposons $L|U=0$, $M|V=0$. Alors on a  (no underline)",
    "underline", "high",
    ("Sous les hypothèses de 1.1, supposons $L|U=0$, $M|V=0$. Alors on a",
     r"\emph{Sous les hypothèses de} 1.1, \emph{supposons} $L|U=0$, $M|V=0$. \emph{Alors on a}"),
    "As for Lemme 2.2.")

add(148, "statement of Lemme 2.4",
    "underlined: 'Pour prouver' | 'on peut supposer que' | 'et' | 'sont des immersions' + 'fermées' | "
    "'et il suffit de démontrer que' | 'si' | 'la flèche de restric-' + 'tion'; not underlined: '1.2,', a, b, "
    "the formulas and the commas",
    "Pour prouver 1.2, on peut supposer que $a$ et $b$ sont des immersions fermées, ... la flèche de restriction "
    "(no underline)",
    "underline", "high",
    ("Pour prouver 1.2, on peut supposer que $a$ et $b$ sont des immersions fermées, et il suffit de démontrer "
     "que, si $L_x=0$, $M_y=0$, la flèche de restriction",
     r"\emph{Pour prouver} 1.2, \emph{on peut supposer que} $a$ \emph{et} $b$ \emph{sont des immersions "
     r"fermées}, \emph{et il suffit de démontrer que}, \emph{si} $L_x=0$, $M_y=0$, \emph{la flèche de "
     r"restriction}"),
    "As for Lemme 2.2; the statement ends on p. 149 ('est nulle.').")

add(149, "end of the statement of Lemme 2.4",
    "'est nulle' underlined, the full stop not",
    "est nulle.  (no underline)",
    "underline", "high",
    ("est nulle.", r"\emph{est nulle}."),
    "As for the rest of the statement on p. 148.")

add(150, "statement of Proposition 2.5",
    "underlined: 'Sous les hypothèses de' | 'on suppose que' | 'et' | 'sont des' + 'immersions fermées et que' | "
    "'Désignons par' | 'le localisé strict' + 'de' | 'en' | 'et identifions' | 'à des sous-schémas fermés de' | "
    "'Alors les flèches de restriction'; not underlined: '1.2,', a, b, T, X x_S Y, z = (x,y), A , B, the "
    "formulas and the punctuation",
    "Sous les hypothèses de 1.2, on suppose que $a$ et $b$ ... Alors les flèches de restriction  (no underline)",
    "underline", "high",
    ("Sous les hypothèses de 1.2, on suppose que $a$ et $b$ sont des immersions fermées et que $L_x=0$, "
     "$M_y=0$. Désignons par $T$ le localisé strict de $X\\times_SY$ en $z=(x,y)$, et identifions $A$, $B$ à "
     "des sous-schémas fermés de $T$. Alors les flèches de restriction",
     r"\emph{Sous les hypothèses de} 1.2, \emph{on suppose que} $a$ \emph{et} $b$ \emph{sont des immersions "
     r"fermées et que} $L_x=0$, $M_y=0$. \emph{Désignons par} $T$ \emph{le localisé strict de} "
     r"$X\times_SY$ \emph{en} $z=(x,y)$, \emph{et identifions} $A$, $B$ \emph{à des sous-schémas fermés de} "
     r"$T$. \emph{Alors les flèches de restriction}"),
    "As for Lemme 2.2.")

add(150, "end of the statement of Proposition 2.5",
    "'sont nulles' underlined, the full stop not",
    "sont nulles.  (no underline)",
    "underline", "high",
    ("sont nulles.", r"\emph{sont nulles}."),
    "As for the rest of the statement.")
