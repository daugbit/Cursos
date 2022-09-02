people = []
person = {}
tot = 0
while True:
    person['name'] = str(input('Nome: '))
    person['gender'] = str(input('Sexo [M/F:] ')).strip().upper()[0]
    while person['gender'] not in 'MmFf':
        person['gender'] = str(input('ERRO! Digite apenas M ou F: ')).strip().upper()[0]
    person['age'] = int(input('Idade: '))
    tot += person['age']
    r = str(input('Deseja continuar? [S/N] ')).strip()[0]
    people.append(person.copy())
    while r not in 'SsNn':
        r = str(input('ERRO! Digite apenas S ou N: ')).strip()[0]
    if r in 'Nn':
        break
print('=-' * 30)
print(f'A) No total, foram cadastradas {len(people)} pessoas.')
print(f'B) A média de idade é de {tot / len(people):.0f} anos.')
print('C) As mulheres cadastradas foram: ', end='')
for i in people:
    if i['gender'] == 'F':
        print(f' - {i["name"]}', end='')
print('\nD) As pessoas com idade acima da média foram: ')
for i in people:
    if i['age'] > (tot / len(people)):
        for j, k in i.items():
            print(f'- {j}= {k} ', end='')
        print()
