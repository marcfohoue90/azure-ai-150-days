# Notes de laboratoire - Jour 6

## Résultat attendu

Le script calcule le prix total de coûts cloud simulés et indique si le budget est respecté.

## Risque principal

Un coût invalide peut fausser le calcul ou interrompre le programme.

## Preuve de réussite

Le script produit un total exact et un message cohérent pour un cas sous le budget et un cas où le budget est dépassé.

## Commande de lancement

```powershell
python .\budget_cloud.py
```

## Résultats observés

Avec `couts_cloud = [25.0, 40.0, 15.5]`, le script affiche un total de `80.5 €` et confirme que le budget est respecté.

Lors d'un test temporaire avec un total supérieur à `100.0`, le script affiche une alerte de dépassement.

## Erreur contrôlée

Un coût négatif, comme `-15.0`, est invalide dans cette simulation. Le script doit afficher `Erreur : un coût ne peut pas être négatif.` au lieu d'annoncer un budget valide.

### Cause racine

Sans validation, un coût négatif réduitrait artificiellement le total et pourrait masquer un dépassement de budget.

### Correction

Chaque coût est vérifié dans la boucle. Lorsqu'une valeur est inférieure à zéro, le booléen `couts_valides` passe à `False` et le calcul final est bloqué.

## Limite et compromis

Le script est volontairement simple : les coûts sont inscrits directement dans le fichier et ne proviennent pas d'un fournisseur cloud réel. Cette simplicité facilite l'apprentissage, mais elle ne convient pas à une estimation de production.
