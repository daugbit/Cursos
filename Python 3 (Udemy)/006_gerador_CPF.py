"""
Progarama que gera um CPF matematicamente válido.
"""

from random import randint

lista1 = []
lista2 = []

cpf = str(randint(000000000, 999999999))    # Cria randomicamente os 9 primeiros dígitos do CPF

for i, v in enumerate(range(10, 1, -1)):    # Cria uma lista com os resultados do primeiro bloco
    lista1.append((int(cpf[i]) * v))

dig1 = 11 - (sum(lista1) % 11)              # Faz a soma dos resultados da lista acima
dig1 = 0 if dig1 > 9 else dig1              # Verifica se o resultado acima é maior que 9, definindo o primeiro dígito

for i, v in enumerate(range(11, 2, -1)):    # Cria uma lista com os resultados do segundo bloco
    lista2.append((int(cpf[i]) * v))
lista2.append(dig1 * 2)                     # Adiciona o primeiro dígito à segunda lista

dig2 = 11 - (sum(lista2) % 11)              # Faz a soma dos resultados da lista acima
dig2 = 0 if dig2 > 9 else dig2              # Verifica se o resultado acima é maior que 9, definindo o segundo dígito

cpf = (cpf[:9] + str(dig1) + str(dig2))     # Faz a montagem do CPF com os dígitos calculados

print('CPF gerado: ', end='')
print(f'{cpf[0]}{cpf[1]}{cpf[2]}.{cpf[3]}{cpf[4]}{cpf[5]}.'         # Exibe o CPF informado com a máscara
      f'{cpf[6]}{cpf[7]}{cpf[8]}-{cpf[9]}{cpf[10]}')
