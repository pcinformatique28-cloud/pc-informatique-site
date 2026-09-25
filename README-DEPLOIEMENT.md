# PC-INFORMATIQUE — mise en place du site officiel

Compte officiel utilisé partout : **pcinformatique28@gmail.com**

Ce dossier contient le point de départ : `index.html` (l'affiche déjà publiée),
`firestore.rules` (règles de sécurité de départ, verrouillées), `firebase.json`,
`firestore.indexes.json` et `.firebaserc`.

---

## 1. Créer le compte GitHub (une seule fois)

Sur le téléphone, dans un navigateur : créer un compte GitHub avec
`pcinformatique28@gmail.com`. Nom d'utilisateur réel : `pcinformatique28-cloud`
(`pcinformatique28` était déjà pris).

Puis créer un nouveau dépôt vide (sans README) nommé
`pc-informatique-site`.

## 2. Créer le projet Firebase (une seule fois)

Sur https://console.firebase.google.com, connecté avec `pcinformatique28@gmail.com` :
- "Ajouter un projet" → nom `pc-informatique`
- Activer **Firestore Database** (mode production)
- Noter l'ID exact du projet affiché (ex: `pc-informatique-xxxxx`) et le
  remplacer dans `.firebaserc` à la place de `"pc-informatique"`

## 3. Créer le compte Cloudinary (une seule fois)

Sur https://cloudinary.com, créer un compte avec `pcinformatique28@gmail.com`.
Dans Settings → Upload → Upload presets : créer un preset **Unsigned**,
dossier fixe `pcinformatique`, formats autorisés restreints à
`jpg,jpeg,png,webp` (même logique de sécurité que sur GSC/AMBI241 : jamais
de clé secrète dans le code, uniquement le cloud name + un preset unsigned).

## 4. Dans Termux — préparer les outils

```bash
pkg update && pkg upgrade -y
pkg install git nodejs -y
npm install -g firebase-tools

git config --global user.name "pcinformatique28"
git config --global user.email "pcinformatique28@gmail.com"
```

## 5. Dans Termux — récupérer ce dossier et l'envoyer sur GitHub

Copie d'abord le dossier `pc-informatique-site` (téléchargé depuis ce chat)
vers le stockage Termux, par exemple dans `~/storage/downloads/`, puis :

```bash
termux-setup-storage
cd ~
cp -r ~/storage/downloads/pc-informatique-site ~/pc-informatique-site
cd ~/pc-informatique-site

git init
git add .
git commit -m "Premier commit — site PC-INFORMATIQUE"
git branch -M main
git remote add origin https://github.com/pcinformatique28-cloud/pc-informatique-site.git
git push -u origin main
```

(Au push, Git demandera un identifiant : utilise un **Personal Access
Token** GitHub — pas le mot de passe du compte — créé depuis
Settings → Developer settings → Personal access tokens sur github.com.)

## 6. Activer GitHub Pages

Sur github.com, dans le dépôt → Settings → Pages → Source : branche `main`,
dossier `/ (root)`. Le site sera en ligne à l'adresse
`https://pcinformatique28-cloud.github.io/pc-informatique-site/` après
quelques minutes.

## 7. Dans Termux — connecter et déployer les règles Firebase

```bash
cd ~/pc-informatique-site
firebase login --no-localhost
```

(Termux n'a pas de navigateur intégré : la commande donne un lien à ouvrir
dans le navigateur du téléphone, puis un code à recoller dans Termux.)

```bash
firebase deploy --only firestore:rules
```

Cela publie les règles de `firestore.rules` (verrouillées par défaut, rien
n'est encore lisible/écrivable — normal tant qu'aucune fonctionnalité
dynamique n'est branchée).

---

## Prochaines étapes possibles (pas encore faites)

- Brancher un vrai formulaire de contact sur le site → écrit dans la
  collection Firestore `demandes` (règle déjà préparée en commentaire dans
  `firestore.rules`, à activer à ce moment-là)
- Migrer les captures d'écran du site (actuellement encodées en base64
  dans `index.html`) vers Cloudinary, pour alléger le fichier et faciliter
  les mises à jour futures
- Nom de domaine personnalisé (optionnel) branché sur GitHub Pages
