"""
Programa que agrupa alunos de acordo com as suas notas.
"""

from itertools import groupby

students = [
    {'aluno': 'Douglas', 'nota': 10},
    {'aluno': 'Maria', 'nota': 8},
    {'aluno': 'Tales', 'nota': 6},
    {'aluno': 'Carol', 'nota': 9},
    {'aluno': 'Gerson', 'nota': 4},
    {'aluno': 'Kaila', 'nota': 2},
    {'aluno': 'Maicon', 'nota': 7},
    {'aluno': 'Lorenzo', 'nota': 6},
    {'aluno': 'Talita', 'nota': 7},
    {'aluno': 'Amanda', 'nota': 5},
    {'aluno': 'Helio', 'nota': 0},
    {'aluno': 'Fabio', 'nota': 0},
    {'aluno': 'Wesley', 'nota': 10},
]

ordenados = lambda item: item['nota']
students.sort(key=ordenados)
agrupados = groupby(students, ordenados)

for nota, turma in agrupados:
    print(f'Alunos que tiraram nota {nota}:')
    for student in turma:
        print(f'\t- {student["aluno"]}')
