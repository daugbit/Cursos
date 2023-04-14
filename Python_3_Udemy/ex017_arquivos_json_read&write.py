import json

user = {}

arquivo = '/home/daug/Documents/GitHub/Cursos/Python_3_Udemy/ex017_arquivo.json'


with open(arquivo, 'r') as file:
    cadastro = json.load(file)
    user['id'] = cadastro[-1]['id'] + 1

print('INCLUSÃO DE NOVO CADASTRO')
user['name'] = input('Nome: ')
user['age'] = int(input('Idade: '))
user['gender'] = input('Sexo [f/m]: ')

cadastro.append(user)

with open(arquivo, 'w') as file2:
    json.dump(cadastro, file2, indent=True, ensure_ascii=False)
