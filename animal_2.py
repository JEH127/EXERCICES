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
        print("Anima existe")


class Reptile(Animal):
    def __init__(self, nom_reptile, taille_reptile):
        Animal.__init__(self, nom_reptile)
        self.taille = taille_reptile

    def manger(self):
        print(f"{self.nom} mange")


# MC
r1 = Reptile("Lézard", 70)
r2 = Reptile("Varengh", 7000)
r1.manger()


def var(x):
    return print(f"{x.nom} mesure {x.taille} cm")


var(r1)
var(r2)

print(f"Nb Animal : {Animal.nb_animal}")
print(f"Type animal : {Animal.type_animal}")
Animal.changer_type('marin')
print(f"Type animal : {Animal.type_animal}")
