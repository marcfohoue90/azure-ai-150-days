# Point d'entrée du programme.

from package_budget.calcul import calculer_total, couts_sont_valides
from package_budget.config import BUDGET_MAXIMUM, COUTS_CLOUD
from package_budget.reporting import afficher_rapport


def main():
    """Lance la validation, le calcul puis le rapport."""
    if not couts_sont_valides(COUTS_CLOUD):
        print("Erreur : un coût ne peut pas être négatif.")
        return

    total = calculer_total(COUTS_CLOUD)
    afficher_rapport(total, BUDGET_MAXIMUM)


if __name__ == "__main__":
    main()
