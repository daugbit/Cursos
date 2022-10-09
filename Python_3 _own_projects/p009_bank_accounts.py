import json

class Conta:
	def __init__(self, a_number, a_owner, a_type=None, a_status=None, a_balance=None):
		self.a_number = a_number
		self.a_owner = a_owner
		self.a_type = a_type
		self.a_status = a_status
		self.a_balance = a_balance

	def open_account(self):
		self.a_status = True
		if self.a_type == 'corrente':
			self.a_balance = 50
		elif self.a_type == 'poupança':
			self.a_balance = 150

	def close_account(self):
		if self.a_balance != 0:
			print('Esta conta não pode ser encerrada, pois possui saldo diferente de R$0')
		else:
			self.a_status = False

	def deposit(self, value):
		if not self.a_status:
			print('Conta desativada')
			return None
		
		self.a_balance += value

	def withdraw(self, value):
		if not self.a_status:
			print('Conta desativada')
			return None
		
		if value > self.a_balance:
			print('O valor informado é maior que o saldo disponível')
		else:
			self.a_balance -= value

	def pay_fee(self):
		if not self.a_status:
			print('Conta desativada')
			return None
		
		if self.a_type == 'corrente':
			self.a_balance -= 20
		elif self.a_type == 'poupança':
			self.a_balance -= 10


file_object = 'p009_bank_accounts.json'

with open(file_object, 'r') as file:
	accounts = file.read()
	accounts = json.loads(accounts)

	count = 0
	for account in accounts.values():
		client = 'client' + str(count)
		client = Conta(account['a_number'], account['a_owner'], account['a_type'], account['a_status'], account['a_balance'])

while True:
	print('=-' * 30)
	print('DAU Bank'.center(60))
	print('=-' * 30)
	print('[1] Consultar conta')
	print('[2] Abrir nova conta')
	print('[3] Encerrar conta')
	print('[4] Depositar')
	print('[5] Sacar')
	print('[6] Debitar taxa de conta')
	print('[7] SAIR')
	print('=-' * 30)
	opt = input('Digite uma das opções: ')

	if opt == '1':
		pass
	elif opt == '2':
		client1 = Conta('001', 'corrente', 'Douglas')
		client1.open_account()
	elif opt == '3':
		client1.close_account()
	elif opt == '4':
		client1.deposit(100)
	elif opt == '5':
		acc = input('Digite o número da conta: ')
		client1.withdraw(130)
	elif opt == '6':
		client1.pay_fee()
	elif opt == '7':
		print('ATÉ LOGO!')
		break
	else:
		print('\033[1:31mOPÇÃO INVÁLIDA!033[m')
		continue
