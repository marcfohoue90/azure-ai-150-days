# Notes de laboratoire - Jour 8

## Résultat attendu

Le programme calcule le budget à partir de la configuration, valide les coûts et affiche un rapport clair.

## Risque principal

Un import mal écrit ou un mauvais découpage entre les modules peut empêcher le programme de démarrer.

## Preuve de réussite

L'exécution de `main.py` affiche le total et le statut du budget. Un test avec un coût négatif confirme que cette valeur est refusée.

## Architecture

- `config.py` contient les valeurs de configuration.
- `calcul.py` valide les coûts et calcule leur total.
- `reporting.py` affiche le résultat.
- `main.py` coordonne les modules et constitue le point d'entrée.

## Commande de lancement

Depuis le dossier `day-008` :

```powershell
python -m package_budget.main
```

## Résultat observé

Avec les coûts `25.0`, `40.0` et `15.5`, le programme affiche un total de `80.5 €` et le message `Budget respecté.`

## Erreur contrôlée

Un coût temporaire de `-15.0` dans `COUTS_CLOUD` doit afficher :

```text
Erreur : un coût ne peut pas être négatif.
```

### Cause racine

Un coût négatif fausserait le total et pourrait masquer un dépassement de budget.

### Correction

La fonction `couts_sont_valides` parcourt les coûts et renvoie `False` dès qu'elle rencontre une valeur négative. `main.py` arrête alors le programme avant le calcul et le rapport.

## Limite et compromis

La séparation en modules facilite les tests et la lecture, mais elle ajoute des imports et plusieurs fichiers à parcourir. Cette organisation est adaptée dès que le programme contient plusieurs responsabilités, mais serait excessive pour un script de quelques lignes.
