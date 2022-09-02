print('GERADOR DE PA')
print('=-=' * 10)
first_term = int(input('Digite o primeiro termo: '))
ratio = int(input('Digite a razão: '))
print('=-=' * 10)
current = first_term
print('PA:', end=' ')
c = 10
while c != 0:
    while c > 0:
        print(f'{current} ->', end=' ')
        current += ratio
        c -= 1
    print('PAUSA')
    c = int(input('Quantos termos a mais você quer mostrar? '))
print('FIM')
