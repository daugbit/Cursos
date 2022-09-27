import json

cadastro = [
    {'id': 1, 'name': 'José', 'age': 35, 'gender': 'm'},
    {'id': 2, 'name': 'Maria', 'age': 12, 'gender': 'f'},
    {'id': 3, 'name': 'Cláudio', 'age': 40, 'gender': 'm'},
    {'id': 4, 'name': 'Juanita', 'age': 65, 'gender': 'f'},
    {'id': 5, 'name': 'Anastor', 'age': 88, 'gender': 'm'},
    {'id': 6, 'name': 'Pedro', 'age': 8, 'gender': 'm'},
    {'id': 7, 'name': 'Kátia', 'age': 14, 'gender': 'f'},
]

lista_json = json.dumps(cadastro, indent=True)

with open('arquivo.json', 'a') as file:
    file.write(lista_json)
