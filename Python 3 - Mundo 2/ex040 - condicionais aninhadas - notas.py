n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
avg = (n1 + n2) / 2
if avg < 5:
    print('O aluno está \033[1;31;40mREPROVADO\033[m')
elif 5 <= avg < 7:
    print('O aluno está em \033[1;33;40mRECUPERAÇÃO\033[m')
else:
    print('O aluno está \033[1;32;40mAPROVADO\033[m')
