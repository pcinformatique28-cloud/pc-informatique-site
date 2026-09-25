# Mise en place — Espace membres PC-INFORMATIQUE

## 1. Copier les fichiers dans le projet (Termux)

```bash
cd ~/pc-informatique-site
# copie inscription.html, connexion.html, profil.html, admin-membres.html
# et remplace firestore.rules par la nouvelle version, depuis ton dossier de téléchargement
```

## 2. Activer l'authentification par e-mail/mot de passe

Dans la console Firebase → Authentication → Sign-in method → active
"E-mail/Mot de passe" si ce n'est pas déjà fait (index.html/admin.html
utilisent déjà Firestore, mais l'Auth doit être activée séparément).

## 3. Déployer les nouvelles règles Firestore

Depuis un poste avec Firebase CLI (ou directement en collant le contenu de
`firestore.rules` dans Console Firebase → Firestore Database → Règles → Publier) :

```bash
firebase deploy --only firestore:rules
```

## 4. Lier la nouvelle page admin

Dans `admin.html`, ajoute un lien vers le nouveau panneau, par exemple dans le menu :

```html
<a href="admin-membres.html">Membres & Projets</a>
```

## 5. Lier inscription/connexion depuis le site public

Ajoute un lien "Espace membres" dans `index.html`, pointant vers `connexion.html`.

## 6. Commit + push

```bash
cd ~/pc-informatique-site
git add inscription.html connexion.html profil.html admin-membres.html firestore.rules
git commit -m "Ajout espace membres (comptes, profils, projets) + admin"
git push
```

## Comment ça marche

- **Comptes** : Firebase Auth (email/mot de passe). Chaque inscription crée
  un document `membres/{uid}` dans Firestore (nom, email, bio, photoURL).
- **Photos** : uploadées directement depuis le navigateur vers Cloudinary
  (cloud `zbof0xbh`, preset unsigned `pc_membres`), l'URL est stockée dans
  Firestore. Aucune clé secrète n'est exposée côté client.
- **Projets** : chaque membre peut ajouter un projet "personnel" ou
  "collaboration". Il part avec le statut `en_attente` et n'apparaît
  publiquement qu'une fois validé par l'admin.
- **Admin** (`admin-membres.html`) : liste tous les membres (désactiver/
  supprimer) et tous les projets (valider/refuser/supprimer), avec compteurs
  en haut de page. Connexion réservée aux comptes présents dans la
  collection `admins` (même mécanisme que ton `admin.html` actuel).

## Pour afficher les projets validés publiquement (optionnel, plus tard)

Une requête `db.collection('projets').where('statut','==','valide')`
peut être ajoutée sur `index.html` pour afficher une galerie de projets
membres sur le site public, si tu le souhaites.
