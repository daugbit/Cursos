num = int(input('Digite um número: '))
print('=-=' * 10)
print('''1 - BINÁRIO
2 - OCTAL
3 - HEXADECIMAL''')
print('=-=' * 10)
base = int(input('Informe a base para a qual você deseja converter o número acima: '))
if base == 1:
    print(f'O número {num}, em binário, é igual a {bin(num)[2:]}')
elif base == 2:
    print(f'O número {num}, em octal, é igual a {oct(num)[2:]}')
elif base == 3:
    print(f'O número {num}, em hexadecimal, é igual a {hex(num)[2:]}')
else:
    print('Opção inválida!"')