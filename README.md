# Ch Team Phones — site

Site vitrine de **Ch Team Phones**, Parc Plaza, Immeuble C, N7 — Mohammédia 28810.

En ligne : https://adancedcourtage.github.io/ch-team-phones-maquettes/

Cinq pages en un seul fichier (`index.html`) : accueil, boutique, réparation,
occasion, avis, contact. Navigation par ancre, aucune dépendance hors
Google Fonts et three.js (CDN).

Les coordonnées, horaires et avis Google sont réels.
**Les prix et délais sont des repères de mise en page** et doivent être
remplacés par les données réelles de la boutique avant mise en ligne définitive.

## Ajouter les photos produit

1. Déposer les photos dans le dossier `img/`, nommées avec l'identifiant du produit
   (ex. `iphone-17-pro.jpg`). La liste complète est dans `PHOTOS-A-FOURNIR.md`.
2. Lancer :

   ```
   python3 outils/maj-photos.py
   ```

Le script met à jour le site et indique les produits encore sans photo.
Les produits sans photo affichent une illustration générée, donc le site
reste complet à tout moment.
