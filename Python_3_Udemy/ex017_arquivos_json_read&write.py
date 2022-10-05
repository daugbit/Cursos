import json

user = {}

with open('arquivo.json', 'r') as file:
    cadastro = file.read()
    cadastro = json.loads(cadastro)
    user['id'] = cadastro[-1]['id'] + 1

print('INCLUSÃO DE NOVO CADASTRO')
user['name'] = input('Nome: ')
user['age'] = int(input('Idade: '))
user['gender'] = input('Sexo [f/m]: ')

cadastro.append(user)
cadastro = json.dumps(cadastro, indent=True)

with open('arquivo.json', 'w') as file2:
    file2.write(cadastro)
