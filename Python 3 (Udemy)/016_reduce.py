from dados import students
from functools import reduce


soma_notas = reduce(lambda ac, i: ac + i['nota'], students, 0)
print(f'A média de notas na turma foi de {soma_notas / len(students)}')
