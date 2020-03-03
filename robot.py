class Robot:
    robots_crees = 0

    def __init__(self, c_name, c_age):
        self.name = c_name
        self.age = c_age
        Robot.robots_crees += 1


r1 = Robot(" ET ", 10)
r2 = Robot(" NONO ", 20)

print(f" Je suis {r1.name} et j'ai {r1.age} ans ")
print(f" Je suis {r2.name} et j'ai {r2.age} ans ")
print(f" Robots créés : {Robot.robots_crees}")
