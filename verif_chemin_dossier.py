import os

# o os.path.isdir() => retourne booléen sur bon chemin dossier
chemin_dossier = input('Entrez un chemin de dossier : ')
dossier_existe = os.path.isdir(chemin_dossier)
print(dossier_existe)
