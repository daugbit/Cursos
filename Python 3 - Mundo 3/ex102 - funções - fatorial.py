def fatorial(n, showdef=False):
    """
    -> Calcula o fatorial de um número
    parâmetro n: número para o qual se quer calcular o fatorial
    parâmetro showdef: especifica se o cálculo do fatorial deve ser exibido
    return: retorna o valor final do fatorial
    """
    c = n - 1
    if not showdef:
        while c > 0:
            n *= c
            c -= 1
        return n
    else:
        print(n, end='')
        while c > 0:
            print(' x ', end='')
            print(c, end='')
            n *= c
            c -= 1
        return n


num = int(input('Número para cálculo do fatorial: '))
calc = str(input('Deseja exibir o cálculo? [S/N] ')).strip().upper()[0]
while calc not in 'SN':
    calc = str(input('Opção inválida. Digite apenas N ou S: ')).strip().upper()[0]
if calc == 'S':
    show = True
elif calc == 'N':
    show = False
fat = fatorial(num, show)
print(f' = {fat}.')
