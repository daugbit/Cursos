aluno = {}
aluno['nome'] = str(input('Nome do aluno: '))
aluno['média'] = float(input('Média do aluno: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'APROVADO'
else:
    aluno['situação'] = 'REPROVADO'
for k, i in aluno.items():
    print(f'{k.title()} é igual a {i}.')
