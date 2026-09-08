# Journal technique du jour 1

Le 7 septembre 2026

Première phase consacrée au développement logiciel

Dépôt `azure-ai-150-days`

## Objectif du jour

Mettre en place une méthode de travail que je pourrai utiliser pendant les 149 prochains jours. Je veux apprendre sans suivre un tutoriel mécaniquement.

Ma méthode tient en quatre verbes. Comprendre, construire, tester et expliquer.

## Ce que je voulais obtenir

- Un journal technique pour garder une trace de mon travail.
- Une méthode de travail quotidienne claire.
- Une idée concrète de ce qu'un développeur junior doit savoir faire en équipe.
- Une liste de critères pour décider qu'une tâche est terminée.
- Une première réalisation enregistrée avec Git.

Je veux pouvoir expliquer cette méthode sans lire mes notes.

## Le risque à éviter

Le principal risque est de suivre les instructions sans comprendre. Lire une notion, reconnaître son nom et savoir réellement l'utiliser sont trois choses différentes. Je veux être capable de mettre une notion en pratique, de l'expliquer et de défendre mes choix.

## Les preuves prévues

Pour ce premier jour, les preuves sont le présent journal, le dossier `day-001`, une vérification avec `git status`, une petite erreur analysée, les exercices et un commit Git envoyé sur GitHub.

## Mon environnement de travail

Je sépare les supports de formation de mes productions personnelles.

```text
C:\
|
+-- AI\AI150_V2\                 supports de formation
|
+-- azure-ai-150-days\            réalisations personnelles
    |-- README.md
    +-- day-001\
        |-- README.md
        +-- journal_technique.md
```

Le dossier `C:\AI\AI150_V2` contient ce que j'étudie. Le dossier `C:\azure-ai-150-days` contient ce que je réalise et ce que je peux montrer comme preuve de progression. Je ne publie pas les contenus du pack de formation.

## Ma méthode pour les 150 jours

Pour chaque journée, je vais suivre cette démarche.

1. Lire l'objectif du jour.
2. Comprendre le cours.
3. Réaliser l'exercice ou le projet.
4. Tester le résultat.
5. Observer les erreurs ou une limite.
6. Chercher la cause du problème avant de modifier quoi que ce soit.
7. Corriger le problème.
8. Vérifier la correction.
9. Faire les exercices avant de regarder le corrigé.
10. Comparer mes réponses avec le corrigé.
11. Résumer ce qui est important.
12. Expliquer les notions essentielles sans notes.
13. Documenter les observations utiles.
14. Garder une preuve du travail avec Git.

En pratique, je pars d'une compréhension du besoin, je réalise quelque chose, je le teste, puis j'observe, corrige et vérifie ce qui doit l'être. Enfin, je l'explique et je conserve une trace du travail.

## Ce qu'est un bon débutant en équipe

Je n'ai pas besoin de tout connaître pour être utile dans une équipe. Je dois pouvoir réaliser une tâche sous supervision de manière propre et reproductible.

Pour cela, je dois apprendre à comprendre le besoin, consulter la documentation, construire une solution, la tester, repérer un problème, en chercher la cause, corriger puis vérifier. Je dois aussi protéger les secrets, documenter mon travail, expliquer mes décisions, reconnaître les limites et demander de l'aide en disant clairement ce que j'ai déjà essayé.

## Expérience avec Git

### Objectif

Observer la manière dont Git repère les changements dans un dossier de travail.

### Manipulation

```powershell
cd C:\azure-ai-150-days\day-001
New-Item test-erreur.txt
git status
```

Le fichier `test-erreur.txt` doit apparaître comme non suivi. Il existe sur le disque mais Git ne le suit pas encore.

Je le supprime ensuite.

```powershell
Remove-Item test-erreur.txt
git status
```

Comme ce fichier n'a jamais été ajouté à Git, il ne doit plus apparaître dans l'état du dépôt.

### Ce que j'ai compris

La présence d'un fichier dans un dépôt local ne suffit pas pour que Git le versionne. Un nouveau fichier est d'abord non suivi. Après `git add`, il est prêt à être enregistré. Après `git commit`, il fait partie de l'historique.

Le statut non suivi vient donc du fait que le fichier existe dans le dossier de travail mais n'a pas été ajouté à l'index de Git.

### Correction et vérification

Dans cet exercice, `test-erreur.txt` est temporaire. La bonne action est donc de le supprimer et de vérifier de nouveau avec `git status`.

Si le fichier était nécessaire au projet, je l'ajouterais avec `git add test-erreur.txt`, puis je vérifierais son état avant de le valider dans un commit.

## Exercices et réponses

### Définir une méthode de travail

Une méthode de travail d'ingénieur est une démarche reproductible qui permet de passer d'un objectif à un résultat vérifié et documenté. Elle demande de comprendre le problème, de construire, de tester et d'expliquer le résultat.

Le journal technique garde la trace du travail. La recherche de cause identifie la raison profonde d'un problème. Les preuves et les critères de fin permettent de montrer que le travail est réellement terminé.

### Pourquoi construire et tester

Comprendre permet de savoir ce que l'on veut résoudre. Construire transforme cette compréhension en résultat concret. Tester permet de comparer le résultat réel avec le résultat attendu. Expliquer oblige à reformuler ce que l'on a fait et permet de vérifier que la compréhension est solide.

### Journal technique et cause d'un problème

Le journal technique rassemble l'objectif, les manipulations, les observations, les erreurs, les décisions, les corrections et les résultats. La cause d'un problème est la raison fondamentale pour laquelle il est arrivé. Le journal est plus large car il garde la trace de tout le travail.

### Exemple de problème de sécurité

Un développeur peut déposer par erreur une clé d'accès dans un fichier envoyé sur un dépôt public. La clé devient alors visible et pourrait être utilisée pour accéder au service ou créer des coûts.

Ce problème peut être repéré en examinant le dépôt, grâce à un outil de détection de secrets, dans les journaux du service ou par une activité inhabituelle. Il montre qu'il faut vérifier les fichiers avant un envoi.

### Preuve du travail

Le fichier `journal_technique.md` est ma preuve principale. Elle est complétée par le résultat visible de `git status` et par le commit qui enregistre le travail. Une preuve ne consiste pas seulement à dire que quelque chose fonctionne. Elle doit pouvoir être observée et reproduite.

### Compromis

Le compromis du jour oppose la rapidité à la fiabilité. Aller vite en exécutant les commandes puis en envoyant le travail sans vérification fait gagner du temps à court terme. Prendre le temps de tester, contrôler l'état de Git et documenter ralentit un peu le travail, mais réduit les erreurs et améliore la sécurité.

### Première réaction face à une panne

Je ne modifierais pas tout de suite la configuration. Je chercherais d'abord à savoir ce qui fonctionne encore, ce qui ne fonctionne plus, ce qui a changé récemment et si le problème peut être reproduit. Je regarderais ensuite les messages d'erreur, les journaux et l'état des services avant de corriger.

## Les notions à retenir

1. Comprendre, construire, tester et expliquer transforme une notion théorique en compétence vérifiée.
2. Un journal technique garde une trace structurée du travail réalisé.
3. Chercher la cause d'un problème évite de ne corriger que son symptôme.
4. Une preuve de travail est un résultat visible, comme un fichier, un test, un journal, une mesure ou un commit.
5. Des critères de fin permettent de décider qu'une tâche est vraiment terminée.

## Risque, limite et compromis

Le risque est de publier un secret ou un fichier qui ne devrait pas être envoyé. La limite est qu'un journal ne garantit pas, à lui seul, que le travail est bon. Il doit correspondre à des tests réellement effectués. Le compromis est le temps passé à vérifier et documenter, en échange d'un travail plus fiable et plus facile à reproduire.

## Checklist du jour

- [x] J'ai compris l'objectif du jour.
- [x] J'ai étudié le cours.
- [x] J'ai produit ce journal technique.
- [x] J'ai défini ma méthode de travail.
- [x] J'ai identifié une erreur ou une limite à tester.
- [x] J'ai identifié la cause d'un problème.
- [x] J'ai répondu aux exercices.
- [x] J'ai identifié un risque, une limite et un compromis.
- [x] J'ai défini une preuve de travail.
- [ ] J'ai vérifié l'état du dépôt avec `git status`.
- [ ] J'ai créé le commit final.
- [ ] J'ai envoyé le travail sur GitHub.

## Bilan du jour 1

Aujourd'hui, j'ai compris que l'objectif n'est pas seulement de terminer des cours. Je dois acquérir une méthode de travail. Je commence par comprendre, je réalise, je teste, je cherche la cause des problèmes, je corrige, je vérifie, j'explique et je garde une preuve de ce que j'ai fait.

Je comprends aussi la différence entre un journal technique, qui garde l'historique du travail, et la cause d'un problème, qui explique son origine. Une tâche n'est pas terminée parce qu'elle semble fonctionner. Elle doit être vérifiée et appuyée par une preuve visible.

## Critères de fin

Le jour 1 sera terminé lorsque je pourrai expliquer le sujet sans notes, que ce journal et les exercices seront terminés, qu'une preuve aura été définie, que l'état du dépôt aura été vérifié et que le travail aura été envoyé sur GitHub.

## Conclusion

Ce premier jour pose la méthode qui servira pour la suite. Mon but est de devenir progressivement capable de comprendre une tâche, de la réaliser, de la tester, de corriger les problèmes et d'expliquer mes décisions avec des preuves simples et reproductibles.
