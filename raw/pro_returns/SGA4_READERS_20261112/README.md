# SGA 4 : texte de lecture français, construction brute du 12 novembre 2026

Ce dossier contient le texte de lecture français de SGA 4 (*Théorie des topos et cohomologie étale des schémas*, tomes 1 à 3, exposés I à XIX, V bis compris).

- `FR/SGA4_FR_texte_de_lecture.pdf` (877 pages) : le texte de lecture. Il donne le texte mathématique corrigé, sans l'apparat critique, sans les relevés de désaccords, sans l'annexe des coquilles possibles et sans les notes éditoriales de l'édition LaTeX. Les numéros de tome et de page de l'édition imprimée figurent en marge.

Les enregistrements de la construction (décisions, placement et jugement des coquilles, décomptes de l'apparat, glossaire français–anglais, journaux de compilation, vérifications, scripts) sont dans le dépôt anglais, avec le texte de lecture anglais : https://github.com/KokunoYumeto/sga-en/tree/main/raw/pro_returns/SGA4_READERS_20261112

La même construction a aussi produit, dans les deux langues, une forme diplomatique, une forme corrigée avec apparat et un maître annoté. Ils ne sont pas publiés ici, pas plus que les sources TeX d'aucune forme, parce qu'ils reproduisent en entier les notes éditoriales (N.D.E.) de l'édition LaTeX. Nos éditions donnent les notes d'un éditeur dans nos propres mots, avec mention de leur auteur ; cette version reste à écrire.

## Qui l'a fait

La construction est due à GPT-6 Astra (OpenAI, ChatGPT Pro mode), le 12 novembre 2026, à partir de notre texte français de SGA 4 vérifié sur les scans et de l'édition anglaise du dépôt sga-en (commit `4a4cbac`, version `v2026-11-12-english-edition`).

- **Séminaire et édition imprimée.** *Séminaire de géométrie algébrique du Bois-Marie 1963–1964* (SGA 4), dirigé par M. Artin, A. Grothendieck et J.-L. Verdier, avec la collaboration de N. Bourbaki, P. Deligne et B. Saint-Donat. M. Artin, A. Grothendieck et J.-L. Verdier sont les éditeurs de l'édition imprimée : Lecture Notes in Mathematics 269 et 270 (Springer, 1972) et 305 (Springer, 1973). Les auteurs de chaque exposé sont nommés dans le texte.
- **Édition LaTeX française.** Le texte français repose sur l'édition LaTeX de SGA 4, tomes 1 à 3, faite et diffusée par Fabrice Orgogozo : https://www.normalesup.org/~forgogozo/SGA4/ (instantané au commit git `71766d9`). Ses corrections de l'imprimé sont conservées dans le texte corrigé et lui restent attribuées.
- **Nos couches.** Le texte français a été vérifié sur les scans de l'imprimé par Claude Opus 5.5 et GPT-6.1 Sol (11 novembre 2026) ; les corrections issues de cette vérification sont des corrections produites par IA (AI-produced corrections). L'assemblage et la composition des livres sont produits par IA (GPT-6 Astra).

Les pages liminaires du livre donnent l'ensemble des crédits et la déclaration de droits.

## Validation annoncée par la construction

- 81 vérifications sur 81 réussies.
- Six livres compilés avec XeLaTeX et amsbook, 0 erreur, 0 glyphe manquant : français 1 050 / 1 684 / 877 pages, anglais 1 008 / 1 413 / 863 pages (diplomatique / corrigé avec apparat / lecture).
- 1 557 pages imprimées placées, avec leurs numéros en marge contrôlés dans chaque livre.
- 898 corrections de transcription convenues et 930 coquilles de l'imprimé convenues prises en compte ; 2 207 entrées d'apparat en français, 1 956 en anglais.
- 1 601 coquilles signalées par un seul modèle jugées : 550 acceptées, 1 043 laissées comme coquilles possibles (annexe de la forme corrigée), 8 rejetées.
- 643 lectures en désaccord sur 443 pages sont signalées sans être tranchées : elles attendent une seconde vérification sur les scans.
- Les 56 corrections françaises à rejouer à la main sont placées ou justifiées ; 18 modifications touchant l'apparat de l'édition LaTeX sont listées, non appliquées.

## Notre contrôle (Claude Opus 5.5, 12 novembre 2026)

- **Complétude.** Chaque PDF a le nombre de pages annoncé.
- **Compilation.** Les six livres ont été recompilés à partir de leur TeX, dans un dossier à part, avec XeLaTeX (trois passes, shell escape désactivé) : 0 erreur, 0 caractère manquant, 0 référence indéfinie ; nombres de pages comme ci-dessus.
- **Confidentialité.** Aucun nom personnel, chemin local, adresse électronique, clé ou jeton dans les fichiers publiés, texte et métadonnées des PDF compris.
- **Pages liminaires.** Nous avons corrigé les pages liminaires dans notre copie du TeX et recompilé le PDF publié ici : les éditeurs de 1972–1973 y sont nommés comme tels, la page d'Orgogozo y est liée, et le lien de demande de retrait renvoie aux issues de ce dépôt (il renvoyait au dépôt anglais). Le texte n'est pas modifié par ailleurs.
- **Texte de lecture.** En trois endroits (V bis p. 138, où la démonstration du lemme 3.3.3.3 a été réécrite dans l'édition LaTeX ; XIV p. 145–146, théorème 1.1 et ses notes ; XVI 3.9–3.10), le texte de lecture ne porte ni note, ni marque de variante, ni marque de désaccord, et ses mots sont ceux de la forme corrigée une fois celles-ci retirées.
- **Pages absentes de la source.** La construction n'avait pas de texte pour les pages de sommaire des exposés (V p. 1, V bis p. 83, VI p. 163–164, VII p. 341, VIII p. 366, XVI p. 206, XVII p. 250–251), ni pour les pages liminaires et les index des tomes. Nos scans les contiennent toutes ; elles seront transcrites plus tard.

## Droits

Les droits sur l'œuvre originale appartiennent à son auteur, à ses représentants ou à ses ayants droit. Dans la mesure où nous détenons des droits sur la transcription, la traduction, les corrections et la composition produites par l'IA, nous les consacrons au domaine public sous CC0 1.0. Cette édition est publiée à des fins éducatives et non lucratives, et nous ne revendiquons aucun droit que nous ne détenons pas. Si vous détenez des droits sur cette œuvre et vous opposez à sa publication ici, veuillez ouvrir une issue GitHub et nous la retirerons.
