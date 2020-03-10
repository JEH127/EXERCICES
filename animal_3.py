class Animal:
    type_animal = 'terrestre'
    nb_animal = 0

    def __init__(self, nom_animal):
        self.nom = nom_animal
        Animal.nb_animal += 1

    @classmethod
    def changer_type(cls, nouveau_type):
        cls.type_animal = nouveau_type

    @staticmethod
    def exister():
        print("Animal existe")


class Reptile(Animal):
    def __init__(self, nom_reptile, taille_reptile):
        Animal.__init__(self, nom_reptile)
        self.taille = taille_reptile

    def manger(self, type_nourriture):
        print(f"{self.nom} mange {type_nourriture}")


# MC
r1 = Reptile("Lézard", 70)
r2 = Reptile("Varengh", 7000)


def longueur_animal(x):
    return f"{x.nom} mesure {x.taille} cm"


r1.manger('de la viande')
print(longueur_animal(r1))
print(longueur_animal(r2))
print(f"Nb Animal : {Animal.nb_animal}")
print(f"Type Animal : {Animal.type_animal}")
Animal.changer_type('marin')
print(f"Type Animal : {Animal.type_animal}")
