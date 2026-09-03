# -*- coding: utf-8 -*-
"""
Aperçus du site, dans un navigateur réel.

    python3 tests/captures.py [http://127.0.0.1:8874/]

Aucune capture ne dépasse 2000 px dans l'une ou l'autre dimension, et
c'est une assertion, pas une intention : on ne photographie jamais la page
entière, seulement la fenêtre, en la faisant défiler.
"""

import os
import sys

from playwright.sync_api import sync_playwright
from PIL import Image

_ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(_ICI)
SORTIE = os.path.join(RACINE, "apercus")

BASE = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8874/"
if not BASE.endswith("/"):
    BASE += "/"

# (nom, page, largeur, hauteur, défilement, action)
VUES = [
    ("01-accueil", "fr/index.html", 1280, 760, 0, None),
    ("02-accueil-piliers", "fr/index.html", 1280, 760, 860, None),
    ("03-accueil-parcours", "fr/index.html", 1280, 760, 1560, None),
    ("04-mission", "fr/mission-et-valeurs.html", 1280, 760, 0, None),
    ("05-mission-regles", "fr/mission-et-valeurs.html", 1280, 760, 2100, None),
    ("06-services", "fr/services-et-activites.html", 1280, 760, 0, None),
    ("07-services-tableau", "fr/services-et-activites.html", 1280, 760,
     980, None),
    ("08-services-attente", "fr/services-et-activites.html", 1280, 760,
     2350, None),
    ("09-calendrier", "fr/calendrier-des-ateliers.html", 1280, 760, 0, None),
    ("10-calendrier-attente", "fr/calendrier-des-ateliers.html", 1280, 760,
     1450, None),
    ("11-benevolat", "fr/benevolat-et-partenariats.html", 1280, 760, 0, None),
    ("12-demande", "fr/demande-d-accueil.html", 1280, 760, 0, None),
    ("13-demande-validee", "fr/demande-d-accueil.html", 1280, 760, 420,
     "valide"),
    ("14-demande-erreurs", "fr/demande-d-accueil.html", 1280, 760, 420,
     "vide"),
    ("15-confidentialite", "fr/confidentialite.html", 1280, 760, 0, None),
    ("16-mentions", "fr/mentions-legales.html", 1280, 760, 300, None),
    ("17-accessibilite", "fr/accessibilite.html", 1280, 760, 300, None),
    ("18-anglais-accueil", "en/index.html", 1280, 760, 0, None),
    ("19-anglais-services", "en/services-and-activities.html", 1280, 760,
     980, None),
    ("20-mobile-accueil", "fr/index.html", 390, 780, 0, None),
    ("21-mobile-menu", "fr/index.html", 390, 780, 0, "menu"),
    ("22-mobile-tableau", "fr/services-et-activites.html", 390, 780, 1100,
     None),
    ("23-mobile-calendrier", "fr/calendrier-des-ateliers.html", 390, 780,
     900, None),
    ("24-mobile-demande", "fr/demande-d-accueil.html", 390, 780, 300, None),
]


def planche_de_marque():
    """La planche de marque est rendue À PARTIR DES SVG DU SITE.

    Redessiner la marque pour la planche laisserait les deux diverger : la
    planche montrerait une version que le site n'utilise pas, et personne
    ne s'en apercevrait avant l'impression.
    """
    a = os.path.join(RACINE, "assets")
    html = """<body style="margin:0;background:#FAF5F3;
 font:13px/1.5 -apple-system,Segoe UI,Roboto,Arial,sans-serif;color:#2A2226">
<div style="padding:26px 26px 8px">
 <div style="font:600 19px/1.3 Georgia,serif;color:#6E2444">
  La marque : un cercle qui ne se referme pas</div>
 <div style="color:#5E545A;max-width:640px;margin-top:6px">
  Une seule figure, déclinée. Aucune figure humaine, aucun cœur, aucune
  silhouette de mère et d'enfant.</div>
</div>
<div style="display:flex;gap:30px;align-items:flex-end;padding:18px 26px">
 <div><img src="file://%s/marque-duo.svg" width="132">
  <div style="text-align:center">deux tons</div></div>
 <div><img src="file://%s/marque-accent.svg" width="86">
  <div style="text-align:center">un ton</div></div>
 <div><img src="file://%s/marque-fonce.svg" width="52">
  <div style="text-align:center">52 px</div></div>
 <div><img src="file://%s/marque-accent.svg" width="34">
  <div style="text-align:center">34 px</div></div>
 <div style="background:#3A1E2E;padding:16px;border-radius:4px">
  <img src="file://%s/marque-clair.svg" width="74"></div>
 <div><img src="file://%s/favicon.svg" width="32">
  <div style="text-align:center">32</div></div>
 <div><img src="file://%s/favicon.svg" width="16">
  <div style="text-align:center">16</div></div>
</div>
<div style="height:96px;background:#3A1E2E url(file://%s/tuile.svg) repeat;
 background-size:170px 170px"></div>
<div style="height:22px;margin:16px 0;
 background:url(file://%s/frise.svg) center/auto 22px repeat-x"></div>
<div style="display:flex;gap:24px;padding:4px 26px 26px;align-items:center">
 <img src="file://%s/panneau.svg" width="176">
 <div style="max-width:520px">
  <div style="font:600 15px/1.3 Georgia,serif;color:#6E2444">
   Le panneau qui remplace une photographie</div>
  <div style="color:#5E545A;margin-top:6px">
   Des ondes concentriques, toutes ouvertes, dont l'ouverture tourne d'un
   cercle au suivant. Il est posé à chaque emplacement où une image viendra
   un jour, avec la phrase qui dit ce qui manque.</div>
  <div style="display:flex;gap:10px;margin-top:14px">
   <span style="background:#F6E4EA;border:1px solid rgba(217,139,166,.55);
    color:#7A2540;font:650 11px/1 sans-serif;letter-spacing:.09em;
    text-transform:uppercase;padding:6px 10px;border-radius:99px">
    À fixer</span>
   <span style="color:#5E545A">le mot d'attente de ce chantier</span>
  </div>
 </div>
</div>
</body>""" % ((a,) * 10)
    chemin = os.path.join(SORTIE, "_planche.html")
    with open(chemin, "w", encoding="utf-8") as f:
        f.write(html)
    return chemin


def main():
    if not os.path.isdir(SORTIE):
        os.makedirs(SORTIE)
    faits = []
    with sync_playwright() as p:
        nav = p.chromium.launch()
        ctx = nav.new_context()
        pg = ctx.new_page()

        chemin = planche_de_marque()
        pg.set_viewport_size({"width": 980, "height": 640})
        pg.goto("file://" + chemin)
        pg.wait_for_timeout(350)
        pg.screenshot(path=os.path.join(SORTIE, "cd-00-marque.png"))
        faits.append("cd-00-marque.png")
        os.remove(chemin)

        for nom, rel, w, h, y, action in VUES:
            pg.set_viewport_size({"width": w, "height": h})
            pg.goto(BASE + rel, wait_until="networkidle")
            pg.wait_for_timeout(220)
            if action == "menu":
                pg.click(".burger")
                pg.wait_for_timeout(180)
            elif action == "vide":
                pg.click(".formulaire button[type=submit]")
                pg.wait_for_timeout(180)
            elif action == "valide":
                pg.fill("#c-prenom", "Sarah")
                pg.fill("#c-contact", "06 00 00 00 00")
                pg.select_option("#c-moment", "soir")
                pg.select_option("#c-besoin", "ecoute")
                pg.check("#k-traitement")
                pg.click(".formulaire button[type=submit]")
                pg.wait_for_timeout(200)
            if y:
                pg.evaluate("window.scrollTo(0,%d)" % y)
                pg.wait_for_timeout(220)
            f = os.path.join(SORTIE, "cd-%s.png" % nom)
            pg.screenshot(path=f)
            faits.append(os.path.basename(f))
        ctx.close()
        nav.close()

    for n in faits:
        im = Image.open(os.path.join(SORTIE, n))
        assert im.width <= 2000 and im.height <= 2000, \
            "%s : %dx%d" % (n, im.width, im.height)
        print("%-28s %dx%d" % (n, im.width, im.height))
    print("%d apercus" % len(faits))


if __name__ == "__main__":
    main()
