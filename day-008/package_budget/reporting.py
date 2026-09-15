# Fonction d'affichage du rapport de budget.


def afficher_rapport(total, budget_maximum):
    """Affiche le total et le statut du budget."""
    print("Coût total :", total, "€")

    if total > budget_maximum:
        print("Alerte : le budget est dépassé.")
    else:
        print("Budget respecté.")
