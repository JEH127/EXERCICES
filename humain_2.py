class Humain:
    nb_humain = 0

    def __init__(self, c_name, c_age):
        self.name = c_name
        self.age = c_age
        Humain.nb_humain += 1

    def parler(self, message):
        return message

    def manger(self, fruit):
        return fruit

    def nager(self, type_nage):
        return type_nage


h1 = Humain('BOB', 30)
h2 = Humain('ALI', 50)

# \" => séquence d'échappement pour écrire " entre ""
print(f" {h1.name} a {h1.age} ans et a dit \"{'Oui Monsieur'}\"")
print(f"{h1.name} mange {h1.manger('des bananes')} et il nage {h1.nager('le crawl')}")

print(f"{h2.name} {h2.age} ans et a dit {'Pourquoi pas ?'}")
print(f"{h2.name} mange {h2.manger('des pastèques')} et il nage {h2.nager('le papillon')}")
