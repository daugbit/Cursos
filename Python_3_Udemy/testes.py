import os

lista = []

while True:
    os.system('cls')
    print('LISTA DE COMPRAS')
    option = input('[l]istar   [i]nserir   [a]pagar   [s]air: ')
    if option == 'l':
        for i, item in enumerate(lista):
            print(i, item)
    elif option == 'i':
        item = input('Item:')
        lista.append(item)
    elif option == 'a':
        try:
            item = int(input('Índice: '))
            lista.pop(item)
        except:
            print('Índice inexistente.')
    elif option == 's':
        break
    else:
        print('Opção inválida')
