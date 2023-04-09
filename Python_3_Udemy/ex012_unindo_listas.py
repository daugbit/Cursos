lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista2 = ['BA', 'SP', 'MG', 'RJ']

def join_list(lista1, lista2):
    smaller = min(len(lista1), len(lista2))
    return [(lista1[i], lista2[i]) for i in range(smaller)]


joined = join_list(lista1, lista2)
print(joined)