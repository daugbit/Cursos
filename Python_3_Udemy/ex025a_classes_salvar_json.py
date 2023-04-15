import bip39

class Pessoa():
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Pessoa('Caroline', 23)
p2 = Pessoa('Bianca', 27)

for instance in Pessoa.__dict__:
    print(instance)
