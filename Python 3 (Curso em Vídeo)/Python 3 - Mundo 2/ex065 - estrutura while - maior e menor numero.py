cont = 'S'
lista = []
while cont == 'S':
    num = int(input('Digite um número: '))
    lista.append(num)
    cont = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
print(f'O menor número digitado foi {min(lista)} e o maior foi {max(lista)}')
print(f'A média entre os números digitados é igual a {sum(lista) / len(lista)}')
