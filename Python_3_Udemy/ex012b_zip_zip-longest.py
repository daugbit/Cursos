lista1 = [1, 2, 3, 4, 5, 6, 7]
lista2 = [1, 2, 3, 4]

somalistas = zip(lista1, lista2)

somadas = [x + y for x, y in somalistas]
print(somadas)
