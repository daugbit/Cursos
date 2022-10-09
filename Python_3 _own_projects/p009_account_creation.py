import json

file_object = 'p009_bank_accounts.json'

lista = [{'a_number': 0, 'a_owner':  'Fulano', 'a_type':  'corrente', 'a_status':  False, 'a_balance':  0}, ]

lista_json = json.dumps(lista, indent=True)

with open(file_object, 'w') as file:
    file.write(lista_json)
