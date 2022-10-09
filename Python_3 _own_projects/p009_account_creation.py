import json

file_object = 'p009_bank_accounts.json'

account = {'a_number': 1, 'a_owner': 'Ciclano', 'a_type': 'corrente', 'a_status':  False, 'a_balance':  0}

lista_json = json.dumps(account, indent=True)

with open(file_object, 'r') as file:
    accounts = file.read()
    accounts = json.loads(accounts)

accounts.append(account)
accounts = json.dumps(accounts, indent=True)

with open(file_object, 'w') as file:
    file.write(accounts)
