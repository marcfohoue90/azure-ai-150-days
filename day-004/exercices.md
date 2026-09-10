# Exercices du Jour 4

## 1. Branches, fusion, pull request et conflits

Une feature branch est une branche séparée créée pour développer un changement sans modifier `main`. Un merge intègre les changements de cette branche dans `main`. Une pull request sert à demander une revue, discuter du changement et vérifier sa qualité avant la fusion. Un conflit apparaît lorsque Git trouve deux modifications incompatibles sur la même partie d'un fichier et ne peut pas choisir seul. Ce fonctionnement permet de travailler en équipe avec des branches courtes tout en protégeant `main`, qui reste une branche stable avec des changements relus et validés.

## 2. Rôle d'une feature branch

Une feature branch permet de développer une fonctionnalité de manière séparée. Elle permet de créer des commits, tester le changement et demander une revue sans modifier `main`. Dans ce lab, `feature/message-equipe` a permis de modifier le statut du message sans affecter la branche principale avant la fusion.

## 3. Merge et pull request

Une pull request sert à présenter une branche pour revue, discussion et validation avant son intégration. Un merge est l'opération qui fusionne réellement les changements de la branche dans `main`, après la revue.

## 4. Exemple de problème réel

Un conflit mal résolu peut provoquer un problème réel. Si une personne garde une seule version sans comprendre les changements de l'autre branche, elle peut supprimer une information utile. Si les marqueurs de conflit restent dans le fichier, le projet peut devenir invalide. Pour éviter cela, il faut comprendre l'intention de chaque branche, vérifier le contenu final et contrôler l'état Git avant le commit.

## 5. Preuve technique du bon fonctionnement

La preuve du lab est le fichier `preuve_conflit_git.md`, le fichier final `message_equipe.md` et l'historique Git. La commande `git log --oneline --graph --decorate --all -8` montre les deux branches et leur réunion dans le commit de fusion `678a99d`. La commande `git status` a aussi montré le conflit, puis sa résolution après `git add`.

## 6. Compromis identifié

Travailler directement sur `main` permet d'aller plus vite, mais augmente le risque de publier une erreur ou un changement non relu. Utiliser une branche et une pull request demande plus de temps, mais protège la branche principale et facilite la revue du travail.

## 7. Premier diagnostic en cas de problème

Si une fusion ne fonctionne pas comme prévu, je commence par réduire le problème : je vérifie ce qui fonctionne, ce qui échoue et les changements récents. Je lis ensuite le message d'erreur et exécute `git status`. Je vérifie la branche active avec `git branch --show-current` et l'historique récent avec `git log --oneline --graph --decorate --all`. En cas de conflit, j'ouvre le fichier concerné, lis les marqueurs et choisis une résolution avant d'utiliser `git add` et de créer le commit de fusion.

## 8. Explication du sujet

Une branche permet de développer un changement sans modifier directement `main`. Une pull request permet de faire relire et valider le changement avant son intégration. Un merge réunit ensuite la branche de fonctionnalité et `main`. Si les deux branches modifient la même ligne de manière différente, Git crée un conflit et demande à une personne de choisir le contenu final. Dans ce lab, le conflit a été résolu en gardant le statut « validé après revue sur main ». Cette méthode demande plus de temps qu'une modification directe, mais elle évite des changements non relus sur `main`.

## Points essentiels

1. Une feature branch isole une modification avant son intégration dans `main`.
2. Un merge intègre les changements d'une branche dans une autre.
3. Une pull request permet la revue et la discussion avant la fusion.
4. Un conflit demande une décision humaine lorsque Git ne peut pas choisir entre deux modifications.
5. Un rebase replace les commits d'une branche sur une base plus récente. Il peut rendre l'historique plus linéaire, mais il ne doit pas réécrire l'historique déjà partagé sans accord de l'équipe.
