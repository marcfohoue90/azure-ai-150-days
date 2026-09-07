# Journal technique — Jour 001

## Méthode de travail d’un ingénieur production

**Date :** 07/09/2026  
**Phase :** 1 — Software Engineering  
**Repository :** `azure-ai-150-days`

---

## 1. Objectif du jour

Adopter une méthode reproductible pour apprendre, expérimenter et documenter sans dépendre d’un tutoriel.

L’objectif de cette première journée est de mettre en place une méthode que je pourrai réutiliser pendant les 149 prochains jours :

**Comprendre → Construire → Tester → Expliquer**

Cette boucle sera complétée dans la pratique par l’observation des erreurs, la recherche de leur cause racine, leur correction et la conservation d’une preuve de travail.

---

## 2. Résultat attendu

À la fin de cette séance, je dois disposer :

- d’un journal technique ;
- d’une méthode quotidienne claire ;
- d’une définition de ce que signifie être un junior production-ready ;
- d’une checklist permettant de savoir quand une tâche est réellement terminée ;
- d’une première preuve de travail versionnée avec Git.

Je dois également être capable d’expliquer cette méthode sans dépendre de mes notes.

---

## 3. Risque principal

Le principal risque est de suivre les cours et les instructions mécaniquement sans réellement comprendre ce que je fais.

Je veux éviter de confondre :

- avoir lu une notion ;
- reconnaître son nom ;
- savoir l’utiliser ;
- comprendre son fonctionnement ;
- être capable de l’expliquer et de la défendre.

---

## 4. Preuve de réussite

Ma réussite doit être observable.

Pour le Jour 001, mes preuves sont :

- le fichier `journal_technique.md` ;
- mon dossier `day-001` ;
- une manipulation Git observable avec `git status` ;
- une erreur ou un cas limite analysé ;
- mes réponses aux exercices ;
- un commit Git ;
- la présence du travail sur mon repository GitHub.

---

## 5. Organisation de mon environnement

Je sépare volontairement mes supports de formation de mes productions personnelles.

```text
C:\
│
├── AI\
│   └── AI150_V2\                  # Supports de formation
│
└── azure-ai-150-days\             # Productions personnelles
    ├── README.md
    └── day-001\
        ├── README.md
        └── journal_technique.md
```

### Règle

`C:\AI\AI150_V2` contient **ce que j’étudie**.

`C:\azure-ai-150-days` contient **ce que je produis et peux montrer comme preuve de progression**.

Je ne publie pas le contenu du pack `AI150_V2` dans mon repository GitHub.

---

## 6. Ma méthode pour les 150 jours

Pour chaque journée :

1. Lire l’objectif du jour.
2. Comprendre le cours.
3. Construire ou réaliser le lab.
4. Tester le résultat.
5. Observer les erreurs ou tester une limite.
6. Rechercher la cause racine avant de corriger.
7. Corriger le problème.
8. Vérifier que la correction fonctionne.
9. Faire les exercices avant le corrigé.
10. Comparer avec le corrigé.
11. Lire le résumé essentiel.
12. Expliquer les notions importantes sans notes.
13. Documenter les observations importantes.
14. Conserver une preuve de travail pertinente avec Git.

Ma boucle complète devient :

```text
Comprendre
    ↓
Construire
    ↓
Tester
    ↓
Observer
    ↓
Diagnostiquer
    ↓
Corriger
    ↓
Vérifier
    ↓
Expliquer
    ↓
Documenter
    ↓
Prouver
```

---

## 7. Définition personnelle de « production-ready junior »

Pour moi, être un junior production-ready ne signifie pas tout connaître.

Cela signifie être capable, sous supervision, de réaliser une tâche technique de manière propre, méthodique et reproductible.

Un junior production-ready doit progressivement savoir :

- comprendre l’objectif avant d’agir ;
- utiliser la documentation ;
- construire une solution ;
- tester son travail ;
- observer un problème ;
- rechercher sa cause racine ;
- corriger puis vérifier ;
- protéger les secrets ;
- documenter son travail ;
- expliquer ses décisions ;
- reconnaître les limites de sa solution ;
- demander de l’aide en précisant ce qui a déjà été testé.

---

# 8. Lab — expérience contrôlée avec Git

## Objectif

Observer comment Git détecte les changements dans mon workspace.

## Manipulation

```powershell
cd C:\azure-ai-150-days\day-001
New-Item test-erreur.txt
git status
```

### Comportement attendu

`test-erreur.txt` apparaît comme un fichier non suivi (`untracked`).

Cela signifie que le fichier existe dans le répertoire de travail, mais qu’il n’est pas encore suivi par Git.

Je supprime ensuite le fichier :

```powershell
Remove-Item test-erreur.txt
git status
```

Puisque le fichier n’a jamais été ajouté à Git, il ne doit plus apparaître comme fichier non suivi.

---

## 9. Cause racine

La présence d’un fichier dans un repository local ne signifie pas automatiquement que Git le versionne.

Un nouveau fichier passe par différents états :

```text
Fichier créé
    ↓
Untracked
    ↓
git add
    ↓
Staged
    ↓
git commit
    ↓
Committed
```

La cause du statut `untracked` est donc que le fichier existe dans le workspace mais n’a pas encore été ajouté à l’index Git.

---

## 10. Correction et vérification

Dans cette expérience, `test-erreur.txt` est uniquement un fichier temporaire.

La correction consiste donc à le supprimer :

```powershell
Remove-Item test-erreur.txt
```

Puis à vérifier :

```powershell
git status
```

S’il s’agissait d’un fichier réellement nécessaire au projet, je pourrais au contraire utiliser :

```powershell
git add test-erreur.txt
git status
```

avant de décider de le committer.

---

# 11. Exercices

## Exercice 1 — Définition précise

Une méthode de travail d’un ingénieur production est une démarche reproductible permettant de passer d’un objectif à un résultat technique vérifié et documenté.

Elle ne consiste pas uniquement à construire quelque chose : elle impose de comprendre le problème, construire, tester et être capable d’expliquer le résultat.

Le journal technique conserve les observations et décisions, tandis que l’analyse de cause racine permet de comprendre pourquoi un problème s’est produit.

Enfin, une preuve de travail et une définition de terminé permettent de démontrer objectivement que le travail a réellement été réalisé.

---

## Exercice 2 — Rôle de la boucle comprendre → construire → tester → expliquer

La boucle empêche de rester dans un apprentissage uniquement théorique.

**Comprendre** permet de savoir ce que l’on cherche à résoudre.

**Construire** transforme cette compréhension en réalisation concrète.

**Tester** permet de vérifier si le comportement réel correspond au comportement attendu.

**Expliquer** oblige à reformuler le fonctionnement et les décisions prises, ce qui permet de vérifier que la compréhension n’est pas superficielle.

---

## Exercice 3 — Journal technique vs cause racine

Le **journal technique** est un document qui conserve la trace du travail : objectif, manipulations, observations, erreurs, décisions, corrections et résultats.

La **cause racine** correspond à la raison fondamentale qui explique pourquoi un problème s’est produit.

Le journal technique a donc une portée plus large : il documente le travail dans son ensemble.

La cause racine est utilisée lorsqu’un problème doit être diagnostiqué afin d’éviter de corriger uniquement son symptôme.

---

## Exercice 4 — Scénario de mauvaise implémentation

Un développeur déploie une application et place accidentellement une clé API directement dans un fichier versionné sur un repository public.

**Déclencheur :** le fichier contenant la clé est ajouté puis poussé sur GitHub.

**Effet :** le secret devient publiquement accessible.

**Impact :** une personne peut utiliser cette clé pour accéder au service, consommer des ressources ou provoquer des coûts.

**Détection :** inspection du repository, outil de détection de secrets, logs ou activité anormale sur le service.

Cet exemple montre pourquoi une méthode de production doit intégrer la vérification et la sécurité avant le commit.

---

## Exercice 5 — Preuve technique du lab

Ma preuve principale est :

`journal_technique.md`

Elle est accompagnée d’un comportement observable avec :

```powershell
git status
```

Le commit Git constitue également une preuve versionnée que le travail a été enregistré.

Une bonne preuve technique ne repose donc pas uniquement sur l’affirmation « ça fonctionne », mais sur un résultat observable et reproductible.

---

## Exercice 6 — Compromis identifié

Le compromis principal identifié aujourd’hui concerne la **vitesse de livraison face à la fiabilité**.

Je pourrais travailler plus rapidement en exécutant directement les commandes et en poussant immédiatement mon travail.

Cependant, prendre le temps de tester, vérifier `git status`, documenter et analyser les erreurs ralentit légèrement la livraison.

Ce temps supplémentaire améliore cependant la fiabilité, la sécurité et la reproductibilité du travail.

---

## Exercice 7 — Premier diagnostic en cas de panne

Je ne commencerais pas immédiatement par modifier la configuration.

Je chercherais d’abord à réduire la portée du problème :

1. Qu’est-ce qui fonctionne encore ?
2. Qu’est-ce qui ne fonctionne plus ?
3. Qu’est-ce qui a changé récemment ?
4. Puis-je reproduire le problème ?
5. Quelles preuves puis-je collecter ?

Je consulterais ensuite les messages d’erreur, logs, états ou résultats de commandes disponibles avant de modifier le système.

L’objectif est de diagnostiquer avant de corriger.

---

## Exercice 8 — Explication en moins de 60 secondes

Une méthode de travail d’ingénieur production consiste à ne pas simplement chercher à faire fonctionner une solution.

Je commence par comprendre le résultat attendu, je construis une solution, puis je teste son comportement.

Lorsqu’un problème apparaît, je collecte des preuves et recherche sa cause racine avant de le corriger.

Je documente ensuite ce que j’ai fait et je conserve une preuve reproductible du résultat.

Par exemple, avec Git, je vérifie les fichiers modifiés avant un commit plutôt que de publier mécaniquement.

La limite est que cette méthode demande plus de discipline et parfois plus de temps, mais elle réduit les erreurs et rend le travail plus fiable.

---

# 12. Auto-évaluation des exercices

| Exercice | Évaluation |
|---|---:|
| Définition | 2/2 |
| Boucle de travail | 2/2 |
| Journal vs cause racine | 2/2 |
| Problème réel | 2/2 |
| Preuve technique | 2/2 |
| Compromis | 2/2 |
| Diagnostic | 2/2 |
| Explication orale | 2/2 |

**Résultat de référence : 16/16 — 100 %**

> Cette auto-évaluation correspond aux réponses de référence rédigées pour le Jour 001. À partir du Jour 002, je dois répondre moi-même avant de consulter le corrigé.

---

# 13. Les cinq notions essentielles

## 1. Boucle comprendre → construire → tester → expliquer

Une méthode qui transforme une connaissance théorique en capacité technique vérifiée.

## 2. Journal technique

Une trace structurée de ce qui a été réalisé, observé, décidé, testé et corrigé.

## 3. Cause racine

La cause fondamentale expliquant pourquoi un problème s’est produit, contrairement au simple symptôme visible.

## 4. Preuve de travail

Un élément observable permettant de démontrer qu’un travail a réellement été réalisé : fichier, test, commande, log, métrique, comportement ou commit.

## 5. Définition de terminé

Un ensemble de critères objectifs permettant de décider qu’une tâche peut réellement être considérée comme terminée.

---

# 14. Risque, limite et compromis

## Risque

Publier accidentellement un secret ou un fichier qui ne devrait pas être versionné.

## Limite

Un journal technique ne garantit pas à lui seul la qualité du travail. Les informations documentées doivent correspondre aux tests réellement effectués.

## Compromis

Documenter et vérifier demande davantage de temps qu’exécuter rapidement une manipulation.

Ce coût est accepté afin d’améliorer la fiabilité, la sécurité, la compréhension et la reproductibilité.

---

# 15. Checklist quotidienne

- [x] J’ai compris l’objectif du jour.
- [x] J’ai étudié le cours.
- [x] J’ai produit `journal_technique.md`.
- [x] J’ai défini ma méthode de travail.
- [x] J’ai identifié une erreur ou un cas limite à tester.
- [x] J’ai identifié une cause racine.
- [x] J’ai répondu aux exercices.
- [x] J’ai comparé les réponses aux critères du corrigé.
- [x] J’ai étudié le résumé essentiel.
- [x] J’ai identifié une limite, un risque et un compromis.
- [x] J’ai défini une preuve de travail.
- [ ] J’ai vérifié une dernière fois le repository avec `git status`.
- [ ] J’ai réalisé le commit final.
- [ ] J’ai poussé le travail sur GitHub.

---

# 16. Bilan personnel du Jour 001

Aujourd’hui, j’ai compris que mon objectif pendant les 150 jours ne sera pas simplement de terminer des cours.

Je dois progressivement développer une méthode d’ingénieur :

**comprendre → construire → tester → diagnostiquer → corriger → expliquer → documenter → prouver.**

J’ai également compris la différence entre un journal technique, qui conserve l’historique et le raisonnement de mon travail, et une cause racine, qui cherche à expliquer l’origine fondamentale d’un problème.

Enfin, une tâche n’est pas terminée parce que je pense qu’elle fonctionne. Je dois disposer d’une preuve observable et d’une définition claire de terminé.

À partir du Jour 002, je dois appliquer cette méthode avec davantage d’autonomie et utiliser l’assistance principalement lorsque je bloque ou lorsque je souhaite être challengé.

---

# 17. Preuve de travail

## Repository

`azure-ai-150-days`

## Dossier

`day-001`

## Livrables

```text
day-001/
├── README.md
└── journal_technique.md
```

## Commit

```text
docs: complete day 001 engineering workflow
```

---

# 18. Définition de terminé

Le Jour 001 est terminé lorsque :

- [x] je peux expliquer le sujet sans mes notes ;
- [x] j’ai produit `journal_technique.md` ;
- [x] les exercices ont été traités ;
- [x] j’ai identifié une limite, un risque ou un compromis ;
- [x] une preuve de travail est définie ;
- [ ] le repository a été vérifié ;
- [ ] le commit a été créé ;
- [ ] le commit a été poussé sur GitHub.

---

# Conclusion

Le Jour 001 établit la méthode qui servira pendant toute la formation.

Mon objectif pour les 149 prochains jours est de devenir progressivement capable de réaliser cette démarche sans assistance :

> **Comprendre ce que je fais, construire, tester, rechercher les causes des problèmes, corriger, expliquer mes décisions et conserver des preuves reproductibles de mon travail.**