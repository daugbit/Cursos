def format(cnpj):
    cnpj = cnpj.replace('.', '').replace('/', '').replace('-', '')
    return cnpj


def sequenceone(cnpj):
    # Cria a sequência auxiliar que será utilizada para cálculo do primeiro dígito
    aux = []
    num = 5
    for i in cnpj:
        if num >= 2:
            aux.append(str(num))
        else:
            num = 9
            aux.append(str(num))
        num -= 1
    return aux


def calcdigitone(raw, aux):
    # Calcula o primeiro verificador e insere na lista da sequência
    num = 0
    for i in range(12):
        calc = int(raw[i]) * int(aux[i])
        num += calc
    dig = 11 - (num % 11)
    if dig > 9:
        dig = 0
    raw.append(str(dig))
    return raw


def sequencetwo(cnpj):
    # Cria a sequência auxiliar que será utilizada para cálculo do segundo dígito
    aux = []
    num = 6
    for i in cnpj:
        if num >= 2:
            aux.append(str(num))
        else:
            num = 9
            aux.append(str(num))
        num -= 1
    return aux


def calcdigittwo(raw, aux):
    # Calcula o segundo verificador e insere na lista da sequência
    num = 0
    for i in range(13):
        calc = int(raw[i]) * int(aux[i])
        num += calc
    dig = 11 - (num % 11)
    if dig > 9:
        dig = 0
    raw.append(str(dig))
    return raw


def reformat(cnpj):
    # Faz join dos dígitos da lista, formatando o CNPJ completo (apenas números)
    cnpj = ''.join(cnpj)
    return cnpj
