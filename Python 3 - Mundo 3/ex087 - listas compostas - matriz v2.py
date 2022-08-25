matriz = [[], [], []]
pares = maior2l = sum3c = 0
for i in range(0, 3):
    for j in range(0, 3):
        num = int(input(f'Digite um número para a posição [{i}, {j}]: '))
        matriz[i].append(num)
        if num % 2 == 0:
            pares += num
        if i == 1 and num > maior2l:
            maior2l = num
        if j == 2:
            sum3c += num
print('-=' * 20)
for c in matriz:
    print(f'[{c[0]:^5}] [{c[1]:^5}] [{c[2]:^5}]')
print('-=' * 20)
print(f'A soma de todos os valores pares é igual a {pares}.')
print(f'A soma dos valores da terceira coluna é igual a {sum3c}.')
print(f'O maior valor da segunda linha é igual a {maior2l}.')
