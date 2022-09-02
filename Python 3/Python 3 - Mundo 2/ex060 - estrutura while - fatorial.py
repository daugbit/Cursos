from math import factorial
print('VISUALIZADOR DE FATORIAL')
print('=-=' * 10)
num = int(input('Digite um número: '))
fat = num
print(f'Calculando {num}!...', end='')
while num > 0:
    print(f'{num}', end=' ')
    print('x' if num > 1 else '=', end=' ') #exibe símbolo de multiplicação até x1 e símbolo de igual após x1
    num -= 1
print(f'{factorial(fat)}')
