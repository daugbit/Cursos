"""
Programa que verifica se um CPF informado é válido ou inválido.
"""
lista1 = []
lista2 = []


def cpf_input():
    """
    Função que recebe o input do CPF e verifica se esse input é válido:
    1) remove espaços em branco, se existentes
    2) remove a máscara, se existente
    3) verifica se a quantidade de dígitos informados é igual a 11
    4) verifica se os caracteres informados são todos numéricos
    return: CPF, se as condições acima forem cumpridas.
    """
    while True:
        cpf1 = input('Informe o CPF: ').strip().replace('.', '').replace('-', '').replace(' ', '')
        if cpf1.isdigit() and len(cpf1) == 11:
            return cpf1
        else:
            print('Entrada inválida. Digite o CPF completo (11 dígitos).')
            continue


def is_sequence():
    """
    Verifica se o CPF informado é uma sequência de mesmos números (inválido).
    O retorno padrão é False. Caso o laço chegue ao final tendo comparado todos
    os números (iguais), o retorno será True.
    """
    global cpf
    if cpf == str(cpf[0]) * 11:
        return True
    else:
        return False


cpf = cpf_input()
print('=-' * 30)
print(f'O CPF informado foi: {cpf[0]}{cpf[1]}{cpf[2]}.{cpf[3]}{cpf[4]}{cpf[5]}.'
      f'{cpf[6]}{cpf[7]}{cpf[8]}-{cpf[9]}{cpf[10]}')        # Exibe o CPF informado com a máscara
print('=-' * 30)

for i, v in enumerate(range(10, 1, -1)):    # Cria uma lista com os resultados do primeiro bloco
    lista1.append((int(cpf[i]) * v))

dig1 = 11 - (sum(lista1) % 11)              # Faz a soma dos resultados da lista acima
dig1 = 0 if dig1 > 9 else dig1              # Verifica se o resultado acima é maior que 9, definindo o primeiro dígito


for i, v in enumerate(range(11, 2, -1)):    # Cria uma lista com os resultados do segundo bloco
    lista2.append((int(cpf[i]) * v))
lista2.append(dig1 * 2)                     # Adiciona o primeiro dígito à segunda lista

dig2 = 11 - (sum(lista2) % 11)              # Faz a soma dos resultados da lista acima
dig2 = 0 if dig2 > 9 else dig2              # Verifica se o resultado acima é maior que 9, definindo o segundo dígito

valid_cpf = (cpf[:9] + str(dig1) + str(dig2))  # Faz a montagem do CPF com os dígitos calculados

if valid_cpf != cpf or is_sequence():                               # Verifica se o CPF informado é igual ao calculado
    print('\033[1:30:41m', 'CPF INVÁLIDO!'.center(58), '\033[m')    # e se o CPF informado não é uma sequência
else:
    print('\033[1:30:42m', 'CPF VÁLIDO!'.center(58), '\033[m')
