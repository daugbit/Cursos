lista = []
for c in range(0, 5):
    peso = float(input(f'Digite o peso da pessoa {c + 1}, em kg: '))
    lista.insert(c, peso)
lista.sort()
print(f'Entre os dados informados, a pessoa mais pesada tem {lista[-1]}kg e a pessoa mais leve tem {lista[0]}kg.')
