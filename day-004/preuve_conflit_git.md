# Preuve de conflit Git du Jour 4

## Résultat attendu

Créer une branche de fonctionnalité, modifier le même fichier sur deux branches, provoquer un conflit lors de la fusion et le résoudre en justifiant le choix retenu.

## Risque principal

Un conflit mal résolu peut supprimer une modification utile ou introduire un texte incohérent. Je dois donc lire les marqueurs de conflit, choisir le contenu final et vérifier le résultat avant le commit de fusion.

## Preuve de réussite

La preuve sera l'historique Git, le fichier final après la fusion, les commandes de vérification et la description de la résolution.

## Commandes exécutées

```powershell
git switch -c feature/message-equipe
git diff
git add day-004/message_equipe.md
git commit -m "feat: valider le message d'équipe"
git switch main
git commit -m "docs: ajouter le statut de revue sur main"
git log --oneline --graph --decorate --all -8
git merge feature/message-equipe
git status
git diff --cached
git commit -m "merge: intégrer feature/message-equipe après résolution de conflit"
git branch -d feature/message-equipe
```

## Résultats observés

La branche `feature/message-equipe` a modifié le statut du message en indiquant qu'il était validé. La branche `main` a modifié la même ligne en indiquant qu'une revue était attendue. Git a refusé de choisir automatiquement entre les deux versions et a interrompu la fusion avec un conflit.

## Conflit et résolution

Le fichier contenait les marqueurs `<<<<<<< HEAD`, `=======` et `>>>>>>> feature/message-equipe`. La première partie représentait la version de `main` et la seconde celle de la branche de fonctionnalité.

La résolution retenue est la suivante :

```text
Statut du message : validé après revue sur main.
```

Elle conserve l'idée de validation de la branche de fonctionnalité et l'exigence de revue de `main`. Après avoir supprimé les marqueurs, `git add day-004/message_equipe.md` a marqué le conflit comme résolu. Le commit de fusion `678a99d` a ensuite réuni les deux historiques.

## Limite, risque et compromis

Le risque est de choisir une version sans comprendre l'intention de chaque branche, ce qui peut supprimer une modification utile. Le compromis est que les branches et la revue demandent plus de temps qu'une modification directe sur `main`, mais elles réduisent le risque de publier un changement non relu. La limite de ce lab est qu'il simule une revue locale et ne crée pas de véritable pull request sur GitHub.

## Bilan personnel

Aujourd'hui, j'ai créé une branche de fonctionnalité, effectué un commit isolé, puis créé une modification concurrente sur `main`. J'ai provoqué un conflit de manière contrôlée, lu ses marqueurs, choisi une résolution et terminé la fusion. Je sais maintenant utiliser une branche courte pour protéger `main` et vérifier un conflit avant de le résoudre.
