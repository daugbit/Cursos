"""
Programa que gera, de forma aleatória, números de CNPJ matematicamente válidos.
Também possui a função de calcular o CNPJ de uma filial, a partir de um CNPJ raiz informado.
"""

from Python_3_Udemy.ex019_CNPJ import cnpj_param as cnpj

print('=-' * 30)
print('[1] Gerar um CNPJ novo (matriz)')
print('[2] Gerar um CNPJ para uma filial')
print('=-' * 30)

option = input('Digite sua opção: ')

if option == '1':
    cnpj1 = cnpj.generator()
elif option == '2':
    root = input('Informe os 8 dígitos do CNPJ raiz: ')
    n_branch = input('Informe o número da filial: ')
    cnpj1 = cnpj.branch(root, n_branch)
else:
    print('Opção inválida!')

cnpj1 = cnpj.calcdigitone(cnpj1)
cnpj2 = cnpj.calcdigittwo(cnpj1)

print('=-' * 30)
print(f'CNPJ gerado:      \033[1:30:47m{cnpj2}\033[m')
print(f'CNPJ com máscara: \033[1:30:47m{cnpj2[0:2]}.{cnpj2[2:5]}.{cnpj2[5:8]}/{cnpj2[8:12]}-{cnpj2[12:]}\033[m')
