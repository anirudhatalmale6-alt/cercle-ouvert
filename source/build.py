# -*- coding: utf-8 -*-
"""
Génère les 18 pages du site (9 en français, 9 en anglais), la page
d'aiguillage à la racine, le plan de site et le fichier robots.

    python3 source/build.py

DÉMO — tant que DEMO vaut True, chaque page porte un bandeau qui dit que
c'est une démonstration ET une balise robots noindex, et le fichier robots
interdit tout. Un site d'association qui n'a encore ni nom validé, ni pays,
ni coordonnées ne doit pas pouvoir être trouvé par une personne en
difficulté qui chercherait de l'aide : elle arriverait sur une porte sans
sonnette. Passer DEMO à False au lancement retire les trois d'un coup.
"""

import os
import sys

_ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(_ICI) if os.path.basename(_ICI) == "source" else _ICI
sys.path.insert(0, _ICI)

import contenu as C  # noqa: E402

DEMO = True
VERSION_CSS = 3
BASE = "https://anirudhatalmale6-alt.github.io/cercle-ouvert/"

LANGUES = ("fr", "en")
HTML_LANG = {"fr": "fr", "en": "en"}


# ------------------------------------------------------------------ outils
def t(couple, lang):
    return couple[0] if lang == "fr" else couple[1]


def ech(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;")
             .replace(">", "&gt;").replace('"', "&quot;"))


def page(cle):
    for p in C.PAGES:
        if p[0] == cle:
            return p
    raise KeyError(cle)


def fichier(cle, lang):
    p = page(cle)
    return p[1] if lang == "fr" else p[2]


def titre(cle, lang):
    p = page(cle)
    return p[3] if lang == "fr" else p[4]


def lien(cle, lang, depuis_lang):
    """Les deux langues vivent dans des dossiers frères : un lien
    inter-langue remonte d'un cran."""
    if lang == depuis_lang:
        return fichier(cle, lang)
    return "../%s/%s" % (lang, fichier(cle, lang))


def actif(cle, courant):
    return ' aria-current="page"' if cle == courant else ""


# --------------------------------------------------------------- fragments
def paras(liste, lang):
    return "\n".join("<p>%s</p>" % t(c, lang) for c in liste)


def cartes(items, lang, niveau="h3", classe="g3"):
    """items : (titre fr, texte fr, titre en, texte en)."""
    o = ['<ul class="%s cartes">' % classe]
    for it in items:
        ti = it[0] if lang == "fr" else it[2]
        tx = it[1] if lang == "fr" else it[3]
        o.append('<li class="carte"><%s>%s</%s><p>%s</p></li>'
                 % (niveau, ti, niveau, tx))
    o.append("</ul>")
    return "\n".join(o)


def liste_simple(items, lang, classe="puces"):
    o = ['<ul class="%s">' % classe]
    for it in items:
        o.append("<li>%s</li>" % t(it, lang))
    o.append("</ul>")
    return "\n".join(o)


def etapes(items, lang):
    """Le parcours. Une liste ORDONNÉE, parce que l'ordre est le sens : on
    ne participe pas avant d'avoir été reçue."""
    o = ['<ol class="etapes">']
    for it in items:
        ti = it[0] if lang == "fr" else it[2]
        tx = it[1] if lang == "fr" else it[3]
        o.append("<li><h3>%s</h3><p>%s</p></li>" % (ti, tx))
    o.append("</ol>")
    return "\n".join(o)


def tableau(lang):
    """Le tableau des activités du chapitre 6.

    Un vrai <table> avec des en-têtes déclarés : c'est de la donnée
    tabulaire, et une grille de <div> la rendrait illisible à voix haute.
    Sur petit écran il défile dans son propre conteneur — jamais la page.
    """
    ent = C.ACTIVITES_ENTETES[0] if lang == "fr" else C.ACTIVITES_ENTETES[1]
    o = ['<div class="cadre-tableau" tabindex="0" role="region" '
         'aria-label="%s">' % ("Tableau des activités" if lang == "fr"
                               else "Table of activities")]
    o.append('<table class="activites"><thead><tr>')
    for e in ent:
        o.append('<th scope="col">%s</th>' % e)
    o.append("</tr></thead><tbody>")
    for a in C.ACTIVITES:
        n, b, f = (a[0], a[1], a[2]) if lang == "fr" else (a[3], a[4], a[5])
        o.append('<tr><th scope="row">%s</th><td>%s</td>'
                 '<td class="freq">%s</td></tr>' % (n, b, f))
    o.append("</tbody></table></div>")
    o.append('<p class="note">%s</p>' % t(C.ACTIVITES_NOTE, lang))
    return "\n".join(o)


def attentes(items, lang):
    """Le bloc « À fixer ».

    Chaque ligne porte le mot d'attente ET la condition qui la lèvera. Une
    ligne vide sans condition ne dit pas au lecteur ce qui manque ; elle dit
    seulement qu'on n'a pas fini.
    """
    mot = t(C.ATTENTE, lang)
    o = ['<ul class="liste-attente">']
    for it in items:
        ti = it[0] if lang == "fr" else it[2]
        cd = it[1] if lang == "fr" else it[3]
        o.append('<li><span class="att">%s</span>'
                 '<strong>%s</strong><span class="cond">%s</span></li>'
                 % (mot, ti, cd))
    o.append("</ul>")
    return "\n".join(o)


def prudence(lang):
    return ('<aside class="prudence" role="note"><p>%s</p>'
            '<p class="confid">%s</p></aside>'
            % (t(C.PRUDENCE, lang), t(C.CONFID, lang)))


def panneau_image(lang, legende_fr, legende_en, prefixe):
    """Emplacement d'image : un ornement dessiné, jamais une photo de
    personne, ni réelle ni générée."""
    lg = legende_fr if lang == "fr" else legende_en
    return ('<figure class="panneau"><img src="%sassets/panneau.svg" alt="" '
            'width="420" height="520" aria-hidden="true">'
            "<figcaption>%s</figcaption></figure>" % (prefixe, lg))


def bouton_principal(lang, depuis, classe="btn btn-fonce"):
    return ('<a class="%s" href="%s">%s</a>'
            % (classe, lien("contact", lang, depuis), t(C.MENU_CTA, lang)))


def actions(lang, secondaire=None):
    o = ['<p class="actions">', bouton_principal(lang, lang)]
    if secondaire:
        o.append('<a class="btn btn-ligne" href="%s">%s</a>'
                 % (lien(secondaire, lang, lang), titre(secondaire, lang)))
    o.append("</p>")
    return "".join(o)


def sec(idn, titre_txt, corps, classe=""):
    return ('<section id="%s"%s><h2>%s</h2>\n%s\n</section>'
            % (idn, ' class="%s"' % classe if classe else "",
               titre_txt, corps))


def frise():
    return '<hr class="frise" aria-hidden="true">'


# ------------------------------------------------------------------ entête
def entete(cle, lang, prefixe):
    autre = "en" if lang == "fr" else "fr"
    fr = lang == "fr"
    o = []
    o.append('<a class="saut" href="#principal">%s</a>'
             % ("Aller au contenu" if fr else "Skip to content"))
    if DEMO:
        o.append('<p class="bandeau-demo">%s</p>' % t(C.DEMO_BANDEAU, lang))

    o.append('<div class="util"><div class="dans">')
    o.append('<span class="mention">%s</span>'
             % ("Confidentiel &middot; sans jugement" if fr
                else "Confidential &middot; no judgment"))
    o.append('<a class="langue" href="%s" lang="%s" hreflang="%s">%s</a>'
             % (lien(cle, autre, lang), HTML_LANG[autre], HTML_LANG[autre],
                t(C.PIED_LANGUE, autre)))
    # Sortie rapide : un vrai lien, pas un bouton. Sans JavaScript il
    # fonctionne quand même ; avec JavaScript il remplace l'entrée
    # d'historique au lieu d'en ajouter une.
    o.append('<a class="sortie" href="%s" rel="noopener noreferrer" '
             'data-sortie="1"><span aria-hidden="true">&#10005;</span> %s</a>'
             % (C.SORTIE_URL, t(C.SORTIE, lang)))
    o.append("</div></div>")

    o.append('<header class="hdr"><div class="dans">')
    o.append('<a class="marque" href="%s">'
             '<img src="%sassets/marque-duo.svg" alt="" width="34" '
             'height="34" aria-hidden="true">'
             '<span class="bloc-nom"><span class="nom">%s</span>'
             '<span class="prov">%s</span></span>'
             '<span class="base">%s</span></a>'
             % (lien("accueil", lang, lang), prefixe, t(C.MARQUE, lang),
                t(C.NOM_TRAVAIL, lang), t(C.BASELINE, lang)))
    o.append('<button class="burger" type="button" aria-expanded="false" '
             'aria-controls="panneau-nav"><span class="barres" '
             'aria-hidden="true"></span><span class="vh">Menu</span></button>')
    o.append('<div class="panneau-nav" id="panneau-nav">')
    o.append('<nav aria-label="%s"><ul>'
             % ("Navigation principale" if fr else "Main navigation"))
    for p in C.PAGES:
        if not p[5]:
            continue
        o.append('<li><a href="%s"%s>%s</a></li>'
                 % (lien(p[0], lang, lang), actif(p[0], cle),
                    t(C.MENU_COURT[p[0]], lang)))
    o.append("</ul></nav>")
    o.append('<a class="btn btn-fonce cta-nav" href="%s"%s>%s</a>'
             % (lien("contact", lang, lang), actif("contact", cle),
                t(C.MENU_CTA_COURT, lang)))
    o.append("</div></div></header>")
    return "\n".join(o)


def fil(cle, lang):
    if cle == "accueil":
        return ""
    lab = "Fil d'Ariane" if lang == "fr" else "Breadcrumb"
    o = ['<nav class="fil" aria-label="%s"><ol>' % lab]
    o.append('<li><a href="%s">%s</a></li>'
             % (lien("accueil", lang, lang), titre("accueil", lang)))
    o.append('<li><span aria-current="page">%s</span></li>' % titre(cle, lang))
    o.append("</ol></nav>")
    return "\n".join(o)


def pied(cle, lang, prefixe):
    fr = lang == "fr"
    o = ['<footer class="pied"><div class="dans">']
    o.append('<div class="cols">')

    o.append('<div class="col col-marque">')
    o.append('<img src="%sassets/marque-clair.svg" alt="" width="40" '
             'height="40" aria-hidden="true">' % prefixe)
    o.append("<p><strong>%s</strong><br>%s</p>"
             % (t(C.MARQUE, lang), t(C.BASELINE, lang)))
    o.append('<p class="prov-pied">%s</p>'
             % ("Nom de travail, non validé." if fr
                else "Working name, not settled."))
    o.append("</div>")

    o.append('<div class="col"><h2>%s</h2><ul>'
             % ("L'association" if fr else "The association"))
    for k in ("mission", "services", "calendrier"):
        o.append('<li><a href="%s">%s</a></li>' % (lien(k, lang, lang),
                                                   titre(k, lang)))
    o.append("</ul></div>")

    o.append('<div class="col"><h2>%s</h2><ul>'
             % ("Participer" if fr else "Take part"))
    for k in ("benevolat", "contact"):
        o.append('<li><a href="%s">%s</a></li>' % (lien(k, lang, lang),
                                                   titre(k, lang)))
    o.append("</ul></div>")

    o.append('<div class="col"><h2>%s</h2><ul>'
             % ("Informations" if fr else "Information"))
    for k in ("confidentialite", "mentions", "accessibilite"):
        o.append('<li><a href="%s">%s</a></li>' % (lien(k, lang, lang),
                                                   titre(k, lang)))
    o.append("</ul></div>")
    o.append("</div>")

    o.append('<div class="bas">')
    o.append("<p>%s</p>" % t(C.PRUDENCE, lang))
    o.append('<p class="mini">%s</p>' % t(C.CONFID, lang))
    o.append('<p class="mini">%s</p>' % t(C.SORTIE_AIDE, lang))
    if DEMO:
        o.append('<p class="mini">%s</p>' % t(C.PIED_DECLARATION, lang))
    o.append("</div></div></footer>")

    # Barre d'actions mobile : la demande d'accueil et la sortie rapide.
    # Ce sont les deux seuls gestes qui doivent rester à portée de pouce.
    o.append('<div class="barre-mobile">'
             '<a class="btn btn-fonce" href="%s">%s</a>'
             '<a class="btn btn-sortie" href="%s" rel="noopener noreferrer" '
             'data-sortie="1">%s</a></div>'
             % (lien("contact", lang, lang), t(C.MENU_CTA_COURT, lang),
                C.SORTIE_URL, t(C.SORTIE, lang)))
    return "\n".join(o)


# ------------------------------------------------------------- constructeurs
def b_accueil(lang, prefixe):
    fr = lang == "fr"
    o = []
    o.append('<section class="heros"><div class="dans heros-grille">')
    o.append('<div class="heros-texte">')
    o.append('<img class="heros-marque" src="%sassets/marque-clair.svg" '
             'alt="" width="76" height="76" aria-hidden="true">' % prefixe)
    o.append("<h1>%s</h1>" % t(C.ACC_TITRE, lang))
    o.append('<p class="chapo">%s</p>' % t(C.ACC_SOUS, lang))
    o.append('<p class="actions">%s'
             '<a class="btn btn-ligne" href="%s">%s</a></p>'
             % (bouton_principal(lang, lang, "btn btn-clair"),
                lien("services", lang, lang), titre("services", lang)))
    o.append("</div>")
    o.append('<div class="heros-image">')
    o.append('<img src="%sassets/panneau.svg" alt="" width="420" '
             'height="520" aria-hidden="true">' % prefixe)
    o.append("</div>")
    o.append("</div></section>")

    o.append('<div class="dans">')
    o.append(sec("intro", "L'association" if fr else "The association",
                 paras(C.ACC_INTRO, lang) + "\n"
                 + cartes(C.ACC_PILIERS, lang, classe="g2")))
    o.append(frise())

    corps = "<p>%s</p>\n" % t(C.ACC_CHEMIN_TEXTE, lang)
    corps += etapes(C.PARCOURS, lang)
    corps += actions(lang, "services")
    o.append(sec("chemin", t(C.ACC_CHEMIN, lang), corps))
    o.append(frise())

    corps = "<p>%s</p>\n" % t(C.CAL_INTRO, lang)
    corps += "<p>%s</p>\n" % (C.CAL_TEXTE[1][0] if fr else C.CAL_TEXTE[1][1])
    corps += ('<p class="actions"><a class="btn btn-ligne" href="%s">%s</a>'
              "</p>" % (lien("calendrier", lang, lang),
                        titre("calendrier", lang)))
    o.append(sec("dates", "Les dates" if fr else "Dates", corps))
    o.append(prudence(lang))
    o.append("</div>")
    return "\n".join(o), t(C.META["accueil"], lang)


def b_mission(lang, prefixe):
    fr = lang == "fr"
    o = ['<div class="dans">']
    o.append("<h1>%s</h1>" % titre("mission", lang))
    o.append('<p class="chapo">%s</p>' % t(C.MISSION_INTRO, lang))
    o.append(sec("objectifs", "Les objectifs" if fr else "The objectives",
                 liste_simple(C.MISSION_OBJECTIFS, lang)))
    o.append(frise())
    o.append(sec("public", "Qui l'association accueille" if fr
                 else "Who the association welcomes",
                 cartes(C.MISSION_PUBLIC, lang)))
    o.append(frise())
    o.append(sec("missions", "Les missions" if fr else "The missions",
                 cartes(C.MISSION_MISSIONS, lang)))
    o.append(frise())
    o.append(sec("regles", "Les règles de fonctionnement" if fr
                 else "The operating rules",
                 liste_simple(C.MISSION_REGLES, lang, "puces regles"),
                 classe="limites"))
    o.append(frise())
    o.append(sec("indicateurs", "Ce que l'association mesurera" if fr
                 else "What the association will measure",
                 "<p>%s</p>\n" % t(C.MISSION_INDICATEURS_INTRO, lang)
                 + liste_simple(C.MISSION_INDICATEURS, lang)))
    o.append(prudence(lang))
    o.append(actions(lang, "services"))
    o.append("</div>")
    return "\n".join(o), t(C.META["mission"], lang)


def b_services(lang, prefixe):
    fr = lang == "fr"
    o = ['<div class="dans">']
    o.append("<h1>%s</h1>" % titre("services", lang))
    o.append('<p class="chapo">%s</p>' % t(C.SERVICES_INTRO, lang))
    o.append('<div class="g2 service-grille"><div>')
    o.append(sec("offre", "Ce qui est proposé" if fr else "What is offered",
                 liste_simple(C.SERVICES_LISTE, lang)))
    o.append("</div><div>")
    o.append(panneau_image(
        lang,
        "Panneau dessiné. Aucune photographie de personne n'est utilisée sur "
        "ce site, ni réelle ni générée — chapitres 9 et 11.",
        "Drawn panel. No photograph of a person is used on this site, "
        "neither real nor generated — chapters 9 and 11.", prefixe))
    o.append("</div></div>")
    o.append(frise())
    o.append(sec("activites", "Le programme de bien-être" if fr
                 else "The well-being programme", tableau(lang)))
    o.append(frise())
    o.append(sec("parcours", "Le parcours d'accompagnement" if fr
                 else "The support pathway", etapes(C.PARCOURS, lang)))
    o.append(frise())
    o.append(sec("attente", "Ce qui reste à fixer" if fr
                 else "What is still to be set",
                 attentes(C.SERVICES_ATTENTES, lang)))
    o.append(prudence(lang))
    o.append(actions(lang, "calendrier"))
    o.append("</div>")
    return "\n".join(o), t(C.META["services"], lang)


def b_calendrier(lang, prefixe):
    fr = lang == "fr"
    o = ['<div class="dans">']
    o.append("<h1>%s</h1>" % titre("calendrier", lang))
    o.append('<p class="chapo">%s</p>' % t(C.CAL_INTRO, lang))
    o.append(paras(C.CAL_TEXTE, lang))
    o.append(sec("rythmes", "Les rythmes annoncés" if fr
                 else "The stated rhythms", tableau(lang)))
    o.append(frise())
    o.append(sec("attente", "Ce qui reste à fixer" if fr
                 else "What is still to be set",
                 attentes(C.CAL_ATTENTES, lang)
                 + '\n<p class="note">%s</p>' % t(C.CAL_APRES, lang)))
    o.append(prudence(lang))
    o.append(actions(lang, "services"))
    o.append("</div>")
    return "\n".join(o), t(C.META["calendrier"], lang)


def b_benevolat(lang, prefixe):
    fr = lang == "fr"
    o = ['<div class="dans">']
    o.append("<h1>%s</h1>" % titre("benevolat", lang))
    o.append('<p class="chapo">%s</p>' % t(C.BEN_INTRO, lang))
    o.append(sec("roles", "Les rôles internes" if fr
                 else "The internal roles", cartes(C.BEN_ROLES, lang)))
    o.append(frise())
    o.append(sec("partenaires", "Les partenariats recherchés" if fr
                 else "The partnerships sought",
                 liste_simple(C.BEN_PARTENAIRES, lang)))
    o.append(frise())
    o.append(sec("attente", "Ce qui reste à fixer" if fr
                 else "What is still to be set",
                 attentes(C.BEN_ATTENTES, lang)))
    o.append(prudence(lang))
    o.append(actions(lang, "mission"))
    o.append("</div>")
    return "\n".join(o), t(C.META["benevolat"], lang)


def b_contact(lang, prefixe):
    fr = lang == "fr"
    o = ['<div class="dans">']
    o.append("<h1>%s</h1>" % titre("contact", lang))
    o.append('<p class="chapo">%s</p>' % t(C.CONTACT_INTRO, lang))
    o.append('<div class="g2 form-grille"><div>')
    o.append('<form class="formulaire" novalidate '
             'aria-describedby="form-note">')
    o.append('<p class="avertissement" id="form-note">%s</p>'
             % t(C.CONTACT_AVERT, lang))
    for (nom, lfr, len_, typ, requis, afr, aen) in C.CHAMPS:
        lab = lfr if fr else len_
        aide = afr if fr else aen
        req = ' <span class="req" aria-hidden="true">*</span>' if requis else ""
        o.append('<p class="champ">')
        o.append('<label for="c-%s">%s%s</label>' % (nom, lab, req))
        o.append('<span class="aide" id="a-%s">%s</span>' % (nom, aide))
        if typ == "textarea":
            o.append('<textarea id="c-%s" name="%s" rows="4" maxlength="400" '
                     'aria-describedby="a-%s"></textarea>' % (nom, nom, nom))
        elif typ == "select":
            o.append('<select id="c-%s" name="%s" aria-describedby="a-%s"%s>'
                     % (nom, nom, nom, " required" if requis else ""))
            o.append('<option value="">%s</option>'
                     % ("Sans réponse" if fr else "No answer"))
            source = {"moment": C.MOMENTS, "langue": C.LANGUES_CHOIX,
                      "besoin": C.BESOINS}[nom]
            for v, vfr, ven in source:
                o.append('<option value="%s">%s</option>'
                         % (v, vfr if fr else ven))
            o.append("</select>")
        else:
            o.append('<input id="c-%s" name="%s" type="text" '
                     'autocomplete="off" aria-describedby="a-%s"%s>'
                     % (nom, nom, nom, " required" if requis else ""))
        o.append('<span class="erreur" id="e-%s" role="alert"></span>' % nom)
        o.append("</p>")
    for (nom, cfr, cen, requis) in C.CONSENTEMENTS:
        o.append('<p class="champ case"><label for="k-%s">'
                 '<input id="k-%s" name="%s" type="checkbox"%s> <span>%s'
                 "</span></label>"
                 '<span class="erreur" id="e-%s" role="alert"></span></p>'
                 % (nom, nom, nom, " required" if requis else "",
                    cfr if fr else cen, nom))
    o.append('<p class="lien-conf"><a href="%s">%s</a></p>'
             % (lien("confidentialite", lang, lang),
                titre("confidentialite", lang)))
    o.append('<p class="actions"><button class="btn btn-fonce" '
             'type="submit">%s</button></p>'
             % ("Envoyer la demande" if fr else "Send the request"))
    o.append('<p class="etat" id="form-etat" role="status"></p>')
    o.append("</form>")
    o.append("</div><div>")
    o.append(sec("attente", "Ce qui reste à fixer" if fr
                 else "What is still to be set",
                 attentes(C.CONTACT_ATTENTES, lang)))
    o.append("</div></div>")
    o.append(prudence(lang))
    o.append("</div>")
    return "\n".join(o), t(C.META["contact"], lang)


def b_confidentialite(lang, prefixe):
    fr = lang == "fr"
    o = ['<div class="dans">']
    o.append("<h1>%s</h1>" % titre("confidentialite", lang))
    o.append('<p class="chapo">%s</p>' % t(C.CONF_INTRO, lang))
    o.append('<aside class="prudence" role="note"><p>%s</p></aside>'
             % t(C.CONF_JURIDIQUE, lang))
    o.append(sec("faits", "Ce qui est vrai aujourd'hui" if fr
                 else "What is true today", cartes(C.CONF_FAITS, lang)))
    o.append(frise())
    o.append(sec("attente", "Ce qui doit être décidé avant la mise en ligne"
                 if fr else "What must be decided before launch",
                 attentes(C.CONF_ATTENTES, lang)))
    o.append("</div>")
    return "\n".join(o), t(C.META["confidentialite"], lang)


def b_mentions(lang, prefixe):
    fr = lang == "fr"
    o = ['<div class="dans">']
    o.append("<h1>%s</h1>" % titre("mentions", lang))
    o.append('<p class="chapo">%s</p>' % t(C.MENT_INTRO, lang))
    o.append(sec("attente", "Ce qui reste à fixer" if fr
                 else "What is still to be set",
                 attentes(C.MENT_ATTENTES, lang)))
    o.append(prudence(lang))
    o.append("</div>")
    return "\n".join(o), t(C.META["mentions"], lang)


def b_accessibilite(lang, prefixe):
    fr = lang == "fr"
    o = ['<div class="dans">']
    o.append("<h1>%s</h1>" % titre("accessibilite", lang))
    o.append('<p class="chapo">%s</p>' % t(C.ACCESS_INTRO, lang))
    o.append(sec("fait", "Ce qui a été mesuré" if fr
                 else "What has been measured", cartes(C.ACCESS_FAIT, lang)))
    o.append(frise())
    o.append(sec("pas-fait", "Ce qui ne l'a pas été" if fr
                 else "What has not been", cartes(C.ACCESS_PAS_FAIT, lang),
                 classe="limites"))
    o.append('<p class="note">%s</p>'
             % ("Un obstacle rencontré sur ce site pourra être signalé dès "
                "qu'une ligne d'accueil existera ; il sera traité comme une "
                "anomalie, pas comme une préférence."
                if fr else
                "Any barrier found on this site will be reportable as soon "
                "as a contact line exists; it will be treated as a defect, "
                "not as a preference."))
    o.append("</div>")
    return "\n".join(o), t(C.META["accessibilite"], lang)


BATISSEURS = {
    "accueil": b_accueil,
    "mission": b_mission,
    "services": b_services,
    "calendrier": b_calendrier,
    "benevolat": b_benevolat,
    "contact": b_contact,
    "confidentialite": b_confidentialite,
    "mentions": b_mentions,
    "accessibilite": b_accessibilite,
}


# ------------------------------------------------------------------- gabarit
def gabarit(cle, lang):
    prefixe = "../"
    corps, desc = BATISSEURS[cle](lang, prefixe)
    # Une description trop courte ou trop longue est tronquée ou ignorée par
    # les moteurs. Ça a déjà cassé une livraison, donc c'est une assertion.
    if not 40 < len(desc) < 320:
        raise SystemExit("description %s/%s : %d caracteres"
                         % (cle, lang, len(desc)))
    ttl = titre(cle, lang)
    marque = t(C.MARQUE, lang)
    ttl_complet = ("%s — %s" % (marque, t(C.BASELINE, lang))
                   if cle == "accueil" else "%s — %s" % (ttl, marque))
    o = ["<!doctype html>", '<html lang="%s">' % HTML_LANG[lang], "<head>",
         '<meta charset="utf-8">',
         '<meta name="viewport" content="width=device-width,'
         'initial-scale=1">',
         "<title>%s</title>" % ech(ttl_complet),
         '<meta name="description" content="%s">' % ech(desc)]
    if DEMO:
        o.append('<meta name="robots" content="noindex,nofollow">')
    # Pas de données structurées. Déclarer une Organization dont le nom est
    # un nom de travail, sans adresse, sans pays et sans téléphone, publie
    # une identité qui n'existe pas ; et c'est exactement ce qu'un moteur
    # recopierait dans un panneau de résultats.
    o.append('<link rel="canonical" href="%s%s/%s">'
             % (BASE, lang, fichier(cle, lang)))
    for lg in LANGUES:
        o.append('<link rel="alternate" hreflang="%s" href="%s%s/%s">'
                 % (HTML_LANG[lg], BASE, lg, fichier(cle, lg)))
    o.append('<link rel="alternate" hreflang="x-default" href="%sfr/%s">'
             % (BASE, fichier(cle, "fr")))
    o.append('<link rel="icon" href="../assets/favicon.svg" '
             'type="image/svg+xml">')
    o.append('<link rel="stylesheet" href="../assets/site.css?v=%d">'
             % VERSION_CSS)
    o.append('<meta property="og:title" content="%s">' % ech(ttl_complet))
    o.append('<meta property="og:description" content="%s">' % ech(desc))
    o.append('<meta property="og:type" content="website">')
    o.append('<meta property="og:locale" content="%s">' % HTML_LANG[lang])
    o.append("</head>")
    o.append('<body class="p-%s">' % cle)
    o.append(entete(cle, lang, prefixe))
    o.append('<main id="principal" tabindex="-1">')
    if cle != "accueil":
        o.append('<div class="dans">%s</div>' % fil(cle, lang))
    o.append(corps)
    o.append("</main>")
    o.append(pied(cle, lang, prefixe))
    o.append('<script src="../assets/site.js?v=%d" defer></script>'
             % VERSION_CSS)
    o.append("</body></html>")
    return "\n".join(o)


def aiguillage():
    """Racine : les deux langues vivent dans /fr/ et /en/, donc la racine ne
    porte aucun contenu — seulement le renvoi."""
    o = ["<!doctype html>", '<html lang="fr">', "<head>",
         '<meta charset="utf-8">',
         '<meta name="viewport" content="width=device-width,'
         'initial-scale=1">',
         '<meta http-equiv="refresh" content="0; url=fr/">',
         '<meta name="robots" content="noindex,nofollow">',
         "<title>%s — %s</title>" % (C.MARQUE[0], C.BASELINE[0]),
         '<link rel="canonical" href="%sfr/index.html">' % BASE,
         '<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">',
         '<link rel="stylesheet" href="assets/site.css?v=%d">' % VERSION_CSS,
         "</head>",
         '<body class="p-aiguillage"><main id="principal" class="dans">',
         '<img src="assets/marque-duo.svg" alt="" width="76" height="76" '
         'aria-hidden="true">',
         "<h1>%s</h1>" % C.MARQUE[0],
         '<p><a href="fr/index.html">Continuer en français</a></p>',
         '<p><a href="en/index.html">Continue in English</a></p>',
         "</main></body></html>"]
    return "\n".join(o)


def plan_du_site():
    o = ['<?xml version="1.0" encoding="UTF-8"?>',
         '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
         'xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for p in C.PAGES:
        for lg in LANGUES:
            o.append("<url><loc>%s%s/%s</loc>" % (BASE, lg,
                                                  fichier(p[0], lg)))
            for lg2 in LANGUES:
                o.append('<xhtml:link rel="alternate" hreflang="%s" '
                         'href="%s%s/%s"/>'
                         % (HTML_LANG[lg2], BASE, lg2, fichier(p[0], lg2)))
            o.append("</url>")
    o.append("</urlset>")
    return "\n".join(o)


def robots():
    if DEMO:
        return "User-agent: *\nDisallow: /\n"
    return "User-agent: *\nAllow: /\nSitemap: %ssitemap.xml\n" % BASE


def main():
    n = 0
    for lang in LANGUES:
        dossier = os.path.join(RACINE, lang)
        if not os.path.isdir(dossier):
            os.makedirs(dossier)
        for p in C.PAGES:
            html = gabarit(p[0], lang)
            with open(os.path.join(dossier, fichier(p[0], lang)), "w",
                      encoding="utf-8") as f:
                f.write(html + "\n")
            n += 1
    with open(os.path.join(RACINE, "index.html"), "w",
              encoding="utf-8") as f:
        f.write(aiguillage() + "\n")
    with open(os.path.join(RACINE, "sitemap.xml"), "w",
              encoding="utf-8") as f:
        f.write(plan_du_site() + "\n")
    with open(os.path.join(RACINE, "robots.txt"), "w",
              encoding="utf-8") as f:
        f.write(robots())
    print("%d pages + aiguillage + sitemap + robots  (DEMO=%s)" % (n, DEMO))


if __name__ == "__main__":
    main()
