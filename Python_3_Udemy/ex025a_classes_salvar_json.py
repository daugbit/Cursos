import json

arquivo = 'Python_3_Udemy/ex025_classes_arquivo.json'

class Pessoa():
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Pessoa('Caroline', 23)
p2 = Pessoa('Bianca', 27)
p3 = Pessoa('Daniela', 32)

lista = [vars(p1), vars(p2), p3.__dict__]


def make_dump():
    with open(arquivo, 'w') as file:
        json.dump(lista, file, indent=True)


if __name__ == '__main__':
    make_dump()
