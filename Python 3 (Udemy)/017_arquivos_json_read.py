import json

with open('arquivo.json', 'r') as file:
    list_read = file.read()
    list_read = json.load(list_read)
    for i in list_read:
        for j, k in i.items():
            print(f'{j}: {k}')
