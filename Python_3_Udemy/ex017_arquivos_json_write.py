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
arquivo = '/home/daug/Documents/GitHub/Cursos/Python_3_Udemy/ex017_arquivo.json'

with open(arquivo, 'w+') as file:
    json.dump(cadastro, file, indent=True, ensure_ascii=False)
