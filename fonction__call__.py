class Citronnier:
    def __init__(self, nbcitrons, age):
        self.nbcitrons = nbcitrons
        self.age = age

    def __call__(self, nbcitrons, age):
        self.nbcitrons = nbcitrons
        self.age = age

    def __str__(self):
        return f"Ce citronnier a {self.age} ans et {self.nbcitrons} citrons"


if __name__ == "__main__":
    c1 = Citronnier(10, 3)
    print(c1)
    c1(30, 4)  # __call__ => objet comme fonction
    print(c1)
