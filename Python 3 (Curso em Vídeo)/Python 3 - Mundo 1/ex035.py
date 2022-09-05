l1 = float(input('Comprimento da primeira reta: '))
l2 = float(input('Comprimenro da segunda reta: '))
l3 = float(input('Comprimento da terceira reta: '))
if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
    print(f'É POSSÍVEL formar um triângulo com as retas {l1}, {l2} e {l3}')
else:
    print(f'NÃO é possível formar um triângulo com as retas {l1}, {l2} e {l3}')
