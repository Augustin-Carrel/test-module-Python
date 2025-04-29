import sys # Importe le module sys pour accéder aux variables et fonctions du système

module_name = "os" # Nom du module à vérifier

if module_name in sys.modules: # Vérifie si le module est présent dans les modules importés
    print(f"{module_name} est installé") # Si oui, affiche un message indiquant que le module est installé
else:
    print(f"{module_name} n'est pas installé") # Sinon, affiche un message indiquant que le module n'est pas installé
