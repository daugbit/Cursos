import random

aux = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

def format(cnpj):
    """
    Função que formata o CNPJ informado pelo usuário, removendo eventuais pontuações, e verifica se o CNPJ não é uma sequência
    param. cnpj: número do CNPJ digitado pelo usuário
    return: número do CNPJ formatado como 'xxxxxxxxxxxxxx'
    """
    cnpj = cnpj.replace('.', '').replace('/', '').replace('-', '')
    if cnpj == cnpj[0] * 14 or len(cnpj) != 14 or not cnpj.isdigit():
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


def generator():
    """
    Função que gera, de forma aleatória, a raiz de um CNPJ, bem como adiciona '0001' ao final.
    return: número de CNPJ gerado, sem os dígitos verificadores.
    """
    cnpj = str(random.randint(00000000, 99999999))
    if len(cnpj) < 8:
        dif = 8 - len(cnpj)
        cnpj = '0' * dif + cnpj
    cnpj = cnpj + '0001'
    return cnpj


def branch(root, n_branch):
    """"
    Função que cria o sequencial da filial no CNPJ (/0005, /0128, etc.)
    return: número de CNPJ com o número da filial.
    """
    if len(n_branch) < 4:
        dif = 4 - len(n_branch)
        n_branch = '0' * dif + n_branch
    cnpj = root + n_branch
    return cnpj

