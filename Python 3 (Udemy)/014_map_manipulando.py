from dados import students


def nova_nota(n):
    n['nova_nota'] = n['nota'] + 1 if n['nota'] < 10 else n['nota']
    return n


nova = map(nova_nota, students)

for student in nova:
    print(f'Aluno: {student["aluno"]} - Nota antiga: {student["nota"]} - Nota nova: {student["nova_nota"]}')
