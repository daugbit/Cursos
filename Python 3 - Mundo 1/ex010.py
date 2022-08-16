real = float(input('Informe quantos reais você tem na carteira: R$'))
dollar = real / 5.07
print(f'Com os seus \033[1;31;40mR${real:.2f}\033[m, você pode comprar \033[1;31;40mUS${dollar:.2f}\033[m')
