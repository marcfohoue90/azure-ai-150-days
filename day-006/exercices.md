# Exercices - Jour 6

## 1. Python, variables, types et contrôle de flux

Python permet d'écrire des programmes lisibles qui manipulent des valeurs et prennent des décisions. Les variables stockent ces valeurs sous des noms explicites. Les types, comme `int`, `float`, `str` et `bool`, indiquent la nature d'une valeur. Les conditions et les boucles contrôlent le chemin suivi par le programme et les actions répétées.

## 2. Rôle des types de base

`int` représente un nombre entier, `float` un nombre décimal, `str` un texte et `bool` une valeur vraie ou fausse. Dans le laboratoire, les coûts et le budget sont des `float`, tandis que `couts_valides` est un booléen qui indique si le calcul peut être utilisé.

## 3. Conditions et boucles

`if`, `elif` et `else` servent à choisir une action selon une condition. `for` parcourt une collection, tandis que `while` répète une action tant qu'une condition reste vraie. Le script utilise `for` pour examiner chaque coût, puis `if` pour décider si le budget est respecté.

## 4. Exemple de problème réel

Un coût négatif ajouté sans contrôle ferait diminuer le total et pourrait masquer un dépassement de budget. Le risque concerne la personne qui prend une décision à partir de cette estimation. La détection est possible avec un test contenant une valeur négative et le message d'erreur attendu.

## 5. Preuve technique

La commande `python .\budget_cloud.py` produit un total de `80.5 €` et le message `Budget respecté.` avec la liste de coûts normale. Un test avec un total supérieur au budget produit une alerte. Un test avec un coût négatif produit un message d'erreur.

## 6. Compromis identifié

Le script reste simple et facile à comprendre, mais ses coûts sont définis dans le code. Cette approche convient à un exercice, mais pas à un calcul de production qui nécessiterait des données réelles et une validation plus complète.

## 7. Diagnostic initial

Je vérifierais d'abord le message d'erreur, les valeurs présentes dans `couts_cloud` et le budget configuré. Je lancerais ensuite le script avec un cas connu avant de modifier le code.

## 8. Explication courte

Les variables permettent de nommer les données d'un programme et les types indiquent ce que ces données représentent. Les conditions permettent de choisir une action, tandis que les boucles évitent de répéter le même code. Dans ce laboratoire, une boucle additionne les coûts cloud et une condition signale un dépassement ou un coût invalide. Le script est utile pour apprendre, mais ses données restent simulées.
