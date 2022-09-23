from dados import students


def filtro(n):
    if n['nota'] < 6:
        return False
    else:
        return True


aprovados = filter(filtro, students)

print('ALUNOS APROVADOS:')
for aluno in aprovados:
    print(aluno["aluno"])
