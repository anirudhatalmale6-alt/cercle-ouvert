# -*- coding: utf-8 -*-
"""
Tout le texte du site, en un seul endroit.

RÈGLE DE PRODUCTION — elle vaut pour chaque ligne de ce fichier.

Rien n'est affirmé qui ne vienne du cahier des charges du client. Le
document ne donne ni le nom de l'association, ni le pays, ni la ville, ni
une adresse, ni un téléphone, ni un horaire, ni une date de séance, ni un
tarif, ni le nom d'une personne. Aucune de ces choses n'est donc écrite
ici. Là où elles manqueront au lecteur, la page porte le mot d'attente du
projet — « À fixer » / « To be set » — accompagné de la condition exacte
qui le lèvera.

Ce que le site n'affiche nulle part, et pourquoi :

* aucun témoignage, même anonyme (chapitre 9 : pas de publication de
  témoignage sans autorisation explicite) ;
* aucune photographie de personne, ni réelle ni générée (même chapitre, et
  chapitre 11 : communication sobre, sans exposition ni victimisation) ;
* aucun chiffre de fréquentation (chapitre 14 : ce sont des indicateurs à
  suivre, pas des résultats déjà obtenus) ;
* aucun numéro d'urgence ni de service social (il dépend du pays, et un
  numéro qui ne répond pas dans le pays du lecteur est pire que rien) ;
* aucune promesse de résultat, aucun conseil médical, psychologique ou
  juridique (chapitre 1 : l'association ne remplace ni les institutions, ni
  les professionnels de santé, ni les services sociaux).

Chaque couple est (français, anglais), français d'abord.
"""

# ------------------------------------------------------------------ marque
# NOM DE TRAVAIL. Le cahier des charges demande au chapitre 11 « un nom et
# un logo simples, rassurants et faciles à retenir » — il ne les donne pas.
# Inventer un nom en douce, c'est laisser croire qu'une décision a été
# prise. Celui-ci est donc affiché comme provisoire sur toutes les pages, et
# il tient en une constante : le changer une fois ici le change partout.
MARQUE = ("Le Cercle Ouvert", "The Open Circle")
BASELINE = ("Accueil, écoute et bien-être",
            "Welcome, listening and well-being")
NOM_TRAVAIL = ("nom de travail", "working name")

# Le mot d'attente de CE chantier. Il ne se mélange à aucun autre.
ATTENTE = ("À fixer", "To be set")

MENU_CTA = ("Faire une demande d'accueil", "Request a first contact")
MENU_CTA_COURT = ("Demande d'accueil", "Request contact")
MENU_COURT = {
    "accueil": ("Accueil", "Home"),
    "mission": ("Mission", "Mission"),
    "services": ("Services", "Services"),
    "calendrier": ("Calendrier", "Calendar"),
    "benevolat": ("Bénévolat", "Volunteering"),
}

SORTIE = ("Quitter le site", "Leave this site")
SORTIE_AIDE = (
    "Ce bouton remplace immédiatement la page par un moteur de recherche. "
    "Il n'efface pas l'historique du navigateur : pensez à le vider si "
    "quelqu'un d'autre utilise cet appareil.",
    "This button replaces the page with a search engine straight away. It "
    "does not clear your browsing history: remember to clear it if someone "
    "else uses this device.")
SORTIE_URL = "https://www.google.com/"

PIED_LANGUE = ("Français", "English")

DEMO_BANDEAU = (
    "Démonstration. Le nom, le pays et les coordonnées ne sont pas encore "
    "fixés, et aucune page n'est indexée.",
    "Demonstration. The name, the country and the contact details are not "
    "settled yet, and no page is indexed.")

# ------------------------------------------------------------- avertissements
PRUDENCE = (
    "L'association n'est ni un service médical, ni un service juridique, ni "
    "un service d'urgence. En cas de danger immédiat pour vous ou pour un "
    "enfant, n'utilisez pas ce site : appelez les secours. Le numéro à "
    "afficher ici dépend du pays d'implantation, qui reste à fixer.",
    "The association is not a medical service, a legal service or an "
    "emergency service. If you or a child are in immediate danger, do not "
    "use this site: call the emergency services. The number to be shown "
    "here depends on the country the association will operate in, which is "
    "still to be set.")

CONFID = (
    "Rien de ce qui est confié à l'association n'est publié — ni photo, ni "
    "nom, ni témoignage — sans autorisation écrite.",
    "Nothing entrusted to the association is published — no photograph, no "
    "name, no testimonial — without written permission.")

# ------------------------------------------------------------------- pages
# (clé, fichier fr, fichier en, titre fr, titre en, dans le menu)
PAGES = [
    ("accueil", "index.html", "index.html",
     "Accueil", "Home", True),
    ("mission", "mission-et-valeurs.html", "mission-and-values.html",
     "Mission et valeurs", "Mission and values", True),
    ("services", "services-et-activites.html", "services-and-activities.html",
     "Services et activités", "Services and activities", True),
    ("calendrier", "calendrier-des-ateliers.html", "workshop-calendar.html",
     "Calendrier des ateliers", "Workshop calendar", True),
    ("benevolat", "benevolat-et-partenariats.html",
     "volunteering-and-partnerships.html",
     "Bénévolat et partenariats", "Volunteering and partnerships", True),
    ("contact", "demande-d-accueil.html", "reception-request.html",
     "Demande d'accueil", "Reception request", False),
    ("confidentialite", "confidentialite.html", "privacy.html",
     "Confidentialité et protection des données",
     "Privacy and data protection", False),
    ("mentions", "mentions-legales.html", "legal-notice.html",
     "Mentions légales", "Legal notice", False),
    ("accessibilite", "accessibilite.html", "accessibility.html",
     "Accessibilité", "Accessibility", False),
]

# ----------------------------------------------------------------- accueil
ACC_TITRE = ("Après une séparation, un lieu pour souffler",
             "After a separation, a place to breathe")
ACC_SOUS = (
    "Un espace d'accueil, d'écoute, d'orientation et de bien-être pour les "
    "mères divorcées, séparées, ou en train de traverser une rupture "
    "familiale. Sans jugement, et sans aucune dimension financière.",
    "A space for welcome, listening, guidance and well-being for divorced "
    "mothers, separated mothers, and women going through a family "
    "breakdown. Without judgment, and with no financial component.")

ACC_INTRO = [
    ("L'association accueille, écoute, oriente et propose des activités de "
     "bien-être. Elle repose sur trois choses seulement : le respect, la "
     "confidentialité et l'absence de jugement.",
     "The association welcomes, listens, guides, and offers well-being "
     "activities. It rests on three things only: respect, confidentiality "
     "and the absence of judgment."),
    ("Elle ne remplace ni les institutions, ni les professionnels de santé, "
     "ni les services sociaux. Son rôle est de faciliter l'accès à "
     "l'information, de proposer des activités collectives et d'offrir un "
     "cadre de soutien moral et social.",
     "It does not replace institutions, healthcare professionals or social "
     "services. Its role is to make information easier to reach, to offer "
     "group activities, and to provide a framework for moral and social "
     "support."),
    ("Quand une situation demande une compétence que l'association n'a pas, "
     "elle oriente vers un professionnel qualifié. C'est une mission à part "
     "entière, pas un aveu de limite.",
     "When a situation calls for a skill the association does not have, it "
     "refers the person to a qualified professional. That is a mission in "
     "its own right, not an admission of failure."),
]

ACC_PILIERS = [
    ("Confidentialité",
     "Ce qui est dit dans l'association reste dans l'association. Aucune "
     "photo, aucun nom, aucun témoignage n'est publié sans autorisation "
     "explicite.",
     "Confidentiality",
     "What is said inside the association stays inside the association. No "
     "photograph, no name and no testimonial is published without explicit "
     "permission."),
    ("Sans jugement",
     "Aucun jugement sur le parcours familial, social ou personnel des "
     "personnes accueillies. On n'a pas à justifier sa situation pour être "
     "reçue.",
     "No judgment",
     "No judgment about anyone's family, social or personal background. "
     "Nobody has to justify their situation in order to be received."),
    ("Sans dimension financière",
     "Le projet est décrit sans composante financière. Ce site ne vend "
     "rien, ne collecte aucun paiement et ne demande aucun don.",
     "No financial component",
     "The project is described with no financial component. This site sells "
     "nothing, takes no payment and asks for no donation."),
    ("Orientation",
     "Centres sociaux, médiateurs familiaux, psychologues, éducateurs, "
     "associations spécialisées, services administratifs : l'association "
     "informe et met en relation.",
     "Guidance",
     "Social centres, family mediators, psychologists, specialised "
     "educators, dedicated associations, administrative services: the "
     "association informs and connects."),
]

ACC_CHEMIN = (
    "Comment ça commence",
    "How it starts")
ACC_CHEMIN_TEXTE = (
    "Un premier contact, un entretien d'orientation confidentiel, puis les "
    "activités qui vous vont — et rien de plus que ce que vous voulez bien. "
    "Le parcours complet est décrit sur la page Services et activités.",
    "A first contact, a confidential orientation conversation, then "
    "whichever activities suit you — and nothing beyond what you choose. "
    "The full pathway is set out on the Services and activities page.")

# ----------------------------------------------------------------- mission
MISSION_INTRO = (
    "Ce que l'association cherche à faire, pour qui, et selon quelles "
    "règles. Cette page reprend les chapitres 2, 3, 4, 9 et 14 du cahier "
    "des charges, sans rien y ajouter.",
    "What the association sets out to do, for whom, and under what rules. "
    "This page follows chapters 2, 3, 4, 9 and 14 of the specifications, "
    "and adds nothing to them.")

MISSION_OBJECTIFS = [
    ("Accueillir les mères divorcées dans un cadre digne, calme et sûr.",
     "Welcome divorced mothers in a dignified, calm and secure setting."),
    ("Soutenir la reconstruction personnelle, la confiance en soi et "
     "l'équilibre émotionnel.",
     "Support personal rebuilding, self-confidence and emotional balance."),
    ("Proposer des activités de bien-être régulières et accessibles.",
     "Offer regular and accessible well-being activities."),
    ("Renforcer le lien social entre des femmes qui traversent des "
     "situations proches.",
     "Strengthen the social bond between women going through similar "
     "situations."),
    ("Soutenir la parentalité après une séparation ou un divorce.",
     "Support parenting after a separation or a divorce."),
    ("Orienter vers des professionnels qualifiés ou des services compétents "
     "lorsque c'est nécessaire.",
     "Refer people to qualified professionals or to the relevant services "
     "when that is needed."),
]

MISSION_PUBLIC = [
    ("Qui est accueillie",
     "Les mères divorcées ou séparées, avec ou sans enfants à charge, les "
     "femmes en cours de séparation, les mères isolées, et celles qui ont "
     "besoin d'un endroit sûr pour parler d'une rupture familiale.",
     "Who is welcomed",
     "Divorced or separated mothers, with or without dependent children, "
     "women currently going through a separation, isolated mothers, and "
     "women who need a safe place to speak about a family breakdown."),
    ("Quels besoins",
     "Écoute, bien-être, soutien moral, appui à la parentalité et "
     "orientation sociale.",
     "Which needs",
     "Listening, well-being, moral support, parenting support and social "
     "guidance."),
    ("Dans quel cadre",
     "Confidentialité, respect, neutralité, absence de jugement. Cadre non "
     "politique et non conflictuel.",
     "In what framework",
     "Confidentiality, respect, neutrality, absence of judgment. A "
     "non-political, non-adversarial framework."),
]

MISSION_MISSIONS = [
    ("Accueil et écoute",
     "Un premier contact qui sert à identifier le besoin de chacune et à "
     "proposer un accompagnement adapté — pas à remplir un dossier.",
     "Reception and listening",
     "A first contact whose purpose is to identify what each person needs "
     "and to suggest a suitable pathway — not to fill in a file."),
    ("Bien-être et apaisement",
     "Des activités de détente, de respiration, d'estime de soi, de "
     "mouvement doux et d'équilibre émotionnel.",
     "Well-being and relief",
     "Activities for relaxation, breathing, self-esteem, gentle movement "
     "and emotional balance."),
    ("Appui à la parentalité",
     "Retrouver une organisation familiale, une communication avec les "
     "enfants et une stabilité au quotidien.",
     "Parenting support",
     "Rebuilding family organisation, communication with children and "
     "day-to-day stability."),
    ("Orientation sociale",
     "Informer et mettre en relation avec les structures appropriées, sans "
     "se substituer à elles.",
     "Social guidance",
     "Informing people and connecting them with the appropriate services, "
     "without standing in for them."),
    ("Lien social",
     "Entraide, parole et solidarité, par des rencontres, des groupes de "
     "parole et des activités collectives.",
     "Social connection",
     "Mutual support, speech and solidarity, through meetings, discussion "
     "groups and group activities."),
]

MISSION_REGLES = [
    ("Confidentialité stricte sur toutes les situations personnelles.",
     "Strict confidentiality over every personal situation."),
    ("Aucun jugement sur le parcours familial, social ou personnel.",
     "No judgment about anyone's family, social or personal background."),
    ("Aucune publication de photo, de nom ou de témoignage sans "
     "autorisation explicite.",
     "No publication of a photograph, a name or a testimonial without "
     "explicit permission."),
    ("Orientation vers un professionnel qualifié dans les situations "
     "sensibles ou urgentes.",
     "Referral to a qualified professional in sensitive or urgent "
     "situations."),
    ("Respect des horaires, des intervenantes, des autres participantes et "
     "des enfants présents.",
     "Respect for schedules, facilitators, other participants and any "
     "children present."),
    ("Cadre non politique et non conflictuel, centré sur le soutien humain "
     "et le bien-être.",
     "A non-political, non-adversarial framework, centred on human support "
     "and well-being."),
]

MISSION_INDICATEURS_INTRO = (
    "Le chapitre 14 fixe ce que l'association suivra pour savoir si elle "
    "est utile. Ce sont des indicateurs à mesurer, pas des résultats déjà "
    "obtenus : aucun chiffre n'est publié sur ce site tant qu'aucun n'a été "
    "relevé.",
    "Chapter 14 sets out what the association will track in order to know "
    "whether it is useful. These are indicators to be measured, not results "
    "already achieved: no figure is published on this site until one has "
    "actually been recorded.")

MISSION_INDICATEURS = [
    ("Nombre de mères accueillies.", "Number of mothers welcomed."),
    ("Nombre d'ateliers et de groupes de parole organisés.",
     "Number of workshops and discussion groups held."),
    ("Taux de participation aux activités.",
     "Rate of participation in activities."),
    ("Retours anonymes des personnes accueillies.",
     "Anonymous feedback from the people welcomed."),
    ("Nombre de partenariats actifs.", "Number of active partnerships."),
    ("Qualité du suivi humain et régularité du calendrier.",
     "Quality of human follow-up and regularity of the calendar."),
    ("Évolution du lien social et du soutien perçu par les participantes.",
     "Change in social connection and in the support participants feel."),
]

# ---------------------------------------------------------------- services
SERVICES_INTRO = (
    "Huit services, sept activités régulières et un parcours en cinq "
    "étapes. Les rythmes ci-dessous sont ceux du cahier des charges ; les "
    "dates réelles vivront sur la page Calendrier, et elles restent à "
    "fixer.",
    "Eight services, seven regular activities and a five-step pathway. The "
    "rhythms below are the ones set out in the specifications; the actual "
    "dates will live on the Calendar page, and they are still to be set.")

SERVICES_LISTE = [
    ("Accueil individuel, sur rendez-vous ou pendant une permanence.",
     "Individual reception, by appointment or during an open session."),
    ("Groupes de parole animés par une personne responsable désignée.",
     "Discussion groups facilitated by a designated responsible person."),
    ("Ateliers de gestion du stress et des émotions.",
     "Workshops on managing stress and emotions."),
    ("Activités de relaxation, de méditation, de respiration et de yoga "
     "doux.",
     "Relaxation, meditation, breathing and gentle yoga activities."),
    ("Ateliers d'estime de soi, d'image de soi et de confiance.",
     "Self-esteem, self-image and confidence workshops."),
    ("Activités mère-enfant, pour renforcer le lien familial.",
     "Mother-and-child activities, to strengthen the family bond."),
    ("Orientation vers des professionnels qualifiés selon la situation.",
     "Referral to qualified professionals according to each situation."),
    ("Rencontres thématiques sur la parentalité, la reconstruction "
     "personnelle et la vie après un divorce.",
     "Themed meetings on parenting, personal rebuilding and life after a "
     "divorce."),
]

# (activité, objectif, fréquence) × 2 langues — chapitre 6, tel quel.
ACTIVITES = [
    ("Yoga doux et étirements", "Détente physique et baisse du stress",
     "Hebdomadaire",
     "Gentle yoga and stretching", "Physical relaxation and less stress",
     "Weekly"),
    ("Méditation guidée", "Calme mental et ancrage émotionnel",
     "Hebdomadaire",
     "Guided meditation", "Mental calm and emotional grounding",
     "Weekly"),
    ("Groupe de parole", "Expression, écoute et entraide",
     "Hebdomadaire ou deux fois par mois",
     "Discussion group", "Expression, listening and mutual support",
     "Weekly or twice monthly"),
    ("Marche collective", "Lien social et activité physique douce",
     "Mensuelle",
     "Group walk", "Social connection and gentle physical activity",
     "Monthly"),
    ("Atelier d'estime de soi", "Confiance et reconstruction personnelle",
     "Mensuel",
     "Self-esteem workshop", "Confidence and personal rebuilding",
     "Monthly"),
    ("Activité mère-enfant", "Renforcer le lien familial après la séparation",
     "Mensuelle",
     "Mother-and-child activity",
     "Strengthening the family bond after separation", "Monthly"),
    ("Atelier nutrition et hygiène de vie", "Équilibre quotidien et prévention",
     "Trimestriel",
     "Nutrition and healthy living workshop",
     "Everyday balance and prevention", "Quarterly"),
]

ACTIVITES_ENTETES = (("Activité", "Objectif", "Fréquence indicative"),
                     ("Activity", "Purpose", "Indicative frequency"))

ACTIVITES_NOTE = (
    "« Indicative » est le mot du cahier des charges, et il est repris tel "
    "quel : ces rythmes décrivent une intention d'organisation, pas un "
    "engagement de séance.",
    "“Indicative” is the word used in the specifications, and it "
    "is kept as it stands: these rhythms describe an intended rhythm of "
    "organisation, not a commitment to hold a given session.")

PARCOURS = [
    ("Premier contact",
     "Par téléphone, par message, par le formulaire de ce site ou pendant "
     "une permanence. Vous n'avez rien à préparer.",
     "First contact",
     "By phone, by message, through the form on this site, or during an "
     "open session. There is nothing to prepare."),
    ("Entretien d'orientation",
     "Un échange confidentiel pour identifier le besoin principal. Il ne "
     "s'agit pas d'un bilan et rien n'est noté à votre insu.",
     "Orientation conversation",
     "A confidential conversation to identify the main need. It is not an "
     "assessment, and nothing is written down without your knowledge."),
    ("Parcours proposé",
     "Inscription aux activités utiles, et orientation vers un service "
     "extérieur si la situation le demande.",
     "Suggested pathway",
     "Signing up for whichever activities are useful, and referral to an "
     "outside service if the situation calls for it."),
    ("Participation",
     "Aux groupes, ateliers et rencontres, selon vos disponibilités. Venir "
     "une fois puis s'arrêter est une réponse acceptable.",
     "Participation",
     "In groups, workshops and meetings, as your availability allows. "
     "Coming once and then stopping is an acceptable answer."),
    ("Suivi humain",
     "Un point régulier avec une personne responsable quand la situation le "
     "demande — jamais imposé.",
     "Human follow-up",
     "A regular check-in with a responsible person when the situation calls "
     "for it — never imposed."),
]

SERVICES_ATTENTES = [
    ("Le lieu des activités",
     "Chapitre 10 : une salle d'accueil confidentielle et une salle "
     "polyvalente sont nécessaires. Aucune adresse ne sera écrite ici avant "
     "qu'un local soit confirmé.",
     "Where the activities take place",
     "Chapter 10: a confidential reception room and a multipurpose room are "
     "required. No address will be written here before a venue is "
     "confirmed."),
    ("Les intervenantes",
     "Les animatrices de yoga, de méditation et de nutrition sont des "
     "professionnelles à recruter (chapitre 13). Aucun nom, aucune "
     "qualification et aucun diplôme ne sera affiché sans justificatif.",
     "The facilitators",
     "Yoga, meditation and nutrition facilitators are professionals still "
     "to be recruited (chapter 13). No name, qualification or diploma will "
     "be shown without documentary proof."),
    ("Les inscriptions",
     "Comment on s'inscrit à un atelier, et si une inscription est "
     "nécessaire, dépend du local et de la taille des groupes.",
     "Signing up",
     "How someone signs up for a workshop, and whether signing up is "
     "required at all, depends on the venue and on group size."),
    ("La garde des enfants",
     "Le cahier des charges prévoit un coin enfants sécurisé pendant les "
     "activités mère-enfant. Savoir s'il existe pendant les autres "
     "activités change tout pour une mère isolée.",
     "Childcare",
     "The specifications provide for a safe children's corner during "
     "mother-and-child activities. Whether one exists during the other "
     "activities changes everything for an isolated mother."),
]

# --------------------------------------------------------------- calendrier
CAL_INTRO = (
    "Cette page est volontairement vide de dates.",
    "This page is deliberately empty of dates.")

CAL_TEXTE = [
    ("Un calendrier est la page la plus utilisée d'un site d'association, "
     "et c'est aussi la seule qu'on ne peut pas remplir à l'avance sans "
     "mentir. Une date inventée fait sortir quelqu'un de chez elle pour "
     "rien ; une mère qui a organisé une garde d'enfants pour venir ne "
     "revient pas une deuxième fois.",
     "A calendar is the most-used page on an association's site, and it is "
     "also the only one that cannot be filled in ahead of time without "
     "lying. An invented date makes someone leave home for nothing; a "
     "mother who arranged childcare in order to come does not come back a "
     "second time."),
    ("Ce que le cahier des charges donne, ce sont des fréquences "
     "indicatives, et elles sont reprises telles quelles sur la page "
     "Services et activités. Ce qu'il ne donne pas — le jour, l'heure, le "
     "lieu, la date de la première séance — reste à fixer et est signalé "
     "comme tel ci-dessous.",
     "What the specifications do give are indicative frequencies, and they "
     "are reproduced as they stand on the Services and activities page. "
     "What they do not give — the day, the time, the place, the date of the "
     "first session — is still to be set and is flagged as such below."),
]

CAL_ATTENTES = [
    ("Le local",
     "Adresse, accès, étage, ascenseur, et si l'on peut venir avec un "
     "enfant. Chapitre 10.",
     "The venue",
     "Address, access, floor, lift, and whether a child can come along. "
     "Chapter 10."),
    ("Le jour et l'heure de chaque activité",
     "Sept activités, sept créneaux. Le cahier des charges donne un rythme, "
     "pas un horaire.",
     "The day and time of each activity",
     "Seven activities, seven slots. The specifications give a rhythm, not "
     "a timetable."),
    ("La date de la première séance",
     "Elle dépend du local et des intervenantes.",
     "The date of the first session",
     "It depends on the venue and on the facilitators."),
    ("La façon de s'inscrire",
     "Sur place, par téléphone, par le formulaire — et si une inscription "
     "est nécessaire.",
     "How to sign up",
     "In person, by phone, through the form — and whether signing up is "
     "needed at all."),
    ("Les périodes de fermeture",
     "Vacances scolaires et jours fériés du pays d'implantation, qui reste "
     "à fixer.",
     "Closing periods",
     "School holidays and public holidays in the country of operation, "
     "which is still to be set."),
]

CAL_APRES = (
    "Dès que ces cinq points seront tranchés, cette page affichera un "
    "calendrier réel : une ligne par séance, avec le lieu, l'heure et la "
    "façon de s'y joindre. Elle est déjà construite pour les recevoir.",
    "As soon as those five points are settled, this page will show a real "
    "calendar: one line per session, with the place, the time and how to "
    "join. It is already built to receive them.")

# ---------------------------------------------------------------- bénévolat
BEN_INTRO = (
    "L'organisation interne reste simple, claire et tournée vers le "
    "service. Les rôles s'adaptent à la taille de l'association et au "
    "nombre de bénévoles disponibles.",
    "The internal structure stays simple, clear and service-oriented. Roles "
    "adapt to the size of the association and to the number of volunteers "
    "available.")

BEN_ROLES = [
    ("Coordination générale",
     "Supervision du service et calendrier des activités.",
     "General coordination",
     "Overseeing the service and the activity calendar."),
    ("Accueil et écoute",
     "Premier contact, orientation et suivi discret.",
     "Reception and listening",
     "First contact, guidance and discreet follow-up."),
    ("Bien-être",
     "Programmation des ateliers et coordination des intervenantes.",
     "Well-being",
     "Planning workshops and coordinating facilitators."),
    ("Appui à la parentalité",
     "Activités mère-enfant et rencontres thématiques.",
     "Parenting support",
     "Mother-and-child activities and themed meetings."),
    ("Partenariats",
     "Relations avec les structures sociales, juridiques, éducatives et de "
     "santé.",
     "Partnerships",
     "Relations with social, legal, educational and health-related "
     "organisations."),
    ("Bénévolat",
     "Accueil, logistique, soutien et animation, selon la formation de "
     "chacune et de chacun.",
     "Volunteering",
     "Reception, logistics, support and facilitation, depending on each "
     "person's training."),
]

BEN_PARTENAIRES = [
    ("Centres sociaux, municipalités, centres de quartier et structures de "
     "soutien aux familles.",
     "Social centres, local councils, neighbourhood centres and family "
     "support organisations."),
    ("Psychologues, médiateurs familiaux, éducateurs spécialisés et "
     "travailleurs sociaux.",
     "Psychologists, family mediators, specialised educators and social "
     "workers."),
    ("Professionnels du bien-être : coachs, professeurs de yoga, "
     "sophrologues et nutritionnistes.",
     "Well-being professionals: coaches, yoga teachers, relaxation "
     "practitioners and nutritionists."),
    ("Écoles, bibliothèques, centres culturels et associations locales.",
     "Schools, libraries, cultural centres and local associations."),
    ("Services d'orientation administrative et structures d'appui aux "
     "femmes.",
     "Administrative guidance services and organisations supporting women."),
]

BEN_ATTENTES = [
    ("Ce qui est demandé à une bénévole",
     "Disponibilité, engagement de confidentialité, formation éventuelle : "
     "à décider avec la coordination.",
     "What is asked of a volunteer",
     "Availability, a confidentiality undertaking, possible training: to be "
     "decided with the coordination team."),
    ("Le canal de candidature",
     "Le formulaire de ce site n'est pas encore branché : aucune adresse ne "
     "existe sur le domaine, qui reste à fixer.",
     "How to apply",
     "The form on this site is not connected yet: no address exists on the "
     "domain, which is still to be set."),
    ("La vérification des intervenantes",
     "Diplômes, assurances et, le cas échéant, vérification d'antécédents "
     "pour les activités où des enfants sont présents.",
     "Checks on facilitators",
     "Qualifications, insurance and, where relevant, background checks for "
     "activities where children are present."),
]

# ------------------------------------------------------------------ contact
CONTACT_INTRO = (
    "Il n'y a pas de formulaire long, pas de compte à créer et pas de "
    "dossier à remplir. Dites seulement comment vous joindre et ce qui vous "
    "amène — en un mot si vous préférez.",
    "There is no long form, no account to create and no file to fill in. "
    "Just say how to reach you and what brings you here — in a word if you "
    "prefer.")

CONTACT_AVERT = (
    "Ce formulaire n'est pas encore branché. Il vérifie ce que vous "
    "écrivez, mais il ne l'envoie nulle part : aucune adresse "
    "professionnelle n'existe pour l'instant sur le domaine. Rien de ce que "
    "vous tapez ici ne quitte votre navigateur.",
    "This form is not connected yet. It checks what you write, but it sends "
    "it nowhere: no professional address exists on the domain at this "
    "stage. Nothing you type here leaves your browser.")

# (nom, libellé fr, libellé en, type, requis, aide fr, aide en)
CHAMPS = [
    ("prenom", "Comment vous appeler", "What to call you", "text", True,
     "Un prénom d'emprunt convient parfaitement.",
     "A name you have chosen for the occasion is perfectly fine."),
    ("contact", "Comment vous joindre", "How to reach you", "text", True,
     "Un numéro ou un autre moyen. Précisez si l'on peut laisser un "
     "message.",
     "A number or another way. Say whether a message can be left."),
    ("moment", "Quand vous pouvez répondre", "When you can answer",
     "select", False,
     "Facultatif. Utile si l'on ne peut pas vous joindre à tout moment.",
     "Optional. Useful if you cannot be reached at any time."),
    ("langue", "Langue préférée", "Preferred language", "select", False,
     "Facultatif.",
     "Optional."),
    ("besoin", "Ce qui vous amène", "What brings you here", "select", False,
     "Facultatif, et modifiable à tout moment.",
     "Optional, and can be changed at any time."),
    ("message", "Si vous voulez en dire plus", "If you want to say more",
     "textarea", False,
     "Facultatif. N'écrivez rien d'urgent ici : ce formulaire n'est pas "
     "relevé en temps réel.",
     "Optional. Do not write anything urgent here: this form is not "
     "monitored in real time."),
]

MOMENTS = [
    ("matin", "Le matin", "In the morning"),
    ("apres-midi", "L'après-midi", "In the afternoon"),
    ("soir", "En soirée", "In the evening"),
    ("nimporte", "N'importe quand", "Any time"),
    ("message", "Laissez plutôt un message", "Please leave a message"),
]

LANGUES_CHOIX = [
    ("fr", "Français", "French"),
    ("en", "Anglais", "English"),
    ("autre", "Une autre langue", "Another language"),
]

BESOINS = [
    ("ecoute", "Parler à quelqu'un", "Speaking to someone"),
    ("bienetre", "Les activités de bien-être", "The well-being activities"),
    ("parentalite", "L'appui à la parentalité", "Parenting support"),
    ("orientation", "Être orientée vers un service",
     "Being referred to a service"),
    ("benevolat", "Devenir bénévole", "Volunteering"),
    ("autre", "Autre chose", "Something else"),
]

CONSENTEMENTS = [
    ("traitement",
     "J'accepte que ces informations soient lues par la personne chargée de "
     "l'accueil, dans le seul but de me recontacter.",
     "I agree that this information may be read by the person in charge of "
     "reception, for the sole purpose of getting back to me.",
     True),
    ("rappel",
     "On peut me rappeler sur ce numéro et laisser un message.",
     "You may call me back on this number and leave a message.",
     False),
    ("nouvelles",
     "Je veux bien recevoir le calendrier des ateliers.",
     "I would like to receive the workshop calendar.",
     False),
]

CONTACT_ATTENTES = [
    ("La ligne d'accueil",
     "Chapitre 10 : une ligne de contact est nécessaire. Aucun numéro ne "
     "sera écrit sur ce site avant qu'il existe et qu'il réponde.",
     "The contact line",
     "Chapter 10: a contact line is required. No number will be written on "
     "this site before one exists and answers."),
    ("Le destinataire du formulaire",
     "Le domaine et l'adresse professionnelle restent à fixer ; d'ici là, "
     "l'envoi n'est branché nulle part et la page le dit.",
     "Where the form goes",
     "The domain and the professional address are still to be set; until "
     "then, sending is connected to nothing and the page says so."),
    ("Les permanences",
     "Jours, heures et lieu des permanences d'accueil sans rendez-vous.",
     "Open sessions",
     "Days, times and place of the drop-in reception sessions."),
    ("Le délai de réponse",
     "Annoncer un délai qu'on ne tient pas est pire que de n'en annoncer "
     "aucun.",
     "The response time",
     "Announcing a response time you cannot keep is worse than announcing "
     "none."),
]

# ----------------------------------------------------------- confidentialité
CONF_INTRO = (
    "Cette page dit ce qui est vrai de ce site aujourd'hui, et ce qui reste "
    "à décider avant qu'il soit mis en ligne. Elle ne recopie pas un modèle "
    "de politique de confidentialité : la moitié des phrases d'un modèle "
    "seraient fausses ici.",
    "This page states what is true of this site today, and what remains to "
    "be decided before it goes live. It is not a copied privacy-policy "
    "template: half the sentences in a template would be false here.")

CONF_FAITS = [
    ("Aucun témoin, aucune mesure d'audience",
     "Le site ne dépose aucun cookie et n'embarque aucun outil de mesure. "
     "Ce n'est pas une intention, c'est vérifié : le contrôle compte les "
     "requêtes sortantes de chaque page, et il y en a zéro.",
     "No cookies, no analytics",
     "The site sets no cookie and carries no analytics tool. That is not an "
     "intention but a measurement: the test suite counts the outbound "
     "requests of every page, and there are none."),
    ("Aucune ressource extérieure",
     "Les polices de caractères sont servies depuis le site. Une police "
     "chargée depuis un tiers transmet à ce tiers l'adresse de la page "
     "consultée — sur ce site-ci, cela révélerait bien plus qu'une "
     "préférence de lecture.",
     "No external resources",
     "The typefaces are served from the site itself. A typeface loaded from "
     "a third party sends that third party the address of the page being "
     "read — on this site, that would reveal a great deal more than a "
     "reading preference."),
    ("Le formulaire n'envoie rien",
     "Il vérifie les champs dans le navigateur et s'arrête là. Aucune "
     "donnée n'est transmise, stockée ni conservée.",
     "The form sends nothing",
     "It checks the fields inside the browser and stops there. No data is "
     "transmitted, stored or kept."),
    ("Le bouton de sortie rapide",
     "Il remplace la page en cours par un moteur de recherche, sans la "
     "laisser dans l'historique de navigation. Il n'efface pas les pages "
     "déjà visitées : elles restent dans l'historique du navigateur tant "
     "que personne ne le vide.",
     "The quick-exit button",
     "It replaces the current page with a search engine, without leaving it "
     "in the session history. It does not erase pages already visited: they "
     "stay in the browser history until someone clears it."),
    ("Aucune photo, aucun nom, aucun témoignage",
     "Il n'y en a aucun sur ce site, et il n'y en aura aucun sans "
     "autorisation écrite de la personne concernée — chapitre 9.",
     "No photograph, no name, no testimonial",
     "There is none on this site, and there will be none without written "
     "permission from the person concerned — chapter 9."),
]

CONF_ATTENTES = [
    ("Le responsable des données",
     "Qui répond juridiquement du traitement : la personne morale, son nom "
     "et son adresse.",
     "The data controller",
     "Who is legally answerable for the processing: the legal entity, its "
     "name and its address."),
    ("Le pays et la loi applicable",
     "Le régime de protection des données, les mentions obligatoires et les "
     "droits des personnes changent d'un pays à l'autre.",
     "The country and the applicable law",
     "The data-protection regime, the mandatory notices and people's rights "
     "differ from one country to another."),
    ("Qui lit les demandes d'accueil",
     "Une seule personne, une équipe, une boîte partagée ? La réponse "
     "détermine ce qu'on peut promettre.",
     "Who reads the reception requests",
     "One person, a team, a shared mailbox? The answer determines what can "
     "be promised."),
    ("La durée de conservation",
     "Combien de temps une demande est gardée, et ce qui en est fait "
     "ensuite.",
     "How long information is kept",
     "How long a request is kept, and what happens to it afterwards."),
    ("L'hébergement",
     "Où le site et les messages seront hébergés, et dans quel pays.",
     "Hosting",
     "Where the site and the messages will be hosted, and in which "
     "country."),
    ("Le registre des autorisations",
     "Comment une autorisation de publier une photo ou un témoignage est "
     "recueillie, conservée et retirée.",
     "The permissions register",
     "How permission to publish a photograph or a testimonial is obtained, "
     "kept and withdrawn."),
]

CONF_JURIDIQUE = (
    "Cette page n'est pas un avis juridique. Elle doit être relue par une "
    "personne compétente dans le pays d'implantation avant la mise en "
    "ligne, en particulier sur la protection des données personnelles et "
    "sur les informations relatives aux enfants.",
    "This page is not legal advice. It must be reviewed by someone "
    "qualified in the country of operation before the site goes live, "
    "particularly on personal-data protection and on information relating "
    "to children.")

# -------------------------------------------------------------- mentions
MENT_INTRO = (
    "Les mentions légales d'un site associatif dépendent du pays et du "
    "statut de l'association. Rien n'est inventé ici : chaque ligne "
    "manquante porte la condition qui la remplira.",
    "The legal notice of an association's site depends on the country and "
    "on the association's legal status. Nothing is invented here: every "
    "missing line carries the condition that will fill it.")

MENT_ATTENTES = [
    ("Le nom de l'association",
     "Chapitre 11 : un nom simple, rassurant et facile à retenir. Celui "
     "affiché sur ce site est un nom de travail, et il est signalé comme "
     "tel sur chaque page.",
     "The name of the association",
     "Chapter 11: a simple, reassuring, memorable name. The one shown on "
     "this site is a working name, and it is flagged as such on every "
     "page."),
    ("Le statut juridique",
     "Association déclarée ou pas encore, et sous quel régime.",
     "The legal status",
     "Whether the association is formally registered or not yet, and under "
     "which regime."),
    ("Le pays et la ville",
     "Ils commandent la langue du site, la loi applicable, les numéros "
     "d'urgence et les partenaires cités.",
     "The country and the city",
     "They govern the language of the site, the applicable law, the "
     "emergency numbers and the partners named."),
    ("Le siège",
     "L'adresse à publier, qui n'est pas forcément celle du local "
     "d'accueil.",
     "The registered address",
     "The address to be published, which is not necessarily that of the "
     "reception venue."),
    ("Le numéro d'enregistrement",
     "S'il existe dans le pays concerné.",
     "The registration number",
     "If one exists in the country concerned."),
    ("La direction de la publication",
     "La personne responsable du contenu publié.",
     "The publication director",
     "The person responsible for the published content."),
    ("L'hébergeur",
     "Raison sociale et adresse, obligatoires dans plusieurs pays.",
     "The host",
     "Company name and address, which several countries require."),
    ("Les canaux officiels",
     "Chapitre 11 : site, Facebook, Instagram, WhatsApp Business, affichage "
     "local. Aucun compte n'est lié tant qu'il n'est pas confirmé — un lien "
     "vers un compte qui n'est pas le vôtre est une usurpation.",
     "The official channels",
     "Chapter 11: website, Facebook, Instagram, WhatsApp Business, local "
     "posters. No account is linked until it is confirmed — a link to an "
     "account that is not yours is an impersonation."),
]

# ------------------------------------------------------------ accessibilité
ACCESS_INTRO = (
    "Une partie des personnes qui liront ce site le feront sur un vieux "
    "téléphone, dans une pièce mal éclairée, en se dépêchant. "
    "L'accessibilité n'est pas une case à cocher ici, c'est la condition "
    "pour que la page serve.",
    "Some of the people who read this site will do so on an old phone, in a "
    "badly lit room, in a hurry. Accessibility is not a checkbox here; it "
    "is the condition for the page to be of any use.")

ACCESS_FAIT = [
    ("Contrastes mesurés",
     "Chaque couleur de texte a été photographiée sur le fond réellement "
     "peint derrière elle, dans un navigateur, et non déduite de la feuille "
     "de style. Le plus faible du site est indiqué dans le dossier de "
     "vérification.",
     "Measured contrasts",
     "Every text colour was photographed against the background actually "
     "painted behind it, in a browser, rather than inferred from the "
     "stylesheet. The lowest on the site is recorded in the verification "
     "report."),
    ("Navigation au clavier",
     "Un lien d'évitement en premier, un contour de focus visible partout, "
     "et le menu qui se referme avec la touche Échap.",
     "Keyboard navigation",
     "A skip link comes first, a visible focus outline everywhere, and the "
     "menu closes with the Escape key."),
    ("Aucun débordement horizontal",
     "Vérifié à dix-neuf largeurs d'écran, de 320 à 1440 pixels, dans les "
     "deux langues.",
     "No horizontal overflow",
     "Checked at nineteen screen widths, from 320 to 1440 pixels, in both "
     "languages."),
    ("Hiérarchie des titres",
     "Un seul titre de premier niveau par page, et aucun saut de niveau.",
     "Heading hierarchy",
     "One first-level heading per page, and no skipped levels."),
    ("Mouvement réduit",
     "Les animations s'arrêtent quand le système demande de réduire les "
     "animations.",
     "Reduced motion",
     "Animations stop when the system asks for reduced motion."),
    ("Lisible sans script",
     "Le contenu, les liens et le texte du formulaire restent lisibles "
     "quand JavaScript est désactivé.",
     "Readable without scripts",
     "The content, the links and the form text stay readable when "
     "JavaScript is switched off."),
]

ACCESS_PAS_FAIT = [
    ("Aucun test avec un lecteur d'écran réel",
     "Le balisage est correct, mais personne n'a écouté ces pages. Ce n'est "
     "pas la même chose.",
     "No test with a real screen reader",
     "The markup is sound, but nobody has listened to these pages. That is "
     "not the same thing."),
    ("Aucun audit de conformité",
     "Aucun niveau WCAG n'est revendiqué. Revendiquer une conformité qu'on "
     "n'a pas fait auditer est une affirmation invérifiable.",
     "No conformance audit",
     "No WCAG level is claimed. Claiming a conformance that has not been "
     "audited is an unverifiable statement."),
    ("Aucune relecture par le public concerné",
     "Le vocabulaire du site n'a pas été relu par des femmes qui ont "
     "traversé une séparation. C'est la relecture qui manque le plus.",
     "No review by the people concerned",
     "The wording of this site has not been read back by women who have "
     "been through a separation. That is the review that is missing most."),
]

# ------------------------------------------------------------------- pied
PIED_DECLARATION = (
    "Site de démonstration. Aucune page n'est indexée, et le nom affiché "
    "est un nom de travail.",
    "Demonstration site. No page is indexed, and the name shown is a "
    "working name.")

# -------------------------------------------------------------------- méta
META = {
    "accueil": (
        "Association d'accueil, d'écoute et de bien-être pour les mères "
        "divorcées ou séparées. Confidentialité, absence de jugement, "
        "orientation vers les services compétents.",
        "An association offering welcome, listening and well-being to "
        "divorced and separated mothers. Confidentiality, no judgment, and "
        "guidance towards the relevant services."),
    "mission": (
        "Objectifs, public accueilli, missions et règles de fonctionnement "
        "de l'association, ainsi que les indicateurs qu'elle suivra pour "
        "savoir si elle est utile.",
        "The objectives, the people welcomed, the missions and the "
        "operating rules of the association, together with the indicators "
        "it will track to know whether it is useful."),
    "services": (
        "Accueil individuel, groupes de parole, ateliers de bien-être et "
        "activités mère-enfant, avec le parcours d'accompagnement en cinq "
        "étapes et les fréquences indicatives.",
        "Individual reception, discussion groups, well-being workshops and "
        "mother-and-child activities, with the five-step support pathway "
        "and the indicative frequencies."),
    "calendrier": (
        "Le calendrier des ateliers n'affiche aucune date tant que le "
        "local, les créneaux et les intervenantes ne sont pas confirmés. "
        "Une date inventée fait sortir quelqu'un pour rien.",
        "The workshop calendar shows no date until the venue, the time "
        "slots and the facilitators are confirmed. An invented date makes "
        "someone leave home for nothing."),
    "benevolat": (
        "Les rôles internes de l'association, ce qui est attendu d'une "
        "bénévole, et les partenariats recherchés avec les structures "
        "sociales, juridiques, éducatives et de santé.",
        "The association's internal roles, what is expected of a volunteer, "
        "and the partnerships sought with social, legal, educational and "
        "health organisations."),
    "contact": (
        "Un formulaire court pour demander un premier contact : un prénom, "
        "même d'emprunt, un moyen de vous joindre, et rien de plus que ce "
        "que vous voulez bien dire.",
        "A short form to ask for a first contact: a first name, even a "
        "chosen one, a way to reach you, and nothing beyond what you choose "
        "to say."),
    "confidentialite": (
        "Ce que ce site fait de vos informations aujourd'hui — aucun "
        "témoin, aucune mesure d'audience, aucune requête extérieure — et "
        "ce qui reste à décider avant sa mise en ligne.",
        "What this site does with your information today — no cookies, no "
        "analytics, no outbound requests — and what remains to be decided "
        "before it goes live."),
    "mentions": (
        "Éditeur, statut juridique, siège, direction de la publication et "
        "hébergeur : les mentions qui dépendent du pays et du statut de "
        "l'association, et qui restent à fixer.",
        "Publisher, legal status, registered address, publication director "
        "and host: the notices that depend on the country and on the "
        "association's status, and that are still to be set."),
    "accessibilite": (
        "Ce qui a été mesuré sur ce site — contrastes, clavier, "
        "débordements, hiérarchie des titres — et ce qui ne l'a pas été, "
        "dit sans revendiquer de conformité.",
        "What has been measured on this site — contrasts, keyboard, "
        "overflow, heading hierarchy — and what has not, stated without "
        "claiming any conformance."),
}
