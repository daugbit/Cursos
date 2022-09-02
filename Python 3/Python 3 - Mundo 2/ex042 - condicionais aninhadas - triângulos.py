l1 = float(input('Comprimento da primeira reta: '))
l2 = float(input('Comprimenro da segunda reta: '))
l3 = float(input('Comprimento da terceira reta: '))
if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
    print(f'É POSSÍVEL formar um triângulo com as retas {l1}, {l2} e {l3}')
    if l1 == l2 == l3:
        tri = 'ESCALENO'
    elif l1 != l2 != l3 != l1:
        tri = 'EQUILÁTERO'
    else:
        tri = 'ISÓSCELES'
    print(f'O triângulo formado será do tipo {tri}.')
else:
    print(f'NÃO é possível formar um triângulo com as retas {l1}, {l2} e {l3}')
