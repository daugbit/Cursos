persons = []
people = []
biggest = smallest = 0
while True:
    persons.append(str(input('Nome: ')))
    persons.append(int(input('Peso (kg): ')))
    if len(people) == 0:
        biggest = persons[1]
        smallest = persons[1]
    else:
        if persons[1] > biggest:
            biggest = persons[1]
        elif persons[1] < smallest:
            smallest = persons[1]
    people.append(persons[:])
    persons.clear()
    r = str(input('Deseja cadastrar outra pessoa? [N/S] ')).strip()[0]
    if r in 'Nn':
        break
print('=-' * 20)
print(f'Foram cadastradas {len(people)} pessoas.')
print(f'O maior peso registrado foi de {biggest}kg. Peso de ', end='')
for p in people:
    if p[1] == biggest:
        print(f'{p[0]}... ', end='')
print(f'\nO menor peso registrado foi de {smallest}kg. Peso de ', end='')
for p in people:
    if p[1] == smallest:
        print(f'{p[0]}... ', end='')
