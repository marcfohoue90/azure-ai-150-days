# Ce script analyse des ressources Azure fictives.
# Il déduplique les régions et indexe chaque ressource par son nom.

ressources = [
    {"nom": "api-production", "region": "francecentral", "type": "app-service"},
    {"nom": "base-donnees", "region": "westeurope", "type": "database"},
    {"nom": "site-vitrine", "region": "francecentral", "type": "app-service"}
]

regions_uniques = set()
ressources_par_nom = {}

for ressource in ressources:
    nom = ressource["nom"]
    region = ressource["region"]
    
    if nom in ressources_par_nom:
        print("Erreur : nom de ressource dupliqué :", nom)
    else:
        ressources_par_nom[nom] = ressource
        regions_uniques.add(region)

print("Régions uniques :", regions_uniques)
print("Ressources indexées :", ressources_par_nom)
