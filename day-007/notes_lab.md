# Notes de laboratoire - Jour 7

## Résultat attendu

Le script parcourt des ressources Azure fictives, affiche les régions uniques et permet de retrouver chaque ressource par son nom.

## Risque principal

Une ressource incomplète ou deux ressources portant le même nom peuvent donner un résultat incorrect ou écraser une donnée dans le dictionnaire.

## Preuve de réussite

L'exécution affiche les ressources indexées et les régions sans doublon. Un test avec un nom dupliqué affiche une erreur claire.

## Commande de lancement

```powershell
python .\resources_parser.py
```

## Résultat observé

Avec trois ressources valides, le script indexe les noms `api-production`, `base-donnees` et `site-vitrine`. Les régions `francecentral` et `westeurope` n'apparaissent qu'une fois dans le `set`, même si deux ressources utilisent `francecentral`.

## Erreur contrôlée

Une quatrième ressource temporaire avec le nom `api-production` a été ajoutée. Le script a affiché :

```text
Erreur : nom de ressource dupliqué : api-production
```

### Cause racine

Deux ressources ont le même nom. Sans contrôle, la seconde pourrait remplacer silencieusement la première dans le dictionnaire.

### Correction

Le script vérifie la présence du nom dans `ressources_par_nom` avant de l'ajouter. En cas de doublon, il conserve la première ressource et affiche l'erreur.

## Limite et compromis

Les ressources sont écrites directement dans le script et seules les clés attendues sont utilisées. Cette version facilite l'apprentissage, mais une version de production devrait lire des données externes et vérifier aussi la présence de chaque clé.
