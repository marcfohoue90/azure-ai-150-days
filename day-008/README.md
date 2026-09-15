# Jour 8 - Python : fonctions, modules et séparation des responsabilités

## Objectif

Découper un programme Python en fonctions testables et modules cohérents.

## Travail prévu

- Séparer la configuration, le calcul et l'affichage d'un budget cloud simulé.
- Utiliser des fonctions qui renvoient des valeurs avec `return`.
- Importer les fonctions nécessaires dans un point d'entrée unique.
- Tester un coût négatif et documenter la correction.

## Livrable principal

[Package de budget](package_budget/)

## Structure

```text
package_budget/
├── __init__.py
├── config.py
├── calcul.py
├── reporting.py
└── main.py
```

## Lancer le programme

Depuis le dossier `day-008` :

```powershell
python -m package_budget.main
```

## Critères de fin

- [x] Je peux expliquer le sujet sans mes notes.
- [x] Le package `package_budget/` est terminé.
- [x] J'ai fait les exercices avant de consulter le corrigé.
- [x] J'ai identifié une limite, un risque ou un compromis.
- [x] J'ai conservé une preuve de travail.
- [x] Le travail a été enregistré dans Git et sera envoyé sur GitHub.
