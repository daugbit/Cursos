turma = []
while True:
    name = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    avg = (n1 + n2) / 2
    turma.append([name, [n1, n2], avg])
    r = str(input('Deseja cadastrar outro aluno? [S/N] ')).strip()[0]
    while r not in 'SsNn':
        r = str(input('Opção inválida! Deseja cadastrar outro aluno? [S/N] ')).strip()[0]
    if r in 'Nn':
        break
print('=-' * 30)
print(f'{"Nº":<4}{"Nome":<9}{"Média":>4}')
print('-=' * 10)
for c in range(0, len(turma)):
    print(f'{c + 1:<3} {turma[c][0]:<9} {turma[c][2]:>5.1f}')
while True:
    print('=-' * 30)
    r = int(input('De qual aluno você quer ver as notas? [999 para sair] '))
    if r == 999:
        break
    elif 0 <= r <= len(turma):
        print(f'Notas do(a) aluno(a) {turma[r-1][0]}: {turma[r-1][1]}')
