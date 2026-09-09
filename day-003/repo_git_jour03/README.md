# Exercice Git du Jour 3

Ce dossier sert à pratiquer le cycle Git sur des fichiers simples.

Le résultat attendu est un historique de trois commits atomiques. Chaque commit doit correspondre à une modification précise et vérifiable.

Les étapes, les commandes, les résultats et l'erreur analysée seront documentés progressivement dans ce fichier.

## Résultat attendu

Le dossier contiendra des notes simples sur le cycle Git. L'historique du dépôt principal montrera trois commits distincts et les commandes `git status`, `git diff` et `git log` permettront de vérifier chaque étape.

## Risque principal

Ajouter tous les fichiers sans les vérifier peut inclure un fichier temporaire, un cache ou un secret. Je vérifie donc le résultat de `git status` et de `git diff --cached` avant chaque commit.

## Preuve de réussite

La preuve sera l'historique Git, les fichiers du dossier et les résultats des commandes de vérification.

## Première observation

Après la création de `working_tree.md`, `git status --short` a affiché le fichier comme non suivi. La commande `git diff` n'a rien affiché, car ce fichier n'était pas encore suivi par Git. Ce cas montre que `git status` sert à repérer les nouveaux fichiers, tandis que `git diff` sert à examiner les différences des fichiers déjà suivis.

## Démonstration de la zone de préparation

Après la préparation de la première version de `staging_commit_historique.md`, le fichier a été modifié une seconde fois. `git status --short` a affiché `AM`. La commande `git diff` a montré les modifications non préparées, tandis que `git diff --cached` a montré la première version gardée dans la zone de préparation. Après une nouvelle commande `git add`, la version finale pourra être enregistrée dans le commit.
