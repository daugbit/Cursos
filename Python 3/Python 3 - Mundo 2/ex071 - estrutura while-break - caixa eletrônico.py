n50 = n20 = n10 = n1 = 0
print('=' * 30)
print(f'BANCO DAU'.center(30))
print('=' * 30)
withdrawal = int(input('Quanto você deseja sacar? R$'))
cont = withdrawal
while True:
    if cont // 50 >= 1:
        n50 += 1
        cont -= 50
    else:
        break
while True:
    if cont // 20 >= 1:
        n20 += 1
        cont -= 20
    else:
        break
while True:
    if cont // 10 >= 1:
        n10 += 1
        cont -= 10
    else:
        break
while True:
    if cont // 1 >= 1:
        n1 += 1
        cont -= 1
    else:
        break
print('=' * 30)
print(f'''O seu saque pode ser feito com:
{n50} nota(s) de R$50
{n20} nota(s) de R$20
{n10} nota(s) de R$10
{n1} nota(s) de R$1
''')
