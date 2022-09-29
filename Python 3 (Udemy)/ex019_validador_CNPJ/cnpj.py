aux = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

def format(cnpj):
    """
    Função que formata o CNPJ informado pelo usuário, removendo eventuais pontuações, e verifica se o CNPJ não é uma sequência
    param. cnpj: número do CNPJ digitado pelo usuário
    return: número do CNPJ formatado como 'xxxxxxxxxxxxxx'
    """
    cnpj = cnpj.replace('.', '').replace('/', '').replace('-', '')
    if cnpj == cnpj[0] * 14:
        return False
    else:
        return cnpj


def calcdigitone(cnpj):
    """
    Função que calcula o primeiro verificador e insere na lista da sequência
    param. cnpj: lista de dígitos (sem os dígitos verificadores) do CNPJ informado pelo usuário
    return: lista de dígitos, agora com o primeiro dígito verificador, do CNPJ informado pelo usuário
    """
    num = 0
    for i in range(12):
        calc = int(cnpj[i]) * aux[i + 1]
        num += calc
    dig = 11 - (num % 11)
    if dig > 9:
        dig = 0
    cnpj = cnpj + str(dig)
    return cnpj


def calcdigittwo(cnpj):
    """
    Função que calcula o segundo verificador e insere na lista da sequência
    param. cnpj: lista de dígitos (apenas com o primeiro dígito verificador calculado) do CNPJ informado pelo usuário
    return: lista de dígitos, agora com os dois dígitos verificadores calculados, do CNPJ informado pelo usuário
    """
    num = 0
    for i in range(13):
        calc = int(cnpj[i]) * aux[i]
        num += calc
    dig = 11 - (num % 11)
    if dig > 9:
        dig = 0
    cnpj = cnpj + str(dig)
    return cnpj
