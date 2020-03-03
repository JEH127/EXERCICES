"""
. Phare : bureau en haut
.         toilettes en bas
.         x marches ( hauteur 1 marche = y cm )
"""


# distance en m
def distance_n_aller_retour_wc(n, x, y):
    return n * x * y / 50


n = int(input("Entrez un nombre entier d'aller-retours aux toilettes : "))
x = int(input("Entrez le nombre de marches du Phare : "))
y = int(input("Entrez un nombre entier en cm comme hauteur d'une marche : "))

print(f"{n} aller-retour wc = {distance_n_aller_retour_wc(n, x, y)} m")
