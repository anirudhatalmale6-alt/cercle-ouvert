# -*- coding: utf-8 -*-
"""
Vérification du site.

Deux natures de contrôle, et la seconde est la seule qui prouve quelque
chose : lire la source dit ce qui a été écrit, mesurer le rendu dit ce que
le navigateur a fait. Les contrastes, les proportions d'images, les
débordements, les ancres et les requêtes réseau sont donc mesurés dans un
Chromium réel, jamais déduits de la feuille de style.

    python3 tests/verif.py [http://127.0.0.1:8874/]
"""

import io
import os
import re
import sys

from playwright.sync_api import sync_playwright
from PIL import Image

_ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(_ICI)
sys.path.insert(0, os.path.join(RACINE, "source"))

import contenu as C          # noqa: E402
import build as B            # noqa: E402

BASE = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8874/"
if not BASE.endswith("/"):
    BASE += "/"

# Les largeurs encadrent CHAQUE point de bascule de la feuille de style
# (420, 760, 800, 900, 1000, 1260) : une règle qui ne se trompe qu'à
# l'intérieur d'une bande étroite ne peut pas se cacher entre deux mesures.
LARGEURS = [320, 360, 390, 414, 419, 421, 480, 600, 759, 761, 799, 801, 899,
            1000, 1001, 1024, 1180, 1259, 1260, 1366, 1440]

ok = 0
echecs = []


def v(cond, nom):
    global ok
    if cond:
        ok += 1
    else:
        echecs.append(nom)


# ---------------------------------------------------------------- motifs
# Chaque motif décrit une AFFIRMATION interdite. « n'est pas garanti » doit
# passer, « est garanti » doit échouer, et une question doit passer.
NEGATIONS = re.compile(
    r"\b(no|not|never|nor|neither|without|cannot|can't|non|ne|n'|ni|"
    r"aucun|aucune|jamais|sans|pas|rien|nothing)\b", re.I)

INTERDITS = [
    # promesses de résultat
    (r"\b(est|sont|seront)\s+garanti", "promesse : garanti"),
    (r"\b(is|are|will be)\s+guaranteed", "promise: guaranteed"),
    (r"\brésultat[s]?\s+(assuré|garanti)", "promesse : resultat assure"),
    (r"\b(guérir|guérison|guérit)\b", "sante : guerison"),
    (r"\b(cures?|healed|healing)\b", "health: cure"),
    (r"\bvous\s+(irez|allez aller)\s+mieux\b", "promesse : aller mieux"),
    (r"\bwill\s+feel\s+better\b", "promise: will feel better"),
    # l'association n'est pas un soignant ni un conseil juridique
    (r"\b(thérapie|psychothérapie|traitement médical)\b", "soin : therapie"),
    (r"\b(therapy|psychotherapy|medical treatment)\b", "care: therapy"),
    (r"\b(conseil|avis)\s+juridique\b", "juridique : conseil"),
    (r"\blegal\s+advice\b", "legal: advice"),
    # superlatifs invérifiables
    (r"\ble\s+meilleur\b|\bla\s+meilleure\b", "superlatif : le meilleur"),
    (r"\bthe\s+best\b", "superlative: the best"),
    (r"\b100\s*%\b", "superlatif : 100 %"),
    # argent : le cahier des charges dit « sans composante financière », il
    # ne dit pas que tout est gratuit. Affirmer la gratuité est une
    # affirmation sur l'argent que personne n'a écrite.
    (r"\bgratuit", "argent : gratuite affirmee"),
    (r"\bfree\s+of\s+charge\b", "money: free of charge"),
    (r"[$€£]\s?\d|\b\d+\s?(CAD|USD|EUR|euros?|dollars?)\b", "chiffre : prix"),
    # chiffres que personne n'a relevés
    (r"\b\d+\s*(ans|années)\s+d['’]expérience", "chiffre : annees"),
    (r"\b\d+\s*years?\s+of\s+experience", "figure: years"),
    (r"\b\d+\s+(mères|femmes|adhérentes|bénévoles)\b",
     "chiffre : frequentation"),
    (r"\b\d+\s+(mothers|women|members|volunteers)\b", "figure: attendance"),
    # horaires et dates inventés
    (r"\b(lundi|mardi|mercredi|jeudi|vendredi|samedi|dimanche)\b",
     "horaire : jour"),
    (r"\b(monday|tuesday|wednesday|thursday|friday|saturday|sunday)\b",
     "schedule: day"),
    (r"\b\d{1,2}\s?h\s?\d{2}\b|\b\d{1,2}:\d{2}\s?(am|pm)\b",
     "horaire : heure"),
    (r"\b(janvier|février|mars|avril|juin|juillet|août|septembre|octobre|"
     r"novembre|décembre)\s+\d{4}\b", "date inventee"),
    # coordonnées : il n'en existe aucune, donc aucune ne doit apparaître
    (r"\+\d[\d\s().-]{7,}", "coordonnee : telephone"),
    (r"\b\d{5}\b", "coordonnee : code postal"),
    (r"[\w.+-]+@[\w-]+\.[a-z]{2,}", "coordonnee : adresse electronique"),
]

MESURE = re.compile(
    r"gtag\(|googletagmanager|google-analytics|matomo\.js|plausible\.io|"
    r"facebook\.net|hotjar|clarity\.ms|<script[^>]*analytic", re.I)

# Les images autorisées : uniquement les ornements produits par motif.py.
# Une photographie de personne ne peut donc pas entrer sans faire échouer
# ce contrôle — c'est la traduction mécanique des chapitres 9 et 11.
IMAGES_PERMISES = {"marque-accent.svg", "marque-fonce.svg", "marque-clair.svg",
                   "marque-duo.svg", "favicon.svg", "tuile.svg", "frise.svg",
                   "panneau.svg"}

# Les mots d'attente des autres chantiers du même client. Ils ne doivent
# jamais servir d'ÉTIQUETTE ici : c'est ce qui permet de savoir, en
# regardant une capture, de quel projet elle vient.
AUTRES_ATTENTES = ("à vérifier", "à définir", "To be decided",
                   "En attente d'autorisation", "À confirmer",
                   "To be confirmed")


def touches(motif, txt):
    """Occurrences NON niées et NON interrogatives d'un motif.

    La négation gouverne sa PHRASE, pas un nombre arbitraire de caractères ;
    et une QUESTION n'est pas une affirmation. Un contrôle qui ne regarde
    que vers l'arrière échoue sur « Est-ce que les résultats sont garantis ?
    — Non. » : le motif tombe dans l'interrogation et la négation est dans
    la phrase suivante. On lit donc aussi la fin de la phrase.
    """
    out = []
    for m in re.finditer(motif, txt, re.I):
        deb = max((txt.rfind(c, 0, m.start()) for c in ".!?;\n"), default=-1)
        fins = [p for p in (txt.find(c, m.end()) for c in ".!?;\n") if p >= 0]
        fin = min(fins) if fins else len(txt)
        avant = txt[deb + 1:m.start()]
        if NEGATIONS.search(avant):
            continue
        if txt[fin:fin + 1] == "?":
            continue
        out.append(m.group(0))
    return out


def sans_balises(h):
    h = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", h, flags=re.S | re.I)
    h = re.sub(r"<[^>]+>", " ", h)
    h = h.replace("&nbsp;", " ").replace("&mdash;", "—")
    h = h.replace("&amp;", "&").replace("&laquo;", "«").replace("&raquo;", "»")
    h = h.replace("&middot;", "·").replace("&quot;", '"')
    h = h.replace("&#10005;", " ").replace("&#8250;", "›")
    return re.sub(r"\s+", " ", h)


# ----------------------------------------------------- contraste mesuré
def luminance(rgb):
    def f(c):
        c = c / 255.0
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(rgb[0]) + 0.7152 * f(rgb[1]) + 0.0722 * f(rgb[2])


def contraste(a, b):
    la, lb = luminance(a), luminance(b)
    if la < lb:
        la, lb = lb, la
    return (la + 0.05) / (lb + 0.05)


def couleur_css(s):
    m = re.findall(r"[\d.]+", s or "")
    if len(m) < 3:
        return None
    return (int(float(m[0])), int(float(m[1])), int(float(m[2])))


def contraste_mesure(pg, selecteur):
    """Contraste réel du texte contre ce qui est peint derrière lui.

    Méthode : rendre le TEXTE transparent, photographier la zone, retenir le
    pixel de fond le plus défavorable.

    Deux pièges, et chacun a déjà donné une lecture fausse dans un projet
    précédent. Cacher l'élément entier (`visibility:hidden`) découvre le
    fond de l'ANCÊTRE : pour un bandeau, un badge ou un bouton, on mesure
    alors le texte contre une couleur qui n'est jamais visible sous lui.
    Et classer les pixels par LUMINANCE suppose du texte clair sur fond
    sombre ; pour du texte sombre sur fond clair, le pire cas est le pixel
    le plus sombre, et le classement donnait la réponse la plus flatteuse.
    On classe donc par contraste et on retient le 2e centile.
    """
    infos = pg.evaluate("""(s)=>{const e=document.querySelector(s);
      if(!e) return null; const r=e.getBoundingClientRect();
      if(r.width<4||r.height<4) return null;
      const st=getComputedStyle(e);
      const b=x=>parseFloat(st['border'+x+'Width'])||0;
      return {x:r.x,y:r.y,w:r.width,h:r.height,couleur:st.color,
              bt:b('Top'),br:b('Right'),bb:b('Bottom'),bl:b('Left')};}""",
                        selecteur)
    if not infos:
        return None, None
    fg = couleur_css(infos["couleur"])
    if not fg:
        return None, None
    mx = infos["bl"] + 2
    my = infos["bt"] + 2
    x = max(0.0, infos["x"] + mx)
    y = max(0.0, infos["y"] + my)
    w = max(4.0, infos["w"] - mx - infos["br"] - 2)
    h = max(4.0, infos["h"] - my - infos["bb"] - 2)

    pg.evaluate("""(s)=>{const e=document.querySelector(s);
      e.dataset.c=e.style.color||''; e.style.setProperty(
        'color','transparent','important');}""", selecteur)
    png = pg.screenshot(clip={"x": x, "y": y, "width": w, "height": h})
    pg.evaluate("""(s)=>{const e=document.querySelector(s);
      e.style.color=e.dataset.c||'';}""", selecteur)

    im = Image.open(io.BytesIO(png)).convert("RGB")
    valeurs = sorted(contraste(fg, px) for px in im.getdata())
    pire = valeurs[max(0, int(len(valeurs) * 0.02) - 1)]
    return pire, fg


# --------------------------------------------------------------- pages
PAGES = [(p[0], lg, "%s/%s" % (lg, B.fichier(p[0], lg)))
         for lg in ("fr", "en") for p in C.PAGES]


# =====================================================================
def section_1_source():
    """Ce que le fichier contient. Ne prouve rien sur le rendu."""
    for cle, lg, rel in PAGES:
        h = open(os.path.join(RACINE, rel), encoding="utf-8").read()
        nom = rel
        v(h.startswith("<!doctype html>"), nom + " doctype")
        v(('<html lang="%s">' % B.HTML_LANG[lg]) in h, nom + " lang")
        v(h.count("<h1") == 1, nom + " un seul h1")
        v('id="principal"' in h, nom + " cible du lien d'evitement")
        v('class="saut"' in h, nom + " lien d'evitement")
        v('rel="canonical"' in h, nom + " canonical")
        v(h.count('rel="alternate" hreflang=') == 3, nom + " hreflang x3")
        v('name="robots" content="noindex' in h, nom + " noindex (demo)")
        v("favicon.svg" in h, nom + " favicon")
        m = re.search(r'name="description" content="([^"]*)"', h)
        v(m and 40 < len(m.group(1)) < 320, nom + " longueur description")
        v(not MESURE.search(h), nom + " aucun outil de mesure")
        # Aucune donnée structurée : déclarer une Organization dont le nom
        # est un nom de travail publierait une identité qui n'existe pas.
        v("application/ld+json" not in h, nom + " aucune donnee structuree")
        # Le nom affiché est marqué comme provisoire, sur CHAQUE page.
        v(('>%s<' % C.NOM_TRAVAIL[0 if lg == "fr" else 1]) in h,
          nom + " le nom est signale comme nom de travail")
        # La sortie rapide est présente deux fois : barre du haut et barre
        # mobile. Sans JavaScript ce sont de vrais liens.
        v(h.count('data-sortie="1"') == 2, nom + " deux sorties rapides")
        v(h.count('href="%s"' % C.SORTIE_URL) == 2, nom + " cible de sortie")

        # ressources tierces
        tiers = re.findall(r'(?:src|href)="(https?://[^"]+)"', h)
        tiers = [u for u in tiers
                 if not u.startswith(("https://schema.org",
                                      "http://www.w3.org",
                                      "https://www.sitemaps.org",
                                      B.BASE, C.SORTIE_URL))]
        v(not tiers, nom + " aucune ressource tierce %s" % tiers[:1])

        # aucune image qui ne soit un ornement produit par motif.py
        srcs = re.findall(r'<img[^>]+src="([^"]+)"', h)
        etrangeres = [s for s in srcs
                      if os.path.basename(s) not in IMAGES_PERMISES]
        v(not etrangeres, nom + " aucune image hors ornements %s"
          % etrangeres[:1])

        txt = sans_balises(h)
        for motif, etiquette in INTERDITS:
            hits = touches(motif, txt)
            v(not hits, "%s : %s %s" % (rel, etiquette, hits[:2]))

        # Le badge d'attente porte EXACTEMENT le mot du projet.
        mot = C.ATTENTE[0] if lg == "fr" else C.ATTENTE[1]
        for texte in re.findall(r'<span class="att">([^<]*)</span>', h):
            v(texte == mot, "%s : badge d'attente « %s »" % (rel, texte))
        # Le vocabulaire d'attente d'un autre chantier ne sert pas
        # d'étiquette ici. On cherche un nœud de texte ENTIER, pas une
        # sous-chaîne : « ce qui reste à définir » est de la prose
        # ordinaire, et un contrôle qui la refuse se trompe de cible.
        for autre in AUTRES_ATTENTES:
            seul = re.search(r">\s*%s\s*<" % re.escape(autre), h, re.I)
            v(not seul, "%s : etiquette d'attente d'un autre projet (%s)"
              % (rel, autre))


def section_2_liens():
    connus = set(rel for _, _, rel in PAGES)
    connus.add("index.html")
    for cle, lg, rel in PAGES:
        h = open(os.path.join(RACINE, rel), encoding="utf-8").read()
        dossier = os.path.dirname(rel)
        for href in re.findall(r'href="([^"#:]+\.html)(?:#[^"]*)?"', h):
            cible = os.path.normpath(os.path.join(dossier, href))
            v(cible.replace(os.sep, "/") in connus,
              "%s : lien mort %s" % (rel, href))
        autre = "en" if lg == "fr" else "fr"
        attendu = "../%s/%s" % (autre, B.fichier(cle, autre))
        v(('class="langue" href="%s"' % attendu) in h,
          "%s : bascule de langue vers la page equivalente" % rel)


def section_3_plan():
    plan = open(os.path.join(RACINE, "sitemap.xml"), encoding="utf-8").read()
    for cle, lg, rel in PAGES:
        v(("/" + rel) in plan, "sitemap : %s present" % rel)
    rob = open(os.path.join(RACINE, "robots.txt"), encoding="utf-8").read()
    v("Disallow: /" in rob, "robots : demo interdite d'indexation")
    v(os.path.isfile(os.path.join(RACINE, "index.html")),
      "aiguillage a la racine")


# =====================================================================
def section_4_rendu(pg, journal):
    """Ce que le navigateur fait vraiment, à vingt et une largeurs."""
    for cle, lg, rel in PAGES:
        journal["erreurs"] = []
        journal["externes"] = []
        pg.goto(BASE + rel, wait_until="networkidle")
        pg.wait_for_timeout(120)
        nom = rel

        v(not journal["erreurs"],
          "%s : aucune erreur console %s" % (nom, journal["erreurs"][:1]))
        # Une requête sortante trahirait la page Confidentialité, qui
        # affirme le contraire. C'est mesuré, pas supposé.
        v(not journal["externes"],
          "%s : aucune requete hors domaine %s" % (nom,
                                                   journal["externes"][:1]))
        v(pg.evaluate("document.fonts.status") == "loaded",
          "%s : polices chargees" % nom)

        for w in LARGEURS:
            pg.set_viewport_size({"width": w, "height": 820})
            pg.wait_for_timeout(40)
            deb = pg.evaluate(
                "document.documentElement.scrollWidth"
                " - document.documentElement.clientWidth")
            v(deb <= 1, "%s @%d : aucun debordement horizontal (%s)"
              % (nom, w, deb))

        pg.set_viewport_size({"width": 1280, "height": 820})
        pg.wait_for_timeout(60)

        etat = pg.evaluate("""()=>{
          const out={casse:[],boite:[]};
          document.querySelectorAll('img').forEach(i=>{
            if(!i.complete||i.naturalWidth===0){out.casse.push(i.src);return;}
            const r=i.getBoundingClientRect();
            if(r.width<2||r.height<2) return;
            const a=r.width/r.height, b=i.naturalWidth/i.naturalHeight;
            if(Math.abs(a/b-1)>0.02) out.boite.push(
              i.getAttribute('src')+' '+a.toFixed(3)+' vs '+b.toFixed(3));
          });
          return out;}""")
        v(not etat["casse"], "%s : aucune image cassee %s"
          % (nom, etat["casse"][:1]))
        v(not etat["boite"], "%s : aucune boite d'image deformee %s"
          % (nom, etat["boite"][:1]))

        saut = pg.evaluate("""()=>{
          let prec=0, mauvais=[];
          document.querySelectorAll('h1,h2,h3,h4').forEach(h=>{
            const n=+h.tagName[1];
            if(prec && n>prec+1) mauvais.push(h.tagName+' '+
              h.textContent.trim().slice(0,26));
            prec=n;});
          return mauvais;}""")
        v(not saut, "%s : hierarchie des titres %s" % (nom, saut[:1]))

        hors = pg.evaluate("""()=>{
          const out=[];
          document.querySelectorAll('body *').forEach(e=>{
            if(e.closest('[aria-hidden="true"]')) return;
            const st=getComputedStyle(e);
            if(st.display==='none'||st.visibility==='hidden') return;
            if(e.classList.contains('saut')) return;
            const r=e.getBoundingClientRect();
            if(r.width<1||r.height<1) return;
            if(r.right>document.documentElement.clientWidth+1.5||r.left<-1.5)
              out.push(e.tagName+'.'+(e.className||'').toString().slice(0,22));
          });
          return out;}""")
        v(not hors, "%s : rien hors ecran %s" % (nom, hors[:2]))


def section_5_ancres(pg):
    """Une ancre qui atterrit sous l'en-tête collant est une ancre cassée,
    et ça ne se voit qu'à la largeur où l'en-tête est le plus haut."""
    cibles = [("fr/services-et-activites.html", "#attente"),
              ("fr/calendrier-des-ateliers.html", "#attente"),
              ("en/mission-and-values.html", "#regles"),
              ("fr/accessibilite.html", "#pas-fait")]
    for w in (390, 1280):
        for rel, anc in cibles:
            pg.set_viewport_size({"width": w, "height": 780})
            pg.goto(BASE + rel + anc, wait_until="networkidle")
            pg.wait_for_timeout(220)
            y = pg.evaluate("""(a)=>{const e=document.querySelector(a);
              if(!e) return null;
              const h=document.querySelector('.hdr').getBoundingClientRect();
              return e.getBoundingClientRect().top - h.bottom;}""", anc)
            v(y is not None and y >= -1,
              "%s%s @%d : la cible ne passe pas sous l'en-tete (%s)"
              % (rel, anc, w, None if y is None else round(y)))


def section_6_clavier(pg):
    pg.set_viewport_size({"width": 1280, "height": 820})
    pg.goto(BASE + "fr/index.html", wait_until="networkidle")
    pg.keyboard.press("Tab")
    prem = pg.evaluate("document.activeElement.className")
    v("saut" in (prem or ""), "premier tabulateur : lien d'evitement")
    v(pg.evaluate("""()=>document.querySelector('.saut')
        .getBoundingClientRect().top > -20;"""),
      "le lien d'evitement devient visible au focus")
    v(pg.evaluate("""()=>getComputedStyle(document.querySelector('.saut'))
        .outlineStyle;""") not in ("none", None),
      "contour de focus visible")

    pg.set_viewport_size({"width": 390, "height": 780})
    pg.wait_for_timeout(80)
    pg.click(".burger")
    v(pg.get_attribute(".burger", "aria-expanded") == "true",
      "burger : aria-expanded passe a true")
    v(pg.is_visible(".panneau-nav nav a"), "burger : la navigation apparait")
    pg.keyboard.press("Escape")
    v(pg.get_attribute(".burger", "aria-expanded") == "false",
      "burger : Echap referme")
    pg.click(".burger")
    pg.set_viewport_size({"width": 1280, "height": 820})
    pg.wait_for_timeout(160)
    v(pg.get_attribute(".burger", "aria-expanded") == "false",
      "burger : l'attribut ne ment pas une fois le panneau masque")


def section_7_formulaire(pg):
    pg.set_viewport_size({"width": 1280, "height": 900})
    pg.goto(BASE + "fr/demande-d-accueil.html", wait_until="networkidle")
    pg.click(".formulaire button[type=submit]")
    pg.wait_for_timeout(120)
    n = pg.evaluate("document.querySelectorAll('.erreur:not(:empty)').length")
    v(n >= 3, "formulaire vide : %d erreurs annoncees" % n)
    v(pg.evaluate("document.activeElement.id") == "c-prenom",
      "formulaire : le focus va au premier champ fautif")
    v(pg.evaluate("document.getElementById('form-etat').textContent") == "",
      "formulaire : aucun message de succes quand il est invalide")

    pg.fill("#c-prenom", "Alex")
    pg.fill("#c-contact", "un numero complet")
    pg.check("#k-traitement")
    pg.click(".formulaire button[type=submit]")
    pg.wait_for_timeout(120)
    etat = pg.evaluate("document.getElementById('form-etat').textContent")
    v("rien n'a été envoyé" in etat,
      "formulaire valide : l'etat dit que rien n'est envoye")
    v("navigateur" in etat,
      "formulaire valide : l'etat dit ou sont restees les reponses")
    # Aucun numéro de repli n'est proposé : il n'en existe pas, et en
    # inventer un serait exactement la faute que tout ce site évite.
    v(not re.search(r"\+?\d[\d\s().-]{7,}", etat),
      "formulaire valide : aucun numero invente dans le message")
    for nom in ("rappel", "nouvelles"):
        v(pg.evaluate("document.getElementById('k-%s').checked" % nom)
          is False, "consentement %s jamais coche d'avance" % nom)
    v(pg.evaluate("""()=>{const t=document.getElementById('c-message');
        return t && t.getAttribute('maxlength')==='400';}"""),
      "le champ libre est borne")
    # Un champ de contact ne doit pas être rempli d'office par le
    # navigateur sur un site que l'on consulte peut-être en cachette.
    v(pg.evaluate("""()=>document.getElementById('c-prenom')
        .getAttribute('autocomplete')==='off'"""),
      "le champ du prenom ne se remplit pas tout seul")


def section_8_langue(pg):
    for cle in ("mission", "services", "calendrier", "contact"):
        depart = "fr/" + B.fichier(cle, "fr")
        pg.set_viewport_size({"width": 1280, "height": 820})
        pg.goto(BASE + depart, wait_until="networkidle")
        pg.click(".langue")
        pg.wait_for_load_state("networkidle")
        v(pg.url.endswith("en/" + B.fichier(cle, "en")),
          "bascule %s -> anglais (%s)" % (cle, pg.url.split("/")[-1]))
        pg.click(".langue")
        pg.wait_for_load_state("networkidle")
        v(pg.url.endswith(depart), "retour %s -> francais" % cle)


def section_9_contraste(pg):
    """Les couleurs telles que l'écran les produit, pas telles que la
    feuille de style les déclare."""
    cas = [
        ("fr/index.html", 1280, ".heros h1", 4.5, "titre du heros"),
        ("fr/index.html", 390, ".heros h1", 4.5, "titre du heros (mobile)"),
        ("fr/index.html", 1280, ".heros .chapo", 4.5, "chapo du heros"),
        ("fr/index.html", 1280, ".bandeau-demo", 4.5, "bandeau de demo"),
        ("fr/index.html", 1280, ".util .mention", 4.5, "mention de la barre"),
        ("fr/index.html", 1280, ".util .sortie", 4.5, "sortie rapide"),
        ("fr/index.html", 1280, ".marque .prov", 4.5, "mention nom de travail"),
        ("fr/index.html", 1280, ".panneau-nav nav a", 4.5, "lien de menu"),
        ("fr/index.html", 1280, ".carte p", 4.5, "texte de carte"),
        ("fr/index.html", 1280, ".etapes h3", 4.5, "titre d'etape"),
        ("fr/index.html", 1280, ".pied a", 4.5, "lien du pied"),
        ("fr/index.html", 1280, ".prudence .confid", 4.5,
         "mention de confidentialite"),
        ("fr/services-et-activites.html", 1280, ".activites .freq", 4.5,
         "frequence du tableau"),
        ("fr/services-et-activites.html", 1280, ".liste-attente .att", 4.5,
         "mot de l'attente"),
        ("fr/services-et-activites.html", 1280, ".liste-attente .cond", 4.5,
         "condition de l'attente"),
        ("fr/demande-d-accueil.html", 1280, ".champ .aide", 4.5,
         "aide de champ"),
        ("fr/demande-d-accueil.html", 1280, ".avertissement", 4.5,
         "avertissement du formulaire"),
        ("fr/mentions-legales.html", 1280, ".fil a", 4.5, "fil d'Ariane"),
        ("fr/index.html", 390, ".barre-mobile .btn-sortie", 4.5,
         "sortie de la barre mobile"),
    ]
    mesures = []
    for rel, w, sel, seuil, etiquette in cas:
        pg.set_viewport_size({"width": w, "height": 900})
        pg.goto(BASE + rel, wait_until="networkidle")
        pg.wait_for_timeout(150)
        pg.evaluate("""(s)=>{const e=document.querySelector(s);
          if(e) e.scrollIntoView({block:'center'});}""", sel)
        pg.wait_for_timeout(120)
        r, fg = contraste_mesure(pg, sel)
        if r is None:
            v(False, "contraste %s : element introuvable" % etiquette)
            continue
        mesures.append((etiquette, w, round(r, 2)))
        v(r >= seuil, "contraste %s @%d : %.2f:1 (seuil %.1f)"
          % (etiquette, w, r, seuil))
    return mesures


def section_10_tableau(pg):
    """Le tableau du chapitre 6 : de la donnée tabulaire, balisée comme
    telle, et qui défile dans son cadre au lieu de pousser la page."""
    for rel in ("fr/services-et-activites.html", "en/workshop-calendar.html"):
        pg.set_viewport_size({"width": 1280, "height": 900})
        pg.goto(BASE + rel, wait_until="networkidle")
        v(pg.evaluate(
            "document.querySelectorAll('.activites thead th[scope=col]')"
            ".length") == 3, "%s : trois en-tetes de colonne" % rel)
        v(pg.evaluate(
            "document.querySelectorAll('.activites tbody tr').length")
          == len(C.ACTIVITES),
          "%s : %d lignes d'activite" % (rel, len(C.ACTIVITES)))
        v(pg.evaluate(
            "document.querySelectorAll('.activites tbody th[scope=row]')"
            ".length") == len(C.ACTIVITES),
          "%s : chaque ligne a son en-tete" % rel)
    # à 320 px le tableau est plus large que l'écran : c'est le CADRE qui
    # doit défiler, et il doit être atteignable au clavier.
    pg.set_viewport_size({"width": 320, "height": 780})
    pg.goto(BASE + "fr/services-et-activites.html", wait_until="networkidle")
    pg.wait_for_timeout(150)
    r = pg.evaluate("""()=>{const c=document.querySelector('.cadre-tableau');
      return {defile:c.scrollWidth>c.clientWidth+1,
              tab:c.getAttribute('tabindex'),
              role:c.getAttribute('role'),
              page:document.documentElement.scrollWidth
                   -document.documentElement.clientWidth};}""")
    v(r["defile"], "tableau @320 : le cadre defile bien")
    v(r["tab"] == "0", "tableau @320 : le cadre est atteignable au clavier")
    v(r["role"] == "region", "tableau @320 : le cadre est annonce")
    v(r["page"] <= 1, "tableau @320 : la page ne defile pas (%s)" % r["page"])


def section_11_sortie(pg):
    """La sortie rapide doit exister sans JavaScript, et le script ne doit
    que l'améliorer."""
    for rel in ("fr/index.html", "en/privacy.html"):
        pg.set_viewport_size({"width": 1280, "height": 820})
        pg.goto(BASE + rel, wait_until="networkidle")
        r = pg.evaluate("""()=>{const a=document.querySelectorAll(
          '[data-sortie]');
          return Array.from(a).map(e=>[e.tagName,e.getAttribute('href'),
            e.getAttribute('rel')]);}""")
        v(len(r) == 2, "%s : deux sorties rapides rendues" % rel)
        for tag, href, rel_attr in r:
            v(tag == "A", "%s : la sortie est un lien (%s)" % (rel, tag))
            v(href == C.SORTIE_URL, "%s : cible de sortie (%s)" % (rel, href))
            v("noopener" in (rel_attr or ""),
              "%s : la sortie ne donne pas la main a la page ouverte" % rel)
    # Elle vide le formulaire avant de partir : un retour arrière ne doit
    # pas retrouver les champs remplis.
    #
    # On ne peut pas lire le champ APRÈS le clic : quoi qu'on fasse, le
    # document part. Annuler l'événement ne sert à rien (le script appelle
    # `location.replace` sans consulter `defaultPrevented`), arrêter la
    # propagation depuis un ancêtre supprimerait aussi la remise à zéro
    # qu'on veut observer, et couper la destination au réseau remplace la
    # page par l'écran d'erreur du navigateur — c'est ce qu'a répondu la
    # première version de ce contrôle, avec un champ introuvable.
    #
    # On écoute donc l'événement `reset`, qui est émis PENDANT le clic, et
    # on le fait sortir du navigateur au moment où il se produit.
    vu = []
    pg.expose_function("__temoin", lambda nom: vu.append(nom))
    pg.route("https://www.google.com/**", lambda r: r.abort())
    pg.goto(BASE + "fr/demande-d-accueil.html", wait_until="networkidle")
    pg.evaluate("""()=>{document.addEventListener('reset',
      ()=>window.__temoin('reset'), true);}""")
    pg.fill("#c-prenom", "Alex")
    pg.click(".util .sortie")
    pg.wait_for_timeout(300)
    v("reset" in vu,
      "la sortie rapide vide le formulaire avant de partir (%r)" % vu)
    pg.unroute("https://www.google.com/**")


def section_12_sans_script(pg):
    """Sans JavaScript, le contenu reste lisible et la sortie fonctionne."""
    ctx = pg.context.browser.new_context(java_script_enabled=False,
                                         viewport={"width": 1280,
                                                   "height": 900})
    p2 = ctx.new_page()
    p2.goto(BASE + "fr/demande-d-accueil.html", wait_until="load")
    v(p2.is_visible(".formulaire"), "sans script : le formulaire est visible")
    v(p2.is_visible(".avertissement"),
      "sans script : l'avertissement reste lu")
    v(p2.evaluate("""()=>document.querySelectorAll('.liste-attente li')
        .length""") == len(C.CONTACT_ATTENTES),
      "sans script : les attentes restent affichees")
    v(p2.get_attribute(".util .sortie", "href") == C.SORTIE_URL,
      "sans script : la sortie rapide reste un lien utilisable")
    p2.close()
    ctx.close()


def section_13_mouvement(pg):
    p2 = pg.context.new_page()
    p2.emulate_media(reduced_motion="reduce")
    p2.set_viewport_size({"width": 1280, "height": 820})
    p2.goto(BASE + "fr/index.html", wait_until="networkidle")
    d = p2.evaluate("""()=>getComputedStyle(document.querySelector('.btn'))
        .transitionDuration;""")
    # Chromium rend « 1e-06s » et non « 0.001ms » : comparer la CHAÎNE fait
    # échouer un comportement correct. On lit le nombre.
    m = re.match(r"([\d.eE+-]+)(ms|s)", d or "")
    sec = float(m.group(1)) / (1000.0 if m.group(2) == "ms" else 1.0) \
        if m else 9.0
    v(sec < 0.01, "mouvement reduit respecte (%s)" % d)
    p2.close()


def section_14_impression(pg):
    p2 = pg.context.new_page()
    p2.set_viewport_size({"width": 1280, "height": 900})
    p2.goto(BASE + "fr/mentions-legales.html", wait_until="networkidle")
    p2.emulate_media(media="print")
    p2.wait_for_timeout(80)
    cache = p2.evaluate("""()=>{
      const q=s=>{const e=document.querySelector(s);
        return e?getComputedStyle(e).display:'absent';};
      return [q('.util'),q('.hdr'),q('.barre-mobile'),q('.bandeau-demo')];}""")
    v(all(c in ("none", "absent") for c in cache),
      "impression : chrome de navigation retire %s" % cache)
    p2.close()


def section_15_barre_mobile(pg):
    """La barre d'actions ne doit jamais masquer la fin du contenu."""
    for w in (320, 360, 390, 414, 419, 421, 480, 759):
        pg.set_viewport_size({"width": w, "height": 720})
        pg.goto(BASE + "fr/index.html", wait_until="networkidle")
        pg.wait_for_timeout(120)
        r = pg.evaluate("""()=>{
          const b=document.querySelector('.barre-mobile');
          const st=getComputedStyle(b);
          const pb=parseFloat(getComputedStyle(document.body).paddingBottom);
          return {aff:st.display, h:b.getBoundingClientRect().height, pb:pb};}
        """)
        v(r["aff"] == "flex", "barre mobile @%d : affichee" % w)
        v(r["pb"] >= r["h"] - 1,
          "barre mobile @%d : le corps reserve sa hauteur (%.0f >= %.0f)"
          % (w, r["pb"], r["h"]))
        pg.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        pg.wait_for_timeout(180)
        chevauche = pg.evaluate("""()=>{
          const b=document.querySelector('.barre-mobile')
            .getBoundingClientRect();
          const p=document.querySelector('.pied .bas p:last-of-type')
            .getBoundingClientRect();
          return p.bottom > b.top + 1;}""")
        v(not chevauche,
          "barre mobile @%d : le dernier texte du pied reste visible" % w)
    pg.set_viewport_size({"width": 1280, "height": 820})
    pg.goto(BASE + "fr/index.html", wait_until="networkidle")
    v(pg.evaluate("""()=>getComputedStyle(
        document.querySelector('.barre-mobile')).display""") == "none",
      "barre mobile : absente sur grand ecran")


# =====================================================================
def main():
    section_1_source()
    section_2_liens()
    section_3_plan()

    journal = {"erreurs": [], "externes": []}
    with sync_playwright() as p:
        nav = p.chromium.launch()
        ctx = nav.new_context(viewport={"width": 1280, "height": 820})
        pg = ctx.new_page()
        pg.on("console", lambda m: journal["erreurs"].append(m.text)
              if m.type == "error" else None)
        pg.on("pageerror", lambda e: journal["erreurs"].append(str(e)))
        pg.on("request", lambda r: journal["externes"].append(r.url)
              if not r.url.startswith(BASE) and not r.url.startswith("data:")
              else None)

        section_4_rendu(pg, journal)
        section_5_ancres(pg)
        section_6_clavier(pg)
        section_7_formulaire(pg)
        section_8_langue(pg)
        mesures = section_9_contraste(pg)
        section_10_tableau(pg)
        section_11_sortie(pg)
        section_12_sans_script(pg)
        section_13_mouvement(pg)
        section_14_impression(pg)
        section_15_barre_mobile(pg)
        ctx.close()
        nav.close()

    print("")
    print("contrastes mesures :")
    for e, w, r in mesures:
        print("   %-34s @%-5d %5.2f:1" % (e, w, r))
    print("")
    print("%d controles, %d echecs" % (ok + len(echecs), len(echecs)))
    for e in echecs:
        print("  ECHEC  " + e)
    return 1 if echecs else 0


if __name__ == "__main__":
    sys.exit(main())
