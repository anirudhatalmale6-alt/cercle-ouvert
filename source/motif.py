# -*- coding: utf-8 -*-
"""
Ornements du site de l'association.

Tout ce qui est dessiné ici sort d'une seule figure : un cercle qui ne se
referme pas. C'est le seul symbole du site, et il dit la seule chose que
l'association promet vraiment — on peut entrer, on peut repartir, personne
ne referme la porte derrière vous.

Deux conséquences pratiques, et elles sont volontaires :

* Aucune figure humaine. Le chapitre 9 du cahier des charges interdit la
  publication de photos, de noms et de témoignages sans autorisation
  explicite. Une photo d'agence qui fait passer une inconnue pour une
  bénéficiaire tombe exactement sous cette interdiction, en pire : elle est
  fausse ET elle expose quelqu'un. Aucune image de personne n'est donc
  utilisée, ni réelle ni générée. Les emplacements d'image portent un
  panneau dessiné.

* Aucun cliché de la détresse. Pas de cœur, pas de mains jointes, pas de
  silhouette de mère et d'enfant. Le chapitre 11 demande une communication
  sobre, respectueuse et sans victimisation ; ces trois images font
  exactement le contraire.

Les noms de fichiers produits ici sont neutres — accent, foncé, clair, duo —
et pas des noms de couleur. La palette a déjà changé une fois ; des fichiers
nommés d'après une teinte auraient forcé à renommer partout, ou à garder un
« marque-cuivre.svg » désormais rose.
"""

import math
import os

_ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(_ICI) if os.path.basename(_ICI) == "source" else _ICI
ACTIFS = os.path.join(RACINE, "assets")

# ---------------------------------------------------------------- palette
# Palette demandée par le client : rose. Elle est tenue en prune profond et
# rose sourd plutôt qu'en rose bonbon — c'est la même famille de teinte, et
# c'est la seule qui laisse le texte lisible.
#
# Chaque valeur de TEXTE a été calculée avant d'être écrite, et remesurée
# ensuite dans un navigateur réel (voir README, « Contrastes mesurés »).
# Le rose clair n'est JAMAIS du texte sur fond clair : il tombe à 2,37:1 sur
# la crème. C'est ROSE_TEXTE qui sert dans ce cas.
CREME = "#FAF5F3"
BLANC = "#FFFFFF"
ENCRE = "#2A2226"
GRIS = "#5E545A"
PRUNE = "#6E2444"
FONCE = "#3A1E2E"
NUIT = "#2A1420"
ROSE = "#D98BA6"
ROSE_TEXTE = "#8E3155"
CLAIR = "#F2E6E9"
ROSE_CLAIR = "#F0C4D2"

# ---------------------------------------------------------------- géométrie
LARGEUR = 200.0
HAUTEUR = 200.0
CX = LARGEUR / 2.0
CY = HAUTEUR / 2.0

R_EXT = 76.0        # rayon du cercle extérieur
EP_EXT = 14.0       # épaisseur du trait extérieur
OUV_EXT = 62.0      # ouverture, en degrés
ANG_EXT = -90.0     # milieu de l'ouverture : en haut

R_INT = 44.0
EP_INT = 10.0
OUV_INT = 74.0
ANG_INT = 62.0      # l'ouverture intérieure regarde ailleurs que l'autre

R_COEUR = 11.0


def _f(v):
    """3 décimales max, sans zéros inutiles : les SVG restent lisibles."""
    s = "%.3f" % v
    s = s.rstrip("0").rstrip(".")
    return s if s not in ("", "-0") else "0"


def _pt(cx, cy, r, deg):
    a = math.radians(deg)
    return cx + r * math.cos(a), cy + r * math.sin(a)


def arc_ouvert(cx, cy, r, milieu, ouverture):
    """Arc de cercle interrompu, décrit par le milieu et la largeur du VIDE.

    On décrit l'ouverture plutôt que le trait parce que c'est l'ouverture
    qui porte le sens : c'est elle qu'on veut pouvoir régler, et c'est elle
    qui doit rester visible quand la marque est réduite à 16 pixels. Sous
    une certaine taille un trait presque fermé se lit comme un anneau plein
    et la figure ne dit plus rien.
    """
    a0 = milieu + ouverture / 2.0
    a1 = milieu - ouverture / 2.0 + 360.0
    x0, y0 = _pt(cx, cy, r, a0)
    x1, y1 = _pt(cx, cy, r, a1)
    grand = 1 if (a1 - a0) % 360.0 > 180.0 else 0
    return "M %s %s A %s %s 0 %d 1 %s %s" % (_f(x0), _f(y0), _f(r), _f(r),
                                             grand, _f(x1), _f(y1))


def _entete(largeur, hauteur, titre):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %s %s" '
            'width="%s" height="%s" role="img" aria-label="%s">'
            % (_f(largeur), _f(hauteur), _f(largeur), _f(hauteur), titre))


def marque(teinte=ROSE, second=None, titre="Le cercle ouvert"):
    """La marque : deux cercles ouverts et un point.

    Elle est monochrome par construction quand `second` n'est pas donné, ce
    qui lui permet de survivre à une impression une couleur, à une broderie
    et à un favicon. Les extrémités sont arrondies : un trait coupé net
    donne une impression de cassure, et c'est précisément le contraire de
    ce que la figure raconte.
    """
    b = second or teinte
    o = [_entete(LARGEUR, HAUTEUR, titre)]
    o.append('<g fill="none" stroke-linecap="round">')
    o.append('<path d="%s" stroke="%s" stroke-width="%s"/>'
             % (arc_ouvert(CX, CY, R_EXT, ANG_EXT, OUV_EXT), teinte,
                _f(EP_EXT)))
    o.append('<path d="%s" stroke="%s" stroke-width="%s"/>'
             % (arc_ouvert(CX, CY, R_INT, ANG_INT, OUV_INT), b, _f(EP_INT)))
    o.append("</g>")
    o.append('<circle cx="%s" cy="%s" r="%s" fill="%s"/>'
             % (_f(CX), _f(CY), _f(R_COEUR), teinte))
    o.append("</svg>")
    return "\n".join(o)


def favicon(fond=FONCE, teinte=CLAIR):
    """32 px : le cercle intérieur disparaît, l'ouverture doit rester.

    À cette taille deux traits concentriques se touchent et se lisent comme
    une tache. On garde donc un seul cercle, plus épais en proportion, et le
    point central.

    L'ouverture est déplacée en haut à gauche, et pas en haut comme sur la
    marque. Un anneau fendu VERS LE HAUT avec un point au centre, c'est le
    pictogramme universel de la mise en marche : à 16 pixels, dans un
    onglet, la première version se lisait comme un bouton d'alimentation.
    """
    o = [_entete(64, 64, "Le cercle ouvert")]
    o.append('<rect width="64" height="64" rx="12" fill="%s"/>' % fond)
    o.append('<path d="%s" fill="none" stroke="%s" stroke-width="7" '
             'stroke-linecap="round"/>'
             % (arc_ouvert(32, 32, 20, -142.0, 72.0), teinte))
    o.append('<circle cx="32" cy="32" r="4.6" fill="%s"/>' % teinte)
    o.append("</svg>")
    return "\n".join(o)


def tuile(cote=170.0, teinte=ROSE, epaisseur=1.4):
    """Fond répété, très faiblement opaque.

    Les quatre coins portent le MÊME arc, sinon le motif ne se raccorde pas
    quand `background-repeat` le répète : chaque coin ne montre qu'un quart
    de cercle, et c'est le quart du voisin qui le complète.

    Le rayon vaut 0,40 fois le côté et non la moitié. À la moitié exacte,
    les cercles voisins se coupent au milieu de chaque bord et dessinent une
    file d'ogives pointues — un motif d'architecture, très visible, qui n'a
    rien à faire ici.
    """
    r = cote * 0.40
    o = [_entete(cote, cote, "Motif de fond")]
    o.append('<g fill="none" stroke="%s" stroke-width="%s" '
             'stroke-linecap="round">' % (teinte, _f(epaisseur)))
    for cx, cy in ((0, 0), (cote, 0), (0, cote), (cote, cote)):
        o.append('<path d="%s"/>' % arc_ouvert(cx, cy, r, -90.0, 54.0))
    o.append('<path d="%s"/>' % arc_ouvert(r, r, cote * 0.28, 62.0, 74.0))
    o.append("</g>")
    o.append('<circle cx="%s" cy="%s" r="3" fill="%s"/>'
             % (_f(r), _f(r), teinte))
    o.append("</svg>")
    return "\n".join(o)


def frise(largeur=1200.0, hauteur=22.0, teinte=ROSE, pas=112.0):
    """Séparateur de section : un trait interrompu par de petits cercles.

    Purement décoratif — d'où `aria-hidden` partout où il est posé, et d'où
    le fait que son contraste de 2,37:1 sur la crème ne pose pas de
    problème : il ne porte aucune information.
    """
    cy = hauteur / 2.0
    o = [_entete(largeur, hauteur, "Frise")]
    o.append('<g stroke="%s" fill="none" stroke-width="1.2" '
             'stroke-linecap="round">' % teinte)
    x = 0.0
    while x < largeur:
        o.append('<path d="M %s %s L %s %s"/>'
                 % (_f(x + 9), _f(cy), _f(min(x + pas - 9, largeur)), _f(cy)))
        o.append('<path d="%s"/>' % arc_ouvert(x + pas, cy, 6.2, 40.0, 84.0))
        x += pas
    o.append("</g></svg>")
    return "\n".join(o)


def panneau(largeur=420.0, hauteur=520.0, teinte=ROSE, fond=FONCE,
            clair=CLAIR):
    """Le panneau qui prend la place d'une photographie.

    Des ondes concentriques, toutes ouvertes, dont l'ouverture tourne d'un
    cercle au suivant : de près on voit une trajectoire, de loin un calme.
    C'est délibérément abstrait. À chaque emplacement où une photo viendra
    un jour, le panneau est posé avec, en dessous, la phrase qui dit ce qui
    manque et à quelle condition il partira.
    """
    cx = largeur / 2.0
    cy = hauteur * 0.46
    o = [_entete(largeur, hauteur, "Panneau ornemental")]
    o.append('<rect width="%s" height="%s" fill="%s"/>'
             % (_f(largeur), _f(hauteur), fond))
    o.append('<g fill="none" stroke-linecap="round">')
    n = 7
    for i in range(n):
        r = largeur * (0.075 + 0.052 * i)
        ang = -90.0 + i * 41.0
        ouv = 44.0 + i * 4.0
        ep = 5.4 - i * 0.42
        col = clair if i % 3 == 1 else teinte
        op = 0.92 - i * 0.055
        o.append('<path d="%s" stroke="%s" stroke-width="%s" opacity="%s"/>'
                 % (arc_ouvert(cx, cy, r, ang, ouv), col, _f(ep), _f(op)))
    o.append("</g>")
    o.append('<circle cx="%s" cy="%s" r="7.5" fill="%s"/>'
             % (_f(cx), _f(cy), clair))
    o.append('<path d="M %s %s L %s %s" stroke="%s" stroke-width="1.6" '
             'opacity="0.55"/>'
             % (_f(largeur * 0.14), _f(hauteur * 0.855),
                _f(largeur * 0.86), _f(hauteur * 0.855), teinte))
    o.append("</svg>")
    return "\n".join(o)


def ecrire():
    if not os.path.isdir(ACTIFS):
        os.makedirs(ACTIFS)
    fichiers = {
        "marque-accent.svg": marque(ROSE),
        "marque-fonce.svg": marque(PRUNE),
        "marque-clair.svg": marque(CLAIR),
        "marque-duo.svg": marque(ROSE, PRUNE),
        "favicon.svg": favicon(),
        "tuile.svg": tuile(),
        "frise.svg": frise(),
        "panneau.svg": panneau(),
    }
    for nom, contenu in sorted(fichiers.items()):
        with open(os.path.join(ACTIFS, nom), "w", encoding="utf-8") as f:
            f.write(contenu + "\n")
        print("ecrit  assets/%s  (%d o)" % (nom, len(contenu) + 1))
    return len(fichiers)


if __name__ == "__main__":
    n = ecrire()
    print("%d fichiers d'ornement" % n)
