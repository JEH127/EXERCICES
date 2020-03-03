class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        return f"Polynomial(*{self.coeffs})"

    def __add__(self, other):
        return Polynomial(*(x + y for x, y in zip(self.coeffs, other.coeffs)))

    def __len__(self):
        return len(self.coeffs)

    def __call__(self, *args):  # update coeffs => objet comme fonction => objet(*coeffs)
        self.coeffs = args


# Main Code
p1 = Polynomial(1, 2, 3)  # x² 2x + 3
p2 = Polynomial(4, 5, 6)  # 4x² 5x + 6
print(p1)
print(p1 + p2)
print(len(p1))
p1(10, 11, 12)
print(p1)
