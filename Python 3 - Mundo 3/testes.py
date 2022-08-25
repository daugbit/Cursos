lista = []
for c in range(0, 4):
    num = int(input('Digite um número: '))
    if c == 0:
        lista.append(num)
    elif c == 1:
        if num < lista[0]:
            lista.insert(0, num)
        else:
            lista.append(num)
    elif c == 2:
        if num < min(lista):
            lista.insert(0, num)
        elif num > max(lista):
            lista.append(num)
        elif lista[0] < num < lista[1]:
            lista.insert(1, num)
    elif c == 3:
        if num < min(lista):
            lista.insert(0, num)
        elif num > max(lista):
            lista.append(num)
        elif num > lista[1]:
            lista.insert(2, num)
        else:
            lista.insert(1, num)
    elif c == 4:
        if num < min(lista):
            lista.insert(0, num)
        elif num > max(lista):
            lista.append(num)
        elif num < lista[1]:
            lista.insert(1, num)
        elif num < lista[2]:
            lista.insert(2, num)
        elif num < lista[3]:
            lista.insert(3, num)
        else:
            lista.append(num)
print(f'Você digitou os valores {lista}')
