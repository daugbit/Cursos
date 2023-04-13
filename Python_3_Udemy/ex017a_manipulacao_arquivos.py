path = 'ex017a_arquivo'

with open(path, 'w+') as file:
    file.write('Nome: Wesley\n')
    file.write('Idade: 38\n')
    file.write('Gênero: Masculino\n')


with open(path, 'a+') as file:
    file.write('Nome: Tânia\n')
    file.write('Idade: 64\n')
    file.write('Gênero: Feminino\n')

    file.seek(0, 0)

    for i in file.readlines():
        print(i, end='')
