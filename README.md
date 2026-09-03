# Association d'appui aux mères divorcées — site de démonstration

Site statique bilingue (français / anglais) bâti sur le cahier des charges
*Specifications Document — Association for the Support of Divorced Mothers*,
fourni par le client. 18 pages rendues, plus la page d'aiguillage, le plan
de site et le fichier `robots.txt`.

Aucun serveur, aucune base de données, aucune dépendance : des fichiers
HTML, une feuille de style, un script de 146 lignes, huit ornements SVG et
deux polices servies depuis le site.

---

## La règle qui gouverne tout le reste

> **Rien n'est affirmé qui ne vienne du cahier des charges.**

Le document ne donne ni le nom de l'association, ni le pays, ni la ville,
ni une adresse, ni un téléphone, ni un horaire, ni une date de séance, ni
un tarif, ni le nom d'une personne. Aucune de ces choses n'apparaît donc
sur le site. Là où elles manqueront au lecteur, la page porte le mot
d'attente du projet — **« À fixer » / « To be set »** — accompagné de la
condition exacte qui le lèvera.

C'est plus long à lire qu'un site plein de texte plausible. C'est aussi la
seule version qu'on peut montrer à quelqu'un sans lui mentir.

### Les cinq absences, et la raison de chacune

| Ce qui n'est pas sur le site | Pourquoi |
|---|---|
| Aucun témoignage, même anonyme | Chapitre 9 : pas de publication de témoignage sans autorisation explicite. Il n'en existe aucune. |
| Aucune photographie de personne, ni réelle ni générée | Même chapitre, plus le chapitre 11 (communication sobre, sans exposition ni victimisation). Une photo d'agence qui fait passer une inconnue pour une bénéficiaire est fausse **et** elle expose quelqu'un. |
| Aucun chiffre de fréquentation | Chapitre 14 : ce sont des indicateurs *à suivre*, pas des résultats déjà obtenus. |
| Aucun numéro d'urgence ni de service social | Il dépend du pays. Un numéro qui ne répond pas dans le pays du lecteur est pire que pas de numéro du tout — et sur ce site-ci, c'est une personne en difficulté qui compose. |
| Aucune promesse de résultat, aucun conseil médical, psychologique ou juridique | Chapitre 1 : l'association ne remplace ni les institutions, ni les professionnels de santé, ni les services sociaux. |

Les cinq sont vérifiées mécaniquement sur les dix-huit pages rendues, pas
relues à l'œil. Voir « Vérification » plus bas.

---

## Le nom affiché est un nom de travail

Le chapitre 11 demande « un nom et un logo simples, rassurants et faciles à
retenir ». Il ne les donne pas.

Le site affiche **« Le Cercle Ouvert » / « The Open Circle »**, marqué
comme nom de travail à trois endroits : sous le nom lui-même dans
l'en-tête, dans le pied de page, et dans le bandeau de démonstration en
haut de chaque page. Ce n'est pas une proposition déguisée en décision —
c'est un nom qui permet de lire les pages en attendant la vraie décision.

Il tient dans une seule constante, `MARQUE`, dans `source/contenu.py`. Le
changer une fois le change sur les dix-huit pages, dans les titres, dans le
plan de site et dans les métadonnées.

---

## Le symbole

Un cercle qui ne se referme pas, avec un second cercle ouvert plus petit et
un point au centre. Il dit la seule chose que l'association promet
vraiment : on peut entrer, on peut repartir, personne ne referme la porte
derrière vous. Il évoque aussi le groupe de parole du chapitre 5.

Tout est produit par `source/motif.py`, à partir d'une seule fonction
géométrique — `arc_ouvert(cx, cy, r, milieu, ouverture)` — qui décrit
l'**ouverture** plutôt que le trait. C'est l'ouverture qui porte le sens,
donc c'est elle qu'on veut pouvoir régler, et c'est elle qui doit rester
visible quand la marque tombe à 16 pixels : sous une certaine taille un
trait presque fermé se lit comme un anneau plein, et la figure ne dit plus
rien.

Deux corrections faites en regardant le rendu, pas le code :

* **Le favicon se lisait comme un bouton d'alimentation.** Un anneau fendu
  vers le haut avec un point au centre, c'est le pictogramme universel de
  la mise en marche. L'ouverture du favicon a été déplacée en haut à
  gauche ; celle de la marque reste en haut, où elle n'a pas ce problème
  parce que le second arc casse la lecture.
* **Le motif de fond dessinait une file d'ogives pointues.** Avec un rayon
  égal à la moitié du côté de la tuile, les cercles des coins se coupent au
  milieu de chaque bord. Le rayon est passé à 0,40 fois le côté.

Ce que le symbole n'est pas, délibérément : un cœur, deux mains jointes,
une silhouette de mère et d'enfant. Le chapitre 11 demande de valoriser la
dignité sans victimisation, et ces trois images font l'inverse.

---

## La palette

Le client a demandé le rose en cours de chantier. Le site est donc tenu en
**prune profond et rose sourd** plutôt qu'en rose bonbon : c'est la même
famille de teinte, et c'est la seule qui laisse le texte lisible. Le rose
vif reste présent, mais uniquement en décor — les ornements, les filets,
les fonds de badge — jamais en texte sur fond clair.

Chaque valeur a été recalculée avant d'être écrite, puis remesurée dans le
navigateur. Le résultat est dans le tableau des contrastes : le point le
plus faible du site est passé de 5,97:1 à **6,72:1**. La palette rose
mesure mieux que celle qu'elle remplace, ce qui n'était ni prévu ni promis
— c'est simplement ce que donne le fait de calculer avant d'écrire.

Les huit ornements SVG portent des noms **neutres** — `marque-accent`,
`marque-fonce`, `marque-clair`, `marque-duo` — et pas des noms de couleur.
La palette a déjà changé une fois ; des fichiers nommés d'après une teinte
auraient forcé à renommer partout, ou à garder un `marque-cuivre.svg`
désormais rose.

---

## Le bouton de sortie rapide

Sur chaque page, en haut à droite et dans la barre mobile : **Quitter le
site**. Il remplace la page en cours par un moteur de recherche.

C'est un ajout au cahier des charges, et c'est une décision que le client
peut annuler d'un mot. Le raisonnement : une partie des personnes qui
liront ce site le liront sur un appareil partagé, et le chapitre 9 fait de
la confidentialité la règle première de l'association. Un site qui promet
la confidentialité et qui laisse une trace évidente dans le navigateur se
contredit.

Quatre précisions, toutes écrites sur le site :

* c'est un **vrai lien** : sans JavaScript il fonctionne quand même ;
* avec JavaScript, il utilise `location.replace`, qui **remplace** l'entrée
  d'historique au lieu d'en ajouter une — sinon le bouton « précédent »
  ramène exactement là où l'on ne veut pas revenir ;
* il **vide le formulaire** avant de partir, parce que les navigateurs
  restaurent les champs ;
* il **n'efface pas l'historique** déjà constitué, et la page
  Confidentialité le dit en toutes lettres plutôt que de laisser croire le
  contraire.

---

## Les 18 pages

Le chapitre 12 fixe sept pages. Les deux dernières s'y ajoutent parce
qu'aucun site publié ne s'en passe.

| Page | Français | Anglais |
|---|---|---|
| Accueil | `fr/index.html` | `en/index.html` |
| Mission et valeurs | `mission-et-valeurs.html` | `mission-and-values.html` |
| Services et activités | `services-et-activites.html` | `services-and-activities.html` |
| Calendrier des ateliers | `calendrier-des-ateliers.html` | `workshop-calendar.html` |
| Bénévolat et partenariats | `benevolat-et-partenariats.html` | `volunteering-and-partnerships.html` |
| Demande d'accueil | `demande-d-accueil.html` | `reception-request.html` |
| Confidentialité | `confidentialite.html` | `privacy.html` |
| Mentions légales | `mentions-legales.html` | `legal-notice.html` |
| Accessibilité | `accessibilite.html` | `accessibility.html` |

### La page calendrier est vide de dates, exprès

C'est la page la plus utilisée d'un site d'association, et la seule qu'on
ne peut pas remplir à l'avance sans mentir. Une date inventée fait sortir
quelqu'un de chez elle pour rien ; une mère qui a organisé une garde
d'enfants pour venir ne revient pas une deuxième fois.

Ce que le cahier des charges donne, ce sont les **fréquences indicatives**
du chapitre 6 — « indicative » est son mot, il est repris tel quel. Elles
sont publiées dans un tableau. Ce qu'il ne donne pas — le jour, l'heure, le
lieu, la date de la première séance, la façon de s'inscrire, les périodes
de fermeture — est listé sous le mot d'attente, avec sa condition.

### Le formulaire n'envoie rien, et il le dit

Il valide les champs dans le navigateur et s'arrête là : il n'existe ni
domaine, ni adresse professionnelle, ni ligne d'accueil. Le message
affiché après une validation réussie dit exactement cela, et il ne propose
**aucun numéro de repli** — il n'y en a pas, et en inventer un serait
précisément la faute que tout le reste du site évite.

Deux détails du formulaire viennent du public visé plutôt que du cahier
des charges : le premier champ demande *« comment vous appeler »* et
précise qu'un prénom d'emprunt convient, et le champ libre porte
`autocomplete="off"` et un avertissement disant de n'y rien écrire
d'urgent, parce qu'il n'est pas relevé en temps réel.

---

## Vérification

```
python3 -m http.server 8874 --bind 127.0.0.1   # depuis la racine du site
python3 tests/verif.py http://127.0.0.1:8874/
```

**1 978 contrôles, 0 échec.** Quinze sections, sur les 18 pages rendues et
à 21 largeurs d'écran de 320 à 1440 pixels.

Lire la source dit ce qui a été écrit ; mesurer le rendu dit ce que le
navigateur a fait. Les contrastes, les proportions d'images, les
débordements, les ancres et les requêtes réseau sont donc mesurés dans un
Chromium réel, jamais déduits de la feuille de style.

Les largeurs testées encadrent **chaque** point de bascule de la feuille de
style (419/421, 759/761, 799/801, 1000/1001, 1259/1260). Une règle qui ne
se trompe qu'à l'intérieur d'une bande étroite ne peut donc pas se cacher
entre deux mesures — c'est comme cela qu'un débordement de 33 pixels,
présent dans une seule des deux langues, a été trouvé sur un autre chantier.

### Contrastes mesurés

Le texte est rendu transparent, la zone est photographiée, et l'on retient
le pixel de fond le plus défavorable (2ᵉ centile du contraste, pas de la
luminance). Cacher l'élément entier découvrirait le fond de son **ancêtre**,
ce qui donne une lecture fausse pour tout ce qui peint son propre fond.

| Élément | Largeur | Mesuré |
|---|---|---|
| Titre du héros | 1280 | 11,47:1 |
| Titre du héros | 390 | 12,02:1 |
| Chapô du héros | 1280 | 9,80:1 |
| Bandeau de démonstration | 1280 | 9,72:1 |
| Mention de la barre utilitaire | 1280 | 8,89:1 |
| Sortie rapide | 1280 | 11,10:1 |
| Mention « nom de travail » | 1280 | 7,14:1 |
| Lien de menu | 1280 | 9,72:1 |
| Texte de carte | 1280 | 15,50:1 |
| Titre d'étape du parcours | 1280 | 14,95:1 |
| Lien du pied de page | 1280 | 12,23:1 |
| Mention de confidentialité | 1280 | 7,72:1 |
| Fréquence du tableau | 1280 | 7,72:1 |
| Badge « À fixer » | 1280 | 7,94:1 |
| Condition de l'attente | 1280 | 7,26:1 |
| Aide de champ | 1280 | 7,26:1 |
| Avertissement du formulaire | 1280 | 13,06:1 |
| Fil d'Ariane | 1280 | 6,72:1 |
| Sortie de la barre mobile | 390 | **6,85:1** |

Le seuil retenu est 4,5:1. Le plus faible du site est 6,72:1.

Ces valeurs sont celles de la palette rose demandée en cours de chantier.
Chacune a été recalculée avant d'être écrite, puis remesurée : la palette
rose mesure **mieux** que celle qu'elle remplace, dont le point le plus
faible était 5,97:1.

Le titre du héros est déclaré à 13,82:1 par l'arithmétique et mesuré à
11,47:1 : le motif de fond posé à 13 % d'opacité sur le prune éclaire
légèrement le fond. L'écart est dans le bon sens — c'est l'instrument qui
a raison, pas le calcul.

Le rose clair (`#D98BA6`) ne sert **jamais** de texte sur fond clair : il
tombe à 2,37:1 sur la crème. Il est réservé au décor, où il ne porte
aucune information ; le texte rose est `#8E3155`, à 7,14:1.

### Ce que la vérification contrôle

1. Structure des fichiers : doctype, langue, un seul `h1`, lien
   d'évitement, canonique, trois `hreflang`, `noindex`, favicon, longueur
   des descriptions, absence de tout outil de mesure, absence de données
   structurées, nom marqué comme provisoire, deux sorties rapides.
2. Aucune ressource tierce, et **aucune image qui ne soit un des huit
   ornements produits par `motif.py`** — une photographie de personne ne
   peut pas entrer sans faire échouer ce contrôle.
3. Les 30 motifs interdits (promesses, guérison, thérapie, conseil
   juridique, superlatifs, gratuité affirmée, prix, chiffres de
   fréquentation, jours de la semaine, heures, dates, téléphones, codes
   postaux, adresses électroniques), en tenant compte des négations **et**
   des questions.
4. Le badge d'attente porte exactement le mot du projet, et le vocabulaire
   d'attente des autres chantiers du même client ne sert jamais d'étiquette
   ici.
5. Liens morts, aller-retour de langue, plan de site, `robots.txt`.
6. Rendu : erreurs console, requêtes hors domaine, polices chargées,
   débordement horizontal à 21 largeurs, images cassées, boîtes d'images
   déformées, hiérarchie des titres, rien hors écran.
7. Ancres sous l'en-tête collant, à 390 et 1280.
8. Clavier : tabulation, lien d'évitement, contour de focus, ouverture et
   fermeture du menu, cohérence de `aria-expanded` au-delà de 1000 px.
9. Formulaire : erreurs annoncées, focus sur le premier champ fautif,
   aucun message de succès quand il est invalide, message honnête quand il
   est valide, **aucun numéro inventé dans ce message**, consentements
   jamais cochés d'avance, champ libre borné, `autocomplete` désactivé.
10. Tableau des activités : en-têtes de colonne et de ligne déclarés, sept
    lignes, et à 320 px c'est le **cadre** qui défile, pas la page.
11. Sortie rapide : c'est un lien, sa cible est la bonne, elle porte
    `noopener`, et elle vide le formulaire avant de partir.
12. Sans JavaScript : le formulaire, l'avertissement, les attentes et la
    sortie rapide restent utilisables.
13. Mouvement réduit, impression, barre mobile à huit largeurs.

### Mutations

Un contrôle qui n'a jamais échoué n'a rien prouvé. Neuf défauts ont été
introduits un par un, chacun avec **sa propre preuve de rendu** à **sa
propre largeur** — sans cette preuve, « 0 échec » a deux causes possibles,
un contrôle aveugle ou une mutation inerte, et on ne peut pas les
distinguer.

| Défaut introduit | Largeur | Preuve au rendu | Échecs |
|---|---|---|---|
| Une promesse de résultat | 1280 | le mot « garantis » est dans la page | 1 |
| Un horaire inventé | 1280 | le mot « mardis » est dans la page | 2 |
| Un numéro de téléphone inventé | 1280 | « +33 » est dans la page | 1 |
| Une photographie de personne | 1280 | `src` vaut `mere-et-enfant.jpg` | 6 |
| Ancre sous l'en-tête collant | 390 | `scroll-margin-top` calculé à `0px` | 8 |
| Minimum de grille en pixels durs | 320 | colonne de `330px` dans une boîte de 288 | 7 |
| Une ressource chargée depuis un tiers | 1280 | 1 `<link>` vers `fonts.googleapis` | 36 |
| La barre mobile masque la fin du pied | 390 | `padding-bottom` calculé à `0px` | 16 |
| La sortie rapide devient un bouton | 1280 | l'élément est un `BUTTON` | 26 |
| *Restauration* | — | — | **0 sur 1 978** |

La troisième ligne de ce tableau a une histoire. À la première exécution,
la mutation « numéro de téléphone » n'a produit **aucun échec**, et sa
preuve de rendu disait `False` : le numéro n'était pas dans la page. La
phrase visée est coupée en deux littéraux dans la source, le
remplacement ne trouvait rien, et la mutation n'écrivait rien. Sans la
preuve de rendu, ce 0 se serait lu comme « le site est propre » alors
qu'il voulait dire « on n'a rien testé ». Le banc compare maintenant
l'empreinte des fichiers avant et après chaque mutation et écrit `ecrit`
ou `INERTE` sur la ligne ; les neuf lignes ci-dessus portent toutes
`ecrit`.

---

## Ce qui bloque la mise en ligne

Aucune de ces décisions ne m'appartient, et chacune est signalée sur la
page concernée.

| # | Décision | Ce qu'elle commande |
|---|---|---|
| A-01 | Le nom de l'association | Il est sur les dix-huit pages, dans les titres et dans le plan de site. |
| A-02 | Le pays et la ville | La loi applicable, les mentions obligatoires, les numéros d'urgence, les partenaires cités, et la langue principale. |
| A-03 | Le statut juridique | Association déclarée ou non, et sous quel régime. |
| A-04 | Les langues de lancement | Le site est bilingue ; le cahier des charges est en anglais et nos échanges en français. |
| A-05 | Le local | Adresse, accès, et s'il existe un coin enfants en dehors des activités mère-enfant. |
| A-06 | Le domaine et l'adresse professionnelle | Sans eux le formulaire n'a pas de destinataire. |
| A-07 | La ligne d'accueil | Le seul canal qu'une personne en difficulté utilisera vraiment. |
| A-08 | Les créneaux et la date de la première séance | La page calendrier reste vide sans eux. |
| A-09 | Les intervenantes | Aucun nom, aucune qualification et aucun diplôme ne sera affiché sans justificatif. |
| A-10 | Le responsable des données et la durée de conservation | La page Confidentialité en dépend. |
| A-11 | Les canaux officiels | Facebook, Instagram, WhatsApp Business : aucun compte n'est lié tant qu'il n'est pas confirmé. Un lien vers un compte qui n'est pas le vôtre est une usurpation. |
| A-12 | Le bouton de sortie rapide | Il est ajouté au cahier des charges. Un mot suffit pour le retirer. |

---

## Notes techniques

* **Démonstration.** `DEMO = True` dans `source/build.py` pose le bandeau,
  la balise `noindex` sur chaque page et un `robots.txt` fermé. Les trois
  ensemble, parce qu'un `robots.txt` n'empêche pas l'indexation d'une URL
  déjà connue. Le passer à `False` retire les trois d'un coup.
* **Aucune donnée structurée.** Déclarer une `Organization` dont le nom est
  un nom de travail, sans adresse, sans pays et sans téléphone, publie une
  identité qui n'existe pas — et c'est exactement ce qu'un moteur
  recopierait dans un panneau de résultats.
* **Polices servies depuis le site** (Playfair Display et Inter, licence
  SIL OFL incluse dans `assets/fonts/`). Une police chargée chez un tiers
  lui transmettrait l'adresse exacte de la page lue ; sur ce site-ci cela
  révélerait bien plus qu'une préférence de lecture.
* **Aucun cookie, aucune mesure d'audience, aucune requête sortante.** Ce
  n'est pas une intention : le contrôle compte les requêtes de chaque page
  et exige zéro.
* **Le tableau du chapitre 6 est un vrai `<table>`** avec `scope="col"` et
  `scope="row"`. C'est de la donnée tabulaire ; une grille de `<div>` la
  rendrait illisible à voix haute.
* **Les numéros du parcours sont un compteur CSS**, jamais écrits dans le
  texte : insérer une étape ne peut donc pas décaler une numérotation
  écrite à la main.

## Régénérer

```
python3 source/motif.py     # les 8 ornements SVG
python3 source/build.py     # les 18 pages + aiguillage + sitemap + robots
python3 tests/verif.py http://127.0.0.1:8874/
python3 tests/captures.py http://127.0.0.1:8874/
```

Les fichiers de `assets/` produits par `motif.py` et les pages produites par
`build.py` ne se modifient pas à la main : ils seraient écrasés au
prochain passage.

## Pour la personne qui relira le juridique

Selon le pays retenu, à examiner en priorité : le régime de protection des
données personnelles et les droits des personnes ; les mentions
obligatoires d'un site d'association ; le traitement des informations
concernant des enfants ; les conditions de recueil, de conservation et de
retrait d'une autorisation de publier une photo ou un témoignage ; et les
obligations de signalement dans les situations où une personne ou un enfant
est en danger.
