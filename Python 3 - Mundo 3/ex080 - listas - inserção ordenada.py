lista = []
for c in range(0, 5):
    num = int(input('Digite um número: '))
    if c == 0 or num > max(lista):
        lista.append(num)
        print('Valor adicionado ao final da lista.')
    else:
        for c2 in range(0, len(lista)):
            if num <= lista[c2]:
                lista.insert(c2, num)
                print(f'Valor adicionado na posição {c2} da lista.')
                break
print(f'Você digitou os valores {lista}')
