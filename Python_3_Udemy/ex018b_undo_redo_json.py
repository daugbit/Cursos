import json
import ex018_undo_redo

arquivo = '/home/daug/Documents/GitHub/Cursos/Python_3_Udemy/ex018b_arquivo.json'

tarefas = ex018_undo_redo.tasks

with open(arquivo, 'w+') as file:
    json.dump(tarefas, file)
