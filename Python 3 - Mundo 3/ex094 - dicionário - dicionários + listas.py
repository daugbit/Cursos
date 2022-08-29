people = []
person = {}
tot = 0
while True:
    person['name'] = str(input('Nome: '))
    person['gender'] = str(input('Sexo [M/F:] ')).strip().upper()
    person['age'] = int(input('Idade: '))
    tot += person['age']
    r = str(input('Deseja continuar? [s/n] ')).strip()[0]
    people.append(person.copy())
    while r not in 'SsNn':
        r = str(input('Opção inválida! Deseja continuar? [s/n] ')).strip()[0]
    if r in 'Nn':
        break
print('=-' * 30)
print(f'No total, foram cadastradas {len(people)} pessoas.')
print(f'A média de idade é de {tot / len(people)} anos.')

