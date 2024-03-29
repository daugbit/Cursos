"""
Progarama que gera um CPF matematicamente válido.
"""

from random import randint

lista1 = []
lista2 = []

cpf = str(randint(000000000, 999999999))    # Cria randomicamente os 9 primeiros dígitos do CPF

for i, v in enumerate(range(len(cpf), 1, -1)):    # Cria uma lista com os resultados do primeiro bloco
    lista1.append((int(cpf[i]) * v))

dig1 = 11 - (sum(lista1) % 11)              # Faz a soma dos resultados da lista acima
dig1 = 0 if dig1 > 9 else dig1              # Verifica se o resultado acima é maior que 9, definindo o primeiro dígito

for i, v in enumerate(range(len(cpf), 2, -1)):    # Cria uma lista com os resultados do segundo bloco
    lista2.append((int(cpf[i]) * v))
lista2.append(dig1 * 2)                     # Adiciona o primeiro dígito à segunda lista

dig2 = 11 - (sum(lista2) % 11)              # Faz a soma dos resultados da lista acima
dig2 = 0 if dig2 > 9 else dig2              # Verifica se o resultado acima é maior que 9, definindo o segundo dígito

cpf = (cpf[:9] + str(dig1) + str(dig2))     # Faz a montagem do CPF com os dígitos calculados

if len(cpf) < 11:                           # Add zeros no início do CPF, caso o número gerado tenha menos de 9 dígitos
    digitszero = 11 - len(cpf)
    cpf = ('0' * digitszero + str(cpf))

print('CPF gerado: ', end='')
print(f'{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}')         # Exibe o CPF informado com a máscara

