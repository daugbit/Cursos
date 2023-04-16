import json
from ex025a_classes_salvar_json import arquivo, Pessoa

with open(arquivo, 'r') as file:
    people = json.load(file)
    p1 = Pessoa(**people[0])
    p2 = Pessoa(**people[1])
    p3 = Pessoa(**people[2])

print(p1.__dict__)
print(p2.__dict__)
print(p3.__dict__)
