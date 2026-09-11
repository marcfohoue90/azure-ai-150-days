# Vérifier l'état d'un dépôt Git

## Objectif

Vérifier les fichiers modifiés, préparés ou non suivis dans un dépôt Git.

## Résultat attendu

La commande `git status --short` affiche un état court et lisible des fichiers du dépôt.

## Risque principal

Une mauvaise lecture des codes affichés par Git peut conduire à oublier un fichier ou à préparer un changement non souhaité.

## Preuve de réussite

La commande est exécutée dans le dépôt et son résultat permet d'identifier clairement l'état de chaque fichier.

## Architecture

```text
day-005/
├── README_professionnel.md
└── README.md
```

## Prérequis

- Git est installé et disponible dans le terminal.
- La commande est exécutée depuis un dépôt Git.

## Utilisation

Ouvrir un terminal à la racine du dépôt, puis exécuter :

```powershell
git status --short
```

## Résultat observé

Avant la préparation des fichiers du Jour 5, Git affiche :

```text
?? day-005/
```

Les deux points d'interrogation indiquent que le dossier est présent, mais que Git ne suit encore aucun de ses fichiers.

## Vérification

Après avoir choisi les fichiers à enregistrer et exécuté `git add` sur ces fichiers, la commande `git status --short` doit afficher `A` devant leur chemin. Cette lettre indique qu'ils sont prêts pour le prochain commit.

## Dépannage : erreur contrôlée

La commande suivante a été exécutée pour simuler un lancement hors d'un dépôt Git :

```powershell
git -C C:\Windows status --short
```

Résultat observé :

```text
fatal: not a git repository (or any of the parent directories): .git
```

### Cause racine

Le dossier `C:\Windows` ne contient pas de dépôt Git. Git ne trouve donc aucun dossier `.git` qui décrit l'historique et l'état des fichiers.

### Correction

Exécuter la commande depuis la racine du dépôt, ou utiliser l'option `-C` avec le chemin d'un dépôt Git valide.

## Limite

`git status --short` donne un état synthétique. Pour comprendre le contenu précis d'une modification, il faut compléter l'analyse avec `git diff` ou `git diff --cached`.
