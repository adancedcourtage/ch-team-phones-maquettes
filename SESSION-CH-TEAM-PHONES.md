# Ch Team Phones — récapitulatif du projet

**Client** : Ch Team Phones, Parc Plaza Immeuble C, N7 — Mohammédia 28810
**Site en ligne** : https://adancedcourtage.github.io/ch-team-phones-maquettes/
**Dépôt** : `adancedcourtage/ch-team-phones-maquettes` (public, GitHub Pages)
**Dossier local** : `~/Desktop/AGENCE_CLAUDE_ECOMMERCE/CH_TEAM_PHONES_SITE/`

---

## 1. Ce que fait la boutique

Données vérifiées sur leur fiche Google Business, leur Instagram et leur page Facebook.

| | |
|---|---|
| Adresse | Parc Plaza, Immeuble C, N7 — Mohammédia 28810 |
| Téléphone | 06 61 79 87 82 (WhatsApp) — second numéro 07 02 96 51 94 |
| E-mail | Chteam.phones@gmail.com |
| Horaires | Lundi au samedi, 10h00 – 22h30 · fermé le dimanche |
| Note Google | **4,9 sur 208 avis** (205 × 5★, 3 × 1★) |
| Instagram | @ch_team_phone — 17,7 K abonnés, 1 429 publications |
| Gérant | Amine, cité dans des dizaines d'avis |
| Paiement | Espèces, carte bancaire, sans contact |
| Livraison | Glovo |
| Garantie | **3 mois** sur tout, réparations comprises |

Métiers : vente de neuf, d'occasion et de reconditionné · réparation en atelier ·
accessoires · reprise de l'ancien appareil.

Leurs deux anciens sites sont morts : `chteamphones.ma` (Shopify désactivé) et
`chteamphones.store` (ne résout plus). C'est la raison du projet.

---

## 2. Historique des livrables

| Étape | Résultat |
|---|---|
| 2 maquettes Web3D React Three Fiber | **Rejetées** — partaient sur un positionnement reconditionné façon Back Market, faux |
| Planche 1 — 4 directions « vitrine noire » | Écartée |
| Planche 2 — 4 directions inédites | Le client choisit la **n° 4, Atelier Suspendu** |
| Site complet | En production, enrichi depuis |

Les maquettes écartées sont conservées dans `~/Desktop/AGENCE_CLAUDE_ECOMMERCE/CH_TEAM_SITES/`.

---

## 3. Le site aujourd'hui

Un seul fichier `index.html`, six pages en navigation par ancre
(`#accueil`, `#boutique`, `#reparation`, `#occasion`, `#avis`, `#contact`),
plus une fiche par produit (`#produit/<identifiant>`).

**Accueil** — hero avec un iPhone 17 Pro en vue éclatée animée (three.js, cinq couches
PBR, environnement studio, cycle assemblé/éclaté, rotation suivant le curseur) ;
vitrine des quatre dernières sorties Apple et Samsung ; avis Google ; appel WhatsApp.

**Boutique** — 152 références, recherche instantanée insensible aux accents,
filtres par type, marque et état.

**Fiche produit** — sélecteur **Neuf / Reconditionné / Occasion** qui change le prix et
la garantie affichée, choix de capacité et de couleur, réservation WhatsApp pré-remplie,
caractéristiques, suggestions de la même famille.

**Réparation** — tarifs **par appareil** : on choisit sa marque puis son modèle, et les
neuf interventions s'affichent avec durée, disponibilité de la pièce et prix calculé selon
la gamme. Jeu d'interventions distinct pour les PC et Mac.

**Avis** — note 4,9, répartition des étoiles, 14 avis Google repris mot pour mot.

**Occasion** — 18 points de contrôle, principe de la reprise (sans barème chiffré),
formulaire d'estimation.

---

## 4. Le catalogue — 152 références

| Catégorie | Références |
|---|---|
| Smartphones Android | 50 |
| iPhone (du 7 au 18 Pro Max) | 41 |
| Montres et objets connectés | 15 |
| Accessoires | 15 |
| Mac | 11 |
| iPad et tablettes | 8 |
| PC portables et bureau | 7 |
| Audio | 5 |

Marques : Apple, Samsung, Google, Xiaomi, Huawei, Honor, OPPO, HP, Lenovo, Microsoft,
MEDION, UGREEN, Beats, Bose, Jabra, Soundpeats, WHOOP.

Le catalogue a été bâti en relevant **289 publications Instagram** : la première version
ne couvrait que le matériel récent, alors que leur fonds de commerce est l'occasion
ancienne, les PC Windows et l'audio multimarque.

---

## 5. Prix — 9 confirmés sur 152

Relevés sur leurs publications :

| Modèle | État | Prix réel |
|---|---|---|
| Galaxy S26 Ultra | Neuf | 11 300 DH |
| Google Pixel 10 Pro | Neuf | 7 950 DH |
| iPhone 15 | Occasion | 4 950 DH |
| iPhone 14 Pro | Reconditionné | 4 950 DH |
| Galaxy S24+ | Occasion | 4 700 DH |
| iPhone 13 Pro | Occasion | 4 300 DH |
| iPhone 12 Pro Max | Reconditionné | 3 800 DH |
| iPhone 13 | Reconditionné | 3 250 DH |
| iPhone 11 Pro Max | Reconditionné | 2 200 DH |

Les **143 autres sont des estimations**. Mes premiers prix étaient jusqu'à **45 % trop
chers** ; ils ont été recalés sur ces neuf-là, mais seule la grille de la boutique les
rendra exacts.

---

## 6. Images

94 photos fournies par la boutique sont intégrées (`img/<identifiant>.jpg|png`,
redimensionnées à 620 px, 2,9 Mo au total). Les 58 produits restants affichent une
**illustration studio générée en SVG** — éclairage trois points, tranches en relief,
objectifs avec bague et reflet, ombre portée et reflet au sol.

Pas de visuel Apple, Samsung ni Amazon : ils sont protégés et exposeraient le client.
Le fond d'écran de l'iPhone du hero a été fourni par toi et est embarqué en base64.

**Pour ajouter des photos** : déposer les fichiers dans `img/` nommés avec l'identifiant
du produit, puis lancer `python3 outils/maj-photos.py`, enfin commiter.

---

## 7. Fichiers du dépôt

| Fichier | Rôle |
|---|---|
| `index.html` | Le site entier |
| `img/` | 94 photos produit |
| `wallpaper-17pro.jpg` | Fond d'écran du hero |
| `outils/maj-photos.py` | Branche les nouvelles photos sur le catalogue |
| `CATALOGUE.csv` | Les 152 produits pour Excel — à faire corriger par le client |
| `CATALOGUE.md` | Le même catalogue en tableaux lisibles |
| `PHOTOS-A-FOURNIR.md` | Cahier des charges photo + noms de fichiers attendus |
| `PHOTOS-MANQUANTES.md` | Les 58 photos encore à obtenir |

---

## 8. Ce qui reste à faire

**À obtenir de la boutique**
1. **La grille tarifaire réelle** — 143 prix produits et les tarifs de réparation
2. Les 58 photos manquantes (surtout Android, accessoires, PC)
3. La liste des marques réellement réparées
4. L'orthographe officielle de l'enseigne : *Ch Team Phones* ou *CH TEAM PHONE*
5. Confirmation du second numéro 07 02 96 51 94

**Technique**
- Domaine : `chteamphones.ma` était à eux — vérifier s'il est récupérable
- Destination des formulaires (devis, estimation, contact) : WhatsApp, e-mail, ou les deux
- Les pages portent `noindex` : à retirer à la mise en ligne définitive

---

## 9. Points techniques à retenir

- **Aucune dépendance** hors Google Fonts et three.js (CDN). Tout le reste est dans le fichier.
- `AFFICHER_PRIX = false` en tête du script masque tous les prix d'un coup.
- `?pose=open` fige l'iPhone en vue éclatée, pratique pour les captures.
- Les identifiants produits viennent du nom ; attention aux collisions (`S22` / `S22+`)
  et au `″` supprimé (`macbook-air-13-m4`, pas `-13-pouces-`).
- Déploiement GitHub Pages : compter 2 à 5 minutes, parfois 15.
- Le token GitHub CLI s'est affiché en clair dans cette session : **à révoquer**
  sur https://github.com/settings/applications
