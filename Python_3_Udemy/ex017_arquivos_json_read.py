import json

arquivo = '/home/daug/Documents/GitHub/Cursos/Python_3_Udemy/ex017_arquivo.json'

with open(arquivo, 'r') as file:
    people = json.load(file)
    
    print(people)

    for i in people:
        for j, k in i.items():
            print(f'{j}: {k}')
