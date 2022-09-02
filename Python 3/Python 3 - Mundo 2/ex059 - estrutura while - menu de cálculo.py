r = 0
while r != 5:
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    print('=-=' * 15)
    print('''[1] SOMAR
[2] SUBTRAIR
[3] MULTIPLICAR
[4] alterar os números
[5] sair''')
    print('=-=' * 15)
    r = int(input(f'O que você quer fazer com {num1} e {num2}? '))
    if r == 1:
        print(f'Aqui está: {num1} + {num2} = {num1 + num2} ')
    elif r == 2:
        print(f'Aqui está: {num1} - {num2} = {num1 - num2}')
    elif r == 3:
        print(f'Aqui está: {num1} x {num2} = {num1 * num2}')
    elif r == 4:
        print('Informe os novos números.')
    elif r == 5:
        print('Fim do programa.')
    else:
        print('Opção inválida.')
    print('=-=' * 15)
