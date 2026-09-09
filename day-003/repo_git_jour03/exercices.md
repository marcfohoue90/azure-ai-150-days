# Exercices du Jour 3

## 1. Git, dépôt, zone de préparation, commit et historique

Git est un outil de gestion de versions qui conserve l'évolution d'un projet dans le temps. Son rôle ici est de créer un historique propre et compréhensible. Le dépôt local contient les fichiers du projet et l'historique Git. La zone de préparation contient les versions choisies avec `git add` pour le prochain commit. Un commit enregistre cette sélection dans l'historique local, `HEAD` désigne le dernier commit de la branche et GitHub peut recevoir les commits après un `git push`.

## 2. Rôle du dossier de travail

Le working tree est l'ensemble des fichiers visibles et modifiables dans le projet. C'est là que je crée ou modifie mes fichiers avant de les préparer avec `git add`. Le dossier `.git`, lui, contient les données internes utilisées par Git pour gérer l'historique.

## 3. Zone de préparation et commit

La zone de préparation contient la version précise des fichiers choisis avec `git add`. Un fichier peut être modifié après cette étape, mais le commit enregistre seulement la version qui est encore préparée. Pour enregistrer la nouvelle version, je dois relancer `git add` avant le commit.

## 4. Exemple de problème réel

Un développeur peut exécuter `git add .` sans vérifier les fichiers ajoutés. Des fichiers de cache, des dossiers de dépendances volumineux ou des secrets peuvent alors se retrouver dans le commit et être envoyés sur GitHub. Cela peut ralentir le dépôt, créer des coûts ou exposer des accès au projet. Pour éviter ce problème, il faut utiliser un fichier `.gitignore`, vérifier `git status` et inspecter le contenu préparé avec `git diff --cached` avant chaque commit.

## 5. Preuve technique du bon fonctionnement

La preuve de mon lab est le dossier `repo_git_jour03` et les trois commits créés dans l'historique. Les commandes `git status`, `git diff`, `git diff --cached` et `git log --oneline --graph --decorate -5` ont montré le passage des fichiers entre le dossier de travail, la zone de préparation et l'historique local.

## 6. Compromis identifié

Choisir précisément les fichiers avec `git add` demande plus de temps que d'ajouter tout le dossier. En échange, cette vérification réduit le risque d'inclure des fichiers inutiles ou sensibles et rend les commits plus faciles à comprendre.

## 7. Premier diagnostic en cas de problème

Je commence par réduire le problème : je vérifie ce qui fonctionne encore, ce qui échoue et ce qui a changé récemment. Je lis ensuite le message d'erreur et vérifie la commande saisie. Je vérifie que Git est installé avec `git --version` et qu'il est accessible depuis le terminal grâce au `PATH`. Si Git fonctionne, j'utilise `git status` pour connaître l'état du dépôt et `git remote -v` pour vérifier le dépôt distant avant de modifier une configuration.

## 8. Explication du sujet

Git est un outil de gestion de versions qui conserve l'évolution d'un projet et permet de créer un historique propre. Le dépôt local contient les fichiers et leur historique, tandis que GitHub est un dépôt distant qui reçoit les commits après un `git push`. La zone de préparation contient les versions choisies avec `git add`, puis un commit les enregistre dans l'historique local. Dans ce lab, j'ai vérifié cette séparation avec un fichier affiché comme `AM`. Cette méthode demande un peu plus de rigueur, mais elle évite de publier des changements non vérifiés.

## Points essentiels

1. Le working tree contient les fichiers actuellement modifiables.
2. La zone de préparation contient les versions sélectionnées pour le prochain commit.
3. Un commit enregistre cette sélection dans l'historique local.
4. `HEAD` désigne le dernier commit de la branche actuelle.
5. Un remote est un dépôt distant, comme `origin` sur GitHub.
