# Ce script calcule un budget cloud simulé.
# Il additionne plusieurs coûts et vérifie si le budget est dépassé.

budget_maximum = 100.0

couts_cloud = [25.0, 40.0, 15.5]

cout_total = 0.0
couts_valides = True

for cout in couts_cloud:
    if cout < 0:
        couts_valides = False
    else:
        cout_total = cout_total + cout

if not couts_valides:
    print("Erreur : un coût ne peut pas être négatif.")
elif cout_total > budget_maximum:
    print("Coût total :", cout_total, "€")
    print("Alerte : le budget est dépassé.")
else:
    print("Coût total :", cout_total, "€")
    print("Budget respecté.")
