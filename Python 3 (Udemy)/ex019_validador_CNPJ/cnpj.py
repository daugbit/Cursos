def format(cnpj):
    """
    Função que formata o CNPJ informado pelo usuário, removendo eventuais pontuações
    param. cnpj: número do CNPJ digitado pelo usuário
    return: número do CNPJ formatado como 'xxxxxxxxxxxxxx'
    """
    cnpj = cnpj.replace('.', '').replace('/', '').replace('-', '')
    return cnpj


def sequenceone(cnpj):
    """
    Função que cria a sequência auxiliar que será utilizada para cálculo do primeiro dígito
    param. cnpj: número do CNPJ no formato de lista de dígitos, sem os dígitos verificadores
    return: lista auxiliar para o cálculo
    """
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
    """
    Função que calcula o primeiro verificador e insere na lista da sequência
    param. raw: lista de dígitos (sem os dígitos verificadores) do CNPJ informado pelo usuário
    param. aux: lista auxiliar
    return: lista de dígitos, agora com o primeiro dígito verificador, do CNPJ informado pelo usuário
    """
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
    """
    Função que cria a sequência auxiliar que será utilizada para cálculo do segundo dígito
    param. cnpj: número do CNPJ no formato de lista de dígitos, apens com o primeiro dígito verificador
    return: segundo lista auxiliar para o cálculo
    """
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
    """
    Função que calcula o segundo verificador e insere na lista da sequência
    param. raw: lista de dígitos (apenas com o primeiro dígito verificador calculado) do CNPJ informado pelo usuário
    param. aux: segunda lista auxiliar
    return: lista de dígitos, agora com os dois dígitos verificadores calculados, do CNPJ informado pelo usuário
    """
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
    """
    Função que faz join dos dígitos da lista, formatando o CNPJ completo (apenas números)
    param. cnpj: lista de dígitos, com os dois dígitos verificadores calculados, do CNPJ informado pelo usuário
    return: número do CNPJ no formato 'xxxxxxxxxxxxxx'
    """
    cnpj = ''.join(cnpj)
    return cnpj
