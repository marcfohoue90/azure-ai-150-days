# Exercices - Jour 5

## 1. Markdown et documentation technique

Markdown est un langage de balisage léger qui structure un document avec des symboles simples. Il permet par exemple de créer des titres, des listes et des blocs de code dans un fichier lisible. La documentation technique explique le fonctionnement d'un projet afin qu'une autre personne puisse le préparer, l'utiliser, le vérifier et le dépanner.

## 2. Rôle du README

Le README est le point d'entrée d'un projet. Il explique son objectif, les prérequis, les étapes d'installation ou d'utilisation, les vérifications à réaliser et les limites connues.

## 3. Prérequis et installation

Les prérequis sont les conditions nécessaires avant de commencer, comme Git installé et disponible dans le terminal. L'installation prépare ensuite le projet à être utilisé, par exemple en clonant le dépôt ou en installant ses dépendances.

## 4. Exemple de problème réel

Si un README ne précise pas qu'un outil doit être accessible dans le `PATH`, un développeur peut installer cet outil puis obtenir une erreur indiquant que la commande est introuvable. Il peut détecter le problème avec une commande de version, comme `git --version`, puis corriger la configuration du `PATH`.

## 5. Preuve technique du laboratoire

Le fichier `README_professionnel.md` contient la commande `git status --short`, le résultat attendu et une erreur contrôlée. La sortie `?? day-005/` montre que Git détecte le dossier sans encore suivre ses fichiers. L'erreur obtenue hors d'un dépôt Git démontre également que le dépannage est documenté.

## 6. Compromis identifié

Une documentation courte reste simple à lire, mais elle ne peut pas couvrir toutes les erreurs possibles. Elle doit prioriser les étapes essentielles et les problèmes les plus fréquents.

## 7. Premières vérifications en cas de problème

Je vérifierais d'abord que Git est disponible avec `git --version`, puis que je suis dans le bon dépôt avec `git status`. Je comparerais ensuite l'erreur observée avec la documentation avant de modifier une configuration.

## 8. Explication courte du sujet

Markdown sert à structurer clairement un texte avec des symboles simples. La documentation technique s'appuie sur ce format pour expliquer comment utiliser et vérifier un projet. Un README bien écrit aide une autre personne à reproduire le travail sans devoir contacter son auteur. Sa limite est qu'il doit rester concis et ne peut pas détailler tous les cas possibles.
