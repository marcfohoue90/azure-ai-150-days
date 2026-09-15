# Exercices - Jour 8

## 1. Fonctions, modules et séparation des responsabilités

Les fonctions découpent un programme en petites tâches testables. Leur signature indique leur nom et les paramètres attendus, tandis que `return` transmet un résultat au reste du programme. Les modules répartissent ces fonctions et leurs données dans des fichiers cohérents. La séparation des responsabilités rend le code plus simple à lire, modifier et tester.

## 2. Rôle de la signature

La signature indique le nom d'une fonction et les paramètres qu'elle reçoit. Par exemple, `def calculer_total(couts):` annonce que la fonction calcule un total à partir de la valeur `couts`. Elle aide un autre développeur à comprendre comment appeler la fonction correctement.

## 3. Return et scope

`return` renvoie une valeur obtenue dans une fonction afin qu'une autre partie du programme puisse l'utiliser. Le scope définit l'endroit où une variable existe. Une variable locale, comme `total` dans `calculer_total`, ne peut pas être utilisée directement hors de cette fonction ; `return` permet de transmettre sa valeur sans exposer la variable locale.

## 4. Exemple de problème réel

Si les calculs, les valeurs de configuration et l'affichage sont mélangés dans une seule fonction, modifier le budget peut casser le rapport ou la validation. Le problème est détectable en lançant un scénario connu après chaque modification. Les modules séparés limitent cet impact.

## 5. Preuve technique

La commande `python -m package_budget.main`, lancée depuis `day-008`, affiche le total de `80.5 €` et le statut du budget. Un test avec un coût négatif affiche le message d'erreur avant tout calcul.

## 6. Compromis identifié

Les modules rendent un programme plus clair et plus testable, mais ils demandent des imports corrects et augmentent le nombre de fichiers. Pour un script très court, ce découpage peut être inutilement lourd.

## 7. Diagnostic initial

Je vérifierais le message d'erreur, le nom des modules importés et le dossier depuis lequel la commande est exécutée. Je lancerais ensuite le programme avec la configuration connue avant de modifier les fonctions.

## 8. Explication courte

Une fonction accomplit une tâche précise et peut renvoyer un résultat avec `return`. Un module est un fichier Python qui regroupe des fonctions ou des données ayant la même responsabilité. Dans ce laboratoire, la configuration, le calcul et l'affichage sont séparés, puis `main.py` les utilise. Cette organisation facilite les tests, mais ajoute des fichiers et des imports à gérer.
