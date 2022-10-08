class Conta:
	def __init__(self, a_number, a_type, a_owner):
		self.number = a_number
		self.type = a_type
		self.owner = a_owner
		self.a_status = None
		self.a_type = None
		self.a_balance = None

	def open_account(self):
		self.a_status = True
		if self.type == 'corrente':
			self.a_balance = 50
		elif self.type == 'poupança':
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
		
		if self.type == 'corrente':
			self.a_balance -= 20
		elif self.type == 'poupança':
			self.a_balance -= 10


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
