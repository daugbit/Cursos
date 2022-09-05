n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    aux = n2
    n2 = n1
    n1 = aux
n3 = int(input('Digite o terceiro número: '))
if n3 > n2:
    n2 = n3
if n3 < n1:
    n1 = n3
print(f'Entre os números informados, o menor foi {n1} e o maior foi {n2}')
