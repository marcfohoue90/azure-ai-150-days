# Fonctions de validation et de calcul du budget.


def couts_sont_valides(couts):
    """Retourne False lorsqu'un coût négatif est présent."""
    for cout in couts:
        if cout < 0:
            return False
    return True


def calculer_total(couts):
    """Retourne la somme des coûts fournis."""
    return sum(couts)
