class Humain:
    nb_humain = 0

    # constructeur
    def __init__(self, c_name, c_age):
        # attributs
        self.name = c_name
        self.age = c_age
        Humain.nb_humain += 1  # variable de classe nb_humain

    # méthodes
    def parler(self, message):
        print(f"{self.name} a {self.age} ans et a dit : {message}")

    def manger(self, fruit):
        print(f"{self.name} mange {fruit}")

    def nager(self, nage):
        print(f"{self.name} sait nager {nage}")

    def respirer(self):
        print(f"{self.name} respire")


# création d'objets
h1 = Humain('BOB', 30)
h2 = Humain('ALI', 50)

print(f" Nombre d'humains : {Humain.nb_humain}")

h1.parler('Allez'), h2.parler('Vas-y')
h1.manger('un melon'), h2.manger('une banane')

h1.nager('le crawl')
h2.nager('le papillon')

h1.respirer()
