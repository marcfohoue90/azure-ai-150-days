# Exercices - Jour 7

## 1. Collections et complexité pratique

Les collections Python permettent de stocker plusieurs données dans une même variable. Une `list` conserve un ordre et peut être modifiée, un `tuple` reste stable, un `set` conserve seulement des valeurs uniques et un `dict` associe des clés à des valeurs. La complexité pratique consiste à choisir la structure adaptée au besoin pour garder un code clair et éviter un travail inutile.

## 2. Rôle d'une liste

Une `list` conserve des éléments dans un ordre défini et peut évoluer. Dans le laboratoire, elle contient les ressources Azure fictives que le script parcourt une à une.

## 3. Tuple et set

Un `tuple` conserve des données ordonnées qui ne doivent pas changer, comme des coordonnées ou une version. Un `set` supprime les doublons et ne garantit pas l'ordre. Il convient par exemple aux régions uniques d'un inventaire cloud.

## 4. Exemple de problème réel

Si deux ressources ont le même nom et qu'un script les place dans un dictionnaire sans contrôle, la seconde peut remplacer la première silencieusement. Une personne peut alors consulter un inventaire incomplet. Le test avec le nom dupliqué `api-production` permet de détecter ce problème.

## 5. Preuve technique

La commande `python .\resources_parser.py` indexe les trois ressources valides et affiche deux régions uniques. Lorsqu'une ressource temporaire porte le même nom qu'une ressource existante, le script affiche une erreur et conserve la première valeur du dictionnaire.

## 6. Compromis identifié

Un `set` simplifie la suppression des doublons et la recherche d'une valeur, mais il ne conserve pas l'ordre. Si l'ordre est indispensable, une `list` ou un `tuple` sera préférable, avec une autre méthode pour gérer les doublons.

## 7. Diagnostic initial

Je lirais d'abord le message d'erreur et la ligne indiquée par Python. Je vérifierais ensuite la syntaxe, l'indentation et la présence des clés attendues dans chaque dictionnaire. Enfin, je relancerais le script avec les trois ressources connues avant de modifier sa logique.

## 8. Explication courte

Les collections Python permettent de regrouper plusieurs données de la manière adaptée au problème. Une liste est modifiable et ordonnée, un tuple est stable, un set supprime les doublons et un dictionnaire retrouve une valeur grâce à une clé. Dans ce laboratoire, une liste contient les ressources, un set déduplique les régions et un dictionnaire les indexe par nom. Le choix de la structure dépend donc du besoin d'ordre, de modification, d'unicité ou d'accès par clé.
