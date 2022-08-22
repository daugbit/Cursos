gender = r = 'o'
men = []
higher18 = []
lower20_w = []
while True:
    print('==== CADASTRO DE PESSOA ====')
    age = int(input('Idade: '))
    if age > 18:
        higher18.append(age)
    while gender not in 'mf':
        gender = str(input('Sexo (m/f): ')).strip().lower()
        if gender == 'm':
            men.append(gender)
        elif gender == 'f' and age < 20:
            lower20_w.append(gender)
    while r not in 'sn':
        print('.' * 15, end='')
        r = str(input('Deseja continuar? [s/n] ')).strip().lower()
    if r == 'n':
        break
    gender = r = 'o'
print('=-=' * 20)
print(f'A) Foram cadastradas {len(higher18)} pessoas com mais de 18 anos.')
print(f'B) Foram cadastrados {len(men)} homens.')
print(f'C) Foram cadastradas {len(lower20_w)} mulheres com menos de 20 anos.')
