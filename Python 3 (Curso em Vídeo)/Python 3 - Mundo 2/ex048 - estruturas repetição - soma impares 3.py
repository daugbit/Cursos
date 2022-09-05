soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
print(f'A soma entre todos os números ímpares, múltiplos de 3, entre 1 e 500, é igual a {soma}')